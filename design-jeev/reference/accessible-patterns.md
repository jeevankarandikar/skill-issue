# Accessible Patterns

Don't reinvent accessible behavior — borrow the *behavior* (focus management, roles, keyboard contracts) from the canonical sources and bring your own taste for the *visuals*. Two references, used together:

- **Inclusive Components** (Heydon Pickering, inclusive-components.design) — the design *intent* and markup rationale: the "why."
- **WCAG ARIA Authoring Practices Guide (APG)** (w3.org/WAI/ARIA/apg) — the normative roles, states, and keyboard contract: the "what + how."

## Check the contract before you build the component

| Component | Where to look | The non-negotiable contract |
|---|---|---|
| **Dialog / Modal** | APG Dialog (Modal) | Focus trap while open; `Esc` closes; focus returns to the trigger; `aria-modal`, labelled by its title. |
| **Menu / Menu Button** | APG Menu Button; IC Menus | Arrow-key nav; `Esc` closes; roving tabindex; `aria-expanded` on the trigger. |
| **Tabs** | APG Tabs; IC Tabbed Interfaces | Arrow keys move between tabs; `role=tab`/`tabpanel`; `aria-selected`; one tab stop into the set. |
| **Combobox / Autocomplete** | APG Combobox | `aria-expanded`, `aria-activedescendant`; arrow keys into the listbox; `Esc` collapses. |
| **Disclosure / Accordion** | APG Disclosure, Accordion; IC Collapsible Sections | A real `<button>` with `aria-expanded`; no div-with-onClick. |
| **Tooltip / Toggletip** | APG Tooltip; IC Tooltips & Toggletips | Tooltip = supplementary, hoverable + focusable, `Esc` dismisses; an *interactive* toggletip needs a button, not a tooltip. |
| **Switch / Toggle Button** | APG Switch; IC Toggle Buttons | `role=switch` + `aria-checked` (on/off) vs toggle button + `aria-pressed` — pick the right one. |
| **Carousel / Slider** | APG Carousel; IC Content Slider | Pause control for auto-advance; keyboard access to each slide; never auto-rotate without a stop. |
| **Data Table** | APG Table/Grid; IC Data Tables | Real `<table>` semantics; `scope` on headers; `grid` role only when cells are interactive. |
| **Notifications** | IC Notifications; APG Alert | `role=status` (polite) vs `role=alert` (assertive) by urgency; don't steal focus for non-critical updates. |

Cross-cutting (reinforced across this skill): touch targets ≥44×44px · visible `:focus-visible` rings · color is never the only signal · honor `prefers-reduced-motion`.

---

**Avoid**: building interactive widgets from `<div onClick>` (no role, no keyboard) · `outline: none` without a `:focus-visible` replacement · hand-rolling a dialog/menu/combobox when the APG contract (or a headless lib like Radix that implements it) already exists. Sources: inclusive-components.design (Heydon Pickering), w3.org/WAI/ARIA/apg.
