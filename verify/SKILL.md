---
name: verify
description: Done check for code changes. Use after implementation, before marking a task done, before ship/commit verification, and inside autonomous loops. Reviews the diff against the original goal and hunts fake-done shortcuts.
version: 1.0.0
user-invocable: true
argument-hint: "[goal or diff scope]"
---

# Verify

Assume the change is not done until the source proves otherwise. The point is
to keep the maker from grading its own homework.

## Read first

1. The original goal or loop charter.
2. The actual diff, not the summary.
3. The relevant test/build output if it exists.

## Fake-done checklist

Check each shortcut explicitly:

1. **Relaxed tests** - assertions weakened, skipped, deleted, or made vague.
2. **Swallowed errors** - catch/log/continue hides failure instead of handling it.
3. **Rename-only fix** - names changed, behavior did not.
4. **Stub return** - hardcoded or placeholder output passes one case.
5. **Comment-as-fix** - TODO, comment, or doc claims solve behavior.
6. **Happy path only** - empty, malformed, failed, slow, or missing-input paths ignored.
7. **Scope creep** - unrelated cleanup, style churn, or opportunistic refactor.
8. **Invented API** - method, prop, command, flag, or file path not present in source.
9. **Silent decision** - schema, auth, data, UX, or compatibility choice made without surfacing it.
10. **Pass-by-mock** - test mocks the behavior it claims to verify.
11. **Off-spec done** - code works, but solves a different goal.

## Output

Findings first. Keep it tight.

If clean:

```json
{"passes": true, "failures": []}
```

If not:

```json
{
  "passes": false,
  "failures": [
    {"file": "path", "line": 42, "shortcut": "happy path only", "why": "missing failed request path"}
  ]
}
```

Do not pad. If you cannot verify a claim, mark it unverified instead of
pretending it passed.
