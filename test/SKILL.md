---
name: test
description: Testing frameworks for AI systems and refactoring safety. Use when building eval harnesses, defining capability benchmarks, setting up regression gates, or generating characterization tests before refactoring existing code.
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

Freeze existing behavior before refactoring. You can't refactor confidently without knowing what behavior you're preserving.

**Use when**: rewriting a class, restructuring a module, extracting logic, migrating between frameworks.

**Do NOT use when**: code is already well-tested, you're deleting the code, it's trivially simple, or you intend to change the behavior.

### 5 Phases

#### Phase 1: Discover

Glob and grep the public API surface of the target:

```bash
# Find public methods / exported symbols
grep -n "func \|public \|export " TargetClass.swift
grep -rn "export " --include="*.ts" src/target/
```

List everything that external code calls — that's what you must characterize.

#### Phase 2: Classify Behavior

Build a classification table before writing a single test:

| Method | Type | Notes |
|--------|------|-------|
| `calculateTotal()` | Pure computation | No side effects |
| `save()` | State mutation + async | Writes to DB |
| `onValueChange` | Event emission | Callback pattern |
| `fetchUser()` | Async + side effect | HTTP + state update |
| `validate()` | Error path | Throws on invalid |

Types: pure computation / state mutation / async / side effect / event emission / error path

#### Phase 3: Generate Tests

Write one test per behavior. Assert **actual current behavior**, even if it looks wrong.

**Swift Testing (preferred):**

```swift
@Suite("Characterization: ItemManager")
@Tag(.characterization)
struct ItemManagerCharacterizationTests {

    // CHARACTERIZATION: returns 11 not 10 due to inclusive range
    // Don't fix this until intentionally changing behavior
    @Test("current behavior: count includes boundary item")
    func countIncludesBoundary() {
        let manager = ItemManager(range: 1...10)
        #expect(manager.count == 11) // CHARACTERIZATION: 11, not 10
    }

    @Test("current behavior: empty title defaults to 'Untitled'")
    func emptyTitleDefault() {
        let item = Item(title: "")
        #expect(item.displayTitle == "Untitled")
    }

    @Test("current behavior: throws on nil ID")
    func throwsOnNilID() {
        #expect(throws: ItemError.invalidID) {
            try ItemManager.fetch(id: nil)
        }
    }
}
```

**TypeScript/Vitest:**

```typescript
describe('Characterization: ItemManager', () => {
    it('current behavior: count includes boundary item', () => {
        // CHARACTERIZATION: returns 11 not 10 due to inclusive range
        const manager = new ItemManager({ range: [1, 10] });
        expect(manager.count).toBe(11); // CHARACTERIZATION
    });

    it('current behavior: empty title defaults to Untitled', () => {
        const item = new Item({ title: '' });
        expect(item.displayTitle).toBe('Untitled');
    });
});
```

#### Phase 4: Fill in Actual Values (CRITICAL)

Run the tests. Many will fail because you guessed the current behavior wrong.

**Do NOT fix the code to match your expectation.** Fix the test to match what the code actually does.

```swift
// You expected 10, test said 11 — update the test, not the code
#expect(manager.count == 11) // CHARACTERIZATION: inclusive range, returns 11
```

Add a comment on every CHARACTERIZATION assert explaining WHY the value might look surprising.

#### Phase 5: Verify and Lock

All characterization tests pass. Run them:

```bash
# Swift
xcodebuild test -only-testing "YourAppTests/ItemManagerCharacterizationTests"

# Vitest
npx vitest run --reporter=verbose src/target/
```

Lock: tag them `@Tag(.characterization)` in Swift or add `// CHARACTERIZATION` comment in TS. These tests should FAIL if you change behavior — that's the point. When you do intentionally change behavior, update the test and remove the CHARACTERIZATION comment.

### Naming

- Suite: `"Characterization: ClassName"`
- Test: `"current behavior: [what it does]"` — describe the behavior, not the method name

### When Tests Fail After Refactor

A failing characterization test means you changed a behavior. Decide:
- **Intentional**: update the test, document why the behavior changed
- **Accidental**: fix the refactor — you broke something

A green characterization suite = behavior-preserving refactor.
