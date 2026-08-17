---
name: ios
description: Swift and Apple-platform work. Use when writing, reviewing, or debugging Swift, SwiftUI, or an Xcode project on iOS, macOS, or watchOS - including @Observable migration, actor-isolation and concurrency errors, type-safe NavigationStack, Dynamic Type, VoiceOver, and HIG review of a screen. Diff review belongs to a fresh-context reviewer; this skill holds the patterns it cites.
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

---

## Patterns

- SwiftUI - state and property wrappers, @Observable, composition, navigation,
  performance, previews: reference/swiftui-patterns.md
- Concurrency - actors, isolation, `Sendable`, async sequences, and the compiler
  errors that actually come up: reference/concurrency.md

Read the one the work needs. The property-wrapper decision table below is kept inline
because it gets consulted constantly and costs almost nothing.
