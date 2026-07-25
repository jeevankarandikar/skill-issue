# Aesthetic modes

Three committed looks. Read the one being asked for; they are alternatives, not a menu to blend.

## High-End Aesthetic (`/design high-end`)

Vanguard premium UI. When the brief demands museum-grade craft — "Apple Store", "luxury SaaS", "show the care."

### Variance Engine

**Pick ONE vibe archetype + ONE layout archetype before writing code.**

**Vibe archetypes:**
- **Ethereal Glass** — deep OLED black + radial mesh gradient + `backdrop-blur` panels, spectral accents, subtle noise texture
- **Editorial Luxury** — warm cream canvas + variable-weight serif headline + extreme negative space, single ink accent
- **Soft Structuralism** — silver-grey system + bold geometric grotesk + mathematical grid, no rounded corners

**Layout archetypes:**
- **Asymmetrical Bento** — fractional grid `2fr 1fr 1fr`, tiles at different heights, deliberate misalignment
- **Z-Axis Cascade** — layers with parallax depth, elements overlapping the fold
- **Editorial Split** — hard vertical divide, text left / media right (or reversed)

### Double-Bezel Architecture

```html
<!-- Outer shell -->
<div class="rounded-[2rem] bg-black/5 ring-1 ring-white/10 p-1.5">
  <!-- Inner core — radius MUST be smaller than outer -->
  <div class="rounded-[calc(2rem-6px)] bg-[--surface] shadow-[inset_0_1px_1px_rgba(255,255,255,0.2)]">
    <!-- Content -->
  </div>
</div>
```

Inner radius = outer radius − padding. Never two identical radii stacked.

### Button-in-Button Pattern

```html
<button class="flex items-center gap-3 px-4 py-2 rounded-full bg-[--accent]">
  <span>Get started</span>
  <span class="flex size-7 items-center justify-center rounded-full bg-white/20">
    <ArrowRight size={14} />
  </span>
</button>
```

### Macrowhitespace

Section padding: `py-24` to `py-40`. Never less than `py-16` for primary sections. `min-h-[100dvh]` — NEVER `h-screen`.

### Custom Easing

```css
--ease-premium: cubic-bezier(0.32, 0.72, 0, 1); /* iOS-like drawer feel */
```

### Scroll Entry

Elements start: `translate-y-16 blur-sm opacity-0` — resolve over `800ms+` with `--ease-premium`.
Use `IntersectionObserver` — NEVER `window.addEventListener('scroll')`.
Stagger: 80-120ms between grid items.

### Island Nav

```css
.island-nav {
  position: fixed;
  top: 1.5rem;
  left: 50%;
  transform: translateX(-50%);
  backdrop-filter: blur(12px);
  border: 1px solid rgba(255,255,255,0.1);
  border-radius: 9999px;
  padding: 8px 16px;
}
```

Hamburger morphs to X. Menu reveals as staggered mask-clipped items.

### Performance Rules

- Animate ONLY `transform` and `opacity` — never `top/left/width/height`
- `will-change: transform` only on elements about to animate; remove immediately after
- `backdrop-filter` on `position: fixed` or `position: sticky` elements only
- GPU promote with `translateZ(0)` or `transform: translate3d(0,0,0)`

---

## Brutalist Aesthetic (`/design brutalist`)

Industrial, raw, structural honesty. Functional beauty through material constraint.

### Pick ONE Mode — No Mixing

**Mode A: Swiss Industrial Print (Light)**
- Canvas: newsprint `#F4F4F0`
- Ink: carbon `#050505`
- Optional: subtle paper noise texture

**Mode B: Tactical Telemetry / CRT (Dark)**
- Canvas: terminal black `#0A0A0A`
- Foreground: white phosphor `#EAEAEA`
- Optional: CRT scanline overlay (see below)

**Single accent in BOTH modes: Aviation Hazard Red `#E61919`.**
No other accent. No gradients. No pastels.

### Typography

**Macro headers** (hero, section titles):
```css
font-family: "Neue Haas Grotesk Display", "Archivo Black", "Monument Extended";
font-size: clamp(4rem, 10vw, 15rem);
letter-spacing: -0.04em;
line-height: 0.9;
text-transform: uppercase;
```

**Micro-type** (data, labels, metadata):
```css
font-family: "JetBrains Mono", "IBM Plex Mono", "Space Mono";
font-size: 11px;
letter-spacing: 0.08em;
text-transform: uppercase;
```

**ZERO border-radius.** `border-radius: 0` on every element.

### Grid as Divider

```css
.brutalist-grid {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: 1px;                /* the gap IS the divider */
  background: #050505;     /* gap color */
}
.brutalist-grid > * {
  background: var(--canvas); /* cells get the actual bg */
}
```

### ASCII Framing

```
[ SECTION TITLE ]   ///   SUBSYSTEM   >>>   STATUS: ACTIVE
```

Use semantic HTML: `<kbd>`, `<samp>`, `<data>`, `<output>`, `<dl>`/`<dt>`/`<dd>`.

### CRT Scanlines (Mode B only)

```css
.crt-overlay::after {
  content: '';
  position: fixed;
  inset: 0;
  background: repeating-linear-gradient(
    0deg,
    transparent 0px, transparent 2px,
    rgba(0,0,0,0.1) 2px, rgba(0,0,0,0.1) 4px
  );
  pointer-events: none;
  z-index: 9999;
}
```

### NEVER in Brutalist Mode

- Any border-radius
- Pastels, gradients, glassmorphism, drop shadows
- Any accent besides `#E61919`
- Decorative images (data visualization is fine)
- Serif fonts

---

## Minimal Aesthetic (`/design minimal`)

Editorial minimalism. Restraint as craft. The absence of noise is the design.

### Canvas & Color

```
Canvas:     #F7F6F3 warm white (preferred) or #FFFFFF pure white
Body text:  #111111 (never pure black) / #2F3437
Secondary:  muted #787774
Borders:    ultra-light #EAEAEA / rgba(0,0,0,0.06)
```

**Accents — pick ONE, use only as background wash:**
- Pale red: `#FDEBEC`
- Pale blue: `#E1F3FE`
- Pale green: `#EDF3EC`
- Pale yellow: `#FBF3DB`

CTAs are `#111111` solid — not accent-colored.

### Typography

- Display: SF Pro Display / Geist Sans — large, `letter-spacing: -0.02em`, weight 300-400
- Editorial headings: Lyon Text / Newsreader / Instrument Serif (confirmed not on reflex list)
- Body: `font-size: clamp(16px, 2vw, 18px)`, `line-height: 1.65`, `max-width: 65ch`
- Links: underline on hover only, no color change

### Cards

```css
.card {
  border-radius: 8px;           /* 8-12px max — never larger */
  border: 1px solid #EAEAEA;
  padding: clamp(24px, 4vw, 40px);
  background: white;
  /* No box-shadow. Cards don't float. */
}
```

### Primary CTA

```css
.btn-primary {
  background: #111111;
  color: white;
  border-radius: 4px;           /* 4-6px only */
  padding: 10px 20px;
  transition: transform 160ms ease-out;
}
.btn-primary:active { transform: scale(0.98); }
```

### Motion

```css
.reveal {
  transform: translateY(12px);
  opacity: 0;
  transition: transform 600ms cubic-bezier(0.16, 1, 0.3, 1),
              opacity    600ms cubic-bezier(0.16, 1, 0.3, 1);
}
.reveal.visible { transform: translateY(0); opacity: 1; }
```

`IntersectionObserver` only. Stagger 80ms per item. Never window scroll events.

### Icons

Phosphor Bold/Fill or Radix UI Icons. Consistent 20-24px size. Never mix stroke weights.

### NEVER in Minimal Mode

- Inter, Roboto, Open Sans, generic Lucide icons
- Tailwind heavy shadows (`shadow-xl`, `shadow-2xl`)
- Primary-colored backgrounds on cards
- Gradients, neon, glassmorphism, outer glows
- Pill buttons on large container CTAs
- Emojis anywhere
- Lorem Ipsum or AI copy clichés
