# fleet-gauge

`fleet-gauge` is a Claude Code mod that warns when usage needs a decision. It needs Claude Code 2.1.287 or later. Cursor and Codex get a smaller version, described at the end.

A row appears above the prompt only when one of these is true:

- the weekly limit is at 50% or more
- the five-hour limit is at 70% or more
- the session's context is at 200k tokens or more
- a subagent is running, with the call count of the longest one

A toast fires when a subagent reaches 150 tool calls, and again at 300. An agent rereads its whole context on every call, so long agents cost the most.

`/fleet` prints every reading and lists the session's subagents by tool calls made.

## Load it

For one session:

```bash
claude --plugin-dir ~/Developer/GitHub/skill-issue/fleet-gauge
```

For every session, including the desktop app, add the path to `~/.claude/settings.json`:

```json
{
  "env": {
    "CLAUDE_CODE_PLUGIN_DIRS": "~/Developer/GitHub/skill-issue/fleet-gauge"
  }
}
```

Start a new session after changing it.

## Change the thresholds

They are constants at the top of the hooks module. Run `claude plugin test .` in this folder after an edit.

## Cursor and Codex

Neither agent lets a mod draw in its interface, so they get the parts that can be rebuilt.

```bash
python3 other-agents/install.py
```

- Both get a hook that counts tool calls in a session. At 150 calls, and every 50 after, it tells the agent to finish the step in hand, write a handoff note and say a new session should take over. Set `FLEET_GAUGE_CALLS` to change the limit.
- Codex also gets a status line showing context used and the five-hour and weekly limits. Codex draws that itself; the installer only turns it on, and leaves a status line you already set alone.
- Cursor does not tell hooks about your usage and has no status row to write to, so there is no limits display there.

Codex skips a new hook until you trust it. Open Codex, type `/hooks`, and press `t`.

`python3 other-agents/install.py --remove` takes it out.
