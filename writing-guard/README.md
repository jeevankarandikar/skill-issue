# writing-guard

`writing-guard` is a hook for Claude Code, Cursor and Codex that blocks machine-sounding prose before it lands. The rules are in [RULES.md](RULES.md). The guard enforces the ones a pattern can catch, in prose files as they are written and in chat replies before they are sent.

It is one Python file with no dependencies, plus an installer that adds it to your settings.

## Install

```bash
python3 install.py
```

It wires the guard into every one of the three agents whose config folder it finds. Name agents to limit it, for example `python3 install.py --cursor`. Start a new session afterwards. `python3 install.py --remove` takes it out again.

Codex skips a new or changed hook until you trust it, and it does so without a warning. Open Codex, type `/hooks`, and press `t` to trust the ones listed. Until then the guard is installed and does nothing there.

## How it behaves

- At the start of a session, and again after the context is compacted, it gives the model the rules list from `RULES.md`. Nothing has to be pasted into a `CLAUDE.md`.
- On a Write or Edit to a prose file that breaks a rule, the tool call is refused and the model gets the offending snippet back, so it rewrites and tries again.
- On a reply that breaks a rule, the stop is refused once with the snippet. The second attempt always goes through, so a reply that has to discuss a banned phrase cannot loop.
- An Edit is judged on what it adds. A file that already holds an em dash can still be edited, as long as the edit does not add another.
- A malformed hook event is allowed through.

## What differs by agent

| | Claude Code | Codex | Cursor |
| --- | --- | --- | --- |
| Rules given at session start | yes | yes | yes |
| Prose file writes refused | yes | yes, read from `apply_patch` | yes |
| Replies | stop refused once | stop refused once | sent, then one follow-up asks for a rewrite |

Cursor has no way to hold a reply back, so the broken reply is shown and the agent is told to redo it.

## Exemptions

Files that must quote what the rules ban, such as a style guide, are skipped when their path contains a fragment listed in `WRITING_GUARD_EXEMPT`. Separate fragments with colons and set the variable in the `env` block of `~/.claude/settings.json`:

```json
"WRITING_GUARD_EXEMPT": "/docs/style-guide.md:/quotes/"
```

This folder is always exempt.

## Check it

```bash
python3 writing_guard.py --selftest
```
