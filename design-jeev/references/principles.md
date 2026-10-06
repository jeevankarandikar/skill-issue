# How good design teams think

Load this at the start of Explore, and whenever a decision is not settled by the project's `DESIGN.md`. It distills what Apple, Google, Meta, OpenAI, Anthropic, Superhuman, Linear, Stripe, Vercel and Airbnb have published about how they design. Every line is a paraphrase. The sources are at the end; open one before quoting it, since these pages change.

A project's canon and `DESIGN.md` still decide the specifics. This file is the judgment underneath them.

## What they agree on

Each of these is stated by at least four of the teams. Treat them as settled, and ask the question beside each before calling work done.

1. The content or the task comes first and the controls serve it. Could a person say what this screen is for in one glance?
2. Hierarchy comes from layout, grouping and space. If the borders, boxes and color were removed, would the order of importance survive?
3. One system holds across every surface. Does this screen use the same parts, words and behavior as the last one?
4. The surface is simple and the depth is reachable. What can move behind one more step without hiding anything a person needs now?
5. Speed is part of how quality feels. Does every action answer at once, and does a slow one show progress?
6. Motion explains a change, and it stops for people who ask it to. What would be lost if this animation were removed?
7. Access has numbers and is checked against them: contrast, target size, text scaling, keyboard reach.
8. Quality is a habit with a slot in the week. Who looks at the finished product as a customer would, and when?

## Where they disagree, and how to choose

The disagreements are where a designer earns their place. Pick a side on purpose and write it in `DESIGN.md`.

| Question | One answer | The other answer | Choose by |
| --- | --- | --- | --- |
| How much personality | Apple and OpenAI ask a product to look native to its host, with brand kept to a few places such as the icon, the accent and the primary button. | Material 3 Expressive reports measured gains from bold shape, color and size contrast. Anthropic's frontend-design skill asks for a committed point of view over safe defaults. | Whose space it is. Inside another platform, or used all day as a tool, hold back. For a product people choose among rivals, or a first impression, commit, and spend the boldness in one place. |
| How much motion | Apple keeps feedback brief and adds none to controls used constantly. Superhuman and Linear cut animation for speed. | Material treats springs and shape changes as a main lever. Stripe allows polish under half a second. | How often the person sees it. The hundredth viewing of an animation is a delay. Save expressive motion for rare moments. |
| Keyboard or touch | Superhuman, Linear and Vercel make every action reachable from the keyboard, with a command palette and visible shortcut hints. | Apple's iPhone guidance keeps few controls on screen, within reach of a thumb. | The device and the hours spent. A work tool on a desk gets full keyboard reach. A phone app gets large targets and fewer choices. |
| Flexible or opinionated | Linear builds for specific workflows and Superhuman onboards along one path. | Meta's business tools balance simplicity against access to advanced functions for experts. | How alike the users are. One kind of user gets one strong path. A wide range gets a simple default with the depth one step away. |
| Capitalization | Vercel prefers title case for headings, and Apple uses it for menus and buttons. | Anthropic's skill uses sentence case throughout. | The canon the project follows. Decide once and apply it everywhere. |

## Numbers worth knowing

Use the project's canon first. These are the published figures to fall back on.

- Targets: Apple gives 44 by 44 points on iPhone and 28 by 28 on Mac as defaults. Vercel gives 24 pixels on desktop and 44 on mobile.
- Text: Apple's default body size is 17 points on iPhone and 13 on Mac, and text should survive enlargement to 200%.
- Contrast: 4.5 to 1 for body text and 3 to 1 for large or bold text.
- Response: Superhuman holds every interaction under 100 milliseconds. Vercel wants a change saved in under 500.
- Loading: Vercel shows an indicator only after about 150 to 300 milliseconds, then keeps it up long enough to be seen, so it never flickers.
- Shape: a nested corner follows its parent. Apple states it as inner radius equals outer radius minus the padding between them.
- Layout: Apple designs for compact and regular size classes. Material moves from one pane to more as the window widens.
- Cards inside a chat host: OpenAI allows at most two primary actions on an inline card and no scrolling nested inside it.

## The practices behind the quality

- Linear gives each engineer a weekly slot to fix small flaws, 30 to 60 minutes each. The stated benefit is that the team learns to see them.
- Stripe is reported to have teams use the product end to end as a customer would.
- Superhuman asks users how they would feel if the product vanished and steers by the share who say very disappointed, with 40% as the bar.
- Anthropic's skill has the designer write a short plan for color, type and layout, critique it against the brief, and replace anything that reads as a default before building.
- Google tested Material 3 Expressive across 46 studies before recommending it.

For an agent this means the rendered product gets looked at every time, small flaws get fixed in the same pass they are seen, and a plan gets criticized before it is built.

## Working as a designer

- Have a point of view and be able to say it in one sentence before drawing anything. A principle is useful when another good team would have chosen differently.
- Start from the subject. The product's own content, its users' words and its real data suggest a better direction than a style picked from a gallery.
- Question the frame as well as the screen. Jason Yuan's Mercury OS asked whether apps and folders are the right model at all, then delivered the answer through interactions people already knew. A new idea needs familiar handles.
- Give the work one hero moment and keep the rest quiet.
- Sweat the small touches. Superhuman turns a typed arrow into a real arrow glyph, and people notice hundreds of such details as one feeling.
- Draw from outside software. Type design, print, film, architecture and music packaging all teach hierarchy and tone, and they keep a product from looking like every other product.
- Design for the person with the least attention to spare. Mercury names focus as a principle because clutter costs more for people sensitive to stimulation.
- Know the defaults well enough to notice when one is being accepted without a reason. Cream with terracotta, near-black with an acid accent, and rows of identical rounded cards are fine when chosen and weak when inherited.

## Sources

- Apple: developer.apple.com/design/human-interface-guidelines (Accessibility, Layout, Motion, Designing for iOS, Designing for macOS) and the WWDC25 session "Get to know the new design system".
- Google: design.google/library/expressive-material-design-google-research and m3.material.io.
- Meta: Margaret Gould Stewart's Facebook Business design principles, collected at principles.design.
- OpenAI: developers.openai.com/apps-sdk/concepts/design-guidelines.
- Anthropic: the frontend-design skill at github.com/anthropics/skills.
- Superhuman: blog.superhuman.com/superhuman-is-built-for-speed and the First Round Review pieces on its product-market-fit survey and onboarding.
- Linear: linear.app/method and linear.app/now/quality-wednesdays.
- Stripe: stripe.com/blog/connect-front-end-experience and the Sessions 2024 talk on craft and beauty.
- Vercel: vercel.com/design/guidelines.
- Airbnb: the four principles of its 2016 design language system.
- Jason Yuan: mercuryos.com.
