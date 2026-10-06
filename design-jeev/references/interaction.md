# Interaction, motion and first run

Load this when building or changing anything a person operates: controls, forms, overlays, loading, animation, onboarding. Each rule is an outcome. [stacks.md](stacks.md) gives the mechanism, and the project's canon and `DESIGN.md` override any number here.

## States

Every interactive element has eight states, and each one is designed.

| State | When |
| --- | --- |
| Default | At rest |
| Hover | A pointer is over it. Touch has no hover. |
| Focus | The keyboard or an assistive tool is on it |
| Pressed | During the press |
| Disabled | Unavailable |
| Loading | Working |
| Error | The input or the action failed |
| Success | The action finished |

- Hover and focus are separate designs. A keyboard user never sees hover.
- Hover styling applies only where a pointer can hover. On touch it sticks after a tap and looks selected.
- A focus ring is visible, has 3 to 1 contrast against what surrounds it, sits outside the element, and looks the same on every control. Never remove one without a replacement.
- A disabled control cannot explain itself in a tooltip to keyboard and touch users. Put the reason in visible text beside it, or keep it focusable and say why it is unavailable.
- Use the platform's real control for the job. A hand-built one has to match its role, its keyboard behavior and its announcements.

## Forms

- Every field has a visible label. Placeholder text disappears on input and cannot stand in for one.
- Give each field its correct type and keyboard, and never block paste.
- Validate when the person leaves the field, or on submit. Validating every keystroke scolds people mid-word, with password strength as the exception.
- Keep the submit button enabled until the request starts. On failure, put each error below its field, tie it to the field for assistive tools, and move focus to the first invalid one.

## Waiting

- For low-stakes actions such as a like or a rename, show the result at once and roll back on failure. Payments and destructive actions wait for confirmation from the system.
- A placeholder in the shape of the content feels faster than a spinner and keeps the layout from jumping.
- Start showing something immediately and fill in progressively. Waiting with nothing to look at feels longer than the same wait with visible progress.
- Under about 80 milliseconds a response feels instant.
- Name what is happening, such as "Saving your draft", and for a long wait give the expected time or real progress.

## Overlays

- A modal traps focus while open, closes on Escape, returns focus to what opened it, and makes the page behind it inert.
- Menus, popovers and tooltips are drawn in the top layer, above every clipping container. A dropdown cut off by its scrolling parent is the most common overlay bug.
- An overlay flips or shifts to stay inside the window.
- A tooltip adds to what is visible and holds nothing a person needs. Anything interactive belongs in a popover opened by a button.

## Destructive actions

- Prefer undo to a confirmation. Remove the item, offer undo for a few seconds, then delete for real. People click through confirmations without reading.
- Confirm only what cannot be undone or is costly. Name the action and its consequence, and label the buttons with the outcomes, such as "Delete project" and "Keep project".
- Show the count when an action covers several items.

## Keyboard and gestures

- A group such as tabs, a menu or a radio set is one tab stop, and arrow keys move within it.
- The first focusable element on a web page skips to the main content.
- A gesture is invisible, so every gesture has a visible alternative, and the first use hints that it exists.
- Input method is separate from screen size. A laptop may have touch and a tablet may have a keyboard, so detect the pointer and hover ability directly.
- Content stays clear of notches, rounded corners and system bars.

## Component contracts

Borrow the behavior from the W3C ARIA Authoring Practices Guide and Heydon Pickering's Inclusive Components, and bring the visual design yourself. Native platforms supply the same contracts through their standard controls.

| Component | What must hold |
| --- | --- |
| Dialog | Focus is trapped, Escape closes, focus returns to the trigger, and the title labels it |
| Menu | Arrow keys move, Escape closes, the trigger reports open or closed |
| Tabs | Arrow keys move between tabs, one tab stop for the set, the selected tab is announced |
| Combobox | Arrow keys enter the list, the active option is announced, Escape collapses |
| Disclosure | A real button that reports expanded or collapsed |
| Switch or toggle button | A switch reports on or off. A toggle button reports pressed. Choose the right one. |
| Carousel | Auto-advance has a pause control, and every slide is reachable by keyboard |
| Data table | Real table semantics with header cells. A grid only when the cells are interactive. |
| Notification | Routine updates are announced politely, urgent errors assertively, and neither steals focus |

## Motion

The project's motion tokens come first. These are starting values.

| Duration | Use |
| --- | --- |
| 100 to 150 ms | Direct feedback: a press, a toggle, a color change |
| 200 to 300 ms | A change of state: a menu, a tooltip |
| 300 to 500 ms | A change of layout: an accordion, a sheet, a drawer |
| 500 to 800 ms | A rare entrance: first load, a hero reveal |

- An exit takes about three quarters of the time of its entrance.
- Duration follows distance. A tooltip moving a few points sits at the floor, and a panel crossing half the window earns the ceiling.
- Entering elements decelerate, leaving elements accelerate, and a toggle eases both ways. Bounce and overshoot draw the eye to the animation, so keep them for a product whose canon asks for expressive motion.
- Animate position, scale and opacity, which are cheap to draw. Animating size or layout properties drops frames.
- Motion that responds to a gesture can be interrupted halfway. A sequence that plays once may run to its end.
- Stagger a group entrance by 50 to 100 milliseconds per item, and cap the total near half a second.
- A pressed button scales to between 0.95 and 0.98. Icons that swap cross-fade.
- Do not animate what happens constantly, such as hover in a long list.
- Turn transitions off while the theme switches between light and dark.
- With reduced motion on, keep progress and focus feedback and remove movement through space.

## First run and empty states

- Get the person to a first real result quickly. Teach the part of the product that delivers most of the value and leave the rest for when they meet it.
- Onboarding happens inside the real product, with working examples. A separate tutorial mode teaches a product that does not exist.
- Introduce at most a few concepts, show progress through the steps, and let anyone skip.
- Ask for the minimum, use sensible defaults, and say why each question is asked.
- Never show the same hint twice, and never block the whole interface for a tour.
- An empty state says what will appear there, why it is worth having, and offers one action to start.
- Empty states differ by cause: first use, cleared by the person, no results, no permission, and error. Each gets its own words and its own next step.

## Sources

Adapted from the reference files of the impeccable skill by Paul Bakaus (github.com/pbakaus/impeccable, Apache 2.0), Rauno Freiberg's interface guidelines at interfaces.dev, the ARIA Authoring Practices Guide at w3.org/WAI/ARIA/apg and inclusive-components.design.
