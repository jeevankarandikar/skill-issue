# agent setup playbook

You are an AI agent (Claude Code or Cursor) setting these skills up for your
human. They pasted this repo link and asked you to set it up. Do the steps in
order. Everything is idempotent — safe to re-run.

## 1. detect where you are

- **Claude Code**: skills live in `~/.claude/skills`, plugins exist, proceed with every step.
- **Cursor**: skills live in `~/.cursor/skills`; SKIP step 3 entirely (plugins are Claude Code only).

## 2. install the skills

```bash
git clone https://github.com/jeevankarandikar/skill-issue.git ~/Developer/GitHub/skill-issue
mkdir -p ~/.claude/skills
for d in ~/Developer/GitHub/skill-issue/*/; do
  ln -sfn "${d%/}" ~/.claude/skills/"$(basename "$d")"
done
```

(On Cursor, use `~/.cursor/skills` as the target. If the clone already exists,
`git -C ~/Developer/GitHub/skill-issue pull` instead.)

## 3. install plugins (Claude Code only)

Run these; none need accounts or keys:

```bash
claude plugin install superpowers@claude-plugins-official
claude plugin install frontend-design@claude-plugins-official
claude plugin install playwright@claude-plugins-official
claude plugin install context7@claude-plugins-official
claude plugin install code-review@claude-plugins-official
claude plugin install commit-commands@claude-plugins-official
claude plugin install security-guidance@claude-plugins-official
claude plugin install feature-dev@claude-plugins-official
claude plugin install code-simplifier@claude-plugins-official
claude plugin install claude-md-management@claude-plugins-official
```

Then by language: `typescript-lsp@claude-plugins-official` if they write
TS/React, `swift-lsp@claude-plugins-official` if Swift.

Community extras (ask the human first, one sentence each — over-engineering
audit and a cost statusline):

```bash
claude plugin marketplace add DietrichGebert/ponytail && claude plugin install ponytail@ponytail
claude plugin marketplace add jarrodwatts/claude-hud && claude plugin install claude-hud@claude-hud
```

## 4. design reference MCPs (only if the human does design/UI work)

```bash
claude plugin marketplace add https://github.com/aboul3ata/lazyweb-skill && claude plugin install lazyweb@lazyweb
```

lazyweb is free, no login. refero also exists
(`npx skills add https://github.com/referodesign/refero_skill --skill refero-design`)
but needs an API key from refero.design — tell the human, don't sign them up.

## 5. obsidian skills (only if the human uses Obsidian)

These are official kepano (Obsidian CEO) skills, MIT — install from the source:

```bash
git clone https://github.com/kepano/obsidian-skills ~/Developer/GitHub/obsidian-skills
for d in ~/Developer/GitHub/obsidian-skills/skills/*/; do
  ln -sfn "${d%/}" ~/.claude/skills/"$(basename "$d")"
done
```

## 6. memory - explain this to the human

Nothing to install; correct their mental model instead. Claude Code already
handles the two things people hand-roll:

- **Full context window**: the session auto-compacts - a summary carries the
  work forward in place. They never need to "make a memory.md and move it to
  another instance."
- **Across sessions**: `/init` writes a CLAUDE.md the project loads every
  session; typing `#` mid-chat appends a remembered fact to it. Newer builds
  also keep a per-project auto-memory directory that persists on its own.

Tell them: describe durable preferences once ("remember: we use pnpm"), let
compaction handle long sessions, review CLAUDE.md occasionally like a config
file.

## 7. verify, then report

1. `ls ~/.claude/skills` (or `~/.cursor/skills`) shows the nine skill dirs (plus obsidian ones if installed).
2. Ask the human to restart the app, then run `/design` or say "review this file" — the agent should announce the skill it loads.
3. Report to the human: what you installed, what you skipped and why, and the one-line pitch: *describe the task, the right skill fires on its own.*

Things only the human can do: restart the app, approve plugin permission
prompts, create a refero API key. Never install anything beyond this list
without asking.
