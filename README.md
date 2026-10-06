# skill-issue

This is the public half of my agent harness. It holds a design skill, a writing guard and a usage gauge. I used to keep 25 skills here. Most of them repeated what the models already do, so they are gone.

## design-jeev

`design-jeev` is a design skill for Claude Code, Cursor and Codex. It works in whatever stack the project already uses: web, SwiftUI, AppKit, UIKit, Compose, Flutter, React Native or a terminal UI.

It runs interface work in stages, and each stage hands a written result to the next through a `DESIGN.md` file in your repository.

| Stage | Ask for it like this | What you get |
| --- | --- | --- |
| Explore | "explore a direction for the settings screen" | The skill draws several directions on a design canvas such as Claude Design, or builds two in your own stack, and writes the one you choose into `DESIGN.md`. |
| Ship | "build it", "polish the sidebar" | The skill makes the change in your code with your tokens, renders it, and looks at every screen size and control state the change touches. |
| Review | "review this before release" | A fresh agent runs a pass or fail checklist on the rendered interface and ranks what it finds from P0 to P2. |

When a project has no interface yet, the skill picks an approach by use case before writing anything. The table it uses is in [choosing.md](design-jeev/references/choosing.md).

The judgment behind the stages lives in reference files the skill loads only when the work touches them:

| Reference | What it holds |
| --- | --- |
| [principles.md](design-jeev/references/principles.md) | How Apple, Google, Meta, OpenAI, Anthropic, Superhuman, Linear, Stripe, Vercel and Airbnb say they design, where they disagree, and how to choose |
| [lenses.md](design-jeev/references/lenses.md) | Ten designers to reason from, sixteen UX laws, the disclosure ladder |
| [craft.md](design-jeev/references/craft.md) | Type, color, spacing, hierarchy and depth |
| [interaction.md](design-jeev/references/interaction.md) | Control states, forms, waiting, overlays, keyboard, motion timing, first run |
| [words.md](design-jeev/references/words.md) | Interface text |
| [data-viz.md](design-jeev/references/data-viz.md) | Chart choice and palettes that survive color blindness |
| [verticals.md](design-jeev/references/verticals.md) | What money, developer, business, health, shop, AI and consumer products each demand |
| [critique.md](design-jeev/references/critique.md) | Heuristic scoring and the signs of a generic look |

It works beside a company or brand design skill and defers to it on brand.

`DESIGN.md` records the guidelines the project follows (Apple's, Material, or its own), its tokens, its licensed and banned assets, its surfaces and its decisions. The skill drafts one from your code the first time, using [this template](design-jeev/references/design-md-template.md).

## writing-guard

`writing-guard` is a hook for Claude Code, Cursor and Codex that refuses machine-sounding prose. It blocks em dashes, middle-dot separators, a list of filler phrases and stock words, and clauses set against each other for effect, in prose files as they are written and in chat replies before they are sent. The model gets the offending snippet back and rewrites. It also reads the full rules in [RULES.md](writing-guard/RULES.md) to the model at the start of each session. Install is one command, and the hook is one Python file with no dependencies. Details are in [its README](writing-guard/README.md).

## fleet-gauge

`fleet-gauge` is a Claude Code mod that stays quiet until usage matters. It adds a row above the prompt once the weekly limit reaches 50%, the five-hour limit reaches 70%, the context reaches 200k tokens, or a subagent is running. A toast fires when a subagent reaches 150 tool calls. `/fleet` prints the same numbers on demand. Cursor and Codex get a smaller version: a hook that tells the agent to hand off after 150 tool calls, and on Codex a status line with the limits. Details are in [its README](fleet-gauge/README.md).

## Install

Clone the repository and run `python3 install.py`. It sets up the design skill and the writing guard for whichever of Claude Code, Cursor and Codex you have. [SETUP.md](SETUP.md) has the details and the fleet-gauge step. To update later, run `git pull` in the clone and restart the agent.
