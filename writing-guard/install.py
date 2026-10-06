#!/usr/bin/env python3
"""Wire the writing guard into Claude Code's user settings.

    python3 install.py           add the hooks
    python3 install.py --remove  take them out

It edits the `hooks` block of ~/.claude/settings.json (or the folder named by
CLAUDE_CONFIG_DIR) and leaves every other entry alone. Running it twice changes
nothing. The first change keeps a copy of the file beside it.
"""
import json
import os
import shutil
import sys
from pathlib import Path

GUARD = Path(__file__).resolve().parent / "writing_guard.py"
EVENTS = {"SessionStart": None, "PreToolUse": "Write|Edit|NotebookEdit", "Stop": None}


def ours(entry) -> bool:
    return isinstance(entry, dict) and any(
        "writing_guard.py" in str(h.get("command", ""))
        for h in entry.get("hooks", []) if isinstance(h, dict))


def main() -> None:
    root = Path(os.environ.get("CLAUDE_CONFIG_DIR") or Path.home() / ".claude")
    path = root / "settings.json"
    try:
        settings = json.loads(path.read_text()) if path.exists() else {}
    except ValueError as error:
        raise SystemExit(f"{path} is not valid JSON, nothing changed: {error}")
    if not isinstance(settings, dict) or not isinstance(settings.get("hooks", {}), dict):
        raise SystemExit(f"{path} has an unexpected shape, nothing changed")
    before = json.dumps(settings, sort_keys=True)
    hooks = settings.setdefault("hooks", {})
    for event, matcher in EVENTS.items():
        entries = hooks.get(event, [])
        if not isinstance(entries, list):
            raise SystemExit(f"{path}: hooks.{event} is not a list, nothing changed")
        entries = [e for e in entries if not ours(e)]
        if "--remove" not in sys.argv:
            entry = {"hooks": [{"type": "command", "command": f'python3 "{GUARD}"', "timeout": 10}]}
            if matcher:
                entry = {"matcher": matcher, **entry}
            entries.append(entry)
        if entries:
            hooks[event] = entries
        else:
            hooks.pop(event, None)
    if not hooks:
        settings.pop("hooks")
    if json.dumps(settings, sort_keys=True) == before:
        print(f"no change: {path}")
        return
    root.mkdir(parents=True, exist_ok=True)
    backup = path.with_name("settings.json.before-writing-guard")
    if path.exists() and not backup.exists():
        shutil.copy2(path, backup)
    path.write_text(json.dumps(settings, indent=2) + "\n")
    verb = "removed from" if "--remove" in sys.argv else "installed in"
    print(f"writing guard {verb} {path}. Start a new Claude Code session.")


if __name__ == "__main__":
    main()
