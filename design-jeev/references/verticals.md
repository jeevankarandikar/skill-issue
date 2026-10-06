# What each kind of product demands

Load this in Explore, and when choosing an approach for a product in one of these fields. It holds constraints, the mistakes that read as wrong in each field, and the calls a designer has to make. It holds no palettes and no font names on purpose, since a stored look turns every product in a field into the same product. Match the project to the closest entry, satisfy its constraints, decide each tension on purpose, and record the decisions in `DESIGN.md`.

For current examples, look at shipping products in the field. Where a current trend breaks a constraint below, the constraint wins.

## Money: banking, payments, lending, investing

- Constraints: numbers are exact and never rounded for looks. Fees and totals appear before the person commits. Contrast meets AA at least, since people are often stressed here.
- Reads wrong: purple and pink gradients, playful illustration on money screens, fees shown late, animated balances.
- Decide: how dense the transaction tables are on a desktop and how hard they collapse on a phone. Where to remove friction (checking a balance) and where to add a step (sending money). How far to depart from the conservative look of the field.
- Trust: compliance marks and security text near forms and transfers.
- Screens that decide it: the transaction list, the transfer confirmation, the empty state, the failed payment.
- Motion confirms and guides, and nothing more.

## Developer tools: APIs, SDKs, infrastructure

- Constraints: developers read the documentation before the marketing. Show real code and real terminal output. A dark theme is expected, with a light one offered.
- Reads wrong: claims in place of a code sample, stock photos, mascots where credibility matters, prose describing what code does when the code could be shown.
- Decide: how much of the first screen is proof (a sample, a live console) and how much is pitch. Density can run high.
- Trust: code that runs, install counts, open-source activity.
- Screens that decide it: install and quickstart, the reference, the first successful call, the error state.
- Motion is minimal and feedback is instant.

## Business software: admin, workflow, team tools

- Constraints: the daily user, the buyer and the administrator are different people. Density follows the role. The marketing site says one thing.
- Reads wrong: a consumer tone, equal feature grids of three columns, the word "platform" with no outcome attached.
- Decide: density for daily users against a gentle first run. Visible pricing against contacting sales.
- Trust: customer logos early, compliance marks, case studies with real figures, testimonials with name, title and company.
- Screens that decide it: setup, the core workflow, team and permissions, the empty new workspace.
- Motion is reduced on actions people repeat all day.

## Health: patients, clinics, telehealth

- Constraints: AA contrast is required and AAA is the target for critical information. Plain language with no jargon. The product stays calm when the person is anxious, and privacy is stated up front.
- Reads wrong: alarm colors outside real alerts, clinical jargon, a playful tone on serious information, red and green as the only status signal.
- Decide: clinicians need density and patients need simplicity, so split by audience. Stay calm without hiding bad news.
- Trust: privacy assurance, provider credentials, clear words about how data is handled.
- Screens that decide it: booking, results and records, medication and care instructions, the first visit.
- Motion is gentle, and reduced motion is honored strictly.

## Shops: storefront, cart, checkout

- Constraints, from Baymard Institute research: several real images per product, guest checkout offered prominently, a short and clearly grouped checkout form, a cart that is always reachable, and no carousel that rotates by itself.
- Reads wrong: costs that first appear at the last step, placeholder product images, an account required before purchase, fake urgency timers.
- Decide: the storefront may be distinctive, and the checkout should be conventional. Rich imagery has to stay fast.
- Trust: reviews with counts, clear returns and shipping, payment marks at checkout.
- Screens that decide it: the listing, the product page, the cart, the checkout, the empty cart.
- Motion is subtle while browsing and absent at checkout.

## AI products: assistants, copilots, agents

- Constraints: the default look of the field (a purple gradient, sparkle icons, the same sans everywhere) is the most overused look in software, so a distinct identity is required here. Set expectations for latency, stream output, and show sources and uncertainty honestly.
- Reads wrong: presenting a guess as certain, hiding that a response is generated, an endless chat box where a structured interface would serve the task better.
- Decide: delight without overpromising. Chat or structured UI, chosen per task.
- Trust: citations, cues for uncertainty, honest labeling of generated content, easy undo and edit.
- Screens that decide it: the prompt and generate loop, streaming output, the empty state that shows what to ask, the refusal or error.
- Motion: a streaming reveal helps, and theatrical thinking animations do not.

## Consumer and social: feeds, messaging, communities

- Constraints: no manipulative patterns, manufactured urgency or scroll that never ends without consent. Design for the phone first.
- Reads wrong: streaks built to exploit, fake notifications, cancellation made hard, stock avatars.
- Decide: real value against compulsion. Personality against legibility.
- Trust: real people and real content, visible controls to mute, block and leave, clear privacy.
- Screens that decide it: the feed, posting, the profile, the empty feed, notifications.
- Motion: delight is more welcome here than anywhere else, still behind the reduced-motion setting.

## Landing pages

Page structure is separate from the field. Any of these orders can serve any of the fields above.

| Pattern | Order | Where proof and action go |
| --- | --- | --- |
| Trust and authority | Hero, logos, problem, solution, proof, security, pricing, questions, final action | The main action in the hero, a security mark by the form, a result quote by the pricing |
| Features first | Hero, value, features, testimonials, pricing, final action | Actions spread through the page, testimonials before the last one |
| Live demo | Hero with the working product, how it works, feature detail, proof, pricing | The product is the hero, and the action comes after the person has seen it work |
| Waitlist | Hero, vision, a hint of proof, email capture | One job and one field |

## Sources

Baymard Institute for shops and checkout (baymard.com). Eleken's guides for money and health products. Field boundaries follow the categories used by Mobbin and Land-book. Conventions drift, so check a constraint against a current source before treating it as settled.
