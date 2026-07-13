---
name: ios
description: Swift and iOS development patterns. Use when building, reviewing, or debugging Swift/SwiftUI code on any Apple platform. Covers SwiftUI architecture with @Observable, Swift 6.2 Approachable Concurrency, type-safe NavigationStack, HIG compliance, and VoiceOver/Dynamic Type accessibility.
version: 2.0.0
user-invocable: true
argument-hint: "[review | accessibility | patterns | concurrency]"
---

# iOS / Swift

All Swift and Apple-platform patterns in one skill. Covers architecture, concurrency, HIG review, and accessibility.

| Mode | What it does |
|---|---|
| `/ios` | Apply all relevant sections based on context |
| `/ios review` | HIG compliance, font usage, and accessibility audit of SwiftUI code |
| `/ios accessibility` | Generate or improve VoiceOver, Dynamic Type, reduce-motion infrastructure |
| `/ios patterns` | SwiftUI architecture: @Observable, navigation, view composition, performance |
| `/ios concurrency` | Swift 6.2 Approachable Concurrency: MainActor defaults, @concurrent, isolated conformances |

---

## SwiftUI Patterns

### State Management — Property Wrapper Selection

Choose the simplest wrapper that fits:

| Wrapper | Use Case |
|---|---|
| `@State` | View-local value types (toggles, form fields, sheet presentation) |
| `@Binding` | Two-way reference to parent's `@State` |
| `@Observable` class + `@State` | Owned model with multiple properties |
| `@Observable` class (no wrapper) | Read-only reference passed from parent |
| `@Bindable` | Two-way binding to an `@Observable` property |
| `@Environment` | Shared dependencies injected via `.environment()` |

Use `@Observable` (not `ObservableObject`) — it tracks property-level changes so SwiftUI only re-renders views that read the changed property:

```swift
@Observable
final class ItemListViewModel {
    private(set) var items: [Item] = []
    private(set) var isLoading = false
    var searchText = ""

    private let repository: any ItemRepository

    init(repository: any ItemRepository = DefaultItemRepository()) {
        self.repository = repository
    }

    func load() async {
        isLoading = true
        defer { isLoading = false }
        items = (try? await repository.fetchAll()) ?? []
    }
}

struct ItemListView: View {
    @State private var viewModel: ItemListViewModel

    init(viewModel: ItemListViewModel = ItemListViewModel()) {
        _viewModel = State(initialValue: viewModel)
    }

    var body: some View {
        List(viewModel.items) { item in ItemRow(item: item) }
            .searchable(text: $viewModel.searchText)
            .overlay { if viewModel.isLoading { ProgressView() } }
            .task { await viewModel.load() }
    }
}
```

Replace `@EnvironmentObject` with `@Environment`:

```swift
// Inject
ContentView().environment(authManager)

// Consume
struct ProfileView: View {
    @Environment(AuthManager.self) private var auth
    var body: some View { Text(auth.currentUser?.name ?? "Guest") }
}
```

### View Composition

Break views into small, focused structs. When state changes, only the subview reading that state re-renders:

```swift
struct OrderView: View {
    @State private var viewModel = OrderViewModel()
    var body: some View {
        VStack {
            OrderHeader(title: viewModel.title)
            OrderItemList(items: viewModel.items)
            OrderTotal(total: viewModel.total)
        }
    }
}
```

`ViewModifier` for reusable styling:

```swift
struct CardModifier: ViewModifier {
    func body(content: Content) -> some View {
        content.padding().background(.regularMaterial)
            .clipShape(RoundedRectangle(cornerRadius: 12))
    }
}

extension View {
    func cardStyle() -> some View { modifier(CardModifier()) }
}
```

### Navigation — Type-Safe NavigationStack

```swift
@Observable
final class Router {
    var path = NavigationPath()
    func navigate(to destination: Destination) { path.append(destination) }
    func popToRoot() { path = NavigationPath() }
}

enum Destination: Hashable {
    case detail(Item.ID)
    case settings
    case profile(User.ID)
}

struct RootView: View {
    @State private var router = Router()
    var body: some View {
        NavigationStack(path: $router.path) {
            HomeView()
                .navigationDestination(for: Destination.self) { dest in
                    switch dest {
                    case .detail(let id): ItemDetailView(itemID: id)
                    case .settings: SettingsView()
                    case .profile(let id): ProfileView(userID: id)
                    }
                }
        }
        .environment(router)
    }
}
```

### Performance

- `LazyVStack` / `LazyHStack` — create views only when visible
- Always use stable, unique IDs in `ForEach` — never array indices
- Never perform I/O or heavy computation inside `body` — use `.task {}`
- Minimize `.shadow()`, `.blur()`, `.mask()` in lists — they trigger offscreen rendering
- Conform expensive views to `Equatable` to skip unnecessary re-renders

```swift
struct ExpensiveChartView: View, Equatable {
    let dataPoints: [DataPoint]
    static func == (lhs: Self, rhs: Self) -> Bool { lhs.dataPoints == rhs.dataPoints }
    var body: some View { /* complex rendering */ }
}
```

### Previews

```swift
#Preview("Empty state") {
    ItemListView(viewModel: ItemListViewModel(repository: EmptyMockRepository()))
}
#Preview("Loaded") {
    ItemListView(viewModel: ItemListViewModel(repository: PopulatedMockRepository()))
}
```

### Anti-Patterns to Avoid

- `ObservableObject` / `@Published` / `@StateObject` / `@EnvironmentObject` in new code — migrate to `@Observable`
- Async work directly in `body` or `init` — use `.task {}`
- Creating view models as `@State` in child views that don't own the data — pass from parent
- `AnyView` type erasure — prefer `@ViewBuilder` or `Group` for conditional views
- Ignoring `Sendable` requirements when passing data to/from actors

---

## Swift 6.2 Approachable Concurrency

Swift 6.2 fixes implicit background offloading — async functions now stay on the calling actor by default, eliminating the most common data-race errors.

### Core Pattern: Single-Threaded by Default

```swift
// Swift 6.1: ERROR — implicit offloading caused data race
// Swift 6.2: OK — async stays on MainActor
@MainActor
final class StickerModel {
    let photoProcessor = PhotoProcessor()

    func extractSticker(_ item: PhotosPickerItem) async throws -> Sticker? {
        guard let data = try await item.loadTransferable(type: Data.self) else { return nil }
        return await photoProcessor.extractSticker(data: data, with: item.itemIdentifier)
    }
}
```

### Isolated Conformances

MainActor types can now conform to non-isolated protocols safely:

```swift
protocol Exportable { func export() }

// Swift 6.2: OK with isolated conformance
extension StickerModel: @MainActor Exportable {
    func export() { photoProcessor.exportAsPNG() }
}

// OK — same actor isolation
@MainActor struct ImageExporter {
    var items: [any Exportable]
    mutating func add(_ item: StickerModel) { items.append(item) }
}

// ERROR — nonisolated context can't use MainActor conformance
nonisolated struct ImageExporter {
    var items: [any Exportable]
    mutating func add(_ item: StickerModel) { items.append(item) } // Error
}
```

### Global and Static Variables

Protect global/static state with MainActor:

```swift
// Swift 6.2: Annotate with @MainActor
@MainActor
final class StickerLibrary {
    static let shared: StickerLibrary = .init()
}

// With MainActor default inference mode enabled (Xcode 26 build setting):
final class StickerLibrary {
    static let shared: StickerLibrary = .init()  // Implicitly @MainActor
}
```

### @concurrent for Explicit Background Work

When you need actual parallelism, opt in explicitly with `@concurrent`. Requires Approachable Concurrency build settings (SE-0466 + SE-0461) — without these, this code has a data race.

```swift
nonisolated final class PhotoProcessor {
    private var cachedStickers: [String: Sticker] = [:]

    func extractSticker(data: Data, with id: String) async -> Sticker {
        if let sticker = cachedStickers[id] { return sticker }
        let sticker = await Self.extractSubject(from: data)
        cachedStickers[id] = sticker
        return sticker
    }

    @concurrent
    static func extractSubject(from data: Data) async -> Sticker { /* ... */ }
}
```

To use `@concurrent`: mark the containing type `nonisolated`, add `@concurrent` + `async` to the function, add `await` at call sites.

### Key Design Decisions

| Decision | Rationale |
|---|---|
| Single-threaded by default | Most natural code is data-race free; concurrency is opt-in |
| Async stays on calling actor | Eliminates implicit offloading that caused data-race errors |
| Isolated conformances | MainActor types can conform to protocols without unsafe workarounds |
| `@concurrent` explicit opt-in | Background execution is a deliberate performance choice |

### Migration Steps

1. Enable in Xcode: Swift Compiler > Concurrency in Build Settings
2. Enable in SPM: use `SwiftSettings` API in package manifest
3. Use swift.org/migration tooling for automatic code changes
4. Start with MainActor inference mode for app targets
5. Add `@concurrent` only where profiling shows it's needed
6. Test thoroughly — data-race issues become compile-time errors

### Anti-Patterns to Avoid

- Applying `@concurrent` to every async function — most don't need background execution
- Using `nonisolated` to suppress compiler errors without understanding isolation
- Keeping legacy `DispatchQueue` patterns when actors provide the same safety
- Fighting the compiler — if it reports a data race, the code has a real concurrency issue

---

## HIG Review (`/ios review`)

→ *Reference materials: [reference/hig-checklist.md](reference/hig-checklist.md), [reference/font-guidelines.md](reference/font-guidelines.md), [reference/accessibility-quick-ref.md](reference/accessibility-quick-ref.md)*
→ *Official: [iOS HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-ios) | [watchOS HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-watchos)*

### Review Process

1. If user specifies files/views, review those. Otherwise scan recent SwiftUI files.
2. Prioritize user-facing views over components.
3. Review across three categories: HIG compliance, font usage, accessibility.

### HIG Compliance — What to Check

- Layout: tap targets (44pt iOS, 40pt watchOS), safe areas, padding
- Navigation: `NavigationStack`, sheets, alerts — correct patterns
- Colors: semantic colors, dark mode support, contrast ratios
- Platform: iOS vs watchOS requirements
- States: loading, empty, error

### Font Usage — What to Check

- Dynamic Type support (system text styles, not fixed sizes)
- Font hierarchy using semantic text styles
- Custom fonts scaling correctly
- Text truncation handled

### Anti-Patterns to Flag

```swift
// BAD — always flag these:
.foregroundColor(.black)           // hardcoded color
.font(.system(size: 14))           // fixed font size
Color(.red)                        // non-semantic color
UIColor(...)                       // use Color(.systemBackground) instead
```

```swift
// GOOD — call out when present:
.foregroundStyle(.primary)         // semantic color
.font(.subheadline)                // system text style with Dynamic Type
Color(.systemBackground)           // semantic system color
```

Missing accessibility labels on icon-only buttons. `.frame()` without considering Dynamic Type expansion. Important information conveyed by color only.

### Review Output Format

```
Reviewing: [FileName.swift]

PASS — HIG Compliance
- [things that comply well]

ISSUES — HIG
1. [File.swift:lineNumber] — [issue]
   Current: [code]
   Fix: [code with explanation]

PASS — Font Usage
- [Dynamic Type patterns used well]

ISSUES — Font
1. [File.swift:lineNumber] — hardcoded size
   Current: .font(.system(size: 14))
   Fix: .font(.subheadline)

PASS — Accessibility
- [well-implemented features]

ISSUES — Accessibility
1. [File.swift:lineNumber] — icon button missing label
   Current: Button { } label: { Image(systemName: "calendar") }
   Fix: .accessibilityLabel("Select date")

TESTING — Recommendations
- Test with VoiceOver enabled
- Test at largest Dynamic Type size
- Verify in Dark Mode
- Use Accessibility Inspector for contrast ratios
```

---

## Accessibility (`/ios accessibility`)

→ *Reference: [reference/accessibility-patterns.md](reference/accessibility-patterns.md), [reference/accessibility-quick-ref.md](reference/accessibility-quick-ref.md)*
→ *Official: [Accessibility in SwiftUI](https://developer.apple.com/documentation/swiftui/accessibility) | [HIG: Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility)*

### Core Patterns

**Labels and hints:**
```swift
Image(systemName: "heart.fill")
    .accessibilityLabel("Favorite")
    .accessibilityHint("Double tap to remove from favorites")
```

**Dynamic Type:**
```swift
Text("Title")
    .font(.title)  // Scales automatically
    .dynamicTypeSize(...DynamicTypeSize.accessibility3)  // Limit max size if needed
```

**Reduce motion:**
```swift
@Environment(\.accessibilityReduceMotion) private var reduceMotion

withAnimation(reduceMotion ? nil : .spring()) {
    // animation
}
```

**VoiceOver groups:**
```swift
VStack {
    Text("Item Name")
    Text("$9.99")
}
.accessibilityElement(children: .combine)
```

### Generated Infrastructure

When building accessibility support from scratch:

```
Sources/Accessibility/
├── AccessibilityModifiers.swift   # Custom view modifiers
├── AccessibilityHelpers.swift     # Label builders
└── AccessibilityStrings.swift     # Localized labels
```

### Audit Checklist

- [ ] All interactive elements have accessibility labels
- [ ] Images have descriptions or are marked decorative (`.accessibilityHidden(true)`)
- [ ] Color is not the only indicator of state or meaning
- [ ] Touch targets at least 44×44 points
- [ ] Dynamic Type supported — no fixed font sizes
- [ ] `prefers-reduced-motion` / `accessibilityReduceMotion` respected
- [ ] VoiceOver navigation order is logical
- [ ] Custom actions provided where gestures exist
