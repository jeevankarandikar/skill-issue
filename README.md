# skill-issue

10 Claude Code skills I've built up and actually use. design, code quality, testing, iOS/Swift, Python, prose editing, engineering research, done checks, and a skill that stops Claude from truncating everything.

each skill handles multiple modes instead of being a single-purpose wrapper.

---

## the skills

| skill | invoke | what it does |
| ----- | ------ | ------------ |
| `/design` | `/design [mode]` | 14 modes: surface layout, full-app design, critique, polish, redesign, brutalist, minimal, high-end. covers the full design workflow in one skill |
| `/tune` | `/tune` | dial adjustments after `/design`. tweak color, motion, spacing, or density without starting over |
| `/check` | `/check [audit\|harden\|normalize\|adapt\|optimize]` | code quality audit, security hardening, env normalization, API adaptation, Core Web Vitals + bundle perf |
| `/test` | `/test [eval\|char]` | two modes: `eval` for AI capability benchmarking (define evals before you build), `char` for freezing current behavior as tests before a big refactor |
| `/ios` | `/ios` | Swift/SwiftUI patterns, Swift 6 concurrency, HIG compliance |
| `/python` | `/python` | Python conventions, type hints, uv, idiomatic patterns |
| `/paulgraham` | `/paulgraham` | rewrites your prose the way PG writes: short sentences, direct claims, cut everything that doesn't need to be there |
| `/research` | `/research [topic]` | engineering research harness: fans out parallel gatherers (papers, OSS repos, ecosystem) on cheap models, synthesizes on a strong one, lands a cited adopt/skip/watchlist memo mapped to your repo |
| `/verify` | `/verify` | checks a diff against the original goal and catches fake-done shortcuts before you mark work complete |
| `full-output-enforcement` | auto-fires | stops Claude from truncating code with `// ...` or "I can provide more if needed." handles token-limit splits cleanly |

---

## setup

you need [Claude Code](https://claude.ai/code). two steps.

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

# writing
/paulgraham               # rewrite in PG style

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
