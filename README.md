# skill-issue

the agent setup i actually use: twenty-one skills, guard hooks, a save command, and a memory layer that survives every session. works with claude code, cursor, and codex - anything that reads markdown skills, on hosted or open-source models.

each skill is small on purpose: a router, a few opinions, reference files it loads only when needed. no rule dumps - the model already knows how to code. these encode judgment: what to weigh, where the failure hides, when to stop.

## setup

paste this repo link into your agent and say "set this up". it follows [SETUP.md](SETUP.md) - skills, plugins, hooks, memory, all of it.

manual: clone it, symlink the skill folders into `~/.claude/skills` (or `~/.cursor/skills`), install the superpowers plugin so skills fire on intent. exact commands in SETUP.md.

## the skills

| skill | what it does |
| ----- | ------------ |
| `design-jeev` | the whole design pipeline: shape, taste rules, build, polish. `lab` mode renders directions to react to |
| `tune` | move one dial: bolder, quieter, colorize, distill, animate, clarify |
| `check` | production-readiness: audit, harden, normalize, adapt, optimize |
| `done-check` | the done check. greps the diff for shortcuts, runs your tests, maps requirements to hunks |
| `test` | build the measuring stick first: evals for AI behavior, characterization before refactors |
| `research` | cheap gatherers, one strong judge, cited memo mapped to your repo |
| `paulgraham` | stress-test a startup idea. five frameworks, one verdict |
| `ios` | swift and swiftui: concurrency, navigation, HIG review |
| `python` | uv-first conventions and the fastapi service shape |
| `i-have-adhd` | long replies shaped for ADHD: next action first, state restated |
| `apple-user-doc-prose` | user-doc voice: imperative, calm, plain |
| `html-default-style` | self-contained HTML house style, no CDN slop |
| `universal-memory` | the memory layer - see below |
| `unslop` | remove AI writing tells without inventing anything. compiled from a ten-skill bake-off; rule zero is never add a fact the source lacks |
| `variate` | design variations of one file on your own localhost, flipped with the arrow keys (vendored, MIT) |
| `defuddle` | clean markdown out of cluttered web pages (vendored from kepano, MIT) |
| `obsidian-markdown` | obsidian-flavored markdown: wikilinks, callouts, embeds, frontmatter (vendored from kepano, MIT) |
| `obsidian-bases` | obsidian .base files: views, filters, formulas (vendored from kepano, MIT) |
| `obsidian-cli` | drive an obsidian vault from the command line (vendored from kepano, MIT) |
| `json-canvas` | .canvas files: nodes, edges, groups (vendored from kepano, MIT) |
| `last30days` | what people said about a topic in the last 30 days, across reddit, x, youtube, hn (fork of mvanhorn's skill, MIT) |

skills fire on intent once superpowers is installed. or invoke by name: `/design-jeev`, `/check audit`, `/done-check`.

## memory

three files, one law each. SOUL = how it behaves, always. MEMORY = what it knows about you. project CLAUDE.md = repo rules. all loaded every session, so nothing gets re-taught, and a correction becomes a file edit on the spot. templates in [universal-memory/templates](universal-memory/templates/), global wiring in [templates/CLAUDE.global.md](templates/CLAUDE.global.md).

and no - you don't hand-make memory.md files when context fills. sessions auto-compact.

## hooks + commands

[hooks/bash_guard.py](hooks/bash_guard.py) blocks the irreversible stuff before it runs: recursive rm outside temp dirs, force push, `DROP TABLE`, hook-bypass flags, commit trailers. [hooks/file_guard.py](hooks/file_guard.py) keeps writes inside the project. [commands/save.md](commands/save.md) banks a session's learnings with one word. wiring is SETUP step 7.

## your own skills

drop a directory with a `SKILL.md` in `~/.claude/skills/`:

```yaml
---
name: your-skill
description: Use when [what should trigger it]
---
```

the description is the router - if a skill isn't firing, fix the description, don't write routing tables.

## why the skills are shaped like this

**progressive disclosure.** `design-jeev` used to be 1091 lines that loaded whether you wanted them or not. detail moved behind reference files read on demand.

**opinions over rules.** the font section used to ban 23 typefaces. now it says the reflex pick is the problem - shorter, and actually true.

**one owner per fact.** motion durations live in one file. severity levels in one file. everything else points at them.
