# Lenses, laws and the disclosure ladder

Load this when shaping a screen or defending a decision in a review. Each entry forces a concrete choice. Name the lens or law that justifies a decision so the reason can be argued with, and apply it. A name dropped as decoration is worth nothing.

## Designers to reason from

| Lens | What it asks |
| --- | --- |
| Edward Tufte | Does every mark carry information? Would several small charts read better than one busy one? |
| Richard Saul Wurman | Which of the five orders fits this content: location, alphabet, time, category or hierarchy? |
| Dieter Rams | What can be removed so the content is all that is left? |
| Massimo Vignelli | Is the system tight enough: few typefaces, a strict grid, a fixed palette? |
| Christopher Alexander | Do the recurring patterns compose into one whole? |
| Don Norman | Does each control show what it does and where it leads? When a person errs, what in the design caused it? |
| Jakob Nielsen | Does it behave the way the other products this person uses behave? |
| Bret Victor | Does the person see the consequence while acting, before committing? |
| Bill Buxton | Has the interaction been sketched over time, and not only the screen? |
| Susan Kare | Do the icons read at small sizes and belong to one vocabulary? |

The lenses conflict on purpose. Tufte wants density where Rams wants restraint, and Nielsen wants convention where a distinctive product wants difference. Decide which one governs this project, record it in `DESIGN.md`, and do not average them.

## Laws that force a decision

| Law | The decision |
| --- | --- |
| Hick | Fewer choices at once. Cap primary actions and move advanced options behind a step. |
| Fitts | The primary action is large and near where the eye and hand already are. |
| Jakob | Keep interaction conventions. Be distinct in look and familiar in behavior. |
| Miller | Chunk long lists and menus into about seven groups or fewer. |
| Tesler | Complexity lands somewhere. Put it on the system through good defaults. |
| Doherty | Respond in under 400 milliseconds, with optimistic updates and placeholders to stay there. |
| Peak-end | Spend the signature detail at the emotional peak, and design the end state on purpose. |
| Aesthetic-usability | Polish earns trust and can hide friction, so test usability separately. |
| Von Restorff | One element per view looks different, and it is the primary action. |
| Serial position | The most important items go first and last. |
| Goal-gradient | Show progress through a multi-step flow. |
| Proximity | Group with spacing before reaching for a border. |
| Common region | Use a container only when spacing alone is ambiguous. |
| Similarity | Controls with the same function look the same. |
| Postel | Accept messy input and format it. Give back precise, predictable states. |
| Information scent | A label predicts its destination. "See pricing" beats "Learn more". |

Jakob's law governs behavior and gives no excuse for a generic look. The laws trade off against each other, so optimizing one alone makes a worse screen.

## The disclosure ladder

Every screen has a primary task, secondary tasks and edge tasks. Give each one a level.

| Level | Where it lives | Use for |
| --- | --- | --- |
| 0 | Always visible | The primary action, the current state, the key data |
| 1 | One scroll away | Supporting content |
| 2 | Inline expand | Secondary details, advanced settings |
| 3 | Drill-down | Sub-flows that need room |
| 4 | Contextual: hover, right-click, long-press | Power-user actions |
| 5 | Modal | Destructive confirmations, focused single-task flows |
| 6 | Shortcut, command palette, menu | Expert operations |

- The primary task is always at level 0.
- A modal takes focus and hides context, so prefer inline editing or a side panel.
- Hover is never the only path to an action. Touch has no hover, and the keyboard needs a route too.
- Work in Dan Saffer's order: reduce, group, hide, decorate. Decoration added to cover clutter means going back to the first step.

The laws are collected at lawsofux.com by Jon Yablonski.
