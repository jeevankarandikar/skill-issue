# Critique

Load this in Review when the request is a judgment of the whole experience, and before a redesign. [review.md](review.md) checks whether an interface is correct. This file asks whether it is good.

Two rules hold for every finding. It carries the fix: the replacement text, the corrected value, the component to use. And it states the reason, such as "the sheet scales up from nothing, so it pops in place of growing from its trigger". A finding without a reason teaches nothing.

## Before looking

- Name two people who use this surface and the task each came to do.
- List the ways a person arrives: a direct link, a menu, search, a notification.
- Note the constraints: devices, access targets, the canon in `DESIGN.md`.

## Score the ten heuristics

Jakob Nielsen's heuristics, each scored 0 to 4, where 0 is absent, 2 is partial and 4 is excellent. Most shipped interfaces land between 20 and 32 out of 40. A total under 15 means the structure needs rethinking, and polish will not help.

| Heuristic | Ask |
| --- | --- |
| Visibility of system status | Does the person always know what is happening? |
| Match with the real world | Are the words and concepts the person's own? |
| Control and freedom | Can they undo, cancel and go back? |
| Consistency and standards | Does the same action do the same thing everywhere, and follow the platform? |
| Error prevention | Do constraints and defaults stop mistakes before they happen? |
| Recognition over recall | Are the options visible, with nothing to memorize between screens? |
| Flexibility and efficiency | Are there shortcuts and faster paths for people who use it daily? |
| Minimal design | Does every element serve the task? |
| Recovery from errors | Do errors say what went wrong and what to do, in plain words? |
| Help | Is help easy to find and tied to the task at hand? |

## Walk it as two people

The expert, who uses it all day, is failed by:

- actions with no keyboard route
- no way to reduce density or animation
- a confirmation on something done fifty times a day
- lists with no bulk actions

The newcomer, on a first visit, is failed by:

- errors written in technical terms
- an empty screen with no guidance
- a main action that does not stand out
- everything shown at once
- a destructive action with no undo

## Signs of too much to think about

- More than about seven items in a menu or a bar
- Several main actions competing on one screen
- Information a person needs that appears only on hover
- A long form with no grouping
- Every element at the same visual weight

## Signs of a generic look

Each of these is fine when chosen for a reason. Several together mean the design was inherited from defaults, and that is the first verdict to give.

Layout:

- equal card grids of three columns as the feature section
- a centered hero on every page
- the same padding everywhere
- a row of equal-weight statistics
- a bento grid by default

Content:

- round invented numbers and placeholder names
- stock marketing verbs in headings
- a middle dot between metadata items
- a bare dash filling an empty field
- headlines built on a number rhyme
- emoji as decoration

Effects:

- gradient text and gradient buttons
- a glow that follows the cursor on every card
- particle fields, meteors and aurora washes
- the same fade-in on every element

Marketing pages:

- version labels and build numbers as decoration
- numbered section eyebrows
- a scroll cue
- a status dot on every list item
- rules above and below every row
- a fake product screenshot built from boxes
- rotated vertical text

## Report

Give the verdict on the generic look first, then the heuristic total with the two lowest scores named. Follow with findings as P0, P1 or P2, each with a location, the reason and the fix, in the format [review.md](review.md) sets.

## Sources

Jakob Nielsen's ten usability heuristics (nngroup.com). The protocol is adapted from the critique reference of the impeccable skill by Paul Bakaus (github.com/pbakaus/impeccable, Apache 2.0).
