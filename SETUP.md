# Install

Clone the repository once. Every install below points at the clone, so `git pull` updates them.

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

## On a machine with an older setup

The install adds one link and touches nothing else, so existing skills, hooks and settings stay as they are.

If the skills directory already holds an older copy of `design-jeev` as a real directory, the script above refuses to replace it. Move the old copy out, then run the script again:

```bash
mv "$(cd ~/.claude/skills && pwd -P)/design-jeev" ~/design-jeev-old
```

A brand design skill stays where it is. `design-jeev` loads it alongside itself and lets it decide color, type, logo, voice and components. To make that reliable, name the brand skill under Canon in each repository's `DESIGN.md` that uses it.

## The writing guard

Claude Code only. Run the installer once:

```bash
python3 ~/Developer/GitHub/skill-issue/writing-guard/install.py
```

It adds the guard to the `hooks` block of `~/.claude/settings.json`, keeps every other entry, and saves a copy of the file beside it the first time. Start a new session. The guard gives the model the rules at the start of each session, so there is nothing to paste.

If an older writing hook is already wired in that file, remove its entry, since both would block the same text with different messages.

To take the guard out:

```bash
python3 ~/Developer/GitHub/skill-issue/writing-guard/install.py --remove
```

## The fleet-gauge mod

Claude Code only. Load it for one session:

```bash
claude --plugin-dir ~/Developer/GitHub/skill-issue/fleet-gauge
```

To load it every time, add this to the `env` block of `~/.claude/settings.json`:

```json
"CLAUDE_CODE_PLUGIN_DIRS": "~/Developer/GitHub/skill-issue/fleet-gauge"
```
