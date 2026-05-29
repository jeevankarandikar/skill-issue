# claude-skills

A consolidated Claude Code skill kit — 8 general-purpose skills covering design, code quality, testing, iOS/Swift, Python, writing, and output completeness.

## Skills

| Skill | Invoke | What it does |
|-------|--------|-------------|
| `check` | `/check [audit\|harden\|normalize\|adapt\|optimize]` | Code quality, security hardening, env normalization, API adaptation, perf audits |
| `design` | `/design [mode]` | 14-mode UI/UX system (surface, full-app, critique, polish, redesign, brutalist, minimal, high-end, and more) |
| `full-output-enforcement` | auto-fires | Prevents truncated code — no `// ...`, no skeleton outputs, handles token-limit splits cleanly |
| `ios` | `/ios` | Swift/SwiftUI patterns, Swift 6 concurrency, HIG compliance |
| `paulgraham` | `/paulgraham` | Edits prose to Paul Graham's style — short sentences, direct claims, cut filler |
| `python` | `/python` | Python conventions, type hints, uv, idiomatic patterns |
| `test` | `/test [eval\|char]` | AI eval harnesses (EDD) + characterization tests before refactors |
| `tune` | `/tune` | Design dial adjustments — tweak color, motion, spacing, density after `/design` |

## Setup (2 steps)

### 1. Install the Skill runtime

Skills need a Skill tool to auto-invoke. Install `superpowers` from the Claude Code marketplace:

```
# In Claude Code, run:
/install-plugin superpowers
```

Or go to **Claude Code → Settings → Plugins → Browse** and install `superpowers@claude-plugins-official`.

> **No plugin?** Skills still work — just paste the relevant SKILL.md into your conversation and tell Claude to follow it.

### 2. Clone skills into `~/.claude/skills/`

```bash
git clone https://github.com/jeevankarandikar/claude-skills.git /tmp/claude-skills-setup
cp -r /tmp/claude-skills-setup/* ~/.claude/skills/
rm -rf /tmp/claude-skills-setup
```

Or clone directly:
```bash
git clone https://github.com/jeevankarandikar/claude-skills.git ~/.claude/skills
```

> If `~/.claude/skills/` already has files, use the `cp` approach above to merge.

Restart Claude Code and the skills are live. Type `/design critique` or `/check audit` to verify.

## Updating

```bash
cd ~/.claude/skills  # or wherever you cloned it
git pull
```

## What's NOT included

Personal skills (`voice`, `coding-profile`) live in a private repo — they contain personal writing history, application drafts, and project conventions specific to one person.
