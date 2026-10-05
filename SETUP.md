# Install

Clone the repository once. Both installs below point at the clone, so `git pull` updates them.

```bash
git clone https://github.com/jeevankarandikar/skill-issue.git ~/Developer/GitHub/skill-issue
```

## The design skill

Link `design-jeev` into your agent's skills directory.

| Agent | Skills directory |
| --- | --- |
| Claude Code | `~/.claude/skills` |
| Cursor | `~/.cursor/skills` |
| Codex | `~/.agents/skills` |

```bash
SKILLS_DIR=~/.claude/skills # Change to ~/.cursor/skills or ~/.agents/skills.
mkdir -p "$SKILLS_DIR"
TARGET="$SKILLS_DIR/design-jeev"
if [ -e "$TARGET" ] && [ ! -L "$TARGET" ]; then
  echo "Refusing to replace an existing directory: $TARGET" >&2
  exit 1
fi
ln -sfn ~/Developer/GitHub/skill-issue/design-jeev "$TARGET"
```

Restart the agent. If you installed an older version of this repository, remove the links to skills that no longer exist:

```bash
find ~/.claude/skills ~/.cursor/skills ~/.agents/skills -maxdepth 1 -type l ! -exec test -e {} \; -print 2>/dev/null
```

That prints the broken links. Delete the ones it lists.

## The fleet-gauge mod

Claude Code only. Load it for one session:

```bash
claude --plugin-dir ~/Developer/GitHub/skill-issue/fleet-gauge
```

To load it every time, add this to the `env` block of `~/.claude/settings.json`:

```json
"CLAUDE_CODE_PLUGIN_DIRS": "~/Developer/GitHub/skill-issue/fleet-gauge"
```
