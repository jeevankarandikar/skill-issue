# SwiftUI Implementation

Design *in* SwiftUI — the taste layer on top of the correctness floor (the `@Observable` macro, type-safe navigation, modifier order, reduce-motion gating are baseline; this file is about making it look intentional). iOS 26+ assumed.

## Liquid Glass (iOS 26+) — the 2026 default material

Liquid Glass is the system material for the navigation and control layer. Adopt it, but obey the layering law or it turns to mud.

```swift
.glassEffect(.regular, in: .capsule)                // default adaptive glass
.glassEffect(.regular.tint(.accent).interactive())  // tint = primary actions ONLY
.buttonStyle(.glass)                                 // translucent
.buttonStyle(.glassProminent)                        // opaque, primary
```

- **Layering law (the rule that matters):** glass belongs ONLY to the layer floating *above* content — nav bars, toolbars, controls, sheets. NEVER on the content layer (lists, tables, cells, media). Three layers: content (no glass) → navigation (glass) → overlay (vibrancy on glass).
- **Group glass elements** in a `GlassEffectContainer(spacing:)` — glass can't sample other glass; the container gives them a shared sampling region. Use `.glassEffectID(_:in:)` + a shared namespace for morphing transitions.
- **Tint sparingly** — `.tint()` marks a *primary* action. Tinting everything defeats the point.
- **Accessibility is automatic** — Reduce Transparency adds frosting, Increase Contrast goes stark, Reduce Motion calms it. Don't override with custom opacity; let the system handle it.

**Anti-patterns (bans):** glass everywhere · glass-on-glass stacking · tinting every control · glass over busy/animated content (readability fail — dim or fade the background first) · custom opacity that bypasses accessibility.

**Adoption:** recompile with Xcode 26 (basic adoption is free, no code change). Temporary opt-out: `UIDesignRequiresCompatibility = true` in Info.plist (expires iOS 27 — not a real escape).

## Type, Color, Spacing — system, not magic numbers

- **Dynamic Type, always.** Semantic fonts (`.font(.body)`, `.title`, `.headline`), never `.font(.system(size: 16))`. This is design consistency *and* accessibility — fixed sizes break both.
- **Semantic colors in the Asset Catalog** with light/dark variants, referenced by name. Never hardcode `Color(red:green:blue:)` inline.
- **No magic spacing.** Define a scale (4/8/12/16/24…) and use it; `.padding(16)`, not `.padding(13)` here and `.padding(17)` two views later.

## Layout & Hierarchy

- `VStack/HStack/ZStack` for linear layout; `LazyVStack/LazyHStack` once a list passes ~100 items; `GeometryReader` sparingly (it's an escape hatch, not a default).
- **Modifier order is load-bearing for appearance.** `.padding().background()` ≠ `.background().padding()` — the first fills *including* the padding, the second fills then pads outside. Decide deliberately.
- Extract repeated visual treatments into a `ViewModifier` (e.g. `CardStyle`) instead of copy-pasting `.shadow().cornerRadius()`. One source of truth for the look.

## Motion

- `withAnimation { }` for state-driven transitions; prefer `.spring()` or `.easeInOut`.
- **Gate decorative motion on `@Environment(\.accessibilityReduceMotion)`** — provide a cross-fade alternative, never just kill it.

## Navigation (iOS 16+)

- `NavigationStack` + `.navigationDestination(for:)` (type-safe). Never deprecated `NavigationView`. Use `@Environment(\.dismiss)`, not `presentationMode`.

## Accessibility = design

- `.accessibilityLabel` on every non-text control; correct traits (Button vs Image). Full Dynamic Type support. VoiceOver is part of the design, not an afterthought.

## Reach for a library only when warranted (verified, 2026)

- State architecture at scale: `pointfreeco/swift-composable-architecture` (~14.7k★)
- Vector animation: `airbnb/lottie-ios` (~26.8k★)
- UIKit escape hatch under SwiftUI: `siteline/swiftui-introspect` (~6.5k★)
- Popups/toasts: `exyte/PopupView` (~4k★) · View unit testing: `nalexn/ViewInspector` (~2.6k★)
- Charts: prefer Apple's native **Swift Charts** (see [data-viz.md](../data-viz.md)); `danielgindi/Charts` (~28k★) only for UIKit/legacy.

---

**Avoid**: glass on the content layer · `.font(.system(size:))` (breaks Dynamic Type) · magic spacing numbers · `NavigationView` · ungated decorative animation · hardcoded inline colors. Sources: Apple HIG (Materials, Liquid Glass) + WWDC25; `conorluddy/LiquidGlassReference` as a digest.
