# Every surface a person sees

The small details hold on everything a person would ever see, at every size they use it. A design or UX change is not done until it holds on the whole inventory below. Use this in polish and audit passes, and before calling any interface work finished.

## 1. Inventory the surfaces first

List every surface the change touches, then check each one. Most products have all of these; rarely opened ones are where flaws hide.

- Main pages and views, in every state: empty, loading, error, full, very long.
- Secondary windows, panes, inspectors and embedded views.
- Every menu: the menu bar and each menu in it, context and right-click menus, command palette, pickers such as a model or account menu, the Dock or app-icon menu.
- Popovers, sheets, alerts, toasts, banners and notifications.
- Words outside the page: error text, tooltips, permission prompt texts the operating system shows for the app, notification text.
- First run: download page, installer or disk image window, onboarding, the first empty screen.
- Settings and setup.
- Anything the product generates for people to read, such as notes or pages it writes.
- The website: every page, its help, download, privacy, release and feedback pages, and its demos.
- The About window and the app icon.

## 2. At every size

Check the smallest window the app allows, a narrow side window, full screen, and a phone width (the narrowest phone the product supports, 360 wide when the project has not said). If a phone app exists or is planned, the rules carry over, with the platform's own conventions (tab bars, sheets, swipe actions, Dynamic Type) replacing desktop ones where they differ.

## 3. The details rules

- **Nothing cut off with room to spare.** Text truncates only when its element already spans the width it can use. A label squeezed by a missing image, a fixed width, or a container that refuses to shrink is a defect.
- **One separator style for one reason.** Space divides sections; one hairline divides groups inside them. Never two lines in a row, never a border and a hairline on one edge, never a line right under a heading that already has space above its group.
- **One order.** Title, then at most one line of context, then content. Each fact once per screen: a heading that carries the date means the rows do not repeat it.
- **One date and one number format per context.** Dates as people say them ("Saturday, September 26" as a heading, "Sep 26" in a row, the year only when it differs); machine formats such as ISO dates only in URLs, tags and data views. Grouped numbers, tabular figures in columns.
- **Spacing on the scale.** Only the project's spacing tokens, no one-off values.
- **One voice.** Every label, menu item, empty state, error and tooltip follows the project's writing rules, with a lint in the build where the project has one.

## 4. Check it with code where it can be measured

A rule that a script can check should fail the build, not wait for a reviewer. Useful gates, each run against the real rendered interface with the stack's own test tools:

- clipped text with free space in its row;
- type sizes, weights and faces outside the scale;
- words that break the writing rules;
- motion outside the motion tokens;
- colors outside the tokens;
- doubled or stray separators, off-scale spacing, the same fact twice on one screen, mixed date formats.

For each gate, prove it with a mutation: put the defect back and watch the gate go red.

## 5. Verify with a bounded list

Give the verifier the inventory and a fixed list of screens and sizes to look at, and have it look at every screenshot. An open-ended "find anything" verifier never lets work pass; findings outside the list become the next task.

The project's `DESIGN.md` holds its own surface table and gates.
