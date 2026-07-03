---
name: check
description: Quality and resilience checks. Use when reviewing technical quality, hardening for production, aligning with design system, or adapting to new device contexts.
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

Run systematic technical quality checks. Document issues — don't fix them. Let other commands address findings.

**Before running**: If no DESIGN.md exists, run `/design teach` first.

### Diagnostic Scan: 5 Dimensions (Score 0-4 each)

**1. Accessibility (A11y)**

Check:
- Contrast ratios < 4.5:1 (or 7:1 for AAA)
- Interactive elements missing proper ARIA roles/labels/states
- Missing focus indicators, illogical tab order, keyboard traps
- Improper heading hierarchy, missing landmarks, divs instead of buttons
- Missing or poor image alt text
- Inputs without labels, poor error messaging, missing required indicators

Score: 0=Fails WCAG A, 1=Major gaps (few ARIA, no keyboard nav), 2=Partial (some effort, significant gaps), 3=Good (WCAG AA mostly met), 4=Excellent (WCAG AA fully met, approaches AAA)

**2. Performance**

Check:
- Layout thrashing (reading/writing layout properties in loops)
- Expensive animations (animating width/height/top/left instead of transform/opacity)
- Missing lazy loading, unoptimized images/assets
- Unnecessary imports, unused dependencies inflating bundle
- Unnecessary re-renders, missing memoization

Score: 0=Severe (layout thrash, unoptimized everything), 1=Major problems (no lazy loading, expensive animations), 2=Partial (some optimization), 3=Good (mostly optimized, minor gaps), 4=Excellent (fast, lean, well-optimized)

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

List in priority order (P0 first). Available commands: `/tune bolder`, `/tune quieter`, `/tune colorize`, `/tune distill`, `/tune typeset`, `/tune animate`, `/tune delight`, `/tune clarify`, `/tune overdrive`, `/check harden`, `/check normalize`, `/check adapt`, `/design`, `/polish`, `/critique`. End with `/polish` if any fixes recommended.

After presenting, tell the user:
> You can ask me to run these one at a time, all at once, or in any order you prefer.
> Re-run `/check audit` after fixes to see your score improve.

**NEVER**: Report issues without explaining impact. Give generic recommendations (be specific). Skip positive findings. Forget to prioritize. Report false positives.

---

## `/check harden`

Strengthen interfaces against edge cases, errors, i18n, and real-world usage.

**Designs that only work with perfect data aren't production-ready.**

### Assess
Test scenarios to consider:
- Extreme inputs: very long text, very short, empty, emoji, RTL, accents, large numbers, 1000+ items
- Error scenarios: network failures, 400/401/403/404/429/500, validation errors, permission errors, concurrent ops
- Internationalization: German (30% longer), RTL, CJK characters, date/number formats, pluralization

### Text Overflow & Wrapping

```css
/* Single line with ellipsis */
.truncate { overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }

/* Multi-line clamp */
.line-clamp {
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

/* Allow wrapping */
.wrap { word-wrap: break-word; overflow-wrap: break-word; hyphens: auto; }

/* Prevent flex/grid overflow */
.flex-item { min-width: 0; overflow: hidden; }
.grid-item { min-width: 0; min-height: 0; }
```

### Internationalization

**Text expansion**: Budget 30-40% for translations. Flexbox/grid that adapts to content. Avoid fixed widths on text containers.

```jsx
// ❌ Bad: assumes short English text
<button className="w-24">Submit</button>
// ✅ Good: adapts to content
<button className="px-4 py-2">Submit</button>
```

**RTL support** — use logical properties:
```css
margin-inline-start: 1rem;   /* not margin-left */
padding-inline: 1rem;         /* not padding-left/right */
border-inline-end: 1px solid; /* not border-right */
[dir="rtl"] .arrow { transform: scaleX(-1); }
```

**Date/number formatting**:
```javascript
new Intl.DateTimeFormat('en-US').format(date);  // 1/15/2024
new Intl.DateTimeFormat('de-DE').format(date);  // 15.1.2024
new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(1234.56);
// Use proper i18n library for pluralization — not manual `${count} item${count !== 1 ? 's' : ''}`
```

### Error Handling

**By HTTP status**:
- 400: Show validation errors inline
- 401: Redirect to login
- 403: Show permission error with explanation
- 404: Show not found state with navigation
- 429: Show rate limit message with retry timing
- 500: Generic error + support contact

**Patterns**: Inline errors near fields. Clear + specific messages. Suggest corrections. Preserve user input on error. Retry button for network failures.

**Graceful degradation**: Core functionality without JavaScript. Alt text on images. Progressive enhancement. Fallbacks for unsupported features.

### Edge Cases

**Empty states**: No items, no results, no notifications — provide clear next action.

**Loading states**: Initial load, pagination, refresh — show what's loading, time estimates for long ops.

**Large datasets**: Pagination or virtual scrolling. Search/filter. Don't load 10,000 items at once.

**Concurrent operations**: Disable button while loading (prevent double-submit). Handle race conditions. Optimistic updates with rollback.

**Permissions**: Clear explanation of why access is denied. Read-only mode states.

### Input Validation

```html
<input
  type="text"
  maxlength="100"
  pattern="[A-Za-z0-9]+"
  required
  aria-describedby="username-hint"
/>
<small id="username-hint">Letters and numbers only, up to 100 characters</small>
```

Client-side validation for UX. Server-side validation always (never trust client-side alone). Validate + sanitize. Rate limiting.

### Accessibility Resilience

Keyboard: all functionality accessible, logical tab order, focus management in modals, skip links.

Screen readers: proper ARIA labels, live regions for dynamic changes, semantic HTML.

```css
@media (prefers-reduced-motion: reduce) {
  * { animation-duration: 0.01ms !important; transition-duration: 0.01ms !important; }
}
```

### Performance Resilience

**Slow connections**: Progressive image loading. Skeleton screens. Optimistic UI updates.

**Memory**: Clean up event listeners, cancel subscriptions, clear timers, abort pending requests on unmount.

**Debounce/throttle**:
```javascript
const debouncedSearch = debounce(handleSearch, 300);
const throttledScroll = throttle(handleScroll, 100);
```

**NEVER**: Assume perfect input. Ignore i18n. Generic error messages ("Error occurred"). Forget offline scenarios. Fixed widths for text. Assume English-length text. Block entire interface when one component errors.

### Verify
- Long text (100+ chars)? Emoji in all fields? RTL test? CJK? Network disabled? 1000+ items? Rapid clicks? API errors forced? All empty states?

---

## `/check normalize`

Analyze and align the feature to match design system standards, tokens, and patterns.

**Before running**: If no DESIGN.md exists, run `/design teach` first.

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

### Assess: Source vs. Target

1. **Source context**: What was it designed for? What assumptions were made (large screen, mouse, fast connection)?
2. **Target context**: Device (mobile/tablet/desktop/print), input method (touch/mouse/keyboard), screen constraints, connection speed, usage context (on-the-go vs. focused).
3. **Challenges**: What won't fit? What won't work (hover states on touch)? What's platform-inappropriate?

### Mobile Adaptation (Desktop → Mobile)

**Layout**: Single column. Vertical stacking. Full-width components. Max-width: 100%.

**Interaction**: Touch targets 44x44px minimum. Swipe gestures for lists/carousels. Bottom sheets instead of dropdowns. Thumbs-first design (controls in thumb reach zone). Larger tap areas with more spacing.

**Content**: Progressive disclosure. Prioritize primary content. Shorter text. 16px minimum body text.

**Navigation**: Bottom navigation bar or hamburger drawer. Reduce navigation complexity. Sticky header for context. Back button in flow.

### Tablet Adaptation (Hybrid)

**Layout**: Two-column (not one or three). Side panels for secondary content. Master-detail views. Adaptive by orientation.

**Interaction**: Support both touch and pointer. 44x44px touch targets. Side navigation drawers. Multi-column forms where appropriate.

### Desktop Adaptation (Mobile → Desktop)

**Layout**: Multi-column (use horizontal space). Side navigation always visible. Multiple panels simultaneously. Fixed widths with max-width constraints (don't stretch to 4K).

**Interaction**: Hover states for additional information. Keyboard shortcuts. Right-click context menus. Drag-and-drop. Multi-select with Shift/Cmd.

**Content**: More information upfront (less progressive disclosure). Data tables with many columns. Richer visualizations.

### Print Adaptation

Page breaks at logical points. Remove navigation, footer, interactive elements. Black/white or limited color. Proper margins. Expand shortened content (full URLs, hidden sections). Add page numbers, headers, metadata. `@media print` stylesheet.

### Email Adaptation

600px max width. Single column only. Inline CSS (no external stylesheets). Table-based layouts for email client compatibility. Large, obvious CTAs (not text links). No hover states. Deep links to web app for complex interactions.

### Implementation Techniques

**Breakpoints** (content-driven, not arbitrary):
- Mobile: 320-767px
- Tablet: 768-1023px
- Desktop: 1024px+

**CSS**: Grid/Flexbox for automatic reflow. Container queries for container-based adaptation. `clamp()` for fluid sizing. Media queries for distinct context styles. `display: none` sparingly (still downloads).

**Touch**: 44x44px minimum tap targets. More spacing between interactive elements. Remove hover-dependent interactions. Add touch feedback (ripples, highlights).

**Responsive images**: `srcset`, `picture` element. Lazy loading for off-screen content.

**Navigation**: Hamburger/drawer on mobile. Bottom nav bar for apps. Persistent side nav on desktop. Breadcrumbs for context on small screens.

**Test on real devices**: DevTools emulation is helpful but not perfect. Test portrait and landscape. Safari, Chrome, Firefox, Edge. iOS, Android, Windows, macOS. Touch + mouse + keyboard. 320px (smallest), 4K (largest). Throttled network.

**NEVER**: Hide core functionality on mobile. Assume desktop = powerful. Use different information architecture across contexts. Break platform expectations. Forget landscape orientation. Use arbitrary breakpoints blindly. Ignore touch on desktop (many desktop devices have touch).

### Verify
- Real devices tested? Both orientations? Multiple browsers? Different OS? Multiple input methods? Edge cases (320px, 4K, slow connection)?

---

## `/check optimize`

Improve runtime and load performance. **Measure before and after — never optimize by instinct.**

### Baseline First

```bash
# Lighthouse CI
npx lighthouse https://your-app.com --output=json --output-path=baseline.json

# Bundle analysis
npx source-map-explorer 'build/static/js/*.js'
# or for Next.js:
ANALYZE=true npm run build
```

### Core Web Vitals Targets

| Metric | Good | Needs Work | Poor |
|--------|------|------------|------|
| LCP (Largest Contentful Paint) | < 2.5s | 2.5-4s | > 4s |
| INP (Interaction to Next Paint) | < 200ms | 200-500ms | > 500ms |
| CLS (Cumulative Layout Shift) | < 0.1 | 0.1-0.25 | > 0.25 |

**Fixing LCP**: serve images via CDN, preload hero image (`<link rel="preload">`), inline critical CSS above the fold.

**Fixing INP**: break long tasks (> 50ms) with `scheduler.yield()` or `setTimeout(0)`, move heavy work to Web Workers.

**Fixing CLS**: `aspect-ratio` on images/video, reserve space for dynamic content (ads, embeds), `font-display: swap` + preload fonts.

```css
/* CLS prevention for images */
.hero-image {
  aspect-ratio: 16 / 9;
  width: 100%;
  height: auto;
}
```

### Images

```html
<!-- Modern formats with srcset -->
<picture>
  <source type="image/avif" srcset="hero.avif 1x, hero@2x.avif 2x">
  <source type="image/webp" srcset="hero.webp 1x, hero@2x.webp 2x">
  <img src="hero.jpg" alt="..." loading="lazy" decoding="async"
       width="800" height="450">
</picture>
```

- Lazy load everything below the fold: `loading="lazy"`
- `decoding="async"` on all images
- Serve via CDN with proper cache headers
- WebP for photos, SVG for icons/illustrations

### JavaScript Bundle

```js
// Route-based code splitting
const HeavyPage = lazy(() => import('./HeavyPage'));

// Dynamic imports for large deps
const { parse } = await import('date-fns');

// Tree shaking: named imports only
import { format } from 'date-fns'; // good — not import * as dateFns
```

- Run `npm ls` to find duplicate dependencies
- `npm dedupe` to consolidate
- Remove unused deps: `npx depcheck`

### CSS

```html
<!-- Critical CSS inline, rest deferred -->
<style>/* above-the-fold styles */</style>
<link rel="preload" href="styles.css" as="style" onload="this.onload=null;this.rel='stylesheet'">
```

CSS containment for complex components:
```css
.card { contain: layout style; }
.independent-widget { contain: strict; }
```

### Fonts

```css
@font-face {
  font-display: swap;           /* show fallback immediately */
  unicode-range: U+0000-00FF;   /* subset to Latin characters */
}
```

Preload critical fonts:
```html
<link rel="preload" href="/fonts/heading.woff2" as="font" type="font/woff2" crossorigin>
```

### Rendering

Batch DOM reads and writes — never interleave:

```js
// BAD: layout thrashing
elements.forEach(el => el.style.height = el.offsetHeight + 'px');

// GOOD: batch reads then writes
const heights = elements.map(el => el.offsetHeight); // all reads first
elements.forEach((el, i) => el.style.height = heights[i] + 'px'); // then all writes
```

`content-visibility: auto` for long scrolling lists:
```css
.list-item { content-visibility: auto; contain-intrinsic-size: 0 64px; }
```

Virtual scrolling for lists > 500 items (use `@tanstack/virtual` or `react-virtuoso`).

### Animations

```css
/* Animate ONLY transform and opacity — never layout properties */
/* BAD: triggers full repaint */
.bad { transition: width 300ms, height 300ms, top 300ms; }

/* GOOD: GPU-composited */
.good { transition: transform 300ms, opacity 300ms; }
```

Use `will-change: transform` right before an animation starts; remove it after:

```js
element.addEventListener('mouseenter', () => element.style.willChange = 'transform');
element.addEventListener('mouseleave', () => element.style.willChange = 'auto');
```

Use `IntersectionObserver` for scroll-triggered effects, never `window.addEventListener('scroll')`.

### React

```jsx
// Memoize expensive renders
const HeavyList = React.memo(({ items }) => (
  <ul>{items.map(item => <Item key={item.id} {...item} />)}</ul>
));

// Stable callbacks
const handleClick = useCallback((id) => removeItem(id), [removeItem]);

// Memoize derived data
const sortedItems = useMemo(() => [...items].sort(compareFn), [items]);
```

Avoid anonymous functions in JSX renders — creates new reference on every render.

### Verify

- Lighthouse score before and after?
- LCP, INP, CLS all in "Good" range?
- Bundle size delta measured?
- Tested on real mid-range Android device (not just MacBook)?
- Slow 3G throttled test passes?
