# /check audit

The five-dimension production-readiness score. Read when running this mode.

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

