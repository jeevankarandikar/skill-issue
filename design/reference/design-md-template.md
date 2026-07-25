# DESIGN.md template

A worked example, not a form. Sections that carry no decision for this project get deleted rather than filled with `[values]`.

## Phase 3: DESIGN.md (`/design generate-design-md`)

Generate `DESIGN.md` at the project root — single source of truth for the design system. AI tools (Google Stitch, Copilot), new contributors, and explicit design decisions all benefit from it.

```markdown
# Design System: [Project Title]

## 1. Visual Theme & Atmosphere
[Evocative description: mood, density, variance, motion intensity.
Example: "A restrained, gallery-airy interface with confident asymmetric layouts
and fluid spring-physics motion. Clinical yet warm — like a well-lit architecture studio."]

## 2. Color Palette & Roles
- **Canvas** ([OKLCH] / [hex]) — primary background surface
- **Surface** ([values]) — card and container fill
- **Primary Text** ([values]) — main content
- **Secondary Text** ([values]) — descriptions, metadata
- **Border** ([values]) — 1px structural lines
- **[Accent Name]** ([values]) — single accent for CTAs, active states, focus rings
Max 1 accent. Saturation < 80%. No purple/neon.

## 3. Typography Rules
- **Display:** [Font] — track-tight, weight-driven hierarchy, not screaming
- **Body:** [Font] — relaxed leading, 65ch max-width, neutral secondary color
- **Mono:** [Font] — code, metadata, timestamps, numbers in dense views
- **Banned fonts:** [list reflex fonts considered and rejected for this project]

## 4. Component Stylings
- **Buttons:** Flat, no outer glow. `-translate-y-[1px]` or `scale-[0.98]` on active.
- **Cards:** Only when elevation communicates hierarchy. Tint shadow to background hue.
  Dense layouts: replace with `border-t` dividers or negative space.
- **Inputs:** Label above, error below, `gap-2` for input blocks. No floating labels.
- **Loaders:** Skeletal shimmer matching exact layout dimensions. No circular spinners.
- **Empty States:** Composed illustrations — not just "No data" text.

## 5. Layout Principles
[Grid-first responsive architecture. Asymmetric splits for hero sections.
Single-column collapse below 768px. Max-width containment.
No flexbox percentage math. Generous internal padding.]

## 6. Motion & Interaction
[Spring physics: stiffness 100, damping 20. Staggered cascade reveals.
Perpetual micro-loops on active dashboard components.
Hardware-accelerated transforms only. Isolated client components for CPU-heavy animations.]

## 7. Anti-Patterns (Banned)
- No emojis
- No [reflex font names used in this project's evaluation]
- No pure black (#000000)
- No neon/outer glow shadows
- No gradient text (`background-clip: text` with gradient)

full canonical list: reference/critique.md
```

**Tips:** Be descriptive ("Deep Charcoal Ink (#18181B)" not "dark text"). Be functional (explain what each element is used for). Name colors by purpose, not appearance. Encode the bans — anti-patterns are as important as positive rules.

---

