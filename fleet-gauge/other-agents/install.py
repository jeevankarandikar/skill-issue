#!/usr/bin/env python3
"""Set up the usage gauge for Cursor and Codex.

    python3 install.py            both, where their config folders exist
    python3 install.py --codex    only the ones named (--cursor, --codex)
    python3 install.py --remove   take it out again

Both get the call counter as a hook that runs after each tool call. Codex also
gets a status line showing context used and the five-hour and weekly limits,
unless its config already sets one. Cursor has no place to show limits.
Running it twice changes nothing.
"""
import json
import os
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
HOME = Path.home()
COUNTER = f'python3 "{HERE / "call_count.py"}"'
STATUS = 'status_line = ["model-with-reasoning", "context-used", "five-hour-limit", "weekly-limit", "git-branch"]'
MARK = "  # fleet-gauge"
# agent: (config folder, hook event, flag, entries nest under "hooks")
AGENTS = {
    "cursor": (HOME / ".cursor", "postToolUse", " --cursor", False),
    "codex": (Path(os.environ.get("CODEX_HOME") or HOME / ".codex"), "PostToolUse", "", True),
}


def save(path: Path, text: str) -> None:
    backup = path.with_name(path.name + ".before-fleet-gauge")
    if path.exists() and not backup.exists():
        backup.write_text(path.read_text())
    temp = path.with_name(f".{path.name}.tmp")
    temp.write_text(text)
    temp.replace(path)


def ours(entry) -> bool:
    return "call_count.py" in json.dumps(entry)


def hook(agent: str, remove: bool) -> str:
    root, event, flag, nested = AGENTS[agent]
    path = root / "hooks.json"
    if path.is_symlink():
        return f"{path} is a symlink, left alone"
    try:
        data = json.loads(path.read_text()) if path.exists() else {}
    except ValueError as error:
        return f"{path} is not valid JSON, left alone: {error}"
    if not isinstance(data, dict) or not isinstance(data.get("hooks", {}), dict):
        return f"{path} has an unexpected shape, left alone"
    before = json.dumps(data, sort_keys=True)
    hooks = data.setdefault("hooks", {})
    entries = [e for e in hooks.get(event, []) if not ours(e)]
    if not remove:
        command = {"command": COUNTER + flag, "timeout": 10}
        entries.append({"hooks": [{"type": "command", **command}]} if nested else command)
        if agent == "cursor":
            data.setdefault("version", 1)
    if entries:
        hooks[event] = entries
    else:
        hooks.pop(event, None)
    if json.dumps(data, sort_keys=True) == before:
        return f"no change: {path}"
    save(path, json.dumps(data, indent=2) + "\n")
    return f"{'removed from' if remove else 'installed in'} {path}"


def status_line(remove: bool) -> str:
    path = AGENTS["codex"][0] / "config.toml"
    text = path.read_text() if path.exists() else ""
    line = STATUS + MARK
    if remove:
        if line not in text:
            return f"no change: {path}"
        new = text.replace(line + "\n", "")
    elif re.search(r"^\s*status_line\s*=", text, re.M):
        return f"{path} already sets a status line, left alone"
    elif re.search(r"^\[tui\]\s*$", text, re.M):
        new = re.sub(r"^\[tui\]\s*$", "[tui]\n" + line, text, count=1, flags=re.M)
    else:
        new = text + ("" if not text or text.endswith("\n") else "\n") + f"\n[tui]\n{line}\n"
    try:
        import tomllib
        tomllib.loads(new)
    except ImportError:
        pass
    except ValueError as error:
        return f"{path} would not parse after the edit, left alone: {error}"
    save(path, new)
    return f"status line {'removed from' if remove else 'set in'} {path}"


def main() -> None:
    remove = "--remove" in sys.argv
    named = [a for a in AGENTS if f"--{a}" in sys.argv]
    chosen = named or [a for a in AGENTS if AGENTS[a][0].is_dir()]
    for agent in chosen:
        print(f"{agent}: {hook(agent, remove)}")
        if agent == "codex":
            print(f"codex: {status_line(remove)}")
    if chosen:
        print("Start a new session in each agent.")
    if "codex" in chosen and not remove:
        print("Codex skips new hooks until you trust them: open codex, type /hooks, press t.")


if __name__ == "__main__":
    main()
