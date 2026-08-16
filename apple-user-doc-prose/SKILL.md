---
name: apple-user-doc-prose
description: Draft or rewrite user-facing instructions, procedures, runbook steps, and how-to topics so they read like Apple's user documentation: calm, direct, second-person, imperative, plain. Use whenever you are writing or revising task steps, setup guides, or end-user procedures and you want Apple user-guide style.
---

# Apple user-doc prose

Write instructions the way Apple writes its User Guides and Support how-to topics.
The reader is busy and capable. Tell them exactly what to do, in order, in plain words.

## Core rules

**Voice and tense**
- Second person. Address the reader as "you"; refer to their device as "your Mac", "your laptop".
- Imperative mood for every action step. Start the step with the verb: Connect, Click, Choose, Open, Enter, Select, Turn on.
- Present tense for descriptions and results ("A code appears on both devices").
- Neutral and factual. No enthusiasm, no reassurance, no selling.

**Step structure**
- Default to a numbered list. Whenever the reader performs two or more actions in order, write them as a numbered list, one action per step. Never run a sequence together as a paragraph.
- One action per step. If two actions are inseparable, join them with "then": "Select the items, then click Continue."
- Start every step with its imperative verb, even a conditional step. Do not open a step with "When", "If", or "Once". Instead state the trigger as a short present-tense result on its own line, then give the verb-first step. For example: "A code appears on both laptops." then "Confirm that the codes match, then click Continue."
- Use a bulleted list for parallel options or things to choose among, not for ordered steps.
- To branch, write "Do one of the following:" then bullet the choices.
- Put the location or context once, at the start, not in every step: "On your laptop, open Settings."

**Referring to the interface (use Apple's verbs exactly)**
- click - buttons, icons, sidebar items, and other controls.
- choose - a command from a menu (for example, choose File then Export).
- select - an item, option, checkbox, or text that does not act immediately.
- enter or type - text the reader supplies in a field.
- Write UI labels exactly as they appear, in their own capitalization, with no quotation marks: click Continue, choose Migration Assistant.

**Sentences and words**
- Short, declarative sentences. One idea each. Prefer under about 20 words.
- Plain, common words. No jargon, no abbreviations the reader must decode.
- State a prerequisite before the steps, on its own line, plainly: "Before you begin, connect both laptops with a cable that supports data transfer."
- State a result in present tense right after the step that causes it.
- Use one term for one thing throughout. Do not alternate synonyms (cable/cord, laptop/machine).

## Forbidden (these fail QA)

- Minimizers and hype: simply, just, easily, quickly, seamlessly, amazing, powerful, effortless.
- "please" in an instruction.
- Slang, jokes, and filler: gotta, wanna, hit (a button), lol, "double check", "and more".
- Em dashes ( - long dash ) of any kind. Use a period, a comma, or parentheses.
- Emoji, exclamation points in steps, and ALL CAPS for emphasis.
- "e.g." and "i.e." in prose. Write "for example" and "that is".
- The ampersand in prose. Write "and".
- Vague quantities and hedges: "a bunch of", "some kind of", "should probably".

## Expected-results checklist (objective rubric)

Score the draft against every item. Each is pass or fail.

1. Every action step starts with an imperative verb. No step opens with "When", "If", or "Once".
2. The text is second person ("you"/"your"); no first person ("we", "I", "let's").
3. Descriptions and results are in present tense.
4. Each step performs one action (or two joined by "then"), not three or more.
5. Two or more sequential actions are written as a numbered list, one action per step, never as a run-on paragraph. Choices use a bullet list; branches use "Do one of the following:".
6. UI verbs match Apple usage: click (controls), choose (menu commands), select (items/options), enter/type (field text).
7. UI labels are written exactly, capitalized as shown, with no quotation marks.
8. No forbidden minimizers or hype words (simply, just, easily, quickly, seamlessly, and similar).
9. No "please", no slang, no jokes, no filler phrases.
10. No em dashes anywhere; no emoji; no exclamation points in steps; no ALL CAPS emphasis.
11. Prerequisites are stated before the steps; results are stated in present tense at the causing step.
12. One term per concept throughout; sentences are short and plain (most under about 20 words).

A draft passes only when all 12 items pass.

## Before / after

**1. Slang and hype to plain imperative**

Before: "Just go ahead and simply plug it in - it's super easy!"

After: "Connect the cable to your laptop."

**2. First person and vague to second-person, specific**

Before: "We'll want to make sure both machines are showing the same kind of code thingy."

After: "Confirm that both laptops show the same code."

**3. Run-on sequence to a prerequisite plus numbered steps**

Before: "Once it's plugged in they'll both show a code so open Settings and find Transfer and click it and pick what to move over."

After:

Before you begin, connect both laptops with a cable that supports data transfer.

1. On your laptop, open Settings.
2. Click Transfer. A code appears on both laptops.
3. Confirm that the codes match, then click Continue.
4. Select the users, apps, and settings to move.
