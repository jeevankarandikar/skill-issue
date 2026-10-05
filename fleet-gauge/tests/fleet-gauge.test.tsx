import { expect, mock, test } from 'claude-code/testing'

const BAND = { plugin: 'fleet-gauge', component: 'AbovePrompt', props: { hasSurvey: false } } as const

test('a subagent call is counted and the band names the longest agent', async ($, on) => {
  mock.clock(on)
  on('tool.call', () => ({ result: { text: 'ok' } }) as never)

  for (let i = 0; i < 3; i += 1) {
    await $.tool.call({ tool: 'Bash', command: 'ls', agentId: 'agent-one' } as never)
  }
  await $.tool.call({ tool: 'Bash', command: 'ls', agentId: 'agent-two' } as never)

  for (const surface of ['terminal', 'desktop'] as const) {
    const ui = await $.ui.mount({ ...BAND, surface } as never)
    expect(await ui.find({ type: 'Text', text: /2 agents running, longest 3 calls \(agent-on\)/ })).toBeDefined()
    await ui.unmount()
  }

  const listed = await $.command.run({ command: 'fleet', args: '' } as never)
  expect((listed as { text?: string }).text).toContain('3 calls')
})

test('a main-loop call is not counted and the band stays out of the way', async ($, on) => {
  mock.clock(on)
  on('tool.call', () => ({ result: { text: 'ok' } }) as never)
  // the mod passes the render on when it has nothing to show; this stands for the engine
  on('ui.render', ($, e) => {
    const { Text } = $.ui.resolve(e)

    return (<Text>the engine's own row</Text>) as never
  })
  await $.tool.call({ tool: 'Bash', command: 'ls' } as never)

  const ui = await $.ui.mount({ ...BAND, surface: 'terminal' } as never)
  expect(await ui.find({ type: 'Text', text: /running/ })).toBeUndefined()
  expect(await ui.find({ type: 'Text', text: /engine's own row/ })).toBeDefined()
  await ui.unmount()
})

test('the band is silent under the thresholds and speaks past them', async ($, on) => {
  mock.clock(on)
  on('ui.render', ($, e) => {
    const { Text } = $.ui.resolve(e)

    return (<Text>the engine's own row</Text>) as never
  })
  on('session.measure', () => ({ changed: [] }) as never)
  const measure = (week: number, tokens: number) =>
    $.session.measure({
      context: { tokens, window: 1_000_000 },
      rateLimits: [
        { kind: 'five_hour', percentUsed: 4 },
        { kind: 'seven_day', percentUsed: week },
      ],
    } as never)

  await measure(8, 131_000)
  let ui = await $.ui.mount({ ...BAND, surface: 'desktop' } as never)
  expect(await ui.find({ type: 'Text', text: /week|context|5h/ })).toBeUndefined()
  await ui.unmount()

  const listed = await $.command.run({ command: 'fleet', args: '' } as never)
  expect((listed as { text?: string }).text).toContain('5h 4%, week 8%, context 131k of 1M')

  await measure(62, 240_000)
  ui = await $.ui.mount({ ...BAND, surface: 'desktop' } as never)
  expect(await ui.find({ type: 'Text', text: /week 62%/ })).toBeDefined()
  expect(await ui.find({ type: 'Text', text: /context 240k of 1M/ })).toBeDefined()
  expect(await ui.find({ type: 'Text', text: /5h/ })).toBeUndefined()
  await ui.unmount()
})

test('an agent that reaches 150 calls is still counted and shown', async ($, on) => {
  mock.clock(on)
  on('tool.call', () => ({ result: { text: 'ok' } }) as never)

  for (let i = 0; i < 150; i += 1) {
    await $.tool.call({ tool: 'Bash', command: 'ls', agentId: 'agent-long' } as never)
  }

  const ui = await $.ui.mount({ ...BAND, surface: 'terminal' } as never)
  expect(await ui.find({ type: 'Text', text: /longest 150 calls/ })).toBeDefined()
  await ui.unmount()
})
