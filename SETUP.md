# Install

Clone the repository, then run the installer:

```bash
git clone https://github.com/jeevankarandikar/skill-issue.git ~/Developer/GitHub/skill-issue
```

```bash
python3 ~/Developer/GitHub/skill-issue/install.py
```

It finds which of Claude Code, Cursor and Codex you have, links the design skill into each and wires the writing guard into each one's hooks. Start a new session in each agent afterwards.

Codex skips a new or changed hook until you trust it, and it does so without a warning. Open Codex, type `/hooks`, and press `t` to trust the ones listed. Until then the hooks are installed and do nothing there.

Everything points at the clone, so `git pull` updates it, and `install.py --remove` takes it out.

It also sets up the usage gauge for Cursor and Codex. The Claude Code gauge is a mod with its own step at the end of this page. The sections below do each part by hand.

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

Works in Claude Code, Cursor and Codex. To install it alone:

```bash
python3 ~/Developer/GitHub/skill-issue/writing-guard/install.py
```

It adds the guard to `~/.claude/settings.json`, `~/.cursor/hooks.json` and `~/.codex/hooks.json`, whichever exist, keeps every other entry, and saves a copy of each file beside it the first time. The guard gives the model the rules at the start of each session, so there is nothing to paste.

In Codex, trust the new hooks with `/hooks` as described at the top of this page.

If an older writing hook is already wired in one of those files, remove its entry, since both would block the same text with different messages.

## The fleet-gauge mod

In Claude Code it is a mod. Load it for one session:

```bash
claude --plugin-dir ~/Developer/GitHub/skill-issue/fleet-gauge
```

To load it every time, add this to the `env` block of `~/.claude/settings.json`:

```json
"CLAUDE_CODE_PLUGIN_DIRS": "~/Developer/GitHub/skill-issue/fleet-gauge"
```

For Cursor and Codex alone:

```bash
python3 ~/Developer/GitHub/skill-issue/fleet-gauge/other-agents/install.py
```
