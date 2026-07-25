# The nine dials

Read the one being asked for.

Every dial runs the same shape: assess what is there now, plan the smallest change that moves the dimension, apply it, then look at it again. Durations, easing curves, and stagger intervals come from design's reference/motion-design.md - do not restate its numbers here.

## `/tune bolder`

Increase visual impact in designs that are too safe, generic, or underwhelming.

**WARNING — AI SLOP TRAP**: AI defaults to the same tired tricks: cyan/purple gradients, glassmorphism, neon accents, gradient text on metrics. These are the OPPOSITE of bold — they're generic. Bold means distinctive, not "more effects."

### Assess
- **Generic choices**: System fonts, basic colors, standard layouts
- **Timid scale**: Everything medium-sized, no drama or hierarchy
- **Low contrast**: Everything has similar visual weight
- **Predictable**: Standard patterns with no surprises

### Plan
- **Focal point**: ONE hero moment — make it amazing
- **Personality direction**: Choose a lane (maximalist chaos? elegant drama? dark moody?)
- **Risk budget**: How experimental can we be given brand/context?
- **Hierarchy amplification**: Big things BIGGER, small things smaller

### Amplify

**Typography**: Extreme scale (3x-5x differences, not 1.5x). Weight contrast: pair 900 with 200, not 600 with 400. Variable fonts, display fonts for headlines, condensed widths, monospace as intentional accent (not lazy "dev tool" default).

**Color**: Increase saturation (not neon). Avoid purple-blue gradient slop. One bold color owns 60%. Sharp accents. Tinted neutrals instead of pure gray. Rich multi-stop gradients that feel intentional.

**Spatial drama**: Important elements 3-5x larger than surroundings. Break the grid. Asymmetric layouts with tension. Generous space (100-200px gaps). Overlap elements intentionally for depth.

**Effects**: Large soft shadows — not generic drop shadows on rounded rectangles. Mesh patterns, noise textures, grain, halftone, duotone — **NOT glassmorphism** (overused AI slop). Thick borders, custom shapes — not rounded rectangles with a colored side-border.

**Motion**: Staggered entrances (50-100ms delays). Scroll-triggered sequences. Satisfying hover: scale + shadow. Ease-out-quart/quint/expo — never bounce or elastic.

**Composition**: Diagonal flows. Full-bleed elements. Unexpected proportions: 70/30, 80/20 splits. Golden ratio? Throw it out.

**NEVER**: Add effects randomly without purpose. Sacrifice readability. Make everything bold (then nothing is). Copy trendy aesthetics blindly (bold = distinctive, not derivative). Ignore accessibility.

### Verify
- Does this NOT look like AI-generated "bold"? If it does, start over.
- Still functional? Coherent? Memorable? Performant? Accessible (WCAG)?

---

## `/tune quieter`

Reduce visual intensity in designs that are too bold, aggressive, or overstimulating.

**"Quieter" means refined, not boring. Think luxury, not laziness.**

### Assess Intensity Sources
- **Color saturation**: Overly bright or saturated colors
- **Contrast extremes**: Too much high-contrast juxtaposition
- **Visual weight**: Too many bold, heavy elements competing
- **Animation excess**: Too much motion or overly dramatic effects
- **Complexity**: Too many visual elements, patterns, decorations

### Refine

**Color**: Reduce saturation to 70-85%. Sophisticated muted tones. 10% rule: neutrals do most work, color as accent. Tinted grays over pure gray — add warm or cool tint for sophistication. **Never gray on color**: gray text on a colored background looks washed out — use a darker shade of that background color or transparency instead.

**Visual weight**: Reduce font weights (900→600, 700→500). Hierarchy through subtlety: weight + size + space instead of color and boldness. More whitespace. Reduce border thickness/opacity or remove entirely.

**Simplification**: Remove gradients, shadows, patterns that don't serve purpose. Simplify shapes. Reduce layering. Clean up blur effects, glows, multiple shadows.

**Motion**: Shorter distances (10-20px instead of 40px). Remove decorative animations — keep functional motion only. Ease-out-quart for understated motion — **never bounce or elastic** (they cheapen). Remove animations with no clear purpose.

**Composition**: Smaller scale jumps between elements. Even out spacing. Align rogue elements back to grid.

**NEVER**: Make everything the same size/weight (hierarchy still matters). Remove all color (quiet ≠ grayscale). Eliminate all personality. Sacrifice usability for aesthetics. Make everything small and light (some anchors needed).

### Verify
- Still functional? Still distinctive (character, not generic)? Better reading? More refined and premium?

---

## `/tune colorize`

Strategically introduce color to designs that are too monochromatic or gray.

**More color ≠ better. Strategic color beats rainbow vomit every time. Every color earns its place.**

### Assess
Identify where color adds: semantic meaning, hierarchy, categorization, emotional tone, wayfinding, or delight. Gather existing brand colors first.

### Plan: 60-30-10 Rule
- **Dominant** (60%): Primary brand color or most-used accent
- **Secondary** (30%): Supporting color for variety
- **Accent** (10%): High contrast for key moments
- **Neutrals**: Gray/black/white for structure (with subtle tint — never pure)

Use OKLCH throughout: perceptually uniform, equal lightness steps *look* equal.

### Apply

**Semantic colors**:
- Success: emerald/forest/mint
- Error: rose/crimson/coral
- Warning: orange/amber
- Info: sky/ocean/indigo
- Neutral: gray/slate for inactive states

**Surfaces**: Replace pure gray (`#f5f5f5`) with warm neutral (`oklch(97% 0.01 60)`) or cool tint (`oklch(97% 0.01 250)`). Tint cards slightly for warmth. Subtle colored section backgrounds.

**Accent application**: Primary CTAs. Links (maintain accessibility). Icons. Section headers. Hover states. Focus rings matching brand.

**Data visualization**: Charts for category encoding, heatmaps for density, comparison color coding.

**Borders**: Colored left/top accents on cards. Underlines for active states. Colored focus rings.

**Accessibility**: 4.5:1 for text, 3:1 for UI components. Don't rely on color alone (use icons/labels too). Test red/green combinations for color blindness.

**NEVER**: Pure gray neutrals (add subtle tint). Gray text on colored backgrounds (use darker shade or transparency). Pure `#000`/`#fff` for large areas. Default to purple-blue gradients. More than 2-4 colors beyond neutrals. Color without semantic meaning.

### Verify
- Better hierarchy? Clearer meaning? More engaging? Still accessible? Not overwhelming?

---

## `/tune distill`

Strip designs to their essence. Remove obstacles between users and their goals.

**Simplicity is not about removing features — it's about removing obstacles.**

### Assess: Find the Essence
- What's the ONE primary user goal?
- What's necessary vs. nice-to-have?
- What's the 20% delivering 80% of value?
- Sources of complexity: competing elements, excessive variation, information overload, visual noise, feature creep

### Simplify

**Information architecture**: Remove secondary actions. Progressive disclosure: hide complexity behind accordions, modals, step-through flows. ONE primary action, few secondary. Remove redundancy — say it once.

**Visual**: 1-2 colors plus neutrals. One font family, 3-4 sizes, 2-3 weights. Eliminate borders/shadows/backgrounds that don't serve hierarchy. Remove unnecessary cards — cards aren't needed for basic layout; use spacing and alignment instead. Never nest cards inside cards. One spacing scale, no arbitrary gaps.

**Layout**: Linear flow where possible. Remove sidebars (move content inline or hide it). Consistent alignment. Generous whitespace. Full-width over complex multi-column.

**Interaction**: Fewer buttons, fewer options, clearer path. Smart defaults (only ask when necessary). ONE obvious CTA. Replace modal flows with inline editing where possible.

**Content**: Cut every sentence in half. Active voice. Remove jargon. No headers restating intros, no repeated explanations. Shorter paragraphs, bullets, clear headings.

**Code**: Remove dead CSS, unused components. Flatten component trees. Consolidate similar styles. Does this component need 12 variants, or can 3 cover 90% of cases?

**NEVER**: Remove necessary functionality (simplicity ≠ feature-less). Sacrifice accessibility. Make things so simple they're unclear. Oversimplify complex domains (match complexity to actual task complexity).

### Verify
- Faster task completion? Reduced cognitive load? Still feature-complete? Clearer hierarchy? Better performance?

---

## `/tune typeset`

Fix font choices, hierarchy, sizing, and readability so text feels intentional.

**Goal: clearer, more readable, more intentional. Good typography is invisible.**

### Assess
1. **Font choices**: Using invisible defaults (Inter, Roboto, Arial, Open Sans, system defaults)? Does font match brand personality? More than 2-3 families?
2. **Hierarchy**: Tell headings from body from captions at a glance? Sizes too close (14/15/16px = muddy)? Weight contrasts strong enough (Medium vs Regular is barely visible)?
3. **Scale**: Consistent ratio or arbitrary? Body ≥ 16px? Fixed `rem` for app UIs; `clamp()` for marketing heading display text.
4. **Readability**: Line lengths 45-75 characters? Line-height right for context? Sufficient contrast?
5. **Consistency**: Same elements styled same way? Weights used consistently across identical roles?

### Implement

**Font selection**: Fonts reflect brand personality. Pair with genuine contrast (serif + sans, geometric + humanist) — or single family in multiple weights. `font-display: swap` with metric-matched fallbacks to prevent layout shift.

**Type scale**: 5 sizes cover most needs: caption → secondary → body → subheading → heading. Consistent ratio (1.25, 1.333, or 1.5). Combine size + weight + color + space for strong hierarchy. App UIs: fixed `rem`. Marketing/content pages: `clamp(min, preferred, max)` for headings only.

**Readability**: `max-width: 65ch` on text containers. Headings: line-height 1.1-1.2. Body: line-height 1.5-1.7 (slightly looser for light-on-dark). Body text ≥ 16px / 1rem.

**Details**: `font-variant-numeric: tabular-nums` for data tables and numbers that should align. Letter-spacing: open for small caps/uppercase, default or tight for large display. Semantic token names (`--text-body` not `--font-16`). `font-kerning: normal`.

**Weights**: 3-4 max (Regular, Medium, Semibold, Bold). Clear role per weight — stick to it. Load only what's used.

**NEVER**: More than 2-3 font families. Arbitrary sizes — commit to a scale. Body below 16px. `px` for font sizes (use `rem` to respect user settings). Decorative/display fonts for body text. Never introduce fonts from the design skill's banned reflex list (design SKILL.md Phase 2); replace them on sight. Two geometric sans-serifs paired together.

### Verify
- Hierarchy instant at a glance? Body comfortable for long passages? Same-role elements identical throughout? Typography reflects brand? Fonts load without layout shift? WCAG contrast met? Zoomable to 200%?

---

## `/tune animate`

Add purposeful animations, micro-interactions, and motion that improve usability and create delight.

**Always respect `prefers-reduced-motion`. Non-animated alternatives are required.**

### Assess
- Missing feedback: actions without visual acknowledgment
- Jarring transitions: instant state changes that feel abrupt
- Unclear spatial/hierarchical relationships
- Joyless interactions — functional but lifeless

### Plan: Animation Layers
- **Hero moment**: ONE signature animation
- **Feedback layer**: Which interactions need acknowledgment?
- **Transition layer**: Which state changes need smoothing?
- **Delight layer**: Where can we surprise?

One well-orchestrated experience beats scattered animations everywhere.

### Implement

**Entrances**: Stagger reveals (30-80ms delays), fade + slide. Scroll-triggered via IntersectionObserver. Modal/drawer: smooth slide + fade + backdrop.

On any numeric conflict, design SKILL.md Phase 5 wins (design high-end's 80-120ms is an intentional mode exception).

**Micro-interactions**:
- Button hover: scale 1.02-1.05, color shift, shadow increase
- Button click: 0.95 → 1 scale, or ripple effect
- Input focus: border color transition, subtle glow
- Validation: shake on error (brief, x-direction), checkmark draw on success
- Toggle: smooth slide + color transition (200-300ms)

**State transitions**: Show/hide: fade + slide (200-300ms). Expand/collapse: height + icon rotation. Loading: skeleton fades, spinners, progress bars. Success/error: color transitions + icon animation.

**Navigation**: Route crossfade or shared element transitions. Tab switching: slide indicator + content fade. Scroll effects: parallax, sticky header state changes.

**Delight**: Empty state floating illustrations. Confetti for major completions. Contextual animations.

### Easing Curves

```css
--ease-out-quart: cubic-bezier(0.25, 1, 0.5, 1);   /* smooth, refined */
--ease-out-quint: cubic-bezier(0.22, 1, 0.36, 1);  /* snappier */
--ease-out-expo:  cubic-bezier(0.16, 1, 0.3, 1);   /* confident, decisive */
/* AVOID: bounce, elastic — feel dated, draw attention to the animation itself */
```

**Durations**: 100-150ms (instant feedback), 200-300ms (state changes), 300-500ms (layout changes), 500-800ms (entrance animations). Exit ≈ 75% of enter duration.

**Performance**: `transform` and `opacity` only (GPU-accelerated). Avoid animating width/height/top/left. `will-change` sparingly. 60fps on target devices.

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

**NEVER**: Bounce or elastic easing. Animate layout properties. >500ms for interaction feedback. Animate without purpose. Ignore `prefers-reduced-motion`. Animate everything. Block interaction during animations.

### Verify
- 60fps smooth? Easing feels natural? Not too fast or slow? Reduced motion works? Doesn't block? Adds value?

---

## `/tune delight`

Add moments of joy, personality, and unexpected polish.

**Delight enhances usability, never obscures it. If users notice the delight more than their goal, you've gone too far.**

### Assess: Natural Delight Moments
- Success states (completed actions, milestones)
- Empty states (first-time experiences, onboarding)
- Loading states (waiting periods)
- Hover states, clicks, drags
- Error moments (soften frustration)
- Easter egg opportunities for curious users

### Principles
- **Amplifies, never blocks**: Delight < 1 second. Never delay core functionality. Make it skippable or subtle.
- **Surprise and discovery**: Hide details for users to find. Don't announce every moment.
- **Appropriate to context**: Banking app ≠ gaming app. Match emotional moment (don't be playful during critical errors).
- **Compound over time**: Vary responses (not same animation every time). Reveal deeper layers with continued use.

### Techniques

**Micro-interactions**:
- Button hover: lifts 2px with ease-out-quart, active presses down 2px
- Loading: playful animations beyond spinners. Skeleton screens with subtle pulse.
- Success: checkmark draw animation, confetti for major achievements, gentle scale + fade

**Copy personality**:
- Error: explain what happened, suggest fix, **never blame the user**
- Empty states: "Your canvas awaits. Create something amazing." — not "No items"
- Loading messages: write product-specific copy ("Crunching your latest numbers...") — **NEVER** clichés like "Herding pixels", "Teaching robots to dance", "Consulting the magic 8-ball" — these are instantly recognizable AI-slop
- Match copy personality to brand (banks can be warm, just not wacky)

**Illustrations**: Custom (not stock icons) for empty/error/loading states. Animated on hover or entrance.

**Satisfying interactions**: Drag-and-drop lift (shadow + scale), snap on drop. Toggle spring physics. Progress bars that celebrate at 100%. Form inputs animate on focus.

**Easter eggs**: Konami code, keyboard shortcut unlocks, developer console messages ("Like what you see? We're hiring!"), hover reveals on logos, seasonal touches.

**Sound design**: Keep subtle. Mute option required. Respect system sound settings. Don't play on every interaction.

**NEVER**: Delay core functionality for delight. Force users through delightful moments. Use delight to hide poor UX. Make every interaction delightful (special moments must be special). Ignore accessibility. Use AI-slop loading copy.

### Verify
- Do users smile? Still pleasant after 100th time? Doesn't block? Performant? Appropriate context? Accessible?

---

## `/tune clarify`

Fix unclear UX copy, error messages, microcopy, labels, and instructions.

**Good UX writing is invisible. Users understand immediately without noticing the words.**

### Assess: Clarity Problems
- Jargon, ambiguity, passive voice, wordiness
- Assumptions (user knowledge they don't have)
- Missing context (don't know what to do or why)
- Tone mismatch (too formal, too casual, inappropriate for situation)

### Improve by Context

**Error messages**:
- Bad: "Error 403: Forbidden" → Good: "You don't have permission. Contact your admin for access."
- Bad: "Invalid input" → Good: "Email addresses need an @ symbol. Try: name@example.com"
- Explain what went wrong in plain language. Suggest how to fix it. Never blame the user. Include examples. Link to help/support.

**Form labels**: Specific not generic. Show format with placeholder or example. Explain why when not obvious. Instructions before the field. Clear required indicators.

**Button/CTA text**: Describe the specific action. Active voice: verb + noun. "Create account" > "Submit". "Save changes" > "OK". Match user's mental model.

**Help text/tooltips**: Add value beyond restating the label. Answer "what is this?" or "why do you need this?" Brief but complete.

**Empty states**: "No projects yet. Create your first project to get started." — never just "No items".

**Success messages**: Confirm what happened. Explain what happens next if relevant. Brief. Match emotional moment.

**Loading states**: Set expectations ("this usually takes 30-60 seconds"). Explain what's happening. Show progress. Offer cancel if appropriate.

**Confirmation dialogs**: State the specific action. Explain consequences. "Delete 'Project Alpha'? This can't be undone." — not "Are you sure?" Clear button labels: "Delete project" not "Yes".

**Navigation**: Specific labels. User language not internal jargon. Clear hierarchy with information scent.

### Six Principles
1. **Specific** — "Enter email" not "Enter value"
2. **Concise** — cut unnecessary words without sacrificing clarity
3. **Active** — "Save changes" not "Changes will be saved"
4. **Human** — "Oops, something went wrong" not "System error encountered"
5. **Helpful** — tell users what to do, not just what happened
6. **Consistent** — pick one term and use it everywhere

**NEVER**: Jargon without explanation. Blame users. Vague errors without fix suggestion. Passive voice unnecessarily. Humor for errors (be empathetic). Vary terminology for variety. Repeat information. Placeholders as the only labels.

### Verify
- Understood without context? Action clear? As short as possible? Consistent terminology? Appropriate tone?

---

## `/tune overdrive`

Push past conventional limits with technically ambitious implementations.

**MANDATORY — PROPOSE FIRST**: Think through 2-3 different directions. Present them with trade-offs. Get user confirmation before writing any code. Skipping this risks building something that gets thrown away.

**MANDATORY — ITERATE**: Technically ambitious effects almost never work on the first try. Use browser automation to preview, visually verify, and iterate. Expect multiple rounds. The gap between "technically works" and "extraordinary" is closed through visual iteration, not code alone.

### What "Extraordinary" Means by Context

**Visual/marketing surfaces** (landing pages, portfolios): Scroll-driven reveals, shader backgrounds, cinematic transitions, generative art responding to cursor.

**Functional UI** (tables, forms, dialogs): A dialog morphing from its trigger via View Transitions. 100k-row table at 60fps via virtual scrolling. Streaming form validation. Drag-and-drop with spring physics.

**Performance-critical UI**: Search filtering 50k items without a flicker. The interface never hesitates.

**Data-heavy interfaces**: GPU-accelerated rendering via Canvas/WebGL. Animated transitions between data states. Force-directed graphs settling naturally.

The common thread: something goes beyond what users expect from a web interface. Technique serves experience, not the other way around.

### The Toolkit

**Cinematic transitions**: View Transitions API (same-document: all browsers; cross-document: no Firefox). `@starting-style` for CSS-only entry from `display: none`. Spring physics via motion/GSAP/custom solver.

**Scroll-driven**: `animation-timeline: scroll()` — CSS-only parallax, progress bars, reveals. (Chrome/Edge/Safari; Firefox: flag only — always provide static fallback.)

**Beyond CSS**: WebGL (Three.js/OGL/regl), WebGPU (Chrome/Edge, fallback to WebGL2), Canvas 2D + OffscreenCanvas for off-thread rendering, SVG filter chains for organic distortion.

**Data alive**: Virtual scrolling — render only visible rows (TanStack Virtual for complex cases). GPU-accelerated charts (deck.gl). D3 animated transitions between states.

**Complex properties**: `@property` (all browsers) — animate gradients, colors, complex values. Web Animations API — programmatic, composable, cancellable.

**Off-thread**: Web Workers (move computation off main thread). OffscreenCanvas (render in Worker). WASM (near-native for heavy computation).

### Discipline
- **Progressive enhancement is non-negotiable**: Fallback must still be good.
- **Target 60fps**: Below 50, simplify.
- **`prefers-reduced-motion`**: Always respected. Provide a beautiful static alternative.
- Lazy-initialize heavy resources (WebGL, WASM) only when near viewport. Pause off-screen rendering.
- Test on real mid-range devices, not just your development machine.
- The last 20% — easing curve, timing offset, secondary motion — is what makes it extraordinary.

**NEVER**: Ignore `prefers-reduced-motion`. Ship effects that cause jank. Bleeding-edge APIs without fallback. Sound without explicit user opt-in. Technical ambition masking weak design fundamentals. Multiple competing extraordinary moments (focus creates impact).

### Verify
- **Wow test**: Do they react?
- **Removal test**: Take it away — does the experience feel diminished?
- **Device test**: Phone, tablet, Chromebook — still smooth?
- **Accessibility test**: Reduced motion — still beautiful?
- **Context test**: Makes sense for this brand and audience?
