# Onboarding and extract modes

Read when running `/design onboard` or `/design extract`.

## Onboarding Flows (`/design onboard`)

Run when scope includes first-run, empty states, or activation flows.

### Core Principles

- **Time to value:** Get users to "aha moment" ASAP. Teach the 20% that delivers 80% of value. Save advanced features for contextual discovery.
- **Show, don't tell:** Working examples over descriptions. Real functionality in onboarding, not a separate tutorial mode.
- **Make it optional:** Let experienced users skip. Don't block product access.
- **Context over ceremony:** Teach features when users encounter them — empty states are onboarding opportunities.
- **Respect intelligence:** Don't patronize. Assume users can handle standard patterns.

### First-Run Flow

1. **Welcome** — clear value proposition, time estimate (honest), skip option for experienced users
2. **Account setup** — minimal required info, smart defaults, explain why you're asking each question
3. **Core concepts** — introduce 1-3 concepts max; interactive not passive; progress indicator (step 1 of 3)
4. **First success** — guide to accomplish something real; pre-populated examples; celebrate completion briefly; clear next steps

### Empty State Design

Every empty state needs all five:
- **What will be here:** "Your recent projects will appear here"
- **Why it matters:** "Projects help you organize your work and collaborate with your team"
- **How to get started:** `[Create project]` or `[Start from template]`
- **Visual interest:** Illustration or icon — not just text on blank page
- **Contextual help:** "Need help? [Watch 2-min tutorial]"

Empty state types:
- **First use** — emphasize value, provide template
- **User cleared** — light touch, easy to recreate
- **No results** — suggest different query, offer to clear filters
- **No permissions** — explain why, how to get access
- **Error** — explain what happened, retry option

### NEVER
- Force users through long onboarding before they can use the product
- Show same tooltip or onboarding twice — track completion in `localStorage`, respect dismissals
- Block all UI during a tour
- Create a separate tutorial mode disconnected from the real product
- Overwhelm upfront — progressive disclosure
- Hide "Skip" or make it hard to find

---

## Extract Mode (`/design extract [target]`)

Pull reusable components and tokens into the design system. Follow the [extract flow](extract.md). Pass any additional text as the extraction target.

---

