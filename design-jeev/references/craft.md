# Type, color, space and depth

Load this when setting or changing tokens, and when a screen looks flat, crowded or generic. Each rule is stated as an outcome. [stacks.md](stacks.md) gives the mechanism for each stack, and the project's canon and `DESIGN.md` override any number here.

## Type

- Use few sizes with clear steps between them. Five roles cover most products: caption, secondary, body, subheading and headline. Pick one ratio between steps, such as 1.25 or 1.333, and keep it.
- Sizes that sit close together, such as 14, 15 and 16, make the hierarchy muddy. Remove the middle ones.
- Body line height is the unit for vertical spacing. With 16 point body text at 1.5, space in multiples of 24.
- Keep a line of running text between 45 and 75 characters.
- Tighten letter spacing on large display type, more as the size grows. Leave body text at its default. Open the spacing on all-caps labels.
- Light text on a dark background reads thinner, so give it slightly more line height and consider one weight step down from the light theme.
- Balance the lines of a heading, and keep a single word from sitting alone on the last line of a paragraph.
- Numbers that change or line up in columns use tabular figures: timers, counters, prices, table cells.
- One family in several weights is usually enough. Add a second face only for real contrast, and make the two differ on more than one axis, such as serif with sans or condensed with wide. Two similar faces compete.
- Choose the face from the brief. Write down a few concrete words for the product's voice, picture a physical object that has that voice, and look for type that belongs on it. Reject the first choice that only looks designed, and the one used on the last project.
- The platform's system font is a strong choice for a tool, where speed and a native look matter more than personality.
- Product UI uses a fixed type scale. Fluid sizing that follows the window belongs to headlines on marketing and editorial pages.
- Text sizes follow the person's text-size setting, the layout survives 200% enlargement, and zoom is never disabled.
- Name type tokens by role, such as body or heading, and never by value.

## Color

- Build palettes in a perceptually uniform space such as OKLCH, where equal steps in lightness look equal. Hold hue and chroma steady and vary lightness, reducing chroma near white and near black.
- The hue is a brand decision. Blue and warm orange are the defaults a model reaches for, so choose either only with a reason.
- A palette has four parts: one accent with a few shades, a neutral scale of about ten steps, the semantic colors for success, warning, error and information, and two or more surface levels. Skip secondary and tertiary accents until something needs them.
- Every step in a scale has a job, such as page background, hover, border, solid fill or body text. Remove steps nothing uses.
- Tint the neutrals very slightly toward the accent hue so surfaces and brand color sit together. Avoid pure grey and pure black across large areas.
- By visual weight, about 60% of a screen is neutral surface, 30% is text and borders, and 10% is accent. An accent works because it is rare.
- Components use semantic tokens named for a role. Primitive values sit one layer below. A dark theme redefines the semantic layer only.
- Add a new token when a new role appears. Borrowing another role's token because the color happens to match breaks the day that role changes.
- A dark theme is designed separately from the light one. Depth comes from lighter surfaces in place of shadows, accents lose a little saturation, and the base is a dark grey.
- Measure contrast against the background the element is drawn on. Placeholder text needs the same 4.5 to 1 as body text.
- Grey text on a colored background looks washed out. Use a darker shade of that background.
- Color is never the only signal. About 8% of men cannot tell red from green, so pair a status color with an icon, a label or a shape.
- Heavy use of transparency usually means the palette is missing a color. Define the overlay color, and keep alpha for focus rings and pressed states.

## Space and hierarchy

- Use a spacing scale on a base of 4: 4, 8, 12, 16, 24, 32, 48, 64, 96. Name the tokens by size role.
- The gap between groups is at least twice the gap inside a group.
- Equal spacing everywhere flattens a screen. Variation in spacing is what shows structure.
- Squint at the screen, or blur a screenshot. The most important element, the second, and the groups should still be visible.
- Build hierarchy from two or more of size, weight, color, position and space at once. A size ratio under 2 to 1 between levels is weak.
- When the main element does not stand out, quiet what competes with it before making it louder.
- Group with spacing and alignment first. Use a card when the content is a distinct object a person acts on or compares, and never put a card inside a card.
- A component adapts to the width of its container, so the same card works in a sidebar and in the main column.
- Align by eye where geometry looks wrong. A play icon sits slightly right of center, and large text needs a small pull to line up with the edge above it.
- A control may look small, but its hit area still meets the canon's minimum, and extended hit areas never overlap.

## Depth

- Set one named stacking order for the product, from dropdown through sticky header, modal and toast to tooltip. Arbitrary layer numbers are a bug waiting to happen.
- Every shadow comes from one light, above and slightly in front, so the vertical offset is larger and the horizontal offset stays near zero.
- As an element rises, its shadow moves further, blurs more and gets fainter.
- Several soft shadows layered at doubling offsets look more real than one heavy shadow.
- Tint shadows toward the surface hue. A shadow that is noticed as a shadow is too strong.
- Separate an element from its surroundings with one device: a shadow, a border or a change of background. Stacking them makes every panel shout.
- A nested corner follows its parent, with inner radius equal to outer radius minus the padding between them.
- An image on a similar background gets a hairline outline at low opacity so its edge holds.

## Sources

Adapted from the reference files of the impeccable skill by Paul Bakaus (github.com/pbakaus/impeccable, Apache 2.0) and from Rauno Freiberg's interface guidelines at interfaces.dev, restated as outcomes for any stack.
