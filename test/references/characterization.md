# /test char

Freeze current behavior before a refactor. Read when running this mode.

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

This is the ONLY sanctioned case of editing an assertion to match code - tag such edits CHARACTERIZATION in the test name or a comment so /done-check skips them.

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
