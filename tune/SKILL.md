---
name: tune
description: Move one dimension of a design that already exists. Use when the ask names a single quality rather than a redesign - "make it bolder", "tone it down", "add some color", "strip it back", "the type is a mess", "give it some motion", "make it fun", "this copy is confusing", "push it further". Nine dials, one dimension each. A new surface or a full pipeline goes to design-jeev; a production-readiness pass goes to check.
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

