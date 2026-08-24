---
name: unslop
description: Remove AI writing tells from prose without inventing anything. Use when the user says text "sounds like AI", "sounds like ChatGPT", "sounds like an LLM", "sounds robotic", or asks to "make this human", "make it sound less AI", "remove the slop", "deslop this", "unslop this", "humanize this", "de-AI this", or "clean up AI writing". Also use proactively when writing or revising any prose a human will read: docs, READMEs, blog posts, release notes, emails, UI copy, marketing pages, reports, and PR descriptions. Never add a fact, number, benchmark, anecdote, or feature the source does not contain.
---

# Unslop

Rewrite prose so it reads like a person wrote it, without changing what it says.

## Rule zero: never invent

The most common failure of this pass is not a leftover tell. It is fabrication.
Under pressure to "be specific" and "add human texture", an editor invents
benchmarks, setup steps, anecdotes, and features that are not in the source.
That output looks better and is worse: it is now wrong.

- Never add a fact, number, date, benchmark, anecdote, quote, name, source,
  feature, or capability that is not in the source text or supplied by the user.
- Cutting filler is always safe. Cutting a fact on the lock list is not: the
  facts stay, the padding goes. Adding requires the source to already contain it.
- A vague claim stays vague, gets cut, or becomes a question to the user. Do not
  upgrade "improves performance" into "cuts latency to 200ms" unless the number
  exists.
- Do not launder weak claims into confident ones. If the source only asserts a
  benefit, the rewrite may not state it as measured fact.
- Do not add editorial stakes the source does not take. Sharpening an opinion the
  author already holds is fine; supplying a new opinion is not.
- Fiction is the one exemption: there, invented detail is the assignment.

Every other rule in this skill yields to this one.

## Procedure

1. **Read the whole text once before editing.** Note the format (doc, post, email,
   UI copy), the audience, and the register. List 3-5 voice traits worth keeping:
   vocabulary, cadence, humor, bluntness, digressions.
2. **Lock the facts.** List every name, number, date, quote, cited source, and
   concrete capability. The rewrite may not add to this list. It may cut filler,
   slogans, and unsourced authority theater. It may not drop a concrete fact.
3. **Separate the brief from the text.** Long inputs often mix the material with
   instructions about it ("keep this casual", "don't promise a fix"). Obey those
   sentences; never print them in the output.
4. **Pick the depth.**
   - Quick pass: scan against the top ten tells below. Enough for short text.
   - Full pass: read `reference/patterns.md` and scan the whole catalog. Do this
     for anything being published, anything over a few paragraphs, and any audit
     request. That file is the catalog; this file is the procedure.
5. **Collect candidates, then validate each one.** Do not edit on first sight.
   For each candidate: is this slop (a pattern put it there) or voice (the author
   could defend it)? Discard false positives. Flag clusters, not lone hits; one
   dash or one "crucial" proves nothing by itself.
6. **Rewrite with minimal edits**, in this order: cut filler and announcements,
   swap banned vocabulary for plain words, break formula structures, restore
   actors (active voice, subjects the source already names), then fix rhythm
   (vary sentence and paragraph length). Prefer the smallest change that kills
   the tell.
7. **Stop when the remaining candidates are voice.** Over-editing flattens a
   real person into the generic polish this skill exists to remove. "This reads
   fine, no changes needed" is a valid output.

## Voice

- A writing sample from the user outranks every style rule here, including
  dashes: if the sample uses em dashes, keep them at the sample's rate.
- Match register to format. Technical and reference prose stay neutral and
  plain; do not inject opinions, first person, or "you" where the source does
  not address the reader. Casual posts keep contractions, fragments, and asides.
  Formal documents keep full sentences without becoming ornate.
- Repeating the exact term is correct in technical writing. Do not vary a
  function name or a defined term for elegance.
- Voice never overrides rule zero. Personality comes from stance, rhythm, and
  word choice, not from invented specifics.

## The top ten tells

Highest-signal patterns. Examples and edge cases live in `reference/patterns.md`.

1. **Formulaic dashes** (U+2014, U+2013, spaced dashes, and ` -- `). Clusters of
   em dashes, especially spaced ones, are a tell. Replace those with a period,
   comma, colon, or parentheses. A lone dash is not evidence and is not a
   rewrite target. Do not add dashes. Do not run a zero-dash purge.
2. **Negative parallelism.** "Not X, but Y", "isn't just X, it's Y", "Not a X.
   Not a Y. A Z." State Y (or Z) directly.
3. **AI vocabulary clusters.** delve, tapestry, leverage, seamless, robust,
   pivotal, crucial, testament, landscape, vibrant, foster, showcase, underscore,
   harness, empower, elevate, paradigm shift. Swap for the plain word or cut.
   A single ordinary use can stay; a cluster cannot.
4. **Padded triads.** Lists forced to three parallel items for rhythm. Use the
   real number; two is often the truth.
5. **-ing analysis tails.** ", highlighting...", ", underscoring...",
   ", ensuring...", ", reflecting..." tacked on to fake depth. Cut the tail, or
   promote its content only when that content is already in the source.
6. **Throat-clearing and announcements.** "Here's the thing", "Let's dive in",
   "It's worth noting", "In today's fast-paced world", "Enter [Name]." Delete
   the frame; state the point.
7. **False agency and actorless passive.** "The decision emerges", "this
   ensures", "results are preserved automatically". Name the actor the source
   already implies (the product, the authors, the reader). Do not inject "you"
   into third-person or reference prose. Scientific methods may keep passive.
8. **Vague authority.** "Experts believe", "studies show", "the implications
   are significant". If the source names who, use that name; otherwise cut the
   theater. Never invent a source. An unsourced direct claim is not this tell.
9. **Metronomic rhythm.** Three-plus consecutive sentences of the same length,
   stacked punchy fragments, every paragraph ending on a mic-drop line. Vary
   lengths and endings. Do not engineer a zigzag.
10. **Marketing residue.** "It just works", "Period.", "Whether you're a X or a
    Y", "The journey starts here", generic upbeat closers. Replace with a
    concrete fact from the source, or end on the last concrete point. Never
    invent a behavior to replace a slogan.

## Verify before returning

A rewrite that skips this step is not done.

1. Re-scan for the ten tells above. Any remaining cluster means another pass.
2. Diff facts against the lock list: every locked fact survives, and nothing
   new appears. A fabrication is a defect even when it reads better.
3. Check that no tell was replaced with a different formula (new aphorism, tidy
   triad, forced contrast, consultant voice).
4. Read as the intended reader. If it now sounds flat, restore the author's
   traits from step 1.

## Output

- **Pasted text (default):** return the rewrite, then a short list of what
  changed and which tell each change removed.
- **Detect only** (audit, or "does this read as AI?"): name clusters first,
  quote the offending line, give the fix in a few words. Mention singletons
  only as weak signals. Do not rewrite. Do not output a probability that AI
  wrote it.
- **File mode:** edit the file in place, prose only. Leave code blocks,
  frontmatter, data, and link targets untouched. Report a short summary.
- **Embedded** (another task is using this skill mid-pipeline): output only the
  final text.

## CREDITS

Compiled from a bake-off of ten overlapping skills: anti-ai-slop-writing,
anti-slop, deslop, humanize, humanizer, humanizer-aboudjem, no-ai-slop,
slopbeth, stop-slop, and unslop. Upstream: stephenturner/skill-deslop;
blader/humanizer, which draws on Wikipedia's "Signs of AI writing". The
bake-off's main lesson, that rewriting often invents facts, became rule zero.
