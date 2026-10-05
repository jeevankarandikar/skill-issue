import { atom, read, update } from 'claude-code'
import type { Register } from 'claude-code'

import type { AgentRow, Gauge } from '../types'

// An agent rereads its whole context on every call, so cost grows with the
// square of its length. In the week of 2026-09-25 the agents past 150 calls
// were 72% of the weekly cap, and the ones past 300 were 36%.
const LONG = 150
const VERY_LONG = 300
const KEEP = 80

const agents = atom({ plugin: 'fleet-gauge', key: 'agents' } as const, {})
const gauge = atom({ plugin: 'fleet-gauge', key: 'gauge' } as const, null)

const tint = (value: number, warn: number, stop: number) =>
  value >= stop ? 'red' : value >= warn ? 'yellow' : undefined

// The band is silent until a number needs a decision. /fleet prints them all.
const SHOW_AT: Record<string, number> = { seven_day: 50, five_hour: 70 }
const CONTEXT_AT = 200_000

const thousands = (tokens: number) =>
  tokens >= 1_000_000
    ? `${(tokens / 1_000_000).toFixed(tokens % 1_000_000 === 0 ? 0 : 1)}M`
    : `${Math.round(tokens / 1000)}k`

function gaugeLine(now: Gauge | null): string {
  if (now === null) {
    return 'No usage reading yet.'
  }

  const parts = now.limits.map(l => `${windowName(l.kind)} ${Math.round(l.percentUsed)}%`)

  if (now.tokens !== undefined) {
    parts.push(`context ${thousands(now.tokens)} of ${thousands(now.window)}`)
  }

  return parts.join(', ')
}

const windowName = (kind: string) =>
  kind === 'seven_day' ? 'week' : kind === 'five_hour' ? '5h' : kind

function trimmed(rows: Record<string, AgentRow>): Record<string, AgentRow> {
  const entries = Object.entries(rows)

  if (entries.length <= KEEP) {
    return rows
  }

  return Object.fromEntries(
    entries.sort((a, b) => b[1].lastAt - a[1].lastAt).slice(0, KEEP),
  )
}

export const register: Register = on => {
  on('session.start', async ($, e, next) => {
    await $.command.register({
      name: 'fleet',
      description: "List this session's subagents by tool calls made",
    })

    return next(e)
  })

  on('session.measure', async ($, e, next) => {
    const now: Gauge = {
      tokens: e.context.tokens,
      window: e.context.window,
      limits: e.rateLimits.map(({ kind, percentUsed, resetsAt }) => ({
        kind,
        percentUsed,
        resetsAt,
      })),
    }
    await update($, gauge, () => now)

    return next(e)
  })

  on('agent.spawn', async ($, e, next) => {
    const started = await next(e)
    const id = 'agentId' in started ? started.agentId : undefined

    if (id !== undefined) {
      const at = await $.clock.now()
      await update($, agents, rows => ({
        ...rows,
        [id]: {
          calls: 0,
          isDone: false,
          ...rows[id],
          label: e.description || e.subagentType,
          lastAt: at,
        },
      }))
    }

    return started
  })

  on('tool.call', async ($, e, next) => {
    const id = e.agentId

    if (id === undefined) {
      return next(e)
    }

    const at = await $.clock.now()
    let row: AgentRow = { label: id.slice(0, 8), calls: 0, lastAt: at, isDone: false }
    await update($, agents, rows => {
      row = { ...row, ...rows[id], lastAt: at, isDone: false }
      row = { ...row, calls: row.calls + 1 }

      return trimmed({ ...rows, [id]: row })
    })

    if (row.calls === LONG || row.calls === VERY_LONG) {
      $.ui.toast(
        `${row.label} has made ${row.calls} tool calls. Long agents cost the most. Consider a handoff.`,
      )
    }

    return next(e)
  })

  on('turn.complete', async ($, e, next) => {
    const id = (e as { agentId?: string }).agentId

    if (id !== undefined) {
      await update($, agents, rows =>
        rows[id] ? { ...rows, [id]: { ...rows[id], isDone: true } } : rows,
      )
    }

    return next(e)
  })

  on('command.run', { command: 'fleet' }, async $ => {
    const rows = Object.values(await read($, agents)).sort((a, b) => b.calls - a.calls)
    const head = gaugeLine(await read($, gauge))

    if (rows.length === 0) {
      return { text: `${head}\nNo subagent has made a tool call in this session.` }
    }

    return {
      text: [
        head,
        ...rows.map(
          r => `${String(r.calls).padStart(4)} calls  ${r.isDone ? 'done   ' : 'running'}  ${r.label}`,
        ),
      ].join('\n'),
    }
  })

  on('ui.render', { component: 'AbovePrompt' }, async ($, e, next) => {
    const now = await read($, gauge)
    const rows = Object.values(await read($, agents))

    const running = rows.filter(r => !r.isDone)
    const longest = running.reduce<AgentRow | null>(
      (top, r) => (top === null || r.calls > top.calls ? r : top),
      null,
    )
    const limits = (now?.limits ?? []).filter(l => l.percentUsed >= (SHOW_AT[l.kind] ?? 80))
    const tokens = now?.tokens !== undefined && now.tokens >= CONTEXT_AT ? now.tokens : undefined

    if (e.props.hasSurvey || (limits.length === 0 && tokens === undefined && longest === null)) {
      return next(e)
    }

    const { Box, Text } = $.ui.resolve(e)

    return (
      <Box>
        {limits.map(limit => (
          <Text color={tint(limit.percentUsed, 50, 80)}>
            {windowName(limit.kind)} {Math.round(limit.percentUsed)}%{'   '}
          </Text>
        ))}
        {now !== null && tokens !== undefined && (
          <Text color={tint(tokens, CONTEXT_AT, 400_000)}>
            context {thousands(tokens)} of {thousands(now.window)}{'   '}
          </Text>
        )}
        {longest !== null && (
          <Text color={tint(longest.calls, LONG, VERY_LONG)} dimColor={longest.calls < LONG}>
            {running.length} {running.length === 1 ? 'agent' : 'agents'} running, longest{' '}
            {longest.calls} calls ({longest.label})
          </Text>
        )}
      </Box>
    )
  })
}
