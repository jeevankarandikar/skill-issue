# skill-issue

The public half of my agent harness: one design skill and one Claude Code mod. I used to keep 25 skills here. Most of them repeated what the models already do, so they are gone.

## design-jeev

A design skill for Claude Code, Cursor and Codex that works in whatever stack the project already uses: web, SwiftUI, AppKit, UIKit, Compose, Flutter, React Native or a terminal UI.

It runs interface work in stages, and each stage hands a written result to the next through a `DESIGN.md` file in your repository.

| Stage | Ask for it like this | What you get |
| --- | --- | --- |
| Explore | "explore a direction for the settings screen" | Real alternatives on a design canvas such as Claude Design, or two rendered in your own stack. The chosen direction is written into `DESIGN.md`. |
| Ship | "build it", "polish the sidebar" | The change in your real code, from your tokens, rendered and inspected at the sizes and states that matter. |
| Review | "review this before release" | Findings ranked P0 to P2 from a pass or fail checklist, run by a fresh agent on the rendered interface. |

When a project has no interface yet, the skill picks an approach by use case before writing anything. The table it uses is in [choosing.md](design-jeev/references/choosing.md).

`DESIGN.md` records the guidelines the project follows (Apple's, Material, or its own), its tokens, its licensed and banned assets, its surfaces and its decisions. The skill drafts one from your code the first time, using [this template](design-jeev/references/design-md-template.md).

## fleet-gauge

A Claude Code mod that stays quiet until usage matters. It adds a row above the prompt once the weekly limit reaches 50%, the five-hour limit reaches 70%, the context reaches 200k tokens, or a subagent is running. A toast fires when a subagent reaches 150 tool calls. `/fleet` prints the same numbers on demand. Details are in [its README](fleet-gauge/README.md).

## Install

See [SETUP.md](SETUP.md). To update later, run `git pull` in the clone and restart the agent.
