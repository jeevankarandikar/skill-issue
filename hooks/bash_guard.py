#!/usr/bin/env python3
"""PreToolUse guard for Bash.

This file is the policy, not a copy of it. SOUL used to also state the destructive-git
rule in prose; the two drifted (SOUL said "confirm first", the hook blocked outright),
so the prose was deleted and this is now the single statement of it.

A rule earns a place here when it is decidable from the command text alone, the
failure is irreversible, and there is no legitimate reason to want the exception.
Rules that fail the last test belong in prose, where judgment can apply. Rules that
generate false positives on read-only work are worse than no rule: they train you to
route around the guard.

Claude Code feeds the tool event as JSON on stdin. Exit 2 blocks the call and returns
stderr to Claude; exit 0 allows. Run `bash_guard.py --selftest` to check.
"""
import json
import os
import re
import sys

# A git trailer is a LINE beginning with the token, not the token anywhere in the
# text. Matching the substring blocked `grep -rln "Co-Authored-By"`, and then blocked
# a commit whose message *described* that bug. Anchor to line-start.
TRAILER_LINE = re.compile(r"^\s*(co-authored-by|signed-off-by)\s*:", re.I | re.M)

# recursive rm is allowed on throwaway paths...
TMP_OK = ("/tmp/", "/private/tmp/", "/private/var/folders/", "/var/folders/")

# ...and on things a build regenerates. Blocking these made /clean painful enough to
# route around, which is the failure mode this guard is supposed to prevent.
REGENERABLE = {
    "node_modules", ".next", ".nuxt", "dist", "build", ".build", "out",
    ".venv", "venv", "__pycache__", ".pytest_cache", ".mypy_cache",
    ".ruff_cache", "target", ".turbo", ".parcel-cache", "DerivedData",
}

# Irreversible git. No confirmation path: if you want one of these, you run it yourself.
DESTRUCTIVE_GIT = (
    "git reset --hard", "git push --force", "git push -f",
    "git clean -fd", "git checkout -- .", "git filter-repo",
    "git branch -d main", "git branch -d master",
)

# soul: "never skip hooks" - bypass flags only when the human explicitly asks
HOOK_BYPASS = ("--no-verify", "--no-gpg-sign")

# DDL only counts when a db client is actually being invoked. Matching the bare words
# blocked `grep -r "drop table" migrations/`.
DB_DESTRUCTIVE = re.compile(
    r"\b(psql|sqlite3|mysql|mariadb|duckdb|pg_dump)\b[^;|&]*"
    r"\b(drop|truncate)\s+table\b", re.I)




def _rm_targets(command: str):
    """Paths a recursive rm would delete, absolute or relative."""
    # strip the rm flags, then take the remaining bare words up to a shell separator
    body = re.sub(r"^.*?\brm\s+(-[a-zA-Z]+\s+)*", "", command, count=1, flags=re.S)
    body = re.split(r"[;|&]", body, maxsplit=1)[0]
    return [w.strip("'\"") for w in body.split() if w and not w.startswith("-")]


def verdict(command: str, cwd: str = ""):
    """return (exit_code, message). 2 = block, 0 = allow."""
    if not isinstance(command, str) or not command.strip():
        return 0, ""
    low = command.lower()

    # Only a real commit can carry a trailer. Matching the whole command line blocked
    # `grep -rn Co-Authored-By .` and `git log --grep=Co-Authored-By`, which are how
    # you'd audit for the problem in the first place.
    if "git commit" in low and (TRAILER_LINE.search(command)
                                or "--trailer" in low):
        return 2, ("BLOCKED: house style: no commit trailers. Remove the "
                   "Co-Authored-By / Signed-off-by line and retry.")

    hit = next((p for p in DESTRUCTIVE_GIT if p in low), None)
    if hit:
        return 2, (f"BLOCKED: {hit!r} is irreversible. If you meant it, run it "
                   "yourself - that is the confirmation.")
    # -D force-deletes unmerged branches; case-sensitive, so check pre-lowering
    if re.search(r"git\s+branch\s+(-[a-zA-Z]*D)", command):
        return 2, ("BLOCKED: git branch -D force-deletes unmerged work. "
                   "-d on merged branches is fine.")
    if DB_DESTRUCTIVE.search(command):
        return 2, "BLOCKED: dropping or truncating a table. run it yourself."

    bypass = next((f for f in HOOK_BYPASS if f in low), None)
    if bypass:
        return 2, (f"BLOCKED: {bypass} skips hooks. A failing hook is a signal, not "
                   "an obstacle; only the human bypasses it.")

    # trash-only rule: recursive rm outside temp/regenerable paths -> /usr/bin/trash
    if re.search(r"\brm\s+-[a-zA-Z]*[rR]", command):
        targets = _rm_targets(command)
        scratch = os.environ.get("CLAUDE_SCRATCHPAD", "")

        def disposable(p: str) -> bool:
            if p.startswith(TMP_OK) or (scratch and p.startswith(scratch)):
                return True
            return os.path.basename(p.rstrip("/")) in REGENERABLE

        if not targets or not all(disposable(p) for p in targets):
            return 2, ("BLOCKED: recursive rm outside temp and build dirs. house rule is trash-only - move it to the "
                       "system trash so a human can review before it's gone.")
    return 0, ""


def _selftest() -> None:
    # ponytail: smallest check that fails if the guard logic breaks
    assert verdict("git commit --trailer 'Co-Authored-By: x'")[0] == 2
    assert verdict("git push --force origin main")[0] == 2
    assert verdict("rm -rf /")[0] == 2
    assert verdict("git commit -m 'normal message'")[0] == 0
    assert verdict("ls -la && git status")[0] == 0
    assert verdict("")[0] == 0

    # measured false positives - read-only work that the old guard blocked
    assert verdict('grep -rln "Co-Authored-By" .')[0] == 0
    assert verdict("git log --grep=Signed-off-by")[0] == 0
    # a commit whose MESSAGE discusses trailers is not a commit WITH a trailer
    assert verdict('git commit -m "fix guard that blocked Co-Authored-By greps"')[0] == 0
    assert verdict('git commit -m "msg" -m "body\nCo-Authored-By: x <a@b.c>"')[0] == 2
    assert verdict('git commit --trailer "Signed-off-by: x"')[0] == 2
    assert verdict('grep -r "drop table" migrations/')[0] == 0
    assert verdict('echo "dd if=x"')[0] == 0
    assert verdict("rm -rf node_modules")[0] == 0
    assert verdict("rm -rf .next dist")[0] == 0
    assert verdict("rm -rf /tmp/proj/build")[0] == 0
    # ...but a real DDL execution still blocks

    # trash-only rule
    assert verdict("rm -rf /Users/someone/Developer/foo")[0] == 2
    assert verdict("rm -rf src/")[0] == 2
    assert verdict("rm -rf /tmp/scratch")[0] == 0
    assert verdict("rm -r /private/tmp/x && ls")[0] == 0
    assert verdict("rm notes.txt")[0] == 0           # non-recursive rm still fine
    # hook bypass + force branch delete + history rewrite
    assert verdict("git commit --no-verify -m 'x'")[0] == 2
    assert verdict("git branch -D feature")[0] == 2
    assert verdict("git branch -d feature")[0] == 0  # merged-branch prune is fine
    assert verdict("git filter-repo --path secrets")[0] == 2
    print("selftest ok")


def main() -> None:
    if "--selftest" in sys.argv:
        _selftest()
        return
    try:
        event = json.load(sys.stdin)
    except Exception:
        sys.exit(0)  # malformed event, fail open rather than block everything
    # Claude Code: tool_input.command. Cursor beforeShellExecution: command.
    tool_input = event.get("tool_input") or event.get("input") or {}
    command = event.get("command") or tool_input.get("command", "")
    cwd = event.get("cwd") or tool_input.get("cwd") or os.getcwd()
    # Cursor events put command at the top level and omit tool_input.
    cursor_style = "tool_input" not in event and "command" in event
    code, message = verdict(command, cwd)
    if code == 2:
        print(message, file=sys.stderr)
        if cursor_style:
            print(json.dumps({
                "permission": "deny",
                "user_message": message,
                "agent_message": message,
            }))
    elif cursor_style:
        print(json.dumps({"permission": "allow"}))
    sys.exit(code)


if __name__ == "__main__":
    main()
