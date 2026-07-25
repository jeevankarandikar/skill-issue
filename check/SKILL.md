---
name: check
description: Production-readiness pass over a frontend surface as it currently stands. Use for "is this ready to ship", "audit the quality", "harden this", "it breaks on mobile", "make it match the design system", "it's slow", "the bundle is too big", "Core Web Vitals". Five modes - audit (score five dimensions, P0-P3 report), harden (overflow, i18n, error paths, hostile input), normalize (design-system drift), adapt (mobile, tablet, print, email), optimize (performance). Scoped to the state of a surface, not to a diff; diff-versus-goal done-checks are the verify skill.
version: 1.0.0
user-invocable: true
argument-hint: "[audit | harden | normalize | adapt | optimize]"
---

Quality checks and hardening for production-ready interfaces.

| Mode | What it does |
|---|---|
| `/check audit` | Technical quality scan — 5 dimensions scored 0-4, P0-P3 severity report |
| `/check harden` | Production resilience — overflow, i18n, error handling, edge cases, input validation |
| `/check normalize` | Design system alignment — find drift, replace with tokens/components, clean up |
| `/check adapt` | Cross-device adaptation — mobile, tablet, desktop, print, email |
| `/check optimize` | Performance — Core Web Vitals, images, JS bundle, rendering, animations, React |

---

## `/check audit`

Score the surface across five dimensions and report findings P0-P3.

Rubric, scoring bands, and report structure: references/audit.md - read when running
this mode.

When torn between two scores, assign the lower one. Rubrics without a tiebreak drift
optimistic, and an audit that grades generously is worth nothing.

A finding is worth reporting when someone could act on it tomorrow: it names a file,
an impact, and a change. Findings that fail that test are noise, and padding the count
with them makes the real ones harder to see.

---

## `/check harden`

Strengthen interfaces against edge cases, errors, i18n, and real-world usage.

**Designs that only work with perfect data aren't production-ready.**

Patterns and snippets: references/harden.md - read when running this mode.

### Assess
Test scenarios to consider:
- Extreme inputs: very long text, very short, empty, emoji, RTL, accents, large numbers, 1000+ items
- Error scenarios: network failures, 400/401/403/404/429/500, validation errors, permission errors, concurrent ops
- Internationalization: German (30% longer), RTL, CJK characters, date/number formats, pluralization

Dimensions covered (see references/harden.md for the patterns and code): text overflow & wrapping, internationalization, error handling by HTTP status, edge cases (empty/loading/large datasets/concurrent ops/permissions), input validation, accessibility resilience, performance resilience.

The assumption to attack: that the data will be well-formed and the network will
answer. A fixed-width container assumes English-length text; a generic "Error
occurred" assumes the user has another way to find out what happened; a component
that takes the whole interface down with it assumes it cannot fail.

### Verify
- Long text (100+ chars)? Emoji in all fields? RTL test? CJK? Network disabled? 1000+ items? Rapid clicks? API errors forced? All empty states?

Each item is pass/fail. Any un-run item goes in the report as "untested"; any failing item is a P1. Minimum evidence: paste the test input used, the DevTools network-offline result, and the forced-error screenshot or DOM state.

---

## `/check normalize`

Analyze and align the feature to match design system standards, tokens, and patterns.

**Before running**: If no DESIGN.md exists, run `/design generate-design-md` (or `/design teach` first when no `.impeccable.md` exists either).

### Plan: Understand Before Changing

1. **Discover the design system**: Grep for "design system", "ui guide", "style guide", component libraries, token files. Understand: core design principles, target audience, component patterns, design tokens (colors, typography, spacing). If something's unclear, ask — don't guess.

2. **Analyze drift**: Where does the feature deviate? Which inconsistencies are cosmetic vs. functional? Root cause: missing tokens, one-off implementations, or conceptual misalignment?

3. **Normalization plan**: Which components can be replaced with design system equivalents? Which styles need tokens instead of hard-coded values? How can UX patterns match established user flows?

### Execute

Apply systematically across these dimensions:

- **Typography**: Design system fonts, sizes, weights, line heights. Replace hard-coded values with typographic tokens or utility classes.
- **Color & Theme**: Design system color tokens. Remove one-off color choices that break the palette.
- **Spacing & Layout**: Spacing tokens for margins, padding, gaps. Align with grid systems and layout patterns used elsewhere.
- **Components**: Replace custom implementations with design system components. Match props and variants to established patterns.
- **Motion & Interaction**: Match animation timing, easing, and interaction patterns to other features.
- **Responsive Behavior**: Ensure breakpoints and responsive patterns align with design system standards.
- **Accessibility**: Verify contrast ratios, focus states, ARIA labels match design system requirements.
- **Progressive Disclosure**: Match information hierarchy and complexity management to established patterns.

### Clean Up

- **Consolidate**: New reusable components should go to shared UI path.
- **Remove orphaned code**: Delete unused implementations, styles, files made obsolete by normalization.
- **Verify quality**: Lint, type-check, test. Ensure normalization didn't introduce regressions.
- **DRY check**: Look for duplication introduced during refactoring — consolidate.

**NEVER**: Create new one-off components when design system equivalents exist. Hard-code values that should use tokens. Introduce patterns that diverge from the design system. Compromise accessibility for visual consistency.

---

## `/check adapt`

Adapt designs to work across different screen sizes, devices, or contexts.

**Adaptation is not just scaling — it's rethinking the experience for the new context.**

Patterns and snippets: references/adapt.md - read when running this mode.

### Assess: Source vs. Target

1. **Source context**: What was it designed for? What assumptions were made (large screen, mouse, fast connection)?
2. **Target context**: Device (mobile/tablet/desktop/print), input method (touch/mouse/keyboard), screen constraints, connection speed, usage context (on-the-go vs. focused).
3. **Challenges**: What won't fit? What won't work (hover states on touch)? What's platform-inappropriate?

Contexts covered (see references/adapt.md for the full patterns): mobile adaptation, tablet adaptation, desktop adaptation, print adaptation, email adaptation, implementation techniques (breakpoints, CSS, touch, responsive images, navigation, real-device testing).

**NEVER**: Hide core functionality on mobile. Assume desktop = powerful. Use different information architecture across contexts. Break platform expectations. Forget landscape orientation. Use arbitrary breakpoints blindly. Ignore touch on desktop (many desktop devices have touch).

### Verify
- Real devices tested? Both orientations? Multiple browsers? Different OS? Multiple input methods? Edge cases (320px, 4K, slow connection)?

Each item is pass/fail. Any un-run item goes in the report as "untested"; any failing item is a P1. Minimum evidence: paste the test input used, the DevTools network-offline result, and the forced-error screenshot or DOM state.

---

## `/check optimize`

Improve runtime and load performance. **Measure before and after — never optimize by instinct.**

Patterns and snippets: references/optimize.md - read when running this mode.

### Core Web Vitals Targets

| Metric | Good | Needs Work | Poor |
|--------|------|------------|------|
| LCP (Largest Contentful Paint) | < 2.5s | 2.5-4s | > 4s |
| INP (Interaction to Next Paint) | < 200ms | 200-500ms | > 500ms |
| CLS (Cumulative Layout Shift) | < 0.1 | 0.1-0.25 | > 0.25 |

Areas covered (see references/optimize.md for the commands, snippets, and code): baseline measurement (Lighthouse, bundle analysis), fixing LCP/INP/CLS, images, JS bundle, CSS, fonts, rendering, animations, React.

### Verify

- Lighthouse score before and after?
- LCP, INP, CLS all in "Good" range?
- Bundle size delta measured?
- Tested on real mid-range Android device (not just MacBook)?
- Slow 3G throttled test passes?
