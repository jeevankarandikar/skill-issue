---
name: research
description: Engineering research that ends in an adoption decision, not a report. Use when the user wants to learn from outside work and act on it - "research X", "state of the art on Y", "best papers or repos for Z", "how does <company> do this", "what should we borrow", "look into these tools", or a pasted list of repos, plugins, or libraries to evaluate. Fans gatherers out on cheap models, judges once on a strong one, lands a cited memo (validated / adopt now / skip / watchlist) mapped to named components of the repo in front of it. Pure fact-finding with no adoption decision is out of scope here.
version: 1.0.0
user-invocable: true
argument-hint: "[topic, question, or a pasted list of things to evaluate]"
---

# Research

Learn from the frontier, then adapt it to the project in front of you. The output
is never a book report: it is an adoption memo the current repo can act on.

## Mode selection

- **Quick** (default for a narrow question): 2-4 targeted WebSearch/WebFetch calls
  inline, same citation discipline, answer in conversation. No workflow, no artifact
  unless asked.
- **Full** (a topic with 3+ orthogonal dimensions, or the user says "deep"/"thorough"):
  the Workflow fan-out below. This skill's instructions are the explicit opt-in to
  call the Workflow tool. (Workflow is main-session only; subagents cannot call it -
  if unavailable, fall back to parallel background Agent calls.)

## Full protocol

### 1. Decompose

Split the topic into 3-6 orthogonal dimensions. The standard cuts:

- **papers/labs** — arXiv + frontier-lab blogs (Anthropic, DeepMind, OpenAI, Meta,
  NVIDIA); what the labs themselves publish about what works
- **OSS repos** — the actual code of the leading implementations. Read source files
  and architecture, not just READMEs. Note module boundaries, eval harnesses, what
  makes the repo legible
- **ecosystem/community** — X, HN, Reddit signal (via agent-reach when available);
  what practitioners adopted vs abandoned, and why
- **benchmarks/evals** — how quality is measured in this space; leaderboards with
  dates, known gaming/failure modes
- **the negative case** — who tried this and stopped; documented failure modes;
  what the evidence says NOT to do

### 2. Fan out (Workflow, model-delegated)

One agent per dimension. Cost policy is fixed: gatherers on `model: 'sonnet'`
(mechanical), synthesis and any evaluator on `model: 'opus'` (judgment tier),
`haiku` only for link-liveness checks; never let a gatherer judge its own
findings. Give every agent a strict task contract: its dimension, a
findings schema, and the project context for relevance judgments.

Schema per agent:
```
{ dimension, key_findings[]   // each names source + lab/author + year + the takeaway
, sources[]                   // title + origin + year + URL
, borrowings[] }              // concrete things THIS project should adopt
```

Rules the agents carry:
- primary sources over commentary; every finding names its source
- nothing from memory: verify stars, versions, benchmark numbers, and dates
  against the live page; the current date comes from the environment, search accordingly
- for repos: cite specific files/functions, not vibes
- flag anything that could not be verified instead of dropping or asserting it

### 3. Synthesize (strong model)

One agent, `model: 'opus'`, `effort: 'high'`, writing a memo in plain terse prose
(no em dashes), with inline citations by name + origin + year:

1. **THE PICTURE** — what the sources collectively say (3-5 sentences)
2. **VALIDATED** — which of the project's existing choices the literature confirms,
   with the specific sources that back each
3. **ADOPT NOW** — the 5-7 highest-leverage additions, each mapped to its source
   AND to a concrete component of the current repo
4. **SKIP** — tempting things the evidence says not to do, with why
5. **WATCHLIST** — not ready yet, worth re-checking later

### 4. Land the artifact

- Write the memo to the repo's research home (`RESEARCH.md`, `runner/RESEARCH.md`,
  `docs/research/` — match the repo's layout) with a one-line header saying what
  question it answers.
- If the repo has a publish/PII gate, run it before committing anything.
- Commit only per the repo's ship policy (never push without an explicit ask).

### 5. Adapt on request

When the user says apply/build it: ADOPT NOW becomes the task list, in dependency
order, each item traceable back to its citation. Do not start building unasked —
the memo is the deliverable of this skill.

## Evaluating a pasted list (tools, plugins, repos)

When the user pastes a list of things to evaluate (common case): one gatherer per
item or per small group, verifying against the live repo/page — stars, last
commit, license, install path, security surface (hooks, marketplaces, network
calls). The memo becomes adopt / evaluate-for-fit / skip with the evidence, and
for anything that installs into the kit: the exact marketplace slug + settings
change, never a guessed repo (typosquat risk).

## Rules

- Judgment is scarce: the fan-out gathers, exactly one strong-model pass judges.
- A finding without a named source does not exist.
- Cost floor first: if 3 quick searches answer it, do not launch a workflow.
- The memo must name the project's components, not speak in generalities — "add X
  to runner/grounding.py" beats "consider adding verification."
