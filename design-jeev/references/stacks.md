# The same outcomes in each stack

The skill states rules as outcomes. This file names the mechanism per stack, so the rule lands in the project's own idiom. Read only the section for the stack in hand. If the stack is not here, answer the seven questions below for it before designing.

## What every stack has to answer

- Where tokens live, so no color, size, space or duration is typed inline.
- How text scales with the person's setting.
- How light and dark appearance are followed.
- How reduced motion is honored.
- How keyboard, focus and a screen reader reach every control.
- How a view is rendered for inspection without running the whole product.
- What can be asserted by a test.

## Web (HTML and CSS, with or without a framework)

- Tokens are CSS custom properties on `:root`, or the theme file of the styling system already in use. Utility classes map to the same tokens.
- Sizes in `rem`, the page usable at 200 percent zoom, text wrapping in scrolling content.
- `prefers-color-scheme` and `color-scheme`, with a manual switch only if the project decided to have one.
- `prefers-reduced-motion`, applied at the token level so every animation obeys it.
- Semantic elements first, then ARIA. `:focus-visible` rings that are never clipped. Tab order follows reading order.
- Inspect on a preview route or a component workshop if the project has one, in a real browser at each width.
- Assert with a browser test runner: computed styles against the scale, clipped text, contrast, focus order, screenshot comparison.
- Layout with flex, grid and container queries. A flex child that holds text needs `min-width: 0` to truncate correctly.

## SwiftUI, AppKit and UIKit

- Tokens are asset-catalog colors and a small set of static values or a custom `EnvironmentValues` entry. System semantic colors and text styles come first.
- On iOS and iPadOS, Dynamic Type: text styles and `@ScaledMetric` in SwiftUI, `UIFontMetrics` in UIKit. Check the largest accessibility size. macOS has no Dynamic Type, so use the system text styles and check the window at its smallest size.
- Asset-catalog color variants and the system appearance. No app-level override unless the project decided on one.
- Reduced motion, checked where the animation is declared: `accessibilityReduceMotion` in the SwiftUI environment, `UIAccessibility.isReduceMotionEnabled` in UIKit, `NSWorkspace.shared.accessibilityDisplayShouldReduceMotion` in AppKit.
- Accessibility labels, traits and the focus system. On the Mac, full keyboard access and menu-bar commands for every action.
- Inspect with previews, one per state and size class, then in the simulator or the running app.
- Assert with snapshot tests and UI tests. Layout warnings in the console count as findings.
- SF Symbols belong to native Apple code only.

## Jetpack Compose

- Tokens are the `MaterialTheme` color scheme, typography and shapes, plus a `CompositionLocal` for anything the theme lacks.
- Text in `sp`, layout in `dp`. Check font scale 2.0.
- `isSystemInDarkTheme` and dynamic color where the project uses it.
- Read the system animator duration scale (`Settings.Global.ANIMATOR_DURATION_SCALE`) and skip nonessential motion when it is zero.
- `Modifier.semantics`, content descriptions, 48 dp touch targets, TalkBack traversal order.
- Inspect with `@Preview` at several devices and font scales.
- Assert with Compose UI tests and screenshot tests.

## Flutter

- Tokens are `ThemeData` and `ThemeExtension` classes. No literal colors or paddings in widgets.
- Respect `MediaQuery` text scaling. Check the largest setting without overflow stripes.
- `ThemeMode.system` with matching light and dark themes.
- `MediaQuery.disableAnimationsOf(context)`.
- `Semantics` widgets, focus traversal groups, 48 logical pixel targets.
- Inspect with widget previews or a catalog app, on a phone size and a tablet size.
- Assert with widget tests and golden files.

## React Native

- Tokens are one theme module, read through the styling approach already in the project.
- Leave font scaling on. Check the largest setting.
- `useColorScheme`.
- `AccessibilityInfo.isReduceMotionEnabled`, applied in the animation helpers.
- `accessibilityLabel`, `accessibilityRole`, 44 pt and 48 dp targets by platform.
- Inspect in both simulators. The platforms differ in shadows, fonts and safe areas.
- Assert with component tests and device-level screenshot tests.

## Terminal UI

- Tokens are a small palette of named roles mapped to ANSI colors. Never depend on one terminal theme.
- Respect `NO_COLOR`, and keep meaning legible without color.
- Layout holds at 80 columns and reflows on resize. Measure the width of wide characters and emoji with a width library.
- Motion is limited to spinners and progress, off when output is not a terminal.
- Every action reachable by keyboard, with the keys shown on screen.
- Screen readers read the terminal as lines of text, so state changes are written as words and redraws do not repeat the whole screen where a plain mode can avoid it.
- Inspect in a narrow and a wide terminal, light and dark.
- Assert with rendered-frame snapshot tests.
