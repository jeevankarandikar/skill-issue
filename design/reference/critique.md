# UX Critique Protocol

Full protocol for `/design critique`. Pair with automated scan (`npx impeccable --json` — see Step 3 for the fallback if it fails).

**Two rules that separate a critique from a complaint:**

1. **Never ship a bare critique — produce the improved version.** Every finding carries a concrete fix: the exact replacement copy, the corrected spacing value, the specific component. Not "this is weak." If you can't say what better looks like, the critique isn't finished.
2. **Name *why* it works or fails.** Not "this feels off" — "the modal animates from `scale(0)`, so it pops instead of growing from its trigger." Articulating the reason is what compounds into taste; vague reactions don't.

Apply the **deference** lens throughout (Apple HIG): the interface exists to serve the content, not to compete with it. Decoration that draws attention to itself is a finding.

---

## Nielsen's 10 Heuristics (Score 0-4 each, total /40)

| # | Heuristic | What to look for |
|---|-----------|-----------------|
| 1 | **Visibility of system status** | Does the user always know what's happening? Loading states, progress indicators, feedback on actions |
| 2 | **Match between system and real world** | Does language match users' vocabulary? Are concepts familiar? No jargon |
| 3 | **User control and freedom** | Can users undo? Cancel? Easily escape mistakes? Back button works? |
| 4 | **Consistency and standards** | Same action = same result everywhere? Platform conventions followed? |
| 5 | **Error prevention** | Does the design prevent errors before they happen? Confirmations, constraints, good defaults |
| 6 | **Recognition over recall** | Are options visible? Doesn't require memorizing state from one part to use another |
| 7 | **Flexibility and efficiency** | Shortcuts for experts? Accelerators? Keyboard navigation? Power user paths? |
| 8 | **Aesthetic and minimalist design** | No irrelevant info? Every element serves a purpose? Signal-to-noise ratio |
| 9 | **Help users recognize, diagnose, and recover from errors** | Error messages in plain language? Explain the problem? Suggest solution? |
| 10 | **Help and documentation** | If help is needed, is it easy to find and task-focused? |

**Score each 0-4:** 0 = absent/broken, 1 = major gaps, 2 = partial, 3 = mostly met, 4 = excellent.

Typical real interfaces: 20-32/40. Below 15 = fundamental restructuring needed.

---

## Process

### Step 1: Preparation

Before reviewing:
- Identify 2-3 primary user personas and their key tasks
- List the entry paths to this surface (direct link, nav click, search, etc.)
- Note any constraints (accessibility targets, browser support, device types)

### Step 2: LLM Assessment

Work through each heuristic systematically. For each violation found, note:
- **Location**: component, page, or flow step
- **Severity**: P0 (blocking) / P1 (major) / P2 (minor) / P3 (polish)
- **User impact**: what goes wrong for the user
- **Recommendation**: specific fix

### Step 3: Automated Scan

Run `npx impeccable --json` in the terminal (fresh subagent if context is long); if the command fails, skip the automated scan and note it in the report:

```bash
npx impeccable --json > critique-scan.json
```

Review the JSON output for:
- Contrast failures
- Missing ARIA labels
- Keyboard trap risks
- Touch target sizes
- Missing alt text
- Form label associations

### Step 4: Combined Report

Merge LLM findings and automated findings. Remove duplicates. Assign final severity.

### Step 5: Output Format

Start with the anti-patterns verdict, then executive summary, then detailed findings.

---

## Anti-Patterns Verdict (Always First)

This is the canonical AI-slop tells list — SKILL.md's Phase 2/3/4 sections keep only their headline tells and point here for the rest. Add new tells here first, then trim SKILL.md's summaries if needed.

Does this look AI-generated? Be brutally honest. List specific tells:

**Visual & CSS:**
- Gradient text (background-clip: text)
- Left/right border stripes on cards (border-left: 3-5px solid color)
- Purple/blue neon glow on buttons
- Pure black (#000000) or pure white (#fff) — always tint
- Warm/cool gray fluctuation within one project
- Custom mouse cursors
- Glassmorphism as decoration
- Hero metrics with colored backgrounds (green/red stat cards)
- Flat color-field / diagonal-gradient hero instead of real content/photography
- One headline word recolored in the accent ("...are they **now?**")

**Typography:**
- Inter + DM Sans + Outfit font stack (or any font from the reflex list)
- Screaming H1s — control hierarchy with weight and color instead
- Serif fonts on dashboards

**Layout:**
- Equal 3-column card grids
- Centered hero (for variance > 4 interfaces)
- Same padding everywhere — vary for hierarchy
- Even N-up stat bar (4 equal-weight metrics in a row)
- Top filter-chip bar where a faceted left rail is the convention

**Content:**
- Generic SVG avatars
- Round fake numbers (99.99%, 50K users)
- Generic placeholder / startup slop names ("John Doe", "Acme", "Nexus")
- AI copy clichés in headings ("Elevate", "Seamless", "Unleash")
- Interpunct `·`/`•` as a metadata separator (`Title · Company · Location`, eyebrows)
- Bare `—` filling empty card fields (unfinished-scaffold look)
- Cute number-rhyme headlines ("Three tabs. Three jobs.")

**Effects/library (2026):**
- Bento grid as the default feature section
- Spotlight/cursor-glow on every card
- Meteors / shooting stars / aurora-gradient washes
- Animated gradient text, rainbow/gradient buttons
- GitHub-globe, magnetic-everything, particle fields
- Uniform fade-in on every element (no orchestrated stagger)

**Structural:**
- Emojis anywhere in UI
- `h-screen` instead of `min-h-[100dvh]`

Verdict: **AI tells detected / Clean / Mostly clean**

---

## Persona Red Flags

Check against these user profiles:

**Alex (power user / expert)**
- Cannot access keyboard shortcuts
- No way to reduce animation / density
- Forced through confirmation dialogs for frequent operations
- No bulk actions on lists
- Pagination with no "items per page" control

**Jordan (first-timer / novice)**
- Error messages use technical jargon
- No empty state with guidance
- Primary action not visually obvious
- No progressive disclosure — everything shown at once
- No undo for destructive actions

---

## Cognitive Load Checklist

High cognitive load symptoms:
- [ ] More than 7 items in any navigation or menu (Miller's Law)
- [ ] Multiple competing CTAs — user doesn't know where to click
- [ ] Critical info only visible on hover
- [ ] Form with more than 7 fields without sections/grouping
- [ ] No visual hierarchy — everything same weight
- [ ] Terminology inconsistency across same flow
- [ ] Required context must be remembered from a previous screen
- [ ] No confirmation/success state after completing an action

---

## Full Output Template

```
## Anti-Patterns Verdict
[Pass/Fail + specific tells listed]

## Executive Summary
Score: [X]/40 — [Rating]
Issues: P0: [n] / P1: [n] / P2: [n] / P3: [n]
Top issues: [3-5 bullet points]
Next steps: [recommended commands]

## Heuristic Scores
| # | Heuristic | Score | Key Finding |
|---|-----------|-------|-------------|
| 1 | Visibility of system status | [0-4] | [finding] |
...
| Total | | [X]/40 | |

## Detailed Findings

### P0 — Blocking
[Issue location] · [Category] · [Impact] · [Recommendation] · [Command]

### P1 — Major
...

### P2 — Minor
...

### P3 — Polish
...

## Systemic Patterns
[Recurring issues indicating a system-level gap]

## Positive Findings
[What's working well — good practices to replicate]

## Recommended Actions (Priority Order)
1. [Command] — [why first]
...
```
