# Redesign Existing Projects — Full Audit Protocol

Full checklist for `/design redesign`. Apply fixes in priority order from SKILL.md.

---

## Typography Audit

- [ ] Body font is Inter, Roboto, Open Sans, DM Sans, or Outfit → replace immediately
- [ ] Heading weight too close to body weight → increase heading to 700-900
- [ ] Letter-spacing missing on headlines → add `-0.02em` to `-0.04em`
- [ ] Line-height on headlines too loose → set `0.9-1.1` for hero type
- [ ] Body text wider than 65-75ch → add `max-width: 65ch`
- [ ] Numbers not tabular → add `font-variant-numeric: tabular-nums` on prices, stats, counts
- [ ] Widows/orphans in key text → add `text-wrap: balance` (headings) + `text-wrap: pretty` (body)
- [ ] Only 2 weights used and they're similar → increase contrast (Light 300 + Bold 700, not Regular + Medium)
- [ ] Heading sizes too similar → at least 1.5x ratio between display and h2

---

## Color Audit

- [ ] Background is `#000000` pure black → off-black (`#0A0A0A`, `#111111`)
- [ ] Accent is oversaturated → OKLCH chroma ≤ 0.18
- [ ] More than one accent color → consolidate to one
- [ ] Purple/blue gradient → solid color or directional gradient staying in one hue family
- [ ] Box-shadows use pure black → tint to brand hue, opacity 0.10-0.18
- [ ] Dark section unexpectedly appearing in light-mode page → remove or add transition
- [ ] Text is `#808080` pure gray → tint toward brand hue
- [ ] Contrast fails on secondary text → minimum 4.5:1

---

## Layout Audit

- [ ] `height: 100vh` → `min-height: 100dvh`
- [ ] Centered hero section when it should be asymmetric → split screen or left-aligned
- [ ] Equal 3-column card grid → 2-column zig-zag, asymmetric, or horizontal scroll
- [ ] No max-width on page → add `max-width: 1400px; margin: 0 auto`
- [ ] `padding: clamp(...)` missing on page edges → add responsive horizontal padding
- [ ] Card heights misaligned across a row → CSS Grid with `align-items: stretch`
- [ ] Feature list items don't align across columns → CSS Grid for feature rows, not nested divs
- [ ] No clear visual containment → add container with consistent internal padding

---

## Interaction States Audit

Every interactive element needs all 8 states:

- [ ] Hover: `opacity` shift, `background` change, or subtle `transform`
- [ ] Focus: visible focus ring at 4.5:1 contrast (not `outline: none`)
- [ ] Active: `scale(0.97-0.99)` or `translateY(1px)` on press
- [ ] Disabled: `opacity: 0.5`, `cursor: not-allowed`, `pointer-events: none`
- [ ] Loading: disabled state + spinner or progress indicator
- [ ] Error: red border + inline error message below field
- [ ] Success: confirmation message with clear next action
- [ ] Empty: illustration or icon + CTA (see empty states below)

Missing states to add: loading skeleton, empty state, error state, pressed feedback.

---

## Loading States Audit

- [ ] Circular spinner as primary loading pattern → replace with skeleton matching layout
- [ ] No loading state at all on async actions → add skeleton or progress
- [ ] Skeleton doesn't match actual layout dimensions → rebuild to match
- [ ] Button doesn't disable during async action → add `disabled` + loading state

---

## Empty State Audit

Every list/grid/table needs an empty state with all five:
- [ ] What will be here: "Your [items] will appear here"
- [ ] Why it matters: one sentence on the value
- [ ] How to start: primary CTA button
- [ ] Visual interest: illustration or icon (not just text)
- [ ] Contextual help: link to docs or 2-min demo

---

## Content Audit

- [ ] Round fake numbers (99.99%, 50K users, 1000+ integrations) → organic: 47.2%, 312 active, 94 integrations
- [ ] Generic names ("John Doe", "Sarah Chen", "Alex Smith") → specific, creative, diverse names
- [ ] AI clichés in headings/CTAs → concrete benefit statements
  - "Elevate your workflow" → "Ship features in half the time"
  - "Seamless experience" → "No installation, works in browser"
  - "Unleash potential" → specify what actually changes
- [ ] Passive voice CTAs ("Get started", "Sign up") → active value CTAs ("Build your first [thing]")
- [ ] Lorem ipsum anywhere → real representative content

---

## Component Audit

**Cards** (most common offender):
- [ ] Card has both border AND drop shadow → pick one or neither
- [ ] Card border-radius > 12px → reduce to 6-12px
- [ ] Card has `border-left: 3-5px solid [color]` stripe → remove entirely
- [ ] Card inside card inside card → flatten to 2 max

**Testimonials** (the 3-card row):
- Replace with large single quote, full-width, speaker name + role + avatar
- Or: scrollable carousel with 1.5 cards visible
- Never: 3 equal cards with generic headshots

**Hero metrics** (colored stat cards):
- Red/green/blue metric tiles → remove background colors entirely
- Use typography size and weight contrast instead

**Buttons**:
- [ ] Primary button has glow/outer shadow → remove
- [ ] CTA is a pill (`border-radius: 9999px`) in a content-heavy context → reduce to 6-8px radius
- [ ] No active press state → add `scale(0.98)`

**Navigation**:
- [ ] Desktop nav items too small to click → minimum 44px touch target even on desktop
- [ ] Mobile nav is just a hamburger with no visible menu indicator → show current section

---

## Icons Audit

- [ ] Using Lucide/Feather icons → replace with Phosphor Bold or Phosphor Fill
- [ ] Rocketship icon for "launch" or "deploy" → too generic; find semantic replacement
- [ ] Shield icon for "security" → too generic; find specific alternative
- [ ] Mixed stroke widths across icons → standardize to one weight (1.5px or 2px)
- [ ] Icons too small at 14-16px → minimum 18px, prefer 20-24px

---

## Code Quality Audit

- [ ] Non-semantic HTML: `<div onClick>` for buttons → `<button>`
- [ ] Inline styles mixed with class-based → move to CSS classes
- [ ] Fixed pixel values for font sizes → `rem` units
- [ ] Missing `alt` text on images → add descriptive alt
- [ ] `z-index: 9999` or other arbitrary z-index → semantic z-index scale
- [ ] Dead code: commented-out components, unused imports → delete

---

## Strategic Omissions (Common Missing Elements)

These are frequently missing and should be added to the redesign scope:

- **Legal links** (Privacy Policy, Terms) — required for any user-facing product
- **Back navigation** in multi-step flows — users need an escape hatch
- **404 page** — often completely unstyled
- **Form validation** — client-side for UX, note that server-side is still required
- **Skip-to-content link** — accessibility requirement
- **Cookie consent** — required in EU contexts
