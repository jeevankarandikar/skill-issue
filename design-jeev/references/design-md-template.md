# DESIGN.md template

Copy this to `DESIGN.md` at the repository root and fill it from the code. Leave a heading in place with "not decided" under it; a missing decision is useful to see. Keep it short enough to read at the start of every design task.

```markdown
# Design

## Product
What it is, who uses it, on which devices, and the feeling it should leave.

## Stack
The UI framework, the styling system, the component source, the icon set, and where each lives in the repository.

## Canon
The guidelines this project follows (Apple's Human Interface Guidelines, Material, or its own system), and the places where it departs from them on purpose.

## Tokens
Where the tokens are defined, and the scales themselves.
- Color roles, light and dark
- Type: faces, sizes, weights
- Spacing scale
- Radius
- Motion: durations and easings, by purpose

## Assets and licenses
Fonts, icons and kits in use, each with its license. Assets that are banned, with the reason.

## Surfaces
Every place a person sees the product: views, menus, popovers, alerts, notifications, permission texts, first run, settings, the website. Mark the ones with known problems.

## Writing
The copy rules for labels, errors and empty states, and the capitalization style.

## Decisions
Dated, one line each: what was chosen, what was rejected, why.

## Open items
Numbered. Things that wait on a person, so a reviewer reports them by number and does not change them.

## How to check
The command that renders or previews the interface, the sizes to check, and the tests that gate it.

## Checked
Written by whoever last shipped a change: the date, the surfaces, sizes and states looked at, and where the screenshots or test results are. A reviewer starts here.
```
