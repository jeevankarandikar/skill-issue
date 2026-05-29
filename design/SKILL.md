---
name: design
description: Full-pipeline design skill. Use when building a new feature, redesigning a surface, generating a DESIGN.md, designing onboarding flows, or any time UX planning, taste rules, production-grade UI implementation, or micro-interaction polish is needed. Invoke with a surface name for the full pipeline, or a mode keyword.
version: 3.0.0
user-invocable: true
argument-hint: "[surface | full-app | teach | generate-design-md | onboard | extract | arrange | critique | polish | redesign | high-end | brutalist | minimal]"
disable-model-invocation: true
---

# Design

Everything design in one skill — UX structure → taste rules → DESIGN.md → production code → micro-interaction polish → onboarding flows.

---

## Modes

| Invocation | What it does |
|---|---|
| `/design [surface]` | Full pipeline for one surface: shape → taste → build → polish |
| `/design full-app` | Full pipeline across all surfaces (prompts for surface list) |
| `/design teach` | Set up design context for the project (writes `.impeccable.md`) |
| `/design generate-design-md` | Generate or update `DESIGN.md` only |
| `/design onboard [flow]` | Design onboarding/first-run flows only |
| `/design extract [target]` | Pull reusable components and tokens into the design system |
| `/design arrange` | Fix layout, spacing, visual rhythm — squint test, spacing system, grid/flex |
| `/design critique [target]` | Full UX critique — Nielsen heuristics, automated scan, persona red flags |
| `/design polish` | Pre-ship final quality pass — all states, typography, copy, edge cases |
| `/design redesign` | Comprehensive upgrade of existing project — audit + fix priority sequence |
| `/design high-end` | Vanguard UI aesthetic — double-bezel, variance engine, spring physics |
| `/design brutalist` | Industrial/terminal aesthetic — Swiss print or CRT mode, hazard red only |
| `/design minimal` | Editorial minimalist — warm monochrome, washed pastels, invisible motion |
| `/design` | Ask what to design |

---

## Step 0: Context (Required Before ANY Design Work)

Design work produces generic output without project context. You MUST have confirmed context before touching any design task.

**Required context (minimum):**
- **Target audience** — who uses this and in what context?
- **Jobs to be done** — what are they trying to accomplish?
- **Brand personality** — how should the interface feel?

**Gathering order:**
1. Check loaded instructions for a `## Design Context` section — if present, proceed.
2. Check `.impeccable.md` in the project root — if it exists with required context, proceed.
3. If neither: STOP and run teach mode. Do NOT infer context from code. Code shows what was built, not who it's for.

---

## Teach Mode (`/design teach`)

One-time setup per project. Establishes design context.

### 1. Explore the Codebase
Scan before asking questions:
- README + docs: project purpose, audience, goals
- package.json: stack, existing design libraries
- Existing components: current patterns, spacing, typography in use
- CSS variables / tokens: existing palettes, font stacks, spacing scales
- Brand assets: logos, favicons, colors already defined

Note what you learned and what remains unclear.

### 2. Ask UX-Focused Questions
Ask only what you couldn't infer. Have a dialogue — don't dump all questions at once.

**Users & Purpose**
- Who uses this? What's their context when using it?
- What emotions should the interface evoke? (confidence, delight, calm, urgency)

**Brand & Personality**
- Brand personality in 3 words?
- Reference sites or apps that capture the right feel? What specifically about them?
- What should this explicitly NOT look like?

**Aesthetic Preferences**
- Visual direction: minimal, bold, elegant, playful, technical, organic?
- Light mode, dark mode, or both?
- Colors that must be used or avoided?

**Accessibility**
- WCAG level? Known needs: reduced motion, color blindness, screen readers?

### 3. Write Design Context

Synthesize into `.impeccable.md` at the project root:

```markdown
## Design Context

### Users
[Who they are, their context, the job to be done]

### Brand Personality
[Voice, tone, 3-word personality, emotional goals]

### Aesthetic Direction
[Visual tone, references, anti-references, theme decision and why]

### Design Principles
[3-5 principles that should guide all design decisions]
```

Ask if they also want this appended to `.github/copilot-instructions.md`.

---

## Phase 1: Shape (UX Planning)

Do NOT write code during this phase. Understand deeply first so implementation is precise.

### Discovery Interview

Adapt based on answers — have a natural dialogue, not a questionnaire dump.

**Purpose & Context**
- What problem does this feature solve?
- Who specifically will use it? (Role, context, frequency — not just "users")
- What does success look like?
- What's the user's state of mind arriving here? (Rushed? Exploring? Anxious? Focused?)

**Content & Data**
- What content or data does this display or collect?
- Realistic ranges: minimum, typical, maximum (e.g., 0 items, 5 items, 500 items)
- Edge cases: empty state, error state, first-time use, power user
- Is any content dynamic? What changes and how often?

**Design Goals**
- Single most important thing a user should do or understand here?
- What should this feel like? (Fast/efficient? Calm/trustworthy? Fun/playful? Premium?)
- Existing patterns in the product this should be consistent with?
- Examples inside or outside the product that capture the right feel?

**Constraints**
- Technical constraints: framework, performance budget, browser support
- Content constraints: localization, dynamic text length, user-generated content
- Mobile/responsive requirements?
- Accessibility beyond WCAG AA?

**Anti-Goals**
- What should this NOT be?
- Biggest risk of getting this wrong?

### Design Brief

Synthesize the interview into these sections. Present to user and get confirmation before Phase 2.

1. **Feature Summary** (2-3 sentences) — what, who, what it must accomplish
2. **Primary User Action** — the single most important thing
3. **Design Direction** — how it should feel; how it expresses the project's design context from `.impeccable.md`
4. **Layout Strategy** — spatial approach, hierarchy, rhythm (not CSS yet)
5. **Key States** — default, empty, loading, error, success, each edge case
6. **Interaction Model** — click/hover/scroll behavior; feedback; flow from entry to completion
7. **Content Requirements** — copy, labels, microcopy, empty state messages, dynamic content ranges
8. **Open Questions** — anything unresolved the implementer should resolve during build

If the user rejects the brief: iterate. If they reject twice, ask directly: "what did I get wrong about what you want here?"

---

## Phase 2: Taste Rules

Commit to metric-based rules before writing implementation code.

### Three Dials

Set at the start of the project. Adapt only when the user explicitly requests it.

- **DESIGN_VARIANCE: 8** (1 = perfect symmetry → 10 = artsy chaos)
- **MOTION_INTENSITY: 6** (1 = static → 10 = cinematic physics)
- **VISUAL_DENSITY: 4** (1 = art gallery airy → 10 = cockpit packed)

**Variance behavior:**
- 1-3: Flexbox `justify-center`, strict symmetrical grids, equal paddings
- 4-7: Overlapping margins, varied aspect ratios, left-aligned headers over centered data
- 8-10: Masonry layouts, fractional CSS Grid (`2fr 1fr 1fr`), massive empty zones (`padding-left: 20vw`)
- **Mobile override (levels 4-10):** Any asymmetric layout above `md:` MUST collapse to strict single-column (`w-full`, `px-4`, `py-8`) below 768px. No horizontal scroll.

**Motion behavior:**
- 1-3: No automatic animations. CSS `:hover` and `:active` only.
- 4-7: `transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1)`. Cascade delays on load-in. Transform and opacity only.
- 8-10: Scroll-triggered reveals or parallax. Framer Motion hooks. Never `window.addEventListener('scroll')`.

**Density behavior:**
- 1-3: Lots of white space, huge section gaps
- 4-7: Normal spacing for standard apps
- 8-10: Tiny paddings, no card boxes — 1px lines only. All numbers in `font-mono`.

### Typography

→ *Deep material on OpenType features, web font loading, and scales: [reference/typography.md](reference/typography.md)*

**Always apply these without consulting the reference:**
- Use a modular type scale with fluid sizing (`clamp()`) for headings on marketing/content pages. Use fixed `rem` scales for app/dashboard UIs.
- Fewer sizes with more contrast. A 5-step scale at 1.25 ratio beats 8 sizes at 1.1 apart.
- Line-height scales inversely with line length. Light text on dark backgrounds: add 0.05-0.1 to normal line-height.
- Cap line length at 65-75ch. Body wider than that is fatiguing.

**Font selection procedure — follow in order on every project:**

Step 1. Write 3 concrete brand voice words — not "modern" or "elegant" (dead categories). Examples: "warm mechanical opinionated", "fast dense unimpressed", "handmade slightly weird".

Step 2. List the 3 fonts you'd normally reach for. Reject any font from this list:

**BANNED — reflex fonts (monoculture across AI output):**
Fraunces, Newsreader, Lora, Crimson, Crimson Pro, Crimson Text, Playfair Display, Cormorant, Cormorant Garamond, Syne, IBM Plex Mono, IBM Plex Sans, IBM Plex Serif, Space Mono, Space Grotesk, Inter, DM Sans, DM Serif Display, DM Serif Text, Outfit, Plus Jakarta Sans, Instrument Sans, Instrument Serif

Step 3. Browse a font catalog with the 3 brand words in mind: Google Fonts, Pangram Pangram, Future Fonts, Adobe Fonts, ABC Dinamo, Klim Type Foundry. Look for something that fits the brand as a *physical object* — a museum label, a hand-painted shop sign, a 1970s mainframe manual, a fabric coat label. Reject the first thing that "looks designy." Keep looking.

Step 4. Cross-check: if your pick lines up with your reflex pattern, go back to Step 3.

**Typography rules:**
- Display/headlines: `text-4xl md:text-6xl tracking-tighter leading-none`. Hierarchy via weight and color, not just size.
- Body: `text-base leading-relaxed max-w-[65ch]`. Neutral secondary color.
- Dashboard/software UI: Sans-serif exclusively (`Geist` + `Geist Mono` or `Satoshi` + `JetBrains Mono`). Serif banned in dashboards.
- High-density (density > 7): all numbers in monospace.

### Color

→ *Deep material on contrast, accessibility, palette construction: [reference/color-and-contrast.md](reference/color-and-contrast.md)*

**Always apply these without consulting the reference:**
- Use **OKLCH**, not HSL. Perceptually uniform — equal lightness steps look equal. As you approach white/black, reduce chroma. Light blue at 85% lightness wants ~0.08 chroma, not 0.15.
- Tint neutrals toward the brand hue. Even 0.005-0.01 chroma creates subconscious cohesion.
- **60-30-10 by visual weight:** 60% neutral/surface, 30% secondary text/borders, 10% accent. Accents work because they're rare.
- Theme (light vs dark) derived from audience and context, not picked as default. A perp DEX → dark. A hospital portal → light. A wedding planner on Sunday morning → light. Don't default to dark "to look cool" or light "to be safe."

**BANNED:**
- AI purple/blue neon — no purple button glows, no neon gradients
- Pure black (#000000) — use Zinc-950, Charcoal, or Off-Black
- Pure white (#fff) — always tint
- Gradient text (`background-clip: text` + gradient) — see absolute bans in Phase 4
- Warm/cool gray fluctuation within one project

### Layout

→ *Deep material on grids, container queries, optical adjustments: [reference/spatial-design.md](reference/spatial-design.md)*

**Always apply these without consulting the reference:**
- CSS Grid over flexbox math. Never `calc()` percentage hacks (`w-[calc(33%-1rem)]`).
- Self-adjusting grid: `grid-template-columns: repeat(auto-fit, minmax(280px, 1fr))`
- Contain layouts: `max-w-[1400px] mx-auto` or `max-w-7xl`.
- Full-height sections: ALWAYS `min-h-[100dvh]`. NEVER `h-screen` (iOS Safari layout jump).
- **Centered hero sections: BANNED when DESIGN_VARIANCE > 4.** Force Split Screen (50/50), Left-Aligned/Right-Asset, or Asymmetric Whitespace.
- **3-column equal card layout: BANNED.** Use 2-column zig-zag, asymmetric grid, or horizontal scroll.
- `gap` over margins for sibling spacing. Eliminates margin collapse.
- Vary spacing for hierarchy — heading with extra space above reads as more important.
- Container queries for components, viewport queries for page layout.
- 4pt spacing scale with semantic names: `--space-xs: 4px`, `--space-sm: 8px`, `--space-md: 16px`, `--space-lg: 24px`, `--space-xl: 48px`.

### Architecture (React / Next.js)

- Verify `package.json` before importing any third-party library. Output install command if missing.
- Default to Server Components (RSC). Global state works ONLY in Client Components.
- Interactivity isolation: if motion is active, interactive components MUST be isolated leaf `'use client'` components. Server Components render static layouts only.
- Tailwind CSS for 90% of styling. Check Tailwind version — v3 and v4 syntax differ.
  - v4: use `@tailwindcss/postcss` or Vite plugin. Do NOT use `tailwindcss` plugin in postcss.config.js.
- Icons: `@phosphor-icons/react` or `@radix-ui/react-icons`. Standardize strokeWidth globally (1.5 or 2.0 — pick one).
- **No emojis anywhere — code, markup, text content, or alt text. Replace with icons or SVG.**

---

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
- No 3-column equal card layouts
- No centered hero sections (when variance > 4)
- No `border-left` / `border-right` > 1px as colored accent stripes
- No gradient text (`background-clip: text` with gradient)
- No AI copywriting clichés ("Elevate", "Seamless", "Unleash", "Next-Gen")
- No broken Unsplash links — use `picsum.photos/seed/{string}/800/600`
- No generic placeholder names ("John Doe", "Acme", "Nexus")
- No `h-screen` — always `min-h-[100dvh]`
```

**Tips:** Be descriptive ("Deep Charcoal Ink (#18181B)" not "dark text"). Be functional (explain what each element is used for). Name colors by purpose, not appearance. Encode the bans — anti-patterns are as important as positive rules.

---

## Phase 4: Build (Production Code)

### Design Direction

Commit to a bold aesthetic direction before writing code:
- **Purpose** — what problem does this interface solve? who uses it?
- **Tone** — pick an extreme: brutally minimal, maximalist chaos, retro-futuristic, organic/natural, luxury/refined, playful/toy-like, editorial/magazine, brutalist/raw, art deco/geometric, soft/pastel, industrial/utilitarian. Execute with intentionality.
- **Differentiation** — what makes this unforgettable? the one thing someone remembers?

Bold maximalism and refined minimalism both work. The key is intentionality, not intensity.

### Absolute Bans

Match and refuse — if you find yourself about to write either of these, stop and rewrite the element entirely.

**BAN 1: Side-stripe borders on cards / callouts / alerts**
- PATTERN: `border-left:` or `border-right:` with width > 1px
- FORBIDDEN: hard-coded colors AND CSS variables. All banned: `border-left: 3px solid red`, `border-left: 4px solid var(--color-warning)`, `border-left: 5px solid oklch(...)`.
- WHY: single most overused "design touch" in admin/dashboard/medical UIs. Never looks intentional.
- REWRITE: full borders, background tints, leading numbers/icons, or no visual indicator at all.

**BAN 2: Gradient text**
- PATTERN: `background-clip: text` (or `-webkit-background-clip: text`) + gradient background
- WHY: decorative not meaningful; one of the top three AI design tells
- REWRITE: solid color. For emphasis: weight or size, not gradient fill.

### AI Slop Test

If you showed this to someone and said "AI made this" — would they believe it immediately? If yes, that's the problem.

**Visual & CSS tells to eliminate:**
- Neon/outer glows → inner borders or subtle tinted shadows
- Pure black → Zinc-950 or Off-Black
- Oversaturated accents → desaturate to blend with neutrals
- Custom mouse cursors → banned
- Glassmorphism as decoration → purposeful only

**Typography tells:**
- Any font from the reflex list → banned
- Screaming H1s → control hierarchy with weight and color
- Serif fonts on dashboards → banned

**Layout tells:**
- 3-column equal card grids → zig-zag, asymmetric grid, or horizontal scroll
- Centered heroes (variance > 4) → split screen or left-aligned
- Same padding everywhere → vary for hierarchy

**Content tells:**
- Generic names ("John Doe", "Sarah Chan") → creative realistic names
- Generic SVG avatars → styled photo placeholders or `picsum.photos/seed/{string}/150/150`
- Fake round numbers (99.99%, 50%) → organic data: 47.2%, +1 (312) 847-1928
- Startup slop names ("Acme", "Nexus", "SmartFlow") → premium contextual names
- AI copy clichés ("Elevate", "Seamless", "Unleash", "Next-Gen") → concrete verbs

### Interactive States (Always Generate All Four)

- **Loading:** Skeletal loaders matching exact layout dimensions. No circular spinners.
- **Empty:** Composed empty states that teach the interface. Not just "nothing here."
- **Error:** Clear, inline error reporting.
- **Press feedback:** `transform: scale(0.98)` or `translateY(-1px)` on active for any pressable element.

### Creative Arsenal

Pull from these instead of defaulting to generic patterns:

**Navigation:** Mac OS Dock magnification, magnetic buttons (cursor pull), Dynamic Island pill, contextual radial menus, floating speed dial, mega menu reveal

**Layout:** Bento grid (asymmetric tiles like Apple Control Center), masonry, chroma grid (animated gradient borders), split-screen scroll (halves slide opposite directions), curtain reveal

**Cards:** Parallax tilt card (3D mouse tracking), spotlight border card (cursor-tracking illumination), holographic foil card (rainbow hover), morphing modal (button expands into dialog)

**Scroll:** Sticky scroll stack (cards stack on top), horizontal scroll hijack (vertical → horizontal pan), zoom parallax, scroll progress path (SVG draws itself)

**Typography:** Kinetic marquee (reverses on scroll), text mask reveal (hero text as video window), text scramble (Matrix-style decode on load), circular text path

**Micro-interactions:** Directional hover-aware button (fill enters from cursor entry side), ripple click effect, animated SVG line drawing, mesh gradient background, particle explosion button

**3D / Canvas (when warranted):** ThreeJS/WebGL for canvas backgrounds. GSAP ScrollTrigger for complex scrolltelling. NEVER mix GSAP/ThreeJS with Framer Motion in the same component tree. Use GSAP/ThreeJS exclusively for isolated full-page scroll or canvas backgrounds, wrapped in strict `useEffect` cleanup.

---

## Phase 5: Polish (Micro-Interactions)

→ *Deep material on timing, easing, and reduced motion: [reference/motion-design.md](reference/motion-design.md) and [reference/interaction-design.md](reference/interaction-design.md)*

Apply after the build is functionally complete. The last 5% that makes work feel crafted.

### Animation Decision Framework

Answer in order before writing any animation:

**1. Should this animate at all?**

| Frequency | Decision |
|---|---|
| 100+ times/day (keyboard shortcuts, command palette) | No animation. Ever. |
| Tens of times/day (hover effects, list nav) | Remove or drastically reduce |
| Occasional (modals, drawers, toasts) | Standard animation |
| Rare/first-time (onboarding, celebrations) | Can add delight |

Never animate keyboard-initiated actions — animation makes them feel slow and disconnected.

**2. Easing guide**

- Entering or exiting element → **ease-out** (starts fast, feels responsive)
- Moving/morphing on-screen → **ease-in-out** (natural acceleration/deceleration)
- Hover/color change → **ease**
- Constant motion (marquee, progress bar) → **linear**

Use custom easing — built-in CSS easings lack punch:
```css
--ease-out:    cubic-bezier(0.23, 1, 0.32, 1);
--ease-in-out: cubic-bezier(0.77, 0, 0.175, 1);
--ease-drawer: cubic-bezier(0.32, 0.72, 0, 1);  /* iOS-like drawer */
```

**Never use ease-in for UI animations.** It delays initial movement — exactly when the user is watching most closely. A dropdown at `ease-in` 300ms *feels* slower than `ease-out` at the same 300ms.

**3. Duration guide**

| Element | Duration |
|---|---|
| Button press feedback | 100-160ms |
| Tooltips, small popovers | 125-200ms |
| Dropdowns, selects | 150-250ms |
| Modals, drawers | 200-500ms |

Rule: UI animations under 300ms. A fast-spinning spinner makes loading feel faster even at identical load times.

### Component Polish Rules

**Buttons — always add press feedback:**
```css
.button { transition: transform 160ms ease-out; }
.button:active { transform: scale(0.97); }
```

**Never animate from scale(0):** Start from `scale(0.95)` + `opacity: 0`. Nothing in the real world disappears completely.

**Popovers — origin-aware:**
```css
.popover { transform-origin: var(--radix-popover-content-transform-origin); }
```
Exception: modals keep `transform-origin: center` — not anchored to a specific trigger.

**Tooltips:** Delay before first tooltip. Once any tooltip is open, adjacent ones open instantly — no animation, no delay. Makes the whole toolbar feel faster.

**Springs — when to use:**
- Drag interactions with momentum
- Elements that should feel "alive" (Dynamic Island)
- Gestures that can be interrupted mid-animation

Spring config:
```js
{ type: "spring", duration: 0.5, bounce: 0.2 }          // Apple approach
{ type: "spring", mass: 1, stiffness: 100, damping: 10 } // physics control
```
Keep bounce 0.1-0.3. Avoid bounce in most UI. Use for drag-to-dismiss and playful interactions.

**Interruptibility:** CSS transitions retarget mid-animation. Keyframes restart from zero. For rapidly-triggered elements (toasts, list toggles), always use transitions.

**clip-path for animation:**
```css
.hidden  { clip-path: inset(0 100% 0 0); } /* fully hidden from right */
.visible { clip-path: inset(0 0 0 0); }    /* fully visible */
```
Use for: tab color transitions (duplicate + clip), hold-to-delete, scroll image reveals, comparison sliders.

**@starting-style for entry without JS:**
```css
.toast {
  opacity: 1; transform: translateY(0);
  transition: opacity 400ms ease, transform 400ms ease;
  @starting-style { opacity: 0; transform: translateY(100%); }
}
```

**Stagger:** 30-80ms between items. Never block interaction during stagger.

**Asymmetric timing:**
```css
.overlay { transition: clip-path 200ms ease-out; }           /* release: fast */
.button:active .overlay { transition: clip-path 2s linear; } /* press: deliberate */
```

**Blur to mask imperfect crossfades:** When a crossfade looks off despite correct easing, add `filter: blur(2px)` during transition. Bridges the visual gap between two states. Keep under 20px — heavy blur is expensive in Safari.

### Performance Rules

- Animate ONLY `transform` and `opacity`. Animating `padding`, `margin`, `height`, `width` triggers full repaint.
- Never animate `top`, `left`, `width`, `height`.
- Don't update CSS variables on containers to drive drag — update `transform` directly. CSS variables on a parent trigger style recalc on all children.
- Framer Motion `x`/`y` shorthand: NOT hardware-accelerated. Use `transform: "translateX()"` for GPU acceleration.
- CSS animations beat JS under load (run off main thread). Use CSS for predetermined; JS for dynamic/interruptible.
- For programmatic CSS animations with JS control, use WAAPI:
  ```js
  element.animate([{ clipPath: 'inset(0 0 100% 0)' }, { clipPath: 'inset(0 0 0 0)' }], {
    duration: 1000, fill: 'forwards', easing: 'cubic-bezier(0.77, 0, 0.175, 1)'
  });
  ```
- Grain/noise filters on `fixed, pointer-events-none` pseudo-elements only. Never on scrolling containers.
- Perpetual motion / infinite loops: wrap in `React.memo`, isolate in their own microscopic Client Component.

### Accessibility

```css
@media (prefers-reduced-motion: reduce) {
  .element { animation: fade 0.2s ease; /* no transform-based motion */ }
}
@media (hover: hover) and (pointer: fine) {
  .element:hover { transform: scale(1.05); } /* gate hover — touch triggers on tap */
}
```

Reduced motion means fewer and gentler animations, not zero. Keep opacity/color transitions; remove movement.

### Polish Review Checklist

| Issue | Fix |
|---|---|
| `transition: all` | Specify: `transition: transform 200ms ease-out` |
| `scale(0)` entry animation | Start from `scale(0.95)` with `opacity: 0` |
| `ease-in` on UI element | Switch to `ease-out` or custom curve |
| `transform-origin: center` on popover | Set to trigger or use Radix CSS variable (modals exempt) |
| Animation on keyboard action | Remove entirely |
| Duration > 300ms on UI element | Reduce to 150-250ms |
| Hover without media query | Add `@media (hover: hover) and (pointer: fine)` |
| Keyframes on rapidly-triggered element | Switch to CSS transitions |
| Framer Motion x/y under load | Use `transform: "translateX()"` |
| Same enter/exit speed | Exit faster than enter |
| Elements appear simultaneously | Stagger 30-80ms between items |

---

## Onboarding Flows (`/design onboard`)

Run when scope includes first-run, empty states, or activation flows.

### Core Principles

- **Time to value:** Get users to "aha moment" ASAP. Teach the 20% that delivers 80% of value. Save advanced features for contextual discovery.
- **Show, don't tell:** Working examples over descriptions. Real functionality in onboarding, not a separate tutorial mode.
- **Make it optional:** Let experienced users skip. Don't block product access.
- **Context over ceremony:** Teach features when users encounter them — empty states are onboarding opportunities.
- **Respect intelligence:** Don't patronize. Assume users can handle standard patterns.

### First-Run Flow

1. **Welcome** — clear value proposition, time estimate (honest), skip option for experienced users
2. **Account setup** — minimal required info, smart defaults, explain why you're asking each question
3. **Core concepts** — introduce 1-3 concepts max; interactive not passive; progress indicator (step 1 of 3)
4. **First success** — guide to accomplish something real; pre-populated examples; celebrate completion briefly; clear next steps

### Empty State Design

Every empty state needs all five:
- **What will be here:** "Your recent projects will appear here"
- **Why it matters:** "Projects help you organize your work and collaborate with your team"
- **How to get started:** `[Create project]` or `[Start from template]`
- **Visual interest:** Illustration or icon — not just text on blank page
- **Contextual help:** "Need help? [Watch 2-min tutorial]"

Empty state types:
- **First use** — emphasize value, provide template
- **User cleared** — light touch, easy to recreate
- **No results** — suggest different query, offer to clear filters
- **No permissions** — explain why, how to get access
- **Error** — explain what happened, retry option

### NEVER
- Force users through long onboarding before they can use the product
- Show same tooltip or onboarding twice — track completion in `localStorage`, respect dismissals
- Block all UI during a tour
- Create a separate tutorial mode disconnected from the real product
- Overwhelm upfront — progressive disclosure
- Hide "Skip" or make it hard to find

---

## Extract Mode (`/design extract [target]`)

Pull reusable components and tokens into the design system. Follow the [extract flow](reference/extract.md). Pass any additional text as the extraction target.

---

## Pipeline Gates (Full Pipeline)

1. Context confirmed → proceed to Shape
2. Brief approved by user → proceed to Taste Rules
3. Taste rules committed → proceed to Build
4. Build complete → proceed to Polish
5. Polish applied → done

**Do NOT implement before the brief is approved.** Commit after each implementation step — never batch screens into one commit.

If the user says "skip planning, just build it": warn once that the result will be shallower. Offer a 5-minute shape pass as a compromise. If they insist, go directly to Phase 4.

---

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
3. **Automated Scan**: Run `npx impeccable --json` in a separate browser tab (isolated context)
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
