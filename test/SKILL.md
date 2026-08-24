---
name: test
description: >-
  Build the measuring stick before the work: eval suites for AI or LLM behavior, regression
  gates, pass@k targets, calibrating an LLM judge; or characterization tests that freeze
  behavior before a refactor. Runs before implementation. Post-hoc done-checks are the done-
  check skill.
version: 1.0.0
user-invocable: true
argument-hint: "[eval | char]"
---

# Test

Two testing disciplines: eval-driven development for AI systems, and characterization testing to lock behavior before refactoring.

| Mode | What it does |
|---|---|
| `/test eval` | Eval-Driven Development — define evals before implementation, capability + regression gates |
| `/test char` | Characterization tests — freeze current behavior before any refactoring |

---

## `/test eval`

**Define evals BEFORE writing implementation code.** The eval is the spec.

If you implement first then write evals, you're measuring what you built — not what you should have built.

### Two Eval Types

**Capability Evals** — can the system do the thing at all?
- Cover happy path, common edge cases, and common failure modes
- Target: `pass@3 >= 90%` (succeeds within 3 attempts)

**Regression Evals** — do existing features still work after a change?
- Every bug fix adds a regression eval
- Target: `pass^3 = 100%` (ALL 3 consecutive attempts must pass — no flakiness allowed)

### Three Grader Types

| Type | When to use | Example |
|------|------------|---------|
| **Code-based** | Deterministic correctness | JSON schema valid, output contains exact string, HTTP 200 |
| **Model-based** | Semantic quality or subjective criteria | "Does this summary capture the main point?" → LLM judge (0-3 score) |
| **Human** | High-stakes, ambiguous, or new grader calibration | Flag for async review, don't block pipeline |

Prefer code-based. Use model-based only when determinism is impossible. Human graders should shrink over time as you learn to codify their judgments.

**Model-based grader contract**: the judge prompt MUST contain (a) the 0-3 scale with one concrete example output per score level, (b) an instruction to quote the exact evidence line before emitting the score, (c) temperature 0 / deterministic settings. Calibration gate: run the judge 3x on 10 fixed examples; any example where scores differ across runs = flaky grader, fix before it gates anything. Judge model: opus for release gates, sonnet acceptable for inner-loop iteration.

### Metrics

| Metric | Meaning | Use for |
|--------|---------|---------|
| `pass@1` | Passes on first attempt | Tight regressions, user-facing features |
| `pass@3` | Passes at least once in 3 runs | New capabilities, acceptable retry scenarios |
| `pass^3` | ALL 3 consecutive runs pass | Zero-flakiness gate — regression suites only |

**Pass@k vs pass^k**: `@k` = success in k tries (reliability). `^k` = success every single time (determinism gate).

### Workflow

```
1. DEFINE   → write evals before any implementation
2. BASELINE → run against current system to confirm they fail (establishes RED)
3. IMPLEMENT → build the feature
4. EVALUATE  → run evals, iterate until targets met
5. REPORT   → document results in eval-summary.md
6. GATE     → regression suite runs on every PR
```

**Never skip the baseline run.** An eval that starts green teaches you nothing.

### File Layout

```
.claude/evals/
  <feature>.md          # eval spec: inputs, expected behavior, grader
  <feature>.log         # run history with timestamps and scores
docs/releases/<ver>/
  eval-summary.md       # pass rates, regressions caught, cost/latency
```

### Eval Spec Template

```markdown
# Eval: [Feature Name]

## Type
[ ] Capability  [ ] Regression

## Target Metrics
- pass@3 >= [90%] OR pass^3 = [100%]

## Test Cases

### Case 1: [Happy path]
**Input**: [exact input or input template]
**Grader**: Code-based — output must contain [X] / match schema [Y]
**Pass criteria**: [specific, unambiguous]

### Case 2: [Edge case]
...

### Case 3: [Failure mode]
...

## Known limitations
[What this eval intentionally does NOT test]
```

### Anti-Patterns

- **Overfitting to examples**: if the eval only uses training examples, you're measuring memorization
- **Happy path only**: evals that never test failures give false confidence
- **Ignoring cost/latency drift**: track token cost and p50/p95 latency per run, not just pass rate
- **Flaky graders in release gates**: a grader that sometimes gives different scores on identical inputs is worse than no grader — you can't tell signal from noise
- **LLM judge without calibration**: before using a model as judge, validate its scores against human ratings on 20-50 examples

---


## `/test char`

Freeze current behavior before a refactor, rewrite, or framework migration, so the
diff has something to be judged against. Characterization tests assert what the code
does today - including the parts that look wrong. A surprising assertion is a finding,
not a bug to fix mid-refactor.

Five-phase protocol with worked Swift and TypeScript: references/characterization.md -
read when running this mode.

Name them so a failure reads as "you changed a behavior," not "a test broke": the
suite and test names should make the frozen behavior obvious from the failure line
alone, without opening the file. Tag such edits `CHARACTERIZATION` in the test name or
a comment so `done-check` skips them - that string is a contract between the two skills.
