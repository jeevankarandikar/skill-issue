# Arrange, critique, polish, redesign

Read when running the matching mode. Severity levels and the AI-slop tells live in reference/critique.md.

## Arrange (`/design arrange`)

Fix layout, spacing, and visual rhythm on an existing surface.

### Squint Test (Do This First)

Blur your eyes or step back from the screen. You should see a clear hierarchy — 1-2 dominant elements, supporting elements, and subtle background elements. If everything has equal visual weight, spacing is the problem.

### Spacing System

Use `gap` over margins for sibling elements — eliminates margin collapse. Use a 4pt scale with semantic names:
- `--space-xs: 4px` — tight grouping (icon + label)
- `--space-sm: 8px` — related elements
- `--space-md: 16px` — section components
- `--space-lg: 24px` — component groups
- `--space-xl: 48px` — section separation
- `--space-2xl: 80px` — page-level whitespace

Vary spacing intentionally: a heading with extra space above reads as more important than identical spacing everywhere.

### Grid/Flex Decision

**Use Flexbox for 1D layouts** — a row of buttons, a nav bar, a single-column form.
**Use CSS Grid for 2D layouts** — card grids, dashboard tiles, magazine layouts.

Default: start with Flexbox. Upgrade to Grid only when you need 2D alignment.

```css
/* Responsive auto-fit grid */
.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: var(--space-lg);
}
```

Never `calc()` percentage hacks (`w-[calc(33%-1rem)]`) → use `grid-template-columns: repeat(3, 1fr)`.

### Z-Index System

No arbitrary z-index values. Build a semantic scale:

```css
--z-base: 0;
--z-raised: 1;
--z-dropdown: 100;
--z-sticky: 200;
--z-overlay: 300;
--z-modal: 400;
--z-toast: 500;
--z-tooltip: 600;
```

### NEVER
- Arbitrary spacing not on the 4pt scale
- Equal spacing on every element — vary for hierarchy
- Nested cards (card inside card inside card)
- CSS Grid when Flexbox is sufficient

---

## Critique (`/design critique`)

Full UX review of an existing surface. Score against Nielsen's heuristics. Run automated detection. Produce a severity-ordered issue list.

→ *Full protocol with all heuristics, persona patterns, and cognitive load checklist: [reference/critique.md](reference/critique.md)*

### Process

1. **Preparation**: Identify user personas, key tasks, entry paths
2. **LLM Assessment**: Score each of Nielsen's 10 heuristics 0-4 (total /40)
3. **Automated Scan**: Run `npx impeccable --json` in the terminal (fresh subagent if context is long); if the command fails, skip the automated scan and note it in the report
4. **Combined Report**: Merge findings, assign P0-P3, surface systemic patterns
5. **Recommendations**: Priority-ordered list with specific commands to fix each issue

**Anti-patterns verdict FIRST**: Does this look AI-generated? List specific tells before anything else.

### Severity Levels

- **P0 Blocking**: Prevents task completion — fix immediately
- **P1 Major**: WCAG AA violation or significant difficulty — fix before release
- **P2 Minor**: Annoyance, workaround exists — fix in next pass
- **P3 Polish**: No real user impact, nice-to-fix

### Nielsen Score

Typical real interfaces: 20-32 out of 40. Below 15 = needs fundamental restructuring.

### Output Format

Anti-patterns verdict → Executive Summary (score + issue count by severity) → Detailed findings by severity (location / category / impact / recommendation) → Systemic patterns → Recommended commands.

---

## Polish (`/design polish`)

Final quality pass before shipping. Apply after the feature is functionally complete.

**NEVER polish before functionally complete.** Polish on broken features wastes time.

### Pre-Polish Discovery

1. Grep for existing tokens and utility classes
2. Understand current spacing scale and component patterns
3. Identify what's shared vs one-off

### Polish Checklist

**Visual Alignment**
- [ ] All elements align to the spacing grid
- [ ] Cards/panels share consistent internal padding
- [ ] Icons vertically centered with text (optical alignment, not mathematical)

**Typography**
- [ ] Clear size hierarchy (large contrast steps, not slight differences)
- [ ] No widows/orphans — add `text-wrap: balance` to headings, `text-wrap: pretty` to body
- [ ] Line length ≤ 65ch on body copy
- [ ] Consistent Title Case vs sentence case throughout

**Color & Contrast**
- [ ] All text meets WCAG AA minimum (4.5:1 normal, 3:1 large)
- [ ] No pure gray (#808080) — use tinted grays
- [ ] Focus rings visible, meet 4.5:1 contrast against adjacent bg

**Interaction States — every interactive element needs all 8:**
default / hover / focus / active / disabled / loading / error / success

**Micro-interactions**
- [ ] Enter uses ease-out, exit faster than enter (~75% of enter duration)
- [ ] Never bounce/elastic easing on UI elements
- [ ] All animations respect `prefers-reduced-motion`

**Content & Copy**
- [ ] Consistent verb tense and terminology
- [ ] No AI clichés ("Seamless", "Elevate", "Unleash", "Next-Gen")
- [ ] No generic placeholder names ("John Doe", "Acme Corp")
- [ ] Error messages explain issue without blaming the user

**Edge Cases**
- [ ] Loading state — skeleton matching exact layout, not spinner
- [ ] Empty state — clear next action, illustrative
- [ ] Error state — specific message + recovery action

**Responsiveness**
- [ ] No horizontal scroll at 320px
- [ ] Touch targets ≥ 44×44px on mobile
- [ ] Readable at 200% browser zoom

---

## Redesign Existing Projects (`/design redesign`)

Comprehensive upgrade of an existing interface. Fix in priority order for maximum visible impact.

→ *Full audit protocol with detailed checklist: [reference/redesign.md](reference/redesign.md)*

### Fix Priority Order

1. **Font swap** — biggest instant improvement; replace Inter/Roboto/Open Sans immediately
2. **Color cleanup** — eliminate pure black/white, oversaturated accents, neon gradients
3. **Hover/active states** — add `scale(0.98)` or `translateY(-1px)` on every interactive element
4. **Layout/spacing** — asymmetry over centering, break equal-3-column grid
5. **Replace generic components** — cards → plain bg, 3-testimonial row → something better
6. **Add missing states** — loading skeletons, empty states, error states
7. **Typography scale** — increase contrast between heading weight and body weight

### Typography Upgrade

- Replace reflex fonts immediately (Inter, Roboto, Open Sans, DM Sans)
- Add headline presence: `font-weight: 700-900`, `letter-spacing: -0.02em` to `-0.04em`, `line-height: 1.1-1.2`
- Set body width: `max-width: 65ch`
- Add tabular-nums: `font-variant-numeric: tabular-nums` on all number displays
- Fix orphans: `text-wrap: balance` on headings, `text-wrap: pretty` on body paragraphs

### Color Cleanup

- `#000000` backgrounds → off-black (`#111111`, `#0A0A0A`)
- Oversaturated accent → desaturate to OKLCH chroma ≤ 0.18
- Consolidate to ONE accent color
- Tint shadows: `box-shadow: 0 4px 16px oklch(0 0 0 / 0.15)` not pure black shadows
- Remove any purple-blue AI gradient

### Layout Fixes

- `height: 100vh` → `min-height: 100dvh` everywhere
- Centered hero (variance > 4) → split screen or left-aligned
- Equal 3-column cards → 2-column zig-zag, asymmetric grid, or horizontal scroll
- Add container: `max-width: 1400px; margin: 0 auto; padding: 0 clamp(16px, 4vw, 40px)`

### Content & Copy

- Round numbers (99.99%, 50%) → organic data (47.2%, 312 users)
- Generic names → creative realistic names
- AI clichés ("Elevate your workflow") → concrete value statements
- Generic Lucide rocketships → Phosphor icons, semantically relevant

---

