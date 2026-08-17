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

## 6. universal memory - set it up

Run the `universal-memory` skill's first-time setup (it's in the set you just
installed - read universal-memory/SKILL.md and follow "First-time setup"):
copy its templates to `~/.claude/SOUL.md` and `~/.claude/MEMORY.md`, wire the
`@` imports into `~/.claude/CLAUDE.md`, then interview the human (five
questions, one message) and seed both files from the answers.

Result: a behavior layer (SOUL) and a fact layer (MEMORY) load in every
session of every project, and from now on any correction or "remember this"
gets filed into the right layer automatically. Also correct the common myth:
context-window overflow is handled by auto-compaction - no hand-made
memory.md transfers, ever.

## 7. verify, then report

1. `ls ~/.claude/skills` (or `~/.cursor/skills`) shows the nine skill dirs (plus obsidian ones if installed).
2. Ask the human to restart the app, then run `/design` or say "review this file" — the agent should announce the skill it loads.
3. Report to the human: what you installed, what you skipped and why, and the one-line pitch: *describe the task, the right skill fires on its own.*

Things only the human can do: restart the app, approve plugin permission
prompts, create a refero API key. Never install anything beyond this list
without asking.
