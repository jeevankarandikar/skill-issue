# SwiftUI patterns

Read when writing or reviewing SwiftUI.

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

