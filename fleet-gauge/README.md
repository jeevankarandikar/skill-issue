# fleet-gauge

A Claude Code mod that warns when usage needs a decision. It needs Claude Code 2.1.287 or later.

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
