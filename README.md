# skill-issue

thirteen Claude Code skills I actually use. each one is deliberately small: a router, a handful of opinions, and reference files it loads only when it needs them.

they're written for Claude 5, which mostly means they don't tell Claude how to write code. a skill that enumerates twenty rules teaches the model that rule twenty-one doesn't matter. these encode the judgment calls instead: what to weigh, what the non-obvious failure is, where the boundary with the next skill sits.

---

## the skills

| skill | invoke | what it does |
| ----- | ------ | ------------ |
| `/design` | `/design [mode]` | the whole design pipeline: shape a surface, commit to taste rules, build it, polish the micro-interactions. `lab` renders real directions to react to when a project has no design context yet. owns the canonical motion timings and the AI-slop tells the other skills reference |
| `/tune` | `/tune [dial]` | move one dimension of something that already exists: bolder, quieter, colorize, distill, typeset, animate, delight, clarify, overdrive |
| `/check` | `/check [audit\|harden\|normalize\|adapt\|optimize]` | production-readiness on a surface as it stands: score it, harden it against hostile input and i18n, fix design-system drift, adapt it across devices, or chase Core Web Vitals |
| `/verify` | `/verify` | the done check. greps the diff for shortcuts, runs your test command itself, maps every requirement to the hunk that satisfies it. built to be run by a fresh subagent, because the model that wrote the code is the worst judge of it |
| `i-have-adhd` | auto | shapes every long reply for ADHD reading: the next action first, numbered steps, state restated so nothing lives only in scrollback |
| `apple-user-doc-prose` | auto | Apple-style user documentation voice: imperative steps, a 12-point pass/fail rubric, before/after examples |
| `html-default-style` | auto | house style for self-contained HTML artifacts: no CDNs, light/dark, an anti-AI-slop checklist, a copy-paste starter |
| `universal-memory` | auto + setup | layered agent memory: a SOUL file (behavior, always), MEMORY file (your facts), project CLAUDE.md - with the maintenance discipline that keeps them from rotting |
| `/test` | `/test [eval\|char]` | build the measuring stick first. `eval` for AI behavior (pass@k vs pass^k, judge calibration), `char` to freeze behavior before a refactor |
| `/research` | `/research [topic]` | fans gatherers out on cheap models, judges once on a strong one, returns a cited memo of validated / adopt now / skip / watchlist, mapped to files in your repo |
| `/paulgraham` | `/paulgraham [framework]` | stress-test a startup idea before a month goes into it. five frameworks, one verdict: strong, weak, or pivot |
| `/ios` | `/ios [mode]` | Swift and SwiftUI: @Observable, concurrency and actor isolation, type-safe navigation, HIG and accessibility review |
| `/python` | `/python [fastapi]` | uv-first project conventions and the FastAPI service shape underneath them |

---

## why they're shaped like this

three things changed in the july 2026 pass:

**progressive disclosure.** `/design` used to be 1091 lines that loaded whether you wanted the brutalist mode or not. `/python` was 484 lines, most of it explaining comprehensions and decorators to a model that already knows them. the detail moved behind reference files the skill reads on demand.

**opinions over rules.** the font section used to ban 23 named typefaces. it now says the reflex pick is the problem, which is both shorter and actually true: a ban list quietly teaches Claude that the other 1400 fonts are fine.

**one owner per fact.** motion durations live in exactly one file. severity levels live in exactly one file. everything else points at them. before, three files carried three different `--ease-out` curves plus a note explaining which one won.

---

## setup

**the lazy way (recommended):** paste this repo link into Claude Code or Cursor and say *"set this up for me"* — the agent follows [SETUP.md](SETUP.md), an agent-executable playbook covering skills, plugins, design MCPs, and the official Obsidian skills.

**the manual way:** you need [Claude Code](https://claude.ai/code). two steps.

**1. install the superpowers plugin** (this is what makes skills auto-invoke):

open Claude Code and run:
```
claude plugin install superpowers@claude-plugins-official
```

**2. clone the skills into `~/.claude/skills/`:**

```bash
git clone https://github.com/jeevankarandikar/skill-issue.git /tmp/skill-issue
mkdir -p ~/.claude/skills
cp -r /tmp/skill-issue/* ~/.claude/skills/
rm -rf /tmp/skill-issue
```

restart Claude Code. type `/design critique` or `/check audit` to verify.

---

## how it works

once superpowers is installed, skills auto-fire when relevant. you can also invoke any skill directly by name.

```bash
# ui work
/design full-app          # full-app layout + component system
/tune                     # adjust after first pass

# before a big refactor
/test char                # freeze current behavior as tests first
# after shipping
/check audit              # quality pass
/verify                   # done check before marking work complete

# before building at all
/paulgraham               # stress-test the idea

# platform-specific
/ios                      # Swift/SwiftUI
/python                   # Python
```

---

## adding your own skills

create a directory in `~/.claude/skills/` with a `SKILL.md` file. the frontmatter needs at minimum:

```yaml
---
name: your-skill-name
description: Use when [triggering conditions]
---
```

superpowers picks it up on restart.

---

## updating

```bash
cd /tmp && git clone https://github.com/jeevankarandikar/skill-issue.git
cp -r skill-issue/* ~/.claude/skills/
rm -rf skill-issue
```
