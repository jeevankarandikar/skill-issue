#!/usr/bin/env python3
"""Wire the writing guard into Claude Code, Cursor and Codex.

    python3 install.py            every agent whose config folder exists
    python3 install.py --cursor   only the ones named (--claude, --cursor, --codex)
    python3 install.py --remove   take the guard out again

It edits the hooks in ~/.claude/settings.json, ~/.cursor/hooks.json and
~/.codex/hooks.json, and leaves every other entry alone. Running it twice
changes nothing. The first change to a file keeps a copy beside it.
"""
import json
import os
import shutil
import sys
from pathlib import Path

GUARD = Path(__file__).resolve().parent / "writing_guard.py"
HOME = Path.home()
# agent: (config folder, hooks file, flag for the guard, nested entries, {event: matcher})
AGENTS = {
    "claude": (Path(os.environ.get("CLAUDE_CONFIG_DIR") or HOME / ".claude"), "settings.json", "", True,
               {"SessionStart": None, "PreToolUse": "Write|Edit|NotebookEdit", "Stop": None}),
    "cursor": (HOME / ".cursor", "hooks.json", " --cursor", False,
               {"sessionStart": None, "preToolUse": "Write|StrReplace|Edit",
                "afterAgentResponse": None, "stop": None}),
    "codex": (Path(os.environ.get("CODEX_HOME") or HOME / ".codex"), "hooks.json", " --codex", True,
              {"SessionStart": None, "PreToolUse": "^(apply_patch|Edit|Write)$", "Stop": None}),
}


def ours(entry) -> bool:
    if not isinstance(entry, dict):
        return False
    nested = [h for h in entry.get("hooks", []) if isinstance(h, dict)] if isinstance(entry.get("hooks"), list) else []
    return any("writing_guard.py" in str(h.get("command", "")) for h in [entry, *nested])


def wire(agent: str, remove: bool) -> str:
    root, filename, flag, nested, events = AGENTS[agent]
    path = root / filename
    try:
        data = json.loads(path.read_text()) if path.exists() else {}
    except ValueError as error:
        return f"{path} is not valid JSON, left alone: {error}"
    if not isinstance(data, dict) or not isinstance(data.get("hooks", {}), dict):
        return f"{path} has an unexpected shape, left alone"
    before = json.dumps(data, sort_keys=True)
    hooks = data.setdefault("hooks", {})
    if any(not isinstance(hooks.get(event, []), list) for event in events):
        return f"{path}: a hooks entry is not a list, left alone"
    command = f'python3 "{GUARD}"{flag}'
    for event, matcher in events.items():
        entries = [e for e in hooks.get(event, []) if not ours(e)]
        if not remove:
            hook = {"command": command, "timeout": 10}
            entry = {"hooks": [{"type": "command", **hook}]} if nested else hook
            entries.append({"matcher": matcher, **entry} if matcher else entry)
        if entries:
            hooks[event] = entries
        else:
            hooks.pop(event, None)
    if not hooks:
        data.pop("hooks")
    elif agent == "cursor":
        data.setdefault("version", 1)
    if json.dumps(data, sort_keys=True) == before:
        return f"no change: {path}"
    root.mkdir(parents=True, exist_ok=True)
    backup = path.with_name(f"{filename}.before-writing-guard")
    if path.exists() and not backup.exists():
        shutil.copy2(path, backup)
    temp = path.with_name(f".{filename}.tmp")
    temp.write_text(json.dumps(data, indent=2) + "\n")
    temp.replace(path)
    return f"{'removed from' if remove else 'installed in'} {path}"


def main() -> None:
    named = [a for a in AGENTS if f"--{a}" in sys.argv]
    chosen = named or [a for a in AGENTS if AGENTS[a][0].is_dir()]
    if not chosen:
        raise SystemExit("no Claude Code, Cursor or Codex config folder found; name one, for example --claude")
    for agent in chosen:
        print(f"{agent}: {wire(agent, '--remove' in sys.argv)}")
    print("Start a new session in each agent.")
    if "codex" in chosen and "--remove" not in sys.argv:
        print("Codex skips new hooks until you trust them: open codex, type /hooks, press t.")


if __name__ == "__main__":
    main()
