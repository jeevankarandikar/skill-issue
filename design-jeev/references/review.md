# Interface review

A pass or fail review for any interface in any stack. Run it on the rendered product, at the smallest and largest sizes it supports, in light and dark, with the keyboard alone and then with a pointer or touch. Mark each line pass, fail or not applicable, and give a location for every fail. A line nobody tested is a fail. Where a line collides with a numbered open item in the project's `DESIGN.md`, report the item by number.

Platform numbers such as target sizes and type sizes come from the project's canon. [stacks.md](stacks.md) names the stack's mechanism for tokens, text scaling, appearance, reduced motion and access.

Start from the list of surfaces, sizes and states the builder recorded under Checked in `DESIGN.md`, and look at each one again. A value in the interface that is not in the `DESIGN.md` tokens is a finding. The review changes no code and no design decision.

## Hierarchy and layout
- [ ] Each screen has one clear purpose, and the most important content comes first in reading order.
- [ ] Related items are grouped by space or by one level of container, with no boxes inside boxes.
- [ ] Controls sit next to what they change.
- [ ] At the smallest and largest sizes nothing clips, overlaps or scrolls sideways, and no feature disappears.

## Actions
- [ ] Each view has at most one prominent action.
- [ ] A destructive action is never the default and asks before it cannot be undone.
- [ ] Every action gives feedback within a moment, and a slow one shows progress.

## Tokens
- [ ] Every color, type size, weight, space, radius and duration comes from a token.
- [ ] The accent marks the primary action, selection and status, and nothing else.

## Text
- [ ] Text scales with the person's setting up to the largest size without clipping.
- [ ] Text truncates only when its element already uses the width available.
- [ ] Labels, errors and empty states follow the project's writing rules and one capitalization style.
- [ ] One date format and one number format per context.

## Color and appearance
- [ ] Body text meets 4.5:1 contrast, large text and interface marks 3:1, in both appearances.
- [ ] Meaning never rests on color alone.
- [ ] Light and dark both look intended, with no pure-white flash or lost borders.

## Input and access
- [ ] Every control is reachable and usable by keyboard or the platform's equivalent, in reading order.
- [ ] Focus is always visible and never cropped.
- [ ] A screen reader announces each control's name, role and state.
- [ ] Touch and pointer targets meet the canon's minimum size.

## Motion
- [ ] Each animation has a job: showing a change of state, a spatial relation, or feedback.
- [ ] Reduced motion is honored, and nothing loops without a way to stop it.
- [ ] An animation can be interrupted, and leaves nothing behind when its view closes.

## States
- [ ] Empty states say why they are empty and offer the next step.
- [ ] Loading waits briefly before showing a spinner, and layout does not jump when content arrives.
- [ ] Errors say what happened and what to do, next to where it happened.
- [ ] Missing data is stated in words, never shown as a blank or a zero.

## Permissions and privacy
- [ ] A permission is asked for at the moment it is needed, with the reason in plain words.
- [ ] Nothing private appears in screenshots, logs or shared links by default.

## Assets
- [ ] Every font, icon and image has a license the project has accepted, and nothing banned in `DESIGN.md` is in the build.

## Reporting

List findings most severe first, each with a location and the change to make.

- P0 blocks shipping: a task that cannot be finished, a control that keyboard or screen-reader users cannot reach, a privacy leak, or a banned asset in the build.
- P1 gets fixed before the next release: a departure people will notice, such as a missing focus ring, two competing primary actions, or text under the contrast floor.
- P2 is polish in spacing, alignment, copy and motion.
- Open items come after P2, by number, each with the surfaces it touches.
