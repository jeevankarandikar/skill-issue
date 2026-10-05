# Choosing a front-end approach

Load this when a project has no interface yet, or when the request is to pick a stack, a component source or a design tool. In an existing project the answer is the stack it already has. A rewrite needs a reason the person has stated.

## Ask these first

- Who uses it, and on what device.
- Whether it is mostly reading or mostly doing.
- Whether it has to feel native to one platform.
- Whether it works offline or holds private data on the device.
- Who maintains it afterward, and what they already know.

## By use case

| Use case | Default choice | Why, and when to leave it |
|---|---|---|
| Marketing site, docs, blog | Static HTML and CSS from a content-first site generator, with small islands of script | Pages are read, so speed and plain markup matter most. Add a framework only for a real interactive section. |
| Web app with accounts, forms and tables | The component framework the team knows, with accessible headless primitives and the project's own tokens | Behavior such as focus traps, menus and comboboxes is hard to get right by hand. Take the behavior from a library and own the look. |
| Dashboard or data-heavy tool | Same as a web app, plus one charting library used through a thin wrapper | A wrapper keeps every chart on the tokens. Dense tables need real keyboard support. |
| Internal tool with few users | The fastest stack the team can maintain, with a ready component kit left mostly at its defaults | Time matters more than identity. Keep accessibility and the review stage. |
| Mac app | SwiftUI with AppKit where it runs out | Menus, windows, shortcuts and settings should behave as the system does. A web view inside a native shell is reasonable when the content is mostly documents. |
| iPhone or iPad app | SwiftUI | Native text scaling, gestures and sheets come with it. |
| Android app | Jetpack Compose with Material | Same reasoning for Android. |
| One team shipping to iOS and Android | React Native if the team writes React, Flutter if it wants one rendering engine and its own look | Budget time for each platform's conventions either way. |
| Web app and mobile apps sharing code | A responsive web app first, then React Native with shared logic if a store app is required | Sharing logic and tokens is realistic. Sharing every screen usually costs the native feel on one side. |
| Desktop app for Windows, Linux and Mac together | A web UI in a native shell, choosing the shell by how much system access is needed | One codebase, with each platform's menus, shortcuts and window behavior handled per platform. Go native per platform when system feel is the product. |
| Command-line tool people watch | A terminal UI library in the tool's own language | Keep a plain, pipeable mode beside it. |
| Prototype or a direction to show someone | A design canvas or one self-contained page | It is thrown away after the choice is recorded. Do not grow it into the product. |

## Where the look comes from

- A platform canon when the product should feel native: Apple's guidelines or Material.
- The project's own system when the product has an identity to hold across platforms. It lives in `DESIGN.md` and in tokens.
- A component kit's defaults when speed matters more than identity. Say so in `DESIGN.md`, so nobody polishes against a canon the project never chose.

## Canvas or code

- Use a design canvas to compare directions, to settle hierarchy and tone, and to show someone who will not run the code.
- Design in the code when the question is about real data, states, motion or the feel of an input.
- Either way, the chosen direction is written into `DESIGN.md` before it is built.

## Before recommending a library

Check that it is maintained, that its license suits the project, that it supports keyboard and screen readers, and that it can take the project's tokens. Read its current documentation; versions and defaults change faster than this file.
