# Industry Context

Vertical-aware design knowledge — the durable constraints, moods, and anti-patterns that make a design *appropriate* before you've seen a single reference. This is fuel for judgment, not a lookup table: it tells you what a vertical demands and *why*, then leaves the visual interpretation to taste + the dials.

**Hard rule:** this file stores constraints, mood words, anti-patterns (with reasons), tensions, and typical flows. It does **NOT** store palettes, hex codes, or font names — that's the monoculture trap. When you need live, current examples of a vertical, query the MCPs (see *Live examples*), don't hardcode a look here.

## How to use

1. Match the project to a vertical by its keywords. No exact match → use the closest and lean on the general taste rules.
2. Read its **constraints** (hard requirements + why), **anti-patterns** (what reads wrong here), and **tensions** (the judgment calls).
3. Pick a direction that satisfies the constraints and *deliberately decides* each tension — then express it through the dials and your font/color procedure. Use the **differentiation move** when the brief wants to break the category.
4. For live execution references, fire the vertical's `live_example_query` at the **lazyweb** (Mobbin/Savee) and **refero** MCPs. The KB says what's durable; the MCPs show what's shipping now. If a live example violates a KB anti-pattern, the KB wins — treat the trend as the thing to avoid.

---

## Verticals

### Fintech / banking / payments
*keywords: bank, neobank, payments, transfer, wallet, lending, brokerage, money, fintech*
- **Constraints**: financial accuracy is non-negotiable — never fake or round numbers, show real precision. WCAG AA minimum (users are often stressed). Surface fees and totals *before* the user commits.
- **Mood**: calm, authoritative, precise — confidence without flash.
- **Anti-patterns**: AI purple/pink gradients (reads as a generic LLM wrapper, not a bank → instant trust loss) · playful illustration on money screens (undercuts fiduciary seriousness) · fees revealed late · over-animated balances.
- **Tensions**: *density↔clarity* — dense scannable tables on desktop, collapse hard on mobile. *friction* — remove it from balance-checks, deliberately ADD a confirmation step to transfers/payments. *trust↔differentiation* — conservative by default, but one warm human accent separates you from clinical blue-white sameness.
- **Trust signals**: regulatory/compliance marks and security copy near forms and transfer actions; real institution logos.
- **Make-or-break screens**: transaction list · transfer/payment confirmation · empty state · failed-payment error.
- **Motion**: confirm and guide only; nothing decorative on money.
- **Differentiation move**: a warm human accent + plain-language copy — an ally, not a vault.
- **Live**: lazyweb `fintech dashboard transaction list` · refero screens `banking transfer confirmation`, flows `fintech onboarding`.

### Developer tools / API / infra
*keywords: api, sdk, cli, devtools, infra, database, observability, deploy, developer*
- **Constraints**: docs-first (devs read docs before marketing); show real code and real terminal output; dark-mode-native expectation; precision over polish.
- **Mood**: precise, fast, unembellished, a little technical.
- **Anti-patterns**: marketing fluff over substance · stock "developer at laptop" photos · pure black `#000` (use `#0a0a0a`/off-black) · explaining what code *does* instead of showing it · friendly mascots where credibility matters.
- **Tensions**: *marketing↔proof* — devs distrust marketing; lead with the code sample / live console, not the value prop. *density* — high is fine, devs tolerate it. *dark/light* — default dark, but offer light (many read docs in light).
- **Trust signals**: code that actually runs · GitHub stars / install counts · open-source signals · named eng teams.
- **Make-or-break screens**: quickstart/install · API reference · the first successful call · error/debug state.
- **Motion**: minimal, instant feedback — devs hate waiting on animation.
- **Differentiation move**: a genuinely great interactive playground / live API console.
- **Live**: lazyweb `developer tool landing dark` · refero screens `api documentation`, flows `developer onboarding quickstart`.

### B2B SaaS (enterprise)
*keywords: enterprise, b2b, saas, platform, workflow, admin, team, crm, erp*
- **Constraints**: multi-stakeholder (daily user ≠ buyer ≠ admin); role-based density; a credibility layer (SOC2, logos) distinct from the submission layer; the marketing site must "say one thing."
- **Mood**: credible, organized, efficient, quietly confident.
- **Anti-patterns**: consumer-cute tone in enterprise context · burying the differentiation · 3-column equal feature grids (the AI tell) · vague "platform" copy with no concrete outcome.
- **Tensions**: *density↔onboarding* — power density for daily users, gentle ramp for first-run. *one-message marketing↔feature-completeness* — landing says one thing, the app does many. *self-serve↔sales-led* — visible pricing (SMB) vs contact-sales (enterprise).
- **Trust signals**: customer logos early · SOC2/compliance · case studies with real metrics · testimonials with title+company.
- **Make-or-break screens**: setup/onboarding wizard · the core workflow · team/permissions admin · new-workspace empty state.
- **Motion**: purposeful; reduce on frequent power-user actions.
- **Differentiation move**: an opinionated, fast, keyboard-first core workflow (Linear-style).
- **Live**: lazyweb `b2b saas dashboard` · refero screens `saas onboarding`, flows `team invite`.

### Healthcare / patient / clinical
*keywords: health, patient, clinic, medical, telehealth, pharmacy, ehr*
- **Constraints**: WCAG AA mandatory, often AAA (impaired/elderly/stressed users); plain language, zero jargon; calm under anxiety; privacy-first framing.
- **Mood**: calm, trustworthy, gentle, clear.
- **Anti-patterns**: harsh alarm colors except for genuine alerts · dense clinical jargon · playful tone on serious health info · red/green as the *only* status signal (colorblind fail).
- **Tensions**: *clarity↔completeness* — clinicians need density, patients need simplicity; segment by audience. *reassurance↔honesty* — calm, but never hide bad news. *accessibility ceiling* — push to AAA when info is critical.
- **Trust signals**: HIPAA/privacy assurance · provider credentials · clear data-handling copy.
- **Make-or-break screens**: appointment booking · results/record view · medication/care instructions · first-visit empty state.
- **Motion**: minimal and gentle; honor reduced-motion strictly.
- **Differentiation move**: warmth + radical clarity — the opposite of cold clinical portals.
- **Live**: lazyweb `telehealth app calm` · refero screens `patient appointment booking`, flows `health onboarding`.

### E-commerce / retail
*keywords: shop, store, ecommerce, retail, checkout, cart, product*
- **Constraints** (Baymard-backed): ≥3-5 real product images; guest checkout must be prominent; ≤8 checkout fields, clearly grouped; cart accessible (upper-right); no auto-rotating carousels.
- **Mood**: brand-tier dependent — but always desirable, trustworthy, frictionless.
- **Anti-patterns**: hidden costs revealed at the last checkout step (the #1 conversion killer) · broken/placeholder product images · forced account creation before purchase · fake urgency timers.
- **Tensions**: *browse↔buy* — inspire on the listing, reassure on the detail page, remove all friction at checkout. *imagery↔performance* — image-rich but optimized (`srcset`). *brand-expression↔convention* — distinctive storefront, boringly conventional checkout.
- **Trust signals**: reviews with counts · return/shipping clarity · secure-payment marks at checkout · real photography.
- **Make-or-break screens**: product listing (PLP) · product detail (PDP) · cart · checkout · empty cart.
- **Motion**: subtle on browse; zero distraction at checkout.
- **Differentiation move**: editorial product storytelling on the storefront; a checkout so fast it's invisible.
- **Live**: lazyweb `ecommerce product page` · refero screens `checkout flow`, flows `ecommerce checkout`.

### AI / LLM product
*keywords: ai, llm, chatbot, copilot, agent, generative, ml-product*
- **Constraints**: THE anti-generic battleground. The default "purple gradient + ✨ sparkles + Inter" is the single most over-used look in software right now — actively avoid it. Set expectations for latency/streaming; show provenance and uncertainty honestly.
- **Mood**: positioning-dependent (tool vs companion vs infra) — but *distinctive is mandatory* here, because the category default is slop.
- **Anti-patterns**: purple/violet gradients + sparkle iconography (the #1 AI tell) · pretending the model is certain when it isn't · hiding that it's AI / fake-human dark patterns · an endless chatbox where a structured UI would serve better.
- **Tensions**: *magic↔trust* — delight without overpromising; show your work. *chat↔structured UI* — don't default to a chatbox. *speed-perception* — stream tokens, show progress, never a dead spinner.
- **Trust signals**: citations/sources · confidence/uncertainty cues · honest "AI-generated" labeling · easy undo/edit.
- **Make-or-break screens**: the generate/prompt loop · streaming output · "what can I ask?" empty state · refusal/error state.
- **Motion**: streaming reveals are good; skip gratuitous "thinking" theatrics.
- **Differentiation move**: literally anything that isn't the purple-sparkle default — an opinionated, non-chatbox interface.
- **Live**: lazyweb `ai product interface` · refero screens `ai chat ui`, flows `ai onboarding`. ⚠️ Most live AI examples *are* the slop — use them as what to avoid.

### Consumer / social
*keywords: social, community, consumer, feed, messaging, lifestyle, creator*
- **Constraints**: engagement matters, but the **ethics guardrail is a hard constraint** — no manipulative dark patterns, no manufactured FOMO, no infinite-scroll-without-consent. Mobile-first.
- **Mood**: alive, personal, expressive (brand-dependent), human.
- **Anti-patterns**: dark patterns (manipulative streaks, fake notifications, hard-to-cancel) · gamification that exploits rather than serves · generic stock avatars · engagement bait.
- **Tensions**: *engagement↔wellbeing* — design for genuine value, not compulsion. *expressive↔legible* — personality without sacrificing usability. *delight↔respect* — celebrate moments, don't manufacture them.
- **Trust signals**: real people and authentic content · transparent controls (mute/block/leave) · clear privacy.
- **Make-or-break screens**: the feed · content creation/posting · profile · no-content empty state · notifications.
- **Motion**: delight is more welcome here than anywhere else — celebrations, micro-interactions, personality. Still gate on reduced-motion.
- **Differentiation move**: a signature interaction or visual identity that *becomes* the brand.
- **Live**: lazyweb `social app feed` · refero screens `social profile`, flows `social onboarding`.

---

## Landing-page patterns

Page structure is orthogonal to vertical — a fintech site and a dev-tools site can both use *Trust & authority*. Section vocabulary: `hero` · `usp/value-prop` · `logo-strip` · `social-proof` · `feature-grid` · `product-demo` · `comparison` · `pricing` · `objection/FAQ` · `lead-form` · `case-study` · `enterprise/contact-sales` · `footer`.

| Pattern | Section order | CTA / proof strategy |
|---|---|---|
| **Trust & authority** | hero → logo strip → problem → solution → proof → security/compliance → pricing → FAQ → final CTA | primary CTA in hero; security badge by the form; result-quote by pricing |
| **Hero → features → CTA** | hero → usp → feature grid → testimonials → pricing → final CTA | distributed CTAs; 3-5 testimonials (photo+name+role) *before* the CTA |
| **Interactive demo** | hero (live demo) → how-it-works → feature deep-dives → social proof → pricing | let the product be the hero; CTA after the "aha" |
| **Waitlist / pre-launch** | hero → vision → teaser proof → email capture | one job: capture; ≤1 field |

---

## To seed (Tier 2/3 — not yet written)

Distinct-enough to deserve their own entries; seed from the cited sources when a project needs one: analytics/dashboard · marketplace (two-sided) · mental-health/wellness · creator/portfolio · productivity/collaboration · gov/public-sector (WCAG AAA) · real-estate · edtech. Skip the long tail (pet tech, wedding, podcast) — they're booking/e-commerce variants with no distinct constraints. Better 16 sharp records than 39 mushy ones.

## Sources

Durable conventions distilled from (refresh ~annually — conventions drift):
- Baymard Institute — e-commerce + checkout (gold standard): https://baymard.com/learn/ecommerce-ux-best-practices · https://baymard.com/research/checkout-usability
- Eleken — fintech & healthcare UI guides: https://www.eleken.co/blog-posts/modern-fintech-design-guide · https://www.eleken.co/blog-posts/user-interface-design-for-healthcare-applications
- B2B SaaS: https://www.onething.design/post/b2b-saas-ux-design · https://genesysgrowth.com/blog/designing-b2b-saas-homepages
- Dev tools / dark mode: https://lovable.dev/guides/dark-mode-website-examples-guide
- Consumer engagement ethics: https://uxmag.com/articles/gamification-or-manipulation-understanding-the-ethics-of-engagement-loops
- Landing structure: https://www.involve.me/blog/landing-page-structure
- Per-vertical anti-patterns cross-checked against ui-ux-pro-max `ui-reasoning.csv`
- Vertical taxonomy bounds: Land-book (https://land-book.com), Mobbin (https://mobbin.com)

---

**Avoid**: storing palettes/fonts/hex here (monoculture trap — defer the look to taste + the MCPs) · treating a vertical as a fixed recipe (it's constraints + tensions, you still decide) · letting live MCP examples override a KB anti-pattern.
