# Design Lab (`/design lab`)

The visual, low-setup on-ramp to the design pipeline. Instead of planning in text and converging on one direction, the lab **renders several distinct directions you can see, react to, and refine** — then locks the winner into DESIGN.md. Built for cold-start: a new project/user with no `.impeccable.md` gets going by reacting to options, not by filling out a context form first.

Principle: **render-then-react.** Don't describe a design and ask the user to imagine it — show it live and let them point at what's right.

## Router — pick the comparison surface

Detect, then route:

1. **Platform = native Apple (SwiftUI / iOS)?** → **Xcode surface**: generate 2-3 `#Preview` variants in a scratch file, build to the simulator, compare side by side. Use Liquid Glass per [stacks/swiftui.md](stacks/swiftui.md). (A web HTML gallery is meaningless here — don't produce one.)
2. **Web — what's the decision scale?** **Default to the static gallery** below — it's the right answer for "I want to design X," and it never makes a newcomer parse design jargon. Only branch to another surface when the user clearly signals a small tweak or a full build/audit:
   - **Broad direction** (new surface, "which way do we go?") → **static multi-variant gallery**: one self-contained `design-lab.html`, all directions rendered side by side. The default, the most "chilled out."
   - **Small / local tweak** ("test these few options") → **live playground**: the HTML ships dial sliders (variance / motion / density) + font & palette toggles that re-render in-browser; the user locks a config that you read back into DESIGN.md.
   - **Whole site/app, or an audit** → **Playwright screenshot loop**: build one direction, screenshot it via the Playwright MCP, the user reacts, iterate. Real renders, one at a time.

## The directions (the core loop)

**Offer 2-3 distinct directions, never one "final answer."** A direction is a *deliberate point of view*, not a color swap. Pull each from a different school so they're genuinely distinct:

| School | Feel |
|---|---|
| **Information** | data-first, dense, chart-forward (Bloomberg) |
| **Editorial** | magazine layout, expressive type, generous whitespace |
| **Expressive** | bold color, asymmetric, motion-forward |
| **Functional** | dense utility, mono accents, minimal decoration |
| **Warm Minimal** | soft neutrals, rounded shapes, subtle texture |

Each direction declares four **anchors** + a context check:
- **Palette** — 3-5 roles in OKLCH, per [color-and-contrast.md](color-and-contrast.md). No reflex hues (no defaulting to blue/purple).
- **Type pairing** — display + body, run the font procedure in [typography.md](typography.md). No reflex fonts (Inter, Space Grotesk, …).
- **Density** — comfortable / compact / spacious (maps to VISUAL_DENSITY).
- **One signature detail** at 120% effort — the thing you'd remember. Pull *one* from the Creative Arsenal per direction; never stack the AI-average effects.
- **Vertical fit** — cite the project's [industry-context.md](industry-context.md) vertical: does this direction respect its constraints and anti-patterns? Cold-start appropriateness comes from here, not from guessing.

**Distinctness rule:** each direction pulls a *non-overlapping* subset of the Creative Arsenal. If two directions could share the same hero, they're one direction with a palette swap — not two.

## The artifact (`design-lab.html`)

Self-contained, opens anywhere (Tailwind Play CDN, no build step). Structure:
- A short **flow / states strip** at the top (the UX layer): the key screens and states this surface needs — default, empty, loading, error — sketched, so directions aren't judged on looks alone.
- Each direction as a **labeled, fully-rendered section**: real components (not swatches), the four anchors printed beside it, and a visible **5-dimension scorecard** (below).
- A lightweight feedback affordance per direction so the user can say *"2, but denser and lose the serif."*

Then **regenerate on feedback** — the file is the shared canvas; the loop runs through chat. Don't rebuild from scratch each round; evolve the chosen direction.

## Ship rubric (score every direction)

Score each direction 1-10 on five dimensions. **Ship threshold = all ≥7, none below 5.** Below 7 → name the fix, don't just flag it.

1. **Philosophy alignment** — a coherent POV, not a trend collage. Recognizable with the brand name removed.
2. **Visual hierarchy** — instant "where do I look first / second / third."
3. **Craft quality** — grid / scale / token discipline; no orphaned words; consistent radii. (Where AI UI fails most.)
4. **Functionality** — primary action obvious, 44pt targets, all states handled, predictable nav.
5. **Originality** — no slop tells, ≥1 signature detail, not confusable with a template.

Run the **AI Slop Test + effect/library tells (SKILL.md Phase 4) as a pre-filter** before scoring — a direction stacking bento + spotlight + aurora is dead on arrival.

## Lock the winner → DESIGN.md

When the user picks (or a hybrid — "2's layout with 3's type"), write the chosen direction into `DESIGN.md` (Phase 3 schema) as a token spec: semantic color / type / spacing tokens + brand-specific Do's & Don'ts + the confidence of each decision (✅ chosen / ⚠️ inferred / ❓ open). Then continue the normal pipeline (Build → Polish) from there. The lab replaces the *planning* front-end; it doesn't replace the build.

---

**Avoid**: one "final" direction instead of options · directions that differ only by palette · stacking the AI-average effects in any direction · scoring on looks before the flow strip exists · shipping a direction below the rubric threshold · in the Xcode surface, Liquid Glass on the content layer (see [stacks/swiftui.md](stacks/swiftui.md)).
