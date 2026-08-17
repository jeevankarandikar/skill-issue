#!/usr/bin/env python3
"""PreToolUse guard for Write/Edit/NotebookEdit.

Together with bash_guard.py's WRONG_ROOT rule this is the whole filesystem policy -
config/CLAUDE.md used to restate it in prose and the two disagreed: the prose claimed
Desktop, Downloads, and ~/Documents were off limits while this guard allowed all
three. The prose is gone; the guard now covers what it claimed.

Exit 2 blocks the call and returns stderr to Claude; exit 0 allows.
Run `file_guard.py --selftest` to check.
"""
import json
import os
import re
import sys

HOME = os.path.expanduser("~")
BAD = (
    re.compile(rf"^{re.escape(HOME)}/Developer/[^/]+$"),             # loose file at Developer root
    re.compile(rf"^{re.escape(HOME)}/Developer/(?!GitHub/)[^/]+/"),  # dir tree beside GitHub/
    re.compile(rf"^{re.escape(HOME)}/Documents(/|$)"),               # incl. retired Documents/GitHub
    re.compile(rf"^{re.escape(HOME)}/Desktop(/|$)"),
    re.compile(rf"^{re.escape(HOME)}/Downloads(/|$)"),
)
MSG = ("BLOCKED: files go in ~/Developer/GitHub/<repo> (or the session scratchpad), "
       "never ~/Developer root, ~/Documents, Desktop, or Downloads. Design artifacts "
       "go in <repo>/.design-refs/.")


def verdict(path: str, cwd: str = ""):
    """return (exit_code, message). 2 = block, 0 = allow."""
    if not isinstance(path, str) or not path:
        return 0, ""
    # A bare `re.match` on the raw string let `~/Developer/loose.txt` and plain
    # `loose.txt` slip past: neither starts with the expanded home path.
    resolved = os.path.abspath(
        os.path.join(cwd or os.getcwd(), os.path.expanduser(path)))
    if any(p.match(resolved) for p in BAD):
        return 2, MSG
    return 0, ""


def _selftest() -> None:
    # ponytail: smallest check that fails if the guard logic breaks
    assert verdict(f"{HOME}/Developer/screenshot.png")[0] == 2
    assert verdict(f"{HOME}/Developer/design-screens/a.png")[0] == 2
    assert verdict(f"{HOME}/Documents/GitHub/x/file.py")[0] == 2
    assert verdict(f"{HOME}/Developer/GitHub/cnew/portal/page.tsx")[0] == 0
    assert verdict(f"{HOME}/Developer/GitHub")[0] == 2  # a FILE named GitHub
    assert verdict("/tmp/scratch/x.md")[0] == 0
    assert verdict("")[0] == 0
    # coverage the prose claimed and this guard used to allow
    assert verdict(f"{HOME}/Documents/notes.md")[0] == 2
    assert verdict(f"{HOME}/Desktop/mock.png")[0] == 2
    assert verdict(f"{HOME}/Downloads/x.md")[0] == 2
    # tilde and relative forms used to bypass the anchored match entirely
    assert verdict("~/Developer/loose.txt")[0] == 2
    assert verdict("loose.txt", f"{HOME}/Developer")[0] == 2
    assert verdict("src/app.ts", f"{HOME}/Developer/GitHub/cnew")[0] == 0
    print("selftest ok")


def main() -> None:
    if "--selftest" in sys.argv:
        _selftest()
        return
    try:
        event = json.load(sys.stdin)
    except Exception:
        sys.exit(0)  # malformed event, fail open rather than block everything
    tool_input = event.get("tool_input") or {}
    path = tool_input.get("file_path") or tool_input.get("notebook_path", "")
    cwd = event.get("cwd") or tool_input.get("cwd") or os.getcwd()
    code, message = verdict(path, cwd)
    if code == 2:
        print(message, file=sys.stderr)
    sys.exit(code)


if __name__ == "__main__":
    main()
