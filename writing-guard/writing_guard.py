#!/usr/bin/env python3
"""Writing guard for Claude Code: blocks the checkable half of RULES.md.

One script, two hook events. On PreToolUse for Write, Edit and NotebookEdit it
reads the text about to land in a prose file. On Stop it reads the reply about to
be sent. Exit 2 blocks and hands the offending snippet back to the model; exit 0
allows. A malformed event allows, so a broken hook never stops work.

Paths that must quote what the rules ban are skipped: this folder, and any path
containing a fragment listed in WRITING_GUARD_EXEMPT (colon-separated).

Run `writing_guard.py --selftest` to check.
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PROSE_EXT = (".md", ".mdx", ".txt", ".html", ".htm", ".rst")

ANTITHESIS = (
    # two short mirrored sentences: "<Noun> is the <noun>. <Noun> is the <noun>."
    re.compile(r"\b[A-Z][\w-]* (?:is|are) (?:the|a|an) [\w-]+\. [A-Z][\w-]* (?:is|are) (?:the|a|an) [\w-]+\."),
    # "not X, Y" / "not X - Y" / "not X, but Y" / "not X, just Y" inside one sentence
    re.compile(r"\b[Nn]ot (?:a|an|the) [\w-]+(?: [\w-]+){0,3}\s*(?:,|;|-|—)\s*(?:a|an|the|but|just|it's|it is) "),
    # "isn't X, it's Y" / "is not X, it is Y"
    re.compile(r"\b(?:isn't|is not|aren't|are not|wasn't|was not) [^.\n]{2,40},\s*(?:it's|it is|they're|they are|that's) "),
    # empty contrast: "not just X, it's Y" / "isn't only X, but Y"
    re.compile(r"\b(?:not|isn't|is not|aren't|are not) (?:just|only|merely|simply) [^.\n]{2,60}[,;]\s*(?:it's|it is|they're|they are|but|that's) ", re.IGNORECASE),
)
# filler authority, insight-shaped filler, chat furniture, and the banned words.
# "landscape" and "navigate" are left out because .html files carry CSS and router
# code that use them; CHAT_ONLY adds them for replies.
FILLER = re.compile(
    r"\b(?:it(?:'s| is) worth noting|it(?:'s| is) important to note|importantly|crucially|"
    r"in essence|at its core|here(?:'s| is) the thing|the short version|bottom line|"
    r"great question|when it comes to|whether you(?:'re| are) an? |"
    r"i understand (?:this|that|how) (?:can|must|might) be|in summary|"
    r"let me know if you(?:'d| would) like|i hope this helps|feel free to|happy to help|"
    r"something real is happening|the stakes couldn't be higher|the key idea is|"
    r"a useful way to think about|this can be understood as|at the end of the day|"
    r"when the dust settles|deep dive|dive into|unpack|"
    r"may potentially|delve|tapestry|robust|leverage|seamless(?:ly)?|elevate|unlock|"
    r"journey|foster|holistic|impactful|empower(?:s|ed|ing)?|streamline[ds]?|"
    r"cutting-edge|game-chang(?:er|ing)|testament to|at the forefront|passionate about|"
    r"uniquely positioned|world-class|best-in-class|state-of-the-art|revolutioni[sz]e|"
    r"transformative|supercharge|next-gen|frictionless|effortless(?:ly)?)\b", re.IGNORECASE)
# em dash anywhere; en dash only when used as a beat (spaced), ranges like Sep–Dec pass
DASH = re.compile(r"—|&mdash;|\s–\s")
# middle-dot or bullet as an item separator ("kcal · protein", "a • b")
DOTSEP = re.compile(r"\S\s*(?:·|&middot;|•|&bull;)\s*\S")
CHECKS = (
    tuple((p, "antithesis in parallel clauses") for p in ANTITHESIS)
    + ((FILLER, "filler or banned word"), (DASH, "em dash"), (DOTSEP, "middle-dot separator"))
)
CHAT_ONLY = re.compile(r"\b(?:landscape|navigate)\b", re.IGNORECASE)
MSG = "BLOCKED: {what} - writing rule, see RULES.md beside this hook. Offending text: {snippet!r}"

FENCE = re.compile(r"```.*?```", re.S)
INLINE = re.compile(r"`[^`\n]*`")
QUOTED = re.compile(r"\"[^\"\n]{1,80}\"")


def exempt(path: str) -> bool:
    norm = os.path.abspath(path).replace("\\", "/")
    if norm.startswith(HERE.replace("\\", "/") + "/"):
        return True
    extra = [p for p in os.environ.get("WRITING_GUARD_EXEMPT", "").split(":") if p]
    return any(part in norm for part in extra)


def hit(text: str, old: str = "", checks=CHECKS):
    """return (what, snippet) for the first rule the text breaks, or None.

    `old` is the text an Edit replaces. A rule only blocks when the new text
    breaks it more often than the old did, so an edit near a line that already
    broke a rule is judged on what it adds.
    """
    for pat, what in checks:
        if old and len(pat.findall(text)) <= len(pat.findall(old)):
            continue
        m = pat.search(text)
        if m:
            start = max(0, m.start() - 20)
            return what, text[start:m.end() + 20]
    return None


def file_verdict(path: str, text: str, old: str = ""):
    """return (exit_code, message) for prose being written. 2 = block, 0 = allow."""
    if not isinstance(text, str) or not text or not isinstance(path, str):
        return 0, ""
    if not path.lower().endswith(PROSE_EXT) or exempt(path):
        return 0, ""
    found = hit(text, old if isinstance(old, str) else "")
    if found:
        return 2, MSG.format(what=found[0], snippet=found[1])
    return 0, ""


def _lines_backward(path: str, block: int = 1 << 20):
    """the file's lines, last first, reading only as far back as the caller pulls."""
    with open(path, "rb") as f:
        f.seek(0, 2)
        pos, buf = f.tell(), b""
        while pos > 0:
            step = min(block, pos)
            pos -= step
            f.seek(pos)
            buf = f.read(step) + buf
            lines = buf.split(b"\n")
            buf = lines[0]  # may be the tail of a line that starts further back
            yield from reversed(lines[1:])
        if buf:
            yield buf


def last_reply(transcript_path: str) -> str:
    """text blocks of every assistant entry since the last real user message."""
    texts = []
    try:
        for raw in _lines_backward(transcript_path):
            try:
                d = json.loads(raw)
            except ValueError:
                continue
            kind = d.get("type")
            content = (d.get("message") or {}).get("content")
            if kind == "user":
                typed = isinstance(content, str) or (
                    isinstance(content, list)
                    and any(isinstance(c, dict) and c.get("type") == "text" for c in content))
                if typed:
                    break
            elif kind == "assistant" and isinstance(content, list):
                texts[:0] = [c["text"] for c in content
                             if isinstance(c, dict) and c.get("type") == "text" and c.get("text")]
    except OSError:
        return ""
    return "\n".join(texts)


def reply_hit(text: str):
    """code and short quotations may carry the words; the prose may not."""
    text = QUOTED.sub(" ", INLINE.sub(" ", FENCE.sub(" ", text)))
    return hit(text, checks=CHECKS + ((CHAT_ONLY, "banned word"),))


def _selftest() -> None:
    import tempfile
    block = [
        "Size is the goal. Strength is the byproduct.",
        "Not a plateau, a reset.",
        "It isn't the number, it's the pattern.",
        "It's not just the number, it's the pattern.",
        "We leverage robust tooling.",
        "At the end of the day it works.",
        "~2,250 kcal · ~110 g",
        "one thing — another",
        "one thing – another",
        "a &middot; b",
    ]
    for t in block:
        assert file_verdict("/x/a.md", t)[0] == 2, t
        assert file_verdict("/x/a.html", t)[0] == 2, t
        assert reply_hit(t), t
    allow = [
        "Bench 180x2, then 165x5. Sep–Dec block, 4 of 5 days.",
        "Sleep landed at 6.1 h. Not a great week.",
        "The scale is not the whole story.",
    ]
    for t in allow:
        assert file_verdict("/x/a.md", t)[0] == 0, t
        assert not reply_hit(t), t
    assert file_verdict("/x/a.py", "leverage · —")[0] == 0
    assert file_verdict(os.path.join(HERE, "RULES.md"), "delve")[0] == 0
    os.environ["WRITING_GUARD_EXEMPT"] = "/quotes/:/style-guide.md"
    assert file_verdict("/x/quotes/a.md", "delve")[0] == 0
    assert file_verdict("/x/docs/style-guide.md", "delve")[0] == 0
    assert file_verdict("/x/docs/a.md", "delve")[0] == 2
    del os.environ["WRITING_GUARD_EXEMPT"]
    # an Edit is judged on what it adds
    row = "- [Gym](gym.md) — bench 180"
    assert file_verdict("/x/INDEX.md", row + ", squat 225", row)[0] == 0
    assert file_verdict("/x/INDEX.md", row + " — squat 225", row)[0] == 2
    assert file_verdict("/x/INDEX.md", row + ", leverage", row)[0] == 2
    assert file_verdict("/x/INDEX.md", row)[0] == 2  # a Write has no old text
    # replies
    assert reply_hit("This lets you navigate the landscape.")
    assert not reply_hit("The rule bans \"it's worth noting\" and `leverage`.")
    assert not reply_hit("```\nleverage · foo — bar\n```\nBench went to 180.")
    rows = [
        {"type": "user", "message": {"content": "hi"}},
        {"type": "assistant", "message": {"content": [{"type": "text", "text": "We leverage it."}]}},
        {"type": "user", "message": {"content": "again"}},
        {"type": "assistant", "message": {"content": [{"type": "tool_use", "name": "Bash"}]}},
        {"type": "user", "message": {"content": [{"type": "tool_result", "content": "leverage"}]}},
        {"type": "assistant", "message": {"content": [{"type": "text", "text": "First."}]}},
        {"type": "assistant", "message": {"content": [{"type": "text", "text": "Second."}]}},
    ]
    with tempfile.NamedTemporaryFile("w", suffix=".jsonl", delete=False) as f:
        f.write("\n".join(json.dumps(r) for r in rows) + "\n")
    assert last_reply(f.name) == "First.\nSecond."
    assert list(_lines_backward(f.name, block=7)) == list(reversed(open(f.name, "rb").read().split(b"\n")))
    os.unlink(f.name)
    assert last_reply("/nonexistent/x.jsonl") == ""
    print("selftest ok")


def main() -> None:
    if "--selftest" in sys.argv:
        _selftest()
        return
    try:
        event = json.load(sys.stdin)
    except Exception:
        sys.exit(0)  # malformed event, fail open rather than block everything
    if not isinstance(event, dict):
        sys.exit(0)
    tool_input = event.get("tool_input")
    if isinstance(tool_input, dict):
        path = tool_input.get("file_path") or tool_input.get("notebook_path") or ""
        if path and not os.path.isabs(path):
            path = os.path.join(event.get("cwd") or os.getcwd(), path)
        text = tool_input.get("content") or tool_input.get("new_string") or ""
        code, message = file_verdict(path, text, tool_input.get("old_string") or "")
    else:
        # Stop. stop_hook_active is set on the retry, so a reply that has to quote
        # a banned phrase goes through on the second pass instead of looping.
        if event.get("stop_hook_active"):
            sys.exit(0)
        found = reply_hit(last_reply(event.get("transcript_path") or ""))
        code, message = (2, MSG.format(what=found[0], snippet=found[1])
                         + " Rewrite the reply without it, then stop.") if found else (0, "")
    if code == 2:
        print(message, file=sys.stderr)
    sys.exit(code)


if __name__ == "__main__":
    main()
