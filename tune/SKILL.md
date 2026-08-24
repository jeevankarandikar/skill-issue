---
name: tune
description: >-
  Move one dimension of a design that already exists - nine dials: bolder, quieter, colorize,
  distill, typeset, animate, delight, clarify, overdrive. Use when the ask names a single
  quality: "make it bolder", "tone it down", "the type is a mess". A new surface or full
  pipeline is design-jeev.
version: 1.0.0
user-invocable: true
argument-hint: "[bolder | quieter | colorize | distill | typeset | animate | delight | clarify | overdrive]"
---

Design adjustment dials. Each mode targets one dimension for a focused improvement pass.

| Mode | What it does |
|---|---|
| `/tune bolder` | Amplify bland/safe design — extreme scale, bold palette, spatial drama |
| `/tune quieter` | Reduce visual intensity — desaturate, lighten weights, increase breathing room |
| `/tune colorize` | Add strategic color to monochromatic interfaces — OKLCH, semantic colors, 60-30-10 |
| `/tune distill` | Strip to essence — remove clutter, progressive disclosure, ruthless simplification |
| `/tune typeset` | Fix font choices, hierarchy, scale, and readability |
| `/tune animate` | Add purposeful motion — entrances, micro-interactions, state transitions |
| `/tune delight` | Add joy and personality — celebrations, empty states, easter eggs |
| `/tune clarify` | Fix UX copy — error messages, labels, CTAs, empty states |
| `/tune overdrive` | Push past conventional limits — WebGL, spring physics, scroll-driven animations |

**Before any mode**: If no DESIGN.md exists, run `/design generate-design-md` (run `/design teach` first if `.impeccable.md` is also missing).

The dial being asked for: references/dials.md - read the matching section when running
this mode.

Every dial runs the same shape, so it is stated once here rather than nine times:
assess what is there now, plan the smallest change that moves that one dimension,
apply it, then look at it again. Moving a second dimension "while you're in there" is
the failure - that is what `/design` is for.

Durations, easing curves, and stagger intervals come from design's
reference/motion-design.md. This skill does not carry its own numbers; three files
carrying three different `--ease-out` curves is how that went wrong before.

