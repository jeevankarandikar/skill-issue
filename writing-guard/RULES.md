# Writing

The guard reads this list to the model at the start of every session, so it writes to the rules before anything has to be blocked. They apply to every surface: chat, pages, UI copy, commit messages and docs. Edit the list to change what the model is told.

- No antithesis in parallel clauses: "X is the goal. Y is the byproduct.", "Not a plateau, a reset.", "It's not the number, it's the pattern.", "Show, don't tell." Say the one thing as a plain sentence.
- No triplets. Lists and adjective runs come in twos, fours, or however many there really are. No "Faster. Cleaner. Yours."
- Do not restate the question before answering. No "Great question", "When it comes to X".
- No filler authority: "it's worth noting", "importantly", "crucially", "in essence", "at its core", "here's the thing", "the short version", "bottom line", "the key idea is", "at the end of the day", "something real is happening".
- No empty contrast: "not just X, it's Y" where Y is fuzzier than X. Delete the first clause.
- Paragraphs stop when the point is made. No closing line written to be quoted.
- Bullets are ragged. Do not open every bullet with a bold noun and a colon. No colon-headers for drama ("The result: nothing.").
- No em dashes, anywhere. An en dash is allowed only inside a range of dates or numbers, never as a beat.
- Banned words: delve, tapestry, landscape, robust, leverage, seamless, elevate, unlock, journey, navigate, foster, holistic, impactful, empower, streamline, cutting-edge, game-changing, "testament to", "at the forefront", "passionate about", "uniquely positioned", "deep dive", "unpack".
- No both-ends framings that name no one: "whether you're a beginner or a pro".
- No empathy preambles ("I understand this can be frustrating") and no reassuring endings ("Let me know if you'd like me to expand").
- No summary that repeats the body. No "In summary".
- Counts are what the content has, never a round number chosen for symmetry.
- One hedge at most. "May potentially help in some cases" is three.
- No middle-dot separators between items in labels, captions, meta lines, or rows. Commas, a sentence, or separate elements.

## What the guard catches

`writing_guard.py` blocks four of these on sight: antithesis in the common shapes, the filler phrases and banned words, em dashes and spaced en dashes, and middle-dot separators. Triplets, restated questions, closing lines, symmetric counts and stacked hedges are left to the reader, since a pattern cannot tell them from honest prose.

In files it checks `.md`, `.mdx`, `.txt`, `.html`, `.htm` and `.rst`, and leaves code alone. "Landscape" and "navigate" pass in files, where CSS and routers use them, and are blocked in replies. In replies, code blocks, inline code and short quoted spans are skipped, so a reply can still name a banned phrase.
