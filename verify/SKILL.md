---
name: verify
description: Done check for code changes. Use after implementation, before marking a task done, before ship/commit verification, and inside autonomous loops. Reviews the diff against the original goal and hunts fake-done shortcuts.
version: 1.1.0
user-invocable: true
argument-hint: "[goal or diff scope]"
---

# Verify

Assume the change is not done until the source proves otherwise. The point is
to keep the maker from grading its own homework.

Scope: diff-scoped done-check against the original goal. State-scoped frontend
quality lives in the check skill; pre-work eval harnesses in the test skill.
The banned-pattern greps below are shared with full-output-enforcement (its
generation-time twin) - update both together.

## Dispatch (who runs this)

Never run inline by the agent that wrote the change. Spawn a fresh-context
subagent on the judgment tier (`model: opus`), briefed with ONLY: the diff,
the original goal/requirements, and this skill. Never pass the implementer's
summary, rationale, or self-assessment - fresh eyes, no author bias. A
generator model must never be graded by an instance of its own tier alone.

## Read first

1. The original goal or loop charter.
2. The actual diff, not the summary.
3. The test/build command - run it yourself (step 2 below); never trust
   pasted output.

## Procedure (run in order; paste evidence, not conclusions)

0. Scope the diff. Run `git diff --stat HEAD` (branch review:
   `git diff <base>...HEAD`; pre-commit: `git diff --staged`). List every
   touched file.
1. Mechanical greps on the diff. Run ALL of these; any hit must be either
   justified in one line or recorded as a failure:
   - placeholders/stubs:
     `git diff -U0 | grep -nEi '^\+.*(TODO|FIXME|HACK|XXX|placeholder|not implemented|for now)'`
   - relaxed tests:
     `git diff -U0 -- '*test*' '*spec*' | grep -nE '^\-.*(expect|assert|XCTAssert|#expect)|^\+.*(\.skip|xit\(|xdescribe|@Skip|toBeTruthy\(\)|assertTrue\(true\))'`
     (deleted assertion or added skip = failure unless the test itself was
     the goal; exception: assertions tagged CHARACTERIZATION per /test char
     are allowed to change)
   - swallowed errors:
     `git diff -U0 | grep -nE '^\+.*(catch[^{]*\{\s*\}|except( \w+)?:\s*pass|\.catch\(\(\) *=>)'`
   - debug residue:
     `git diff -U0 | grep -nE '^\+.*(console\.log|debugger|print\(|dbg!)'`
   - mocks outside tests:
     `git diff --name-only | grep -viE 'test|spec|mock' | xargs grep -lnE '\b(mock|stub|fake)[A-Z_(]' 2>/dev/null`
2. Run the project's named test/build command (from CLAUDE.md or the package
   manifest). Paste the exact command and its exit code. Exit != 0 = fail.
   If no command exists or it cannot run, add it to "unverified" - never
   count it as passed.
3. Invented-API check: for every method/prop/flag/path the diff CALLS but
   does not define, grep the codebase or the dependency for its definition.
   Not found = failure.
4. Goal re-read: restate the goal in one sentence. Map each requirement to
   the diff hunk that satisfies it (requirement with no hunk = off-spec
   done; hunk with no requirement = scope creep).
5. Negative paths: for each new function/endpoint/state, name what happens
   on empty input, error input, and dependency failure. "Unhandled +
   reachable" = failure.

## Fake-done checklist

The procedure above catches most of these mechanically; check the rest
explicitly:

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

Findings first. Keep it tight. Evidence is compulsory.

If clean:

```json
{"passes": true,
 "evidence": {"test_command": "npx vitest run", "exit_code": 0, "greps_run": 5},
 "unverified": [],
 "failures": []}
```

If not:

```json
{"passes": false,
 "evidence": {"test_command": "npx vitest run", "exit_code": 1, "greps_run": 5},
 "unverified": ["e2e not run: no dev server"],
 "failures": [
   {"file": "path", "line": 42, "shortcut": "happy path only", "why": "missing failed request path"}
 ]}
```

Do not pad. If you cannot verify a claim, mark it unverified instead of
pretending it passed.
