# Swift concurrency

Read when the diff touches actors, `async`/`await`, `Sendable`, or an actor-isolation compiler error.

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

