#!/usr/bin/env python3
"""Count tool calls in a Cursor or Codex session and say so when it runs long.

An agent rereads its whole context on every call, so a long session costs far
more per call than a short one. This hook runs after every tool call, keeps a
count per session in the temp folder, and tells the agent once the count reaches
the limit, then again every 50 calls.

    FLEET_GAUGE_CALLS   the limit, 150 unless set

Run `python3 call_count.py --selftest` to check it.
"""
import json
import os
import re
import sys
import tempfile
from pathlib import Path

REPEAT = 50
NOTE = (
    "This session has made {n} tool calls. Every call rereads the whole context, so each "
    "one now costs more than the last. Finish the step in hand, write what is done and "
    "what is left to a notes file, and tell the user a new session should pick it up."
)


def limit() -> int:
    try:
        return max(1, int(os.environ.get("FLEET_GAUGE_CALLS", "150")))
    except ValueError:
        return 150


def bump(session: str, folder: str = "") -> int:
    name = re.sub(r"[^A-Za-z0-9_-]", "", session)[:80] or "unknown"
    path = Path(folder or tempfile.gettempdir()) / f"fleet-gauge-{name}.count"
    try:
        count = int(path.read_text()) + 1
    except (OSError, ValueError):
        count = 1
    try:
        path.write_text(str(count))
    except OSError:
        pass
    return count


def due(count: int, at: int) -> bool:
    return count >= at and (count - at) % REPEAT == 0


def reply(count: int, cursor: bool) -> str:
    note = NOTE.format(n=count)
    if cursor:
        return json.dumps({"additional_context": note})
    return json.dumps({"hookSpecificOutput": {"hookEventName": "PostToolUse", "additionalContext": note}})


def selftest() -> None:
    with tempfile.TemporaryDirectory() as folder:
        assert [bump("a/b", folder) for _ in range(3)] == [1, 2, 3]
        assert bump("other", folder) == 1
    assert [n for n in range(1, 260) if due(n, 150)] == [150, 200, 250]
    assert "additional_context" in reply(150, True)
    assert json.loads(reply(150, False))["hookSpecificOutput"]["additionalContext"].startswith("This session has made 150")
    print("selftest ok")


def main() -> None:
    if "--selftest" in sys.argv:
        return selftest()
    try:
        event = json.load(sys.stdin)
    except ValueError:
        return
    if not isinstance(event, dict):
        return
    cursor = "--cursor" in sys.argv or "cursor_version" in event
    count = bump(str(event.get("conversation_id") or event.get("session_id") or ""))
    if due(count, limit()):
        print(reply(count, cursor))


if __name__ == "__main__":
    main()
