---
name: universal-memory
description: Set up and maintain a layered agent memory that survives every session and every project - a SOUL file (how the agent should behave, always), a MEMORY file (durable facts about the user), and per-project CLAUDE.md files (project rules). Use at first setup ("set up my memory", "make claude remember me"), whenever the user gives a correction or preference worth keeping ("remember this", "always do X", "stop doing Y"), and at the end of substantial sessions to bank learnings. The failure this prevents: re-teaching the agent the same things every session.
---

# universal-memory

Three layers, one law each. Everything the user ever teaches the agent lands in
exactly one of them:

| layer | file | carries | example |
|---|---|---|---|
| SOUL | `~/.claude/SOUL.md` | values + behavior, project-independent | "verify after each step", "surgical diffs only" |
| MEMORY | `~/.claude/MEMORY.md` | durable facts about the user | "prefers pnpm", "CS student at X", "main machine is an M2 Air" |
| project | `<repo>/CLAUDE.md` | rules true only in that repo | "tests run with `make check`", "never touch legacy/" |

`~/.claude/CLAUDE.md` imports the first two with `@~/.claude/SOUL.md` and
`@~/.claude/MEMORY.md`, so every session in every project loads them
automatically. That is the whole trick - no copying memory between chats, no
hand-made memory.md transfers.

## First-time setup

1. If `~/.claude/SOUL.md` / `~/.claude/MEMORY.md` don't exist, copy them from
   [templates/SOUL.md](templates/SOUL.md) and [templates/MEMORY.md](templates/MEMORY.md).
2. Ensure `~/.claude/CLAUDE.md` exists and contains both `@` imports - the
   repo's `templates/CLAUDE.global.md` is the starter (imports + routing rules).
3. Interview the human - five questions, one message: what they do, their
   stack/tools, machine, the agent habit that most annoys them, how they like
   answers (terse vs explanatory). Write the answers into MEMORY (facts) and
   SOUL (the annoyance, inverted into a rule).
4. Tell them the ongoing contract: say "remember this" and it gets filed; say
   it wrong once and correcting it once is enough.

## The maintenance discipline (the part that keeps it useful)

- **A correction becomes a file edit, immediately.** User says "stop doing X" →
  SOUL gets a rule. User states a fact → MEMORY. Project-local rule → that
  project's CLAUDE.md. Never just apologize and move on.
- **One home per rule.** If it's in SOUL, no project file repeats it. Duplicated
  rules drift and contradict.
- **Prune, don't append.** These files are loaded every session - a stale rule
  misleads and costs context forever. When editing, delete what no longer holds.
  If SOUL gets long, it is failing at its job.
- **Facts change; check dates.** Convert "next month" to absolute dates when
  writing MEMORY. When a fact expires (job, school, machine), update the line,
  don't stack a new one under it.
- **Never wipe without an explicit ask.** Updates yes, resets no.
- **Session end**: if the session produced a durable learning (a preference
  surfaced, a workflow decided, a mistake worth not repeating), file it before
  finishing. Working state and one-off details stay out - memory is for what
  the next session needs, not a diary.

## When MEMORY outgrows a page: the index tier

Both files are loaded whole every session - that only works while they stay
small. When MEMORY.md starts crowding a page, split it:

1. One fact per file in `~/.claude/memory/`, short kebab-case names
   (`prefers-pnpm.md`, `thesis-deadline.md`), a one-line body each.
2. MEMORY.md becomes the index: `- [prefers pnpm](memory/prefers-pnpm.md) -
   one-line hook` per fact. The index stays always-loaded; a fact's body gets
   read only when its topic comes up.
3. Same discipline applies: update the fact file, keep the index line honest,
   delete both when stale.

This keeps the always-loaded cost flat forever. The third tier, when memory
outgrows loose facts entirely, is the LLM-wiki pattern: a real vault of linked
plain-text notes (Obsidian or similar) that the agent reads, links, and grows -
searched on demand, never bulk-loaded. Same law all the way up: plain files you
own, an index that stays small, bodies fetched when relevant. This skill covers
the first two tiers; the vault tier is its own setup on the same principles.

## What does NOT go in memory

Code structure (the repo shows it), git history, anything derivable by reading
the project, one-conversation context, and secrets - never API keys, passwords,
or tokens in any memory file.
