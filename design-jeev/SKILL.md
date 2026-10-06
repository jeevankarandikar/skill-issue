---
name: design-jeev
description: >-
  Design, build and review a product interface in any stack: web, SwiftUI, AppKit,
  UIKit, Compose, Flutter, React Native or a terminal UI. Use to explore a new visual
  direction, to choose a front-end approach for a use case, to ship or polish UI in the
  real code, to review an interface before release, and for purposeful motion. Do not
  use for ordinary nonvisual coding, Figma files, video, or document work.
version: 6.2.0
user-invocable: true
argument-hint: "[explore | ship | review]"
---

# Design

Interface work runs in stages: explore a direction, ship it in the real code, review it before release. Enter at the stage the request names. Each stage ends by handing something to the next, and that handoff is not optional.

## Before any stage

- Find the stack from the project's manifests and its existing UI code, then work in it: its components, its tokens, its layout system, its test tools. The rules in this skill are stated as outcomes. [references/stacks.md](references/stacks.md) gives the mechanism for each stack. Never add a second UI framework or styling system to make one design easier.
- When there is no UI yet, or the request is to pick an approach, load [references/choosing.md](references/choosing.md) and choose by use case before writing anything.
- Read `DESIGN.md` at the repository root, or the design document the project's agent instructions name. It records the canon the project follows, its tokens, its banned assets, its surfaces and the decisions already made. If the project has none, draft one from [references/design-md-template.md](references/design-md-template.md) by reading the code, and ask only what the code cannot answer. During a review, report the missing file as a finding and write nothing.
- Follow the canon `DESIGN.md` names: Apple's Human Interface Guidelines, Material, or the project's own system. For Apple platforms and Apple-style web UI, read Apple's pages for the surface in hand at developer.apple.com/design/human-interface-guidelines, or the project's own digest of them when `DESIGN.md` names one. Open the page before quoting Apple or settling a close call. Where the canon is silent, decide from [references/principles.md](references/principles.md), which distills how the strongest product design teams think, where they agree, and how to choose where they disagree.
- When a company or brand design skill is installed, or `DESIGN.md` names a brand system, load it alongside this skill. It decides the brand: color, type, logo, voice and components. This skill supplies the stages and the craft underneath. Where the two conflict the brand system wins, except on access minimums, and the conflict is recorded as an open item.
- Use only fonts, icons and UI kits whose license the project has accepted.

Load a reference when the work touches its subject, and only then:

| Reference | Load it for |
| --- | --- |
| [lenses.md](references/lenses.md) | Shaping a screen or defending a decision: named designers' lenses, the UX laws, the disclosure ladder |
| [craft.md](references/craft.md) | Type, color, spacing, hierarchy, shadows and depth |
| [interaction.md](references/interaction.md) | Control states, forms, waiting, overlays, keyboard, motion timing, first run and empty states |
| [words.md](references/words.md) | Labels, buttons, errors and other interface text |
| [data-viz.md](references/data-viz.md) | Any chart or dashboard |
| [verticals.md](references/verticals.md) | What a field demands: money, developer tools, business software, health, shops, AI products, consumer apps, landing pages |

## Explore

Use this stage for a new direction, a new surface, or a redesign.

- Load [references/principles.md](references/principles.md) first, and [references/verticals.md](references/verticals.md) when the product sits in a field it covers. Before drawing, state the point of view in one sentence: what this product is for, and the one choice another good team would have made differently.

- If the session offers a design canvas (in Claude, the Design artifact type and the account's design systems), work there. Start from the project's design system, building one from `DESIGN.md` and the tokens in the code when the account has none. Show real alternatives with real content, and let the person choose by pointing.
- Without a canvas, render two alternatives in the project's own stack, on a preview route, a preview provider or a scratch screen.
- Alternatives differ in structure or hierarchy. Two color variations of one layout are a single alternative.
- Handoff: write the chosen direction into `DESIGN.md`. That means the tokens for color, type, spacing, radius and motion, the decisions made, and what was rejected with the reason. From then on, build from the file. A later change of direction goes into the file first.

## Ship

- Start from `DESIGN.md` and the existing components. Values come from tokens. For a focused adjustment, change only the requested quality.
- Keep composition deliberate and copy sparse and plain: no em dashes, no middle-dot separators, no filler, no pairs of clauses set against each other for effect. Avoid decorative emoji, gradient text and colored callout rails unless the product calls for them.
- Motion uses one token source, with values chosen by what the motion does. Support reduced motion, interruption and replay where relevant, and clean up when the view closes. Prefer the stack's own animation system over an added library.
- Run the interface and look at it. Inspect at the sizes and states that matter, including keyboard and focus, overflow, empty, loading and error. Measure performance claims, and call untested behavior untested.
- For polish, or any change a person will see, load [references/every-surface.md](references/every-surface.md) and hold the change to the whole inventory at every size.
- If the code has to depart from `DESIGN.md`, change the file in the same piece of work, with the reason under Decisions.
- Handoff: under Checked in `DESIGN.md`, record the date and the surfaces, sizes and states looked at, with where the screenshots or test results are.

## Review

- Run [references/review.md](references/review.md) on the rendered interface, starting from what Ship recorded under Checked. For Apple-style web UI, including web content inside a Mac app, also run [references/apple-hig-checklist.md](references/apple-hig-checklist.md). Native Apple code is reviewed against the Human Interface Guidelines pages for its surface. When the request is a judgment of the whole experience, or a redesign is on the table, also run [references/critique.md](references/critique.md).
- Handoff: the ranked findings, and new numbered open items for anything that waits on a person.
- Report findings as P0, P1 or P2, each with a location and the change to make. Where the canon and a merged project convention disagree, report the open item and leave the code alone.
- The reviewer is not the builder. Where the harness has subagents, give a fresh one the rendered surfaces and the requirement, and keep the builder's reasoning out of the brief.
