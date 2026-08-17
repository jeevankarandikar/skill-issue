# agent setup playbook

You are an AI agent (Claude Code, Cursor, or Codex) setting this kit up for
your human. They pasted the repo link and asked you to set it up. Do the steps
in order. Everything is idempotent - safe to re-run.

## 1. detect where you are

- **Claude Code**: skills in `~/.claude/skills`, plugins exist - every step applies.
- **Cursor**: skills in `~/.cursor/skills`; skip step 3 (plugins are Claude Code only).
- **Codex**: no skills dir - merge the skill descriptions into `~/.codex/AGENTS.md`
  as an index the agent can follow to each SKILL.md; skip steps 3 and 7's hooks.

## 2. install the skills

```bash
git clone https://github.com/jeevankarandikar/skill-issue.git ~/Developer/GitHub/skill-issue
mkdir -p ~/.claude/skills
for d in ~/Developer/GitHub/skill-issue/*/; do
  [ -f "$d/SKILL.md" ] && ln -sfn "${d%/}" ~/.claude/skills/"$(basename "$d")"
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

## 7. guard hooks + the save command (Claude Code only)

Copy, don't symlink (the human may edit their copies):

```bash
mkdir -p ~/.claude/hooks ~/.claude/commands
cp ~/Developer/GitHub/skill-issue/hooks/*.py ~/.claude/hooks/
cp ~/Developer/GitHub/skill-issue/commands/save.md ~/.claude/commands/
python3 ~/.claude/hooks/bash_guard.py --selftest
```

Then wire both hooks into `~/.claude/settings.json` (merge, don't clobber):

```json
{
  "hooks": {
    "PreToolUse": [
      {"matcher": "Bash",
       "hooks": [{"type": "command", "command": "python3 \"$HOME/.claude/hooks/bash_guard.py\""}]},
      {"matcher": "Write|Edit|NotebookEdit",
       "hooks": [{"type": "command", "command": "python3 \"$HOME/.claude/hooks/file_guard.py\""}]}
    ]
  }
}
```

What they buy: recursive rm outside temp dirs, force push, DROP TABLE,
hook-bypass flags, and commit trailers all get blocked BEFORE they run;
writes stay inside the project. `/save` banks a session's learnings into
changelog/journal/CLAUDE.md with one word.

## 8. verify, then report

1. `ls ~/.claude/skills` (or `~/.cursor/skills`) shows the thirteen skill dirs (plus obsidian ones if installed) - and NOT hooks/commands/templates (those aren't skills).
2. Ask the human to restart the app, then run `/design` or say "review this file" — the agent should announce the skill it loads.
3. Report to the human: what you installed, what you skipped and why, and the one-line pitch: *describe the task, the right skill fires on its own.*

Things only the human can do: restart the app, approve plugin permission
prompts, create a refero API key. Never install anything beyond this list
without asking.
