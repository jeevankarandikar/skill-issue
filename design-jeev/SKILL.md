---
name: design-jeev
description: Design work end to end - UX shape, taste rules, DESIGN.md, production UI code, micro-interaction polish. Use for "design this screen", "build the landing page", "make this look better", "redesign it", "this looks AI-generated", onboarding and first-run flows, brand assets, or exploring visual directions. Owns the canonical motion timings, easing curves, severity levels, and AI-slop tells that other skills reference rather than restate. Start a cold project with `lab`. A single-dimension adjustment to an existing surface goes to tune; a production-readiness pass goes to check.
version: 4.0.0
user-invocable: true
argument-hint: "[surface | lab | assets | full-app | teach | generate-design-md | onboard | extract | arrange | critique | polish | redesign | high-end | brutalist | minimal]"
---

# Design

Everything design in one skill — UX structure → taste rules → DESIGN.md → production code → micro-interaction polish → onboarding flows.

**New to a project, or no design context yet? Start with `/design lab [surface]`** — it renders a few real directions to react to, needs zero setup, and infers the rest from what you pick.

The bans here aren't personal quirks. Anthropic's own frontend-design skill and Vercel's v0 independently ban the same tells — purple/violet gradients and converging on reflex fonts (Inter, Space Grotesk). When justifying or killing a direction, reason from named priors rather than asserting taste: [reference/design-priors.md](reference/design-priors.md).

Every build/polish pass also applies the vendored [reference/interfaces-cheat-sheet.md](reference/interfaces-cheat-sheet.md) (interfaces.dev, Rauno Freiberg) as the mechanical floor — radius concentricity, transition hygiene, focus states, hit areas, copy rules. Cheap to check, expensive to skip.

Reference tools, vetted 2026-08: `variate` skill for side-by-side variations of one file on localhost; lazyweb + refero MCPs for real product screens and flows; recent.design for fresh references, og images, and app screenshots; posts.design for launch/announcement post layouts; animos.app for a client-side launch teaser video (exports mp4, nothing uploaded). Skipped on aesthetic mismatch: gradient packs, glossy-3d and webgl generators, hosted embeds (CSP).

---

## Modes

| Invocation | What it does |
|---|---|
| `/design [surface]` | Full pipeline for one surface: shape → taste → build → polish |
| `/design lab [surface]` | Interactive exploration: render 2-3 distinct directions, react and refine, lock the winner — the visual, low-setup on-ramp |
| `/design assets [icons\|og\|favicon\|logo]` | Generate brand assets — all keyless; OG/icons/favicons by codegen, logos as SVG or a paste-ready image prompt |
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
| `/design` | Ask what to design — for a new surface, point them to `lab` |

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
3. If neither: run teach mode — **or `/design lab`** ([reference/design-lab.md](reference/design-lab.md)), which proposes directions with minimal setup and infers context from what the user reacts to (the low-friction on-ramp for new projects and users). Either way, do NOT silently infer context from code — code shows what was built, not who it's for.

**Once the product's vertical is known** (fintech, dev tool, healthcare, e-commerce, AI product, B2B SaaS, consumer/social…), consult [reference/industry-context.md](reference/industry-context.md) for its constraints, anti-patterns, mood, and the tensions to decide deliberately — then fetch live execution references via the lazyweb/refero MCPs. It's vertical-aware fuel: what the category demands and why, without prescribing a look.

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
[Voice, tone, 3-word personality, emotional goals - these steer type, color, motion. Wording follows the voice skill's product copy law: labels are plain nouns, no metaphor.]

### Aesthetic Direction
[Visual tone, references, anti-references, theme decision and why]

### Design Principles
[3-5 principles that should guide all design decisions]
```

Ask if they also want this appended to `.github/copilot-instructions.md`.

---

## Lab Mode (`/design lab`)

The visual, low-setup on-ramp — render 2-3 distinct directions, react, refine, lock the winner into DESIGN.md. Built for cold-start (no `.impeccable.md` needed; context comes from what the user reacts to). Routes to the right comparison surface by platform + decision scale: static gallery (broad direction) / live playground (small tweak) / Playwright loop (full build or audit) / Xcode previews (native Apple).

→ *Full protocol — router, the 5 schools, the four anchors, the self-contained `design-lab.html`, the 5-dimension ship rubric: [reference/design-lab.md](reference/design-lab.md)*

---

## Assets Mode (`/design assets`)

Generate brand assets **codegen-first** — deterministic where the asset is structural, and **keyless throughout**. OG images (satori), icon sets (Iconify assembly), and favicons (pwa-asset-generator) are free. Logos are too: **SVG authored by the running model** (wordmark/geometric), or — for illustrative marks — a **ready-to-paste image-gen prompt** for whatever image tool the user already has (ChatGPT/Gemini/Midjourney/Recraft). API keys are an opt-in automation, never required. Runnable scripts live in `scripts/assets/`.

→ *Per-asset tooling, the free/gated split, and the scripts: [reference/asset-gen.md](reference/asset-gen.md)*

---

## Phase 1: Shape (UX Planning)

Do NOT write code during this phase. Understand deeply first so implementation is precise.

### The Design Read

Before the interview, extract what the brief already says: surface kind (form / list / dashboard / settings / onboarding / landing / detail), audience (which picks the aesthetic, not your taste), vibe words the user used, reference URLs or screenshots, existing brand assets, quiet constraints (accessibility-first, regulated industry, kids' product — these OVERRIDE aesthetic preference), and platform signals (`.swift` files vs `package.json`). Then declare it in one line before anything else:

> *"Reading this as: \<surface kind> for \<audience>, with a \<vibe> language, on \<platform>."*

If the read genuinely diverges (Linear-clean vs Awwwards-experimental), ask exactly ONE question. If you can confidently infer, declare and proceed — never open with a multi-question dump.

→ *UX laws that should inform the brief — Hick's, Fitts's, Jakob's, Miller's, Peak-End, Von Restorff: [reference/ux-laws.md](reference/ux-laws.md). UX copy — labels, errors, empty states, microcopy: [reference/ux-writing.md](reference/ux-writing.md)*

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

- **DESIGN_VARIANCE** (1 = perfect symmetry → 10 = artsy chaos)
- **MOTION_INTENSITY** (1 = static → 10 = cinematic physics)
- **VISUAL_DENSITY** (1 = art gallery airy → 10 = cockpit packed)

Infer the values from the Design Read, state them explicitly with a one-sentence justification, then adapt only when the user asks. Fallback when no row fits: 8 / 6 / 4.

| Signal | VARIANCE | MOTION | DENSITY |
|---|---|---|---|
| Apple settings/form/utility screen | 4-5 | 3-4 | 4-6 |
| Apple consumer flagship (onboarding, hero detail) | 6-7 | 5-7 | 3-4 |
| Productivity app (lists, sidebars, dashboards) | 4-6 | 3-4 | 5-7 |
| Public-sector / regulated / accessibility-critical | 3-4 | 2-3 | 4-5 |
| Marketing landing (SaaS) | 7 | 6 | 4 |
| Marketing landing (agency / creative) | 9 | 8 | 3 |
| Editorial / blog | 6 | 4 | 3 |
| Redesign — preserve | match existing | +1 | match |
| Redesign — overhaul | +2 | +2 | match |

**Apple platforms cap MOTION at 7** unless the user explicitly asks for cinematic motion — iOS/macOS users come with system motion expectations, and overshooting feels foreign.

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

Step 1. Write 3 concrete brand voice words — not "modern" or "elegant" (dead categories). Examples: "warm mechanical opinionated", "fast dense unimpressed", "handmade slightly weird". These pick the font, never the copy: a "slightly weird" brand still labels a chart "heart rate", not "the heart's rest".

Step 2. **List the 3 fonts you'd normally reach for, then reject all three.** The
reflex pick is the problem, not any particular family. Fraunces, Space Grotesk, Inter,
DM Sans and their cohort are the usual suspects specifically because they *are* the
reflex: if a font is what you'd have chosen in the first two seconds, it is what every
other model chose too, and the interface will read as generated. The full
observed-monoculture list is in reference/critique.md - treat it as evidence of the
pattern, not as the boundary of it. A font that isn't on the list is not thereby a
good choice.

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

full canonical list: reference/critique.md

### Layout

→ *Deep material on grids, container queries, optical adjustments: [reference/spatial-design.md](reference/spatial-design.md). Adapting across breakpoints, print, and email: [reference/responsive-design.md](reference/responsive-design.md)*

**Always apply these without consulting the reference:**
- CSS Grid over flexbox math. Never `calc()` percentage hacks (`w-[calc(33%-1rem)]`).
- Self-adjusting grid: `grid-template-columns: repeat(auto-fit, minmax(280px, 1fr))`
- Contain layouts: `max-w-[1400px] mx-auto` or `max-w-7xl`.
- Full-height sections: ALWAYS `min-h-[100dvh]`. NEVER `h-screen` (iOS Safari layout jump).
- **Centered hero.** It is the default because it is the easiest thing to build, not
  because it is right - above VARIANCE 4 it will read as unconsidered. Move the
  composition off-axis (split, left-aligned with a right asset, asymmetric whitespace)
  unless centering is doing specific work: a single-action landing page, a
  confirmation screen, an actual symmetry brief.
- **Three equal columns of cards.** Same problem: it is what the grid does when nobody
  decided anything. Zig-zag, asymmetric weighting, or horizontal scroll all say
  something; three equal boxes say the content was poured in.
- `gap` over margins for sibling spacing. Eliminates margin collapse.
- Vary spacing for hierarchy — heading with extra space above reads as more important.
- Container queries for components, viewport queries for page layout.
- 4pt spacing scale with semantic names: `--space-xs: 4px`, `--space-sm: 8px`, `--space-md: 16px`, `--space-lg: 24px`, `--space-xl: 48px`.

### Architecture (React / Next.js)

→ *Per-stack design-implementation: [reference/stacks/web.md](reference/stacks/web.md) (Tailwind v4, shadcn, Next App Router) and [reference/stacks/swiftui.md](reference/stacks/swiftui.md) (iOS 26 Liquid Glass). Dashboards & charts: [reference/data-viz.md](reference/data-viz.md).*

- Verify `package.json` before importing any third-party library. Output install command if missing.
- Default to Server Components (RSC). Global state works ONLY in Client Components.
- Interactivity isolation: if motion is active, interactive components MUST be isolated leaf `'use client'` components. Server Components render static layouts only.
- Tailwind CSS for 90% of styling. Check Tailwind version — v3 and v4 syntax differ.
  - v4: use `@tailwindcss/postcss` or Vite plugin. Do NOT use `tailwindcss` plugin in postcss.config.js.
- Icons: `@phosphor-icons/react` or `@radix-ui/react-icons`. Standardize strokeWidth globally (1.5 or 2.0 — pick one).
- **No emojis anywhere — code, markup, text content, or alt text. Replace with icons or SVG.**

---

## Phase 4: Build (Production Code)

→ *Build + visual-iteration workflow (load references, build, inspect in a browser, iterate): [reference/craft.md](reference/craft.md)*

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

**Headline tells to eliminate:**
- Neon/outer glows → inner borders or subtle tinted shadows
- Any font from the reflex list → banned
- 3-column equal card grids → zig-zag, asymmetric grid, or horizontal scroll
- Generic names / startup slop names ("John Doe", "Acme", "Nexus") → creative, contextual names
- AI copy clichés ("Elevate", "Seamless", "Unleash", "Next-Gen") → concrete verbs
- Figurative labels and headings ("the body ledger", "ink to ember", "person of record") → the plain noun ("your body", "heart rate", "people"). Blurbs that tell the reader how to read a section → delete; the data shows it. Full law + kill list: voice skill, enforced by hooks/copy_guard.py

full canonical list: reference/critique.md

### Interactive States (Always Generate All Five)

- **Loading:** Skeletal loaders matching exact layout dimensions. No circular spinners.
- **Empty:** Composed empty states that teach the interface. Not just "nothing here."
- **Error:** Clear, inline error reporting.
- **Partial:** Some data loaded, some failed — the state everyone forgets. Show what arrived, flag what didn't.
- **Press feedback:** `transform: scale(0.98)` or `translateY(-1px)` on active for any pressable element.

### Creative Arsenal

Pull from these instead of defaulting to generic patterns. **The patterns aren't slop — thoughtless, uniform application is.** A spotlight card, magnetic button, or bento grid is fine *once, with intent*; the tell is the same effect on every element, or the AI-average stack (bento + spotlight + aurora + meteors). One deliberate signature beats ten reflexive effects. Drop-in tasteful primitives: Sonner (toasts), Vaul (drawers), shared-layout `layoutId` tabs; ReactBits / Magic UI as engine-agnostic grab-bags.

**Navigation:** Mac OS Dock magnification, magnetic buttons (cursor pull), Dynamic Island pill, contextual radial menus, floating speed dial, mega menu reveal

**Layout:** Bento grid (asymmetric tiles like Apple Control Center), masonry, chroma grid (animated gradient borders), split-screen scroll (halves slide opposite directions), curtain reveal

**Cards:** Parallax tilt card (3D mouse tracking), spotlight border card (cursor-tracking illumination), holographic foil card (rainbow hover), morphing modal (button expands into dialog)

**Scroll:** Sticky scroll stack (cards stack on top), horizontal scroll hijack (vertical → horizontal pan), zoom parallax, scroll progress path (SVG draws itself)

**Typography:** Kinetic marquee (reverses on scroll), text mask reveal (hero text as video window), text scramble (Matrix-style decode on load), circular text path

**Micro-interactions:** Directional hover-aware button (fill enters from cursor entry side), ripple click effect, animated SVG line drawing, mesh gradient background, particle explosion button

**3D / Canvas (when warranted):** ThreeJS/WebGL for canvas backgrounds. GSAP ScrollTrigger for complex scrolltelling. NEVER mix GSAP/ThreeJS with Framer Motion in the same component tree. Use GSAP/ThreeJS exclusively for isolated full-page scroll or canvas backgrounds, wrapped in strict `useEffect` cleanup.

---

## Phase 5: Polish (Micro-Interactions)

→ *Deep material on timing, easing, and reduced motion: [reference/motion-design.md](reference/motion-design.md) and [reference/interaction-design.md](reference/interaction-design.md). Accessible component contracts (roles/states/keyboard): [reference/accessible-patterns.md](reference/accessible-patterns.md)*

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

Built-in CSS easings lack punch, so use the custom curves. **The actual curve and
duration values live in reference/motion-design.md** - read it before writing any
transition. They are not restated here: this block used to carry a different
`--ease-out` than that file, and a third value showed up in the minimal aesthetic, so
nothing in the kit agreed on what "ease out" meant.

**Never use ease-in for UI animations.** It delays initial movement — exactly when the user is watching most closely. A dropdown at `ease-in` 300ms *feels* slower than `ease-out` at the same 300ms.

**3. Duration**

Under 300ms for anything the user is waiting on. Durations by element: same file. The
judgment worth keeping here is the one above the numbers — how often the user sees a
thing decides whether it should animate at all, and a frequently-repeated animation is
a tax paid on every interaction.

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

## Pipeline Gates (Full Pipeline)

1. Context confirmed → proceed to Shape
2. Brief approved by user → proceed to Taste Rules
3. Taste rules committed → proceed to Build
4. Build complete → proceed to Polish
5. Polish applied → done

**Do NOT implement before the brief is approved.** Commit after each implementation step — never batch screens into one commit.

If the user says "skip planning, just build it": warn once that the result will be shallower. Offer a 5-minute shape pass as a compromise. If they insist, go directly to Phase 4.

---


---

## References

The pipeline above is the spine. Everything below loads on demand - read the one the
mode needs, not all of them.

| Mode / need | File |
|---|---|
| `/design high-end`, `brutalist`, `minimal` | reference/aesthetics.md |
| `/design onboard`, `/design extract` | reference/onboarding.md |
| `/design arrange`, `critique`, `polish`, `redesign` | reference/refine-modes.md |
| `/design generate-design-md` | reference/design-md-template.md |
| `/design lab` | reference/design-lab.md |
| `/design assets` | reference/asset-gen.md |
| Any transition, duration, easing, stagger | reference/motion-design.md |
| Severity levels, AI-slop tells, the font monoculture list | reference/critique.md |
| The vertical's constraints and mood | reference/industry-context.md |
| Justifying or killing a direction from named priors | reference/design-priors.md |
| Typography, color, spatial, responsive, interaction, UX writing, data viz, a11y | reference/*.md by name |
| SwiftUI or web stack specifics | reference/stacks/ |

These files own their numbers. When something here and a reference disagree, the
reference wins and the copy here is the bug.
