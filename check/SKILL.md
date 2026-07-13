---
name: check
description: Quality and resilience checks. Use when reviewing technical quality, hardening for production, aligning with design system, or adapting to new device contexts.
version: 1.0.0
user-invocable: true
argument-hint: "[audit | harden | normalize | adapt | optimize]"
---

Quality checks and hardening for production-ready interfaces.

Scope: state-scoped frontend/production quality (not diff-scoped). Diff-vs-goal done-checks live in the verify skill; pre-work eval harnesses in the test skill.

| Mode | What it does |
|---|---|
| `/check audit` | Technical quality scan — 5 dimensions scored 0-4, P0-P3 severity report |
| `/check harden` | Production resilience — overflow, i18n, error handling, edge cases, input validation |
| `/check normalize` | Design system alignment — find drift, replace with tokens/components, clean up |
| `/check adapt` | Cross-device adaptation — mobile, tablet, desktop, print, email |
| `/check optimize` | Performance — Core Web Vitals, images, JS bundle, rendering, animations, React |

---

## `/check audit`

Run systematic technical quality checks. Document issues — don't fix them. Let other commands address findings.

**Before running**: If no DESIGN.md exists, run `/design generate-design-md` (or `/design teach` first when no `.impeccable.md` exists either).

### Diagnostic Scan: 5 Dimensions (Score 0-4 each)

When torn between two scores, assign the LOWER one. A score of 3+ requires zero P0/P1 findings in that dimension.

**1. Accessibility (A11y)**

Check:
- Contrast ratios < 4.5:1 (or 7:1 for AAA)
- Interactive elements missing proper ARIA roles/labels/states
- Missing focus indicators, illogical tab order, keyboard traps
- Improper heading hierarchy, missing landmarks, divs instead of buttons
- Missing or poor image alt text
- Inputs without labels, poor error messaging, missing required indicators

Score: 0=Fails WCAG A, 1=Major gaps (few ARIA, no keyboard nav), 2=Partial (some effort, significant gaps), 3=Good (WCAG AA mostly met), 4=Excellent (WCAG AA fully met, approaches AAA)

Mechanical path: run `npx @axe-core/cli <url>` or Lighthouse accessibility. Score from violations: 0 serious+ = 4; 1-2 = 3; 3-5 = 2; 6-10 = 1; >10 or any critical = 0. No running app: extract every fg/bg token pair from the theme file and compute the WCAG ratio ((L1+0.05)/(L2+0.05)); each pair < 4.5:1 (normal text) or < 3:1 (18px+/bold) is one P1.

**2. Performance**

Check:
- Layout thrashing (reading/writing layout properties in loops)
- Expensive animations (animating width/height/top/left instead of transform/opacity)
- Missing lazy loading, unoptimized images/assets
- Unnecessary imports, unused dependencies inflating bundle
- Unnecessary re-renders, missing memoization

Score: 0=Severe (layout thrash, unoptimized everything), 1=Major problems (no lazy loading, expensive animations), 2=Partial (some optimization), 3=Good (mostly optimized, minor gaps), 4=Excellent (fast, lean, well-optimized)

Mechanical path: `npx lighthouse <url> --only-categories=performance`; score 4 = LCP/INP/CLS all Good, 3 = one Needs-Work, 2 = two Needs-Work, 1 = any Poor, 0 = two+ Poor.

**3. Theming**

Check:
- Hard-coded colors not using design tokens
- Missing dark mode variants, poor contrast in dark theme
- Inconsistent token usage, mixing token types
- Values that don't update on theme change

Score: 0=No theming (everything hard-coded), 1=Minimal tokens, 2=Partial (inconsistently used), 3=Good (tokens used, minor hard-coded), 4=Excellent (full token system, dark mode perfect)

**4. Responsive Design**

Check:
- Fixed widths that break on mobile
- Touch targets < 44x44px
- Horizontal scroll on narrow viewports
- Layouts breaking when text size increases
- Missing mobile/tablet breakpoints

Score: 0=Desktop-only (breaks on mobile), 1=Major issues, 2=Partial (works roughly), 3=Good (responsive, minor issues), 4=Excellent (fluid, all viewports, proper touch targets)

**5. Anti-Patterns (CRITICAL)**

Check against all DON'T guidelines from `/design`. Look for AI slop tells: AI color palette, gradient text, glassmorphism, hero metrics with colored cards, generic fonts, nested cards, gray-on-color, bounce easing, redundant copy.

Score: 0=AI slop gallery (5+ tells), 1=Heavy AI aesthetic (3-4 tells), 2=Some tells (1-2), 3=Mostly clean (subtle), 4=No AI tells (distinctive, intentional)

### Generate Report

**Audit Health Score table**:

| # | Dimension | Score | Key Finding |
|---|-----------|-------|-------------|
| 1 | Accessibility | ? | [most critical issue] |
| 2 | Performance | ? | [most critical issue] |
| 3 | Responsive Design | ? | [most critical issue] |
| 4 | Theming | ? | [most critical issue] |
| 5 | Anti-Patterns | ? | [specific tells or "--"] |
| **Total** | | **??/20** | **[Rating]** |

Rating bands: 18-20 Excellent, 14-17 Good, 10-13 Acceptable (significant work), 6-9 Poor (major overhaul), 0-5 Critical.

**Anti-Patterns Verdict first**: Pass/fail — does this look AI-generated? List specific tells. Be brutally honest.

**Executive Summary**: Score + band. Issue count by severity (P0/P1/P2/P3). Top 3-5 critical issues. Recommended next steps.

**Detailed Findings by Severity**:

- **P0 Blocking**: Prevents task completion — fix immediately
- **P1 Major**: Significant difficulty or WCAG AA violation — fix before release
- **P2 Minor**: Annoyance, workaround exists — fix in next pass
- **P3 Polish**: Nice-to-fix, no real user impact

For each issue: Location (component, file, line) · Category · Impact · Standard violated · Recommendation · Suggested command

**Patterns & Systemic Issues**: Recurring problems indicating systemic gaps ("Hard-coded colors in 15+ components").

**Positive Findings**: Note what's working — good practices to replicate.

### Recommended Actions

List in priority order (P0 first). Available commands: `/tune bolder`, `/tune quieter`, `/tune colorize`, `/tune distill`, `/tune typeset`, `/tune animate`, `/tune delight`, `/tune clarify`, `/tune overdrive`, `/check harden`, `/check normalize`, `/check adapt`, `/design`, `/design polish`, `/design critique`. End with `/polish` if any fixes recommended.

After presenting, tell the user:
> You can ask me to run these one at a time, all at once, or in any order you prefer.
> Re-run `/check audit` after fixes to see your score improve.

**NEVER**: Report issues without explaining impact. Give generic recommendations (be specific). Skip positive findings. Forget to prioritize. Report false positives.

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

**NEVER**: Assume perfect input. Ignore i18n. Generic error messages ("Error occurred"). Forget offline scenarios. Fixed widths for text. Assume English-length text. Block entire interface when one component errors.

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
