# Pre-flight

Read before invoking the engine. Query-trap detection, handle and repo resolution, community resolution, and query planning.

## Step 0.45: Query Quality Pre-Flight (detect keyword-trap topics BEFORE running the engine)

**MANDATORY. Before Step 0.5, diagnose the topic for known failure classes. If the topic is a keyword trap, reframe or ask a clarifying question BEFORE calling the engine. Running the engine on a doomed query burns 5+ minutes and produces junk. Detecting the trap upfront costs one turn.**

Known keyword-trap classes and how to handle each:

**Class 1: Demographic shopping query**
- Pattern: `gift for {age} year old {gender}`, `what to buy for my {relationship}`, `present for {demographic}`, `birthday gift for {age} {gender}`.
- Why it fails: no human on Reddit posts "I bought a 42 year old man a gift." Real posts use relationship + hobbies + budget. The literal phrase is not the vocabulary of the actual discussions. The 2026-04-18 "Birthday gift for 42 year old man" run returned r/todayilearned, r/japannews crime posts, r/LivestreamFail drama - none about gifts.
- Action: **Ask ONE clarifying question upfront**:
  > "Before I research, tell me a bit more - hobbies (cooks / runs / reads / gaming / outdoors / golf / music)? Relationship (husband / dad / friend / boss / brother)? Budget range? A 'gift for a 42 year old man' is a wide net; hobbies + relationship narrow it 10x."
- If the user declines to narrow ("just run it"), reframe to generic-demographic and scope to gift subreddits:
  - Drop the literal age (age 42 reads identically to 41 or 43 in social content; the number causes keyword collisions like Jackie Robinson #42)
  - Rewrite as `gifts for men in their 40s` or `gifts for men who [hobby]`
  - Scope `--subreddits=GiftIdeas,BuyItForLife,AskMen,malefashionadvice,Dads` (plus hobby-specific subs when known)
  - Note in the Resolved block: "Reframed demographic shopping query. Dropping literal age; scoping to gift communities."

**Class 2: Numeric / age keyword trap**
- Pattern: topic contains a specific number that collides with unrelated content (42 = Jackie Robinson + Hitchhiker's + a 42" quilt; 40 = 40th anniversary posts; 50 = state-count posts; 100 = bench-press posts).
- Why it fails: the number dominates retrieval and pulls in unrelated content. A search that prominently features "42" returns jersey-number posts; a search for "the 100" returns TV-show posts.
- Action: Strip the number from the engine search query unless changing or removing it would change the topic itself (e.g., "GPT-4" yes, "40 year old man" no, "Area 51" yes, "top 10 foods" no). Keep the number in the user's original framing for context; drop it from the engine query. Document in Resolved: "Dropping '{number}' from the search query - it is a keyword trap that pulls in unrelated content. Search will cover the concept generically."

**Class 3: Overly-literal concept phrase**
- Pattern: `how to use X`, `what is Y`, `tutorial for Z`, `explain A` — tutorial-shaped phrasing where social posts are in different vocabulary.
- Why it fails: social posts about Docker do not say "how to use Docker"; they say "my Docker setup", "nginx in Docker", "my dev loop", "tip for folks using Docker Compose". Tutorial phrasing matches blog titles, not social discussions.
- Action: Reframe from tutorial phrasing to discussion phrasing: "how to use Docker" becomes "Docker tips tricks workflows" or "Docker production setups". Document the reframe in the Resolved block.

**Class 4: Generic single-noun common word**
- Pattern: topic is a single common noun with no specific hook (`bread`, `sneakers`, `coffee`, `shoes`, `headphones`).
- Why it fails: single-noun queries have no anchor — the corpus is infinite and the signal is noise.
- Action: Ask for specificity before running:
  > "{TOPIC} is a huge category - are you asking about {specific-facet-A}, {specific-facet-B}, or {specific-facet-C}? Each is a different community. Pick one or tell me the angle."

**Class 5: Non-English / non-Latin-script topic (Hebrew, Arabic, Chinese, Japanese, etc.)**
- Pattern: topic contains non-Latin characters (Hebrew [\u0590-\u05FF], Arabic [\u0600-\u06FF], CJK [\u4E00-\u9FFF], etc.).
- Why it fails without intervention: Reddit, HackerNews, GitHub, and Polymarket are English-dominant platforms. A Hebrew brand like "קפה עלית" scores zero entity-matches across all four sources and returns only English-language noise as fallback padding.
- Action: **Mandatory pre-flight steps for non-English topics:**
  1. **Force `--web-backend brave`** in the engine command. Brave indexes non-English web (Ynet/Walla/Mako for Hebrew; Haber7/Hurriyet for Turkish; etc.) and is the only available source with real-language coverage.
  2. **Skip `--subreddits` targeting unless the topic has a known English-speaking community.** Generic subreddits (r/food, r/Israel) return English noise; omit them or scope tightly to known bilingual communities.
  3. **Note in the Resolved block:** "Non-English topic detected ([language]). Routing to `--web-backend brave`; Reddit/HN/GitHub will likely return zero on-topic results."
  4. **X/Twitter and YouTube are the highest-value missing sources for non-English topics.** Surface this clearly in the output so the user knows what would unlock deeper coverage.
- Do NOT skip this class check for mixed-script queries (e.g. "קפה עלית Elite Coffee") - if any non-Latin characters are present, Class 5 applies.

**Pre-Flight decision flow (do this BEFORE any WebSearch):**
1. Read the topic. Match against Classes 1-5 above.
2. If the topic matches a class, ALWAYS emit a visible pre-flight note before the Resolved block:
   - `Pre-Flight: topic matches {Class N} ({class name}). {Action: clarifying question / reframe / specificity ask}.`
3. If the action is a clarifying question, STOP after emitting it. Wait for the user response before any engine work.
4. If the topic does NOT match any class, emit a one-liner: `Pre-Flight: topic is a {named-entity / comparison / concept} - proceeding to Step 0.5.` Then proceed.

**One-turn gate rule:** do NOT run the engine on a keyword-trap topic without either (a) explicit user confirmation to "just run it anyway", or (b) a concrete reframed query. Burning 5 minutes on a doomed run is worse than a one-turn clarifying question.

**When the user provides context inline:** if a Class 1 query already contains hobbies/relationship/budget ("gift for my cooking-obsessed husband, $200"), SKIP the clarifying question and go straight to the reframe + scope action. The clarifying question exists to fill in the gaps; if the gaps are already filled, move on.

---

## Step 0.5: Pre-Flight Resolution (handles, repos, communities)

**Pre-Flight Checklist — do NOT stop after the first flag. Every applicable flag below is MANDATORY for its topic class.**

Before running the engine, determine which flags apply to this topic and resolve them. Reading only the "X handle" subsection and stopping there is the named failure mode of the Peter Steinberger disaster #2 (2026-04-18). The model admitted on debug: "I treated the 'X handle resolution' section as the full contract for pre-flight resolution and didn't --help the script to see what else existed." The checklist below IS the full contract.

| Flag | Resolved in | Applies when |
|------|-------------|--------------|
| `--x-handle={handle}` | Step 0.5 (Section A below) | Topic is a person, brand, product, or creator with an X presence |
| `--x-related={h1,h2,...}` | Step 0.5 (Section A below) | Topic has associated entities (founders, commentators, spouse, collaborators, media handles) |
| `--github-user={user}` | Step 0.5b | Topic is a person who ships code (developer, engineer, CEO-who-codes, researcher) |
| `--github-repo={owner/repo}` | Step 0.5c | Topic is a product / project / open-source tool |
| `--trustpilot-domain={domain}` | Step 0.5d | Topic is a company / brand / service with a Trustpilot presence AND the run includes the Trustpilot source |
| `--subreddits={sub1,sub2,...}` | Step 0.55 | Always — almost every topic has active Reddit communities |
| `--tiktok-hashtags={h1,h2,...}` | Step 0.55 | Always — inferred from topic |
| `--tiktok-creators={c1,c2,...}` | Step 0.55 | Creator / influencer / brand topics |
| `--ig-creators={c1,c2,...}` | Step 0.55 | Creator / brand topics |
| `--web-backend brave` | Step 0.45 Class 5 | **MANDATORY** for non-Latin-script topics (Hebrew, Arabic, CJK, etc.) — Brave is the only source that indexes non-English web |
| `--auto-resolve` | Fallback | WebSearch is available but Step 0.55 could not resolve everything cleanly — use as belt-and-suspenders |

**Checkpoint before running the engine:** your Bash command must include every flag from the checklist that applies to this topic. For a person who ships code (the Peter Steinberger class), that is MINIMUM `--x-handle` AND `--github-user` AND `--subreddits`, and typically `--x-related` too. A command with only `--x-handle` on a person topic is a pre-flight skip and a Step 0.5 regression.

---

### Section A: Resolve X Handles (if topic could have X accounts)

If TOPIC looks like it could have its own X/Twitter account - **people, creators, brands, products, tools, companies, communities** (e.g., "Dor Brothers", "Jason Calacanis", "Nano Banana Pro", "Seedance", "Midjourney"), do WebSearches to find handles in three categories:

**1. Primary handle** (the entity itself):
```
WebSearch("{TOPIC} X twitter handle site:x.com")
```

**2. Company/organization handle OR founder/creator handle** -- This mapping is bidirectional:
- If the topic is a **PERSON**, resolve their company's X handle. A CEO's story is inseparable from their company's story.
- If the topic is a **PRODUCT or COMPANY**, resolve the founder/creator's personal X handle. The creator's personal account often has the most candid, high-signal content.
```
WebSearch("{TOPIC} company CEO of site:x.com")
```
OR for products:
```
WebSearch("{TOPIC} creator founder X twitter site:x.com")
```
Examples: Sam Altman -> @OpenAI, Dario Amodei -> @AnthropicAI, OpenClaw -> @steipete (Peter Steinberger), Paperclip -> @dotta, Claude Code -> @alexalbert__.

**3. 1-2 related handles** -- People/entities closely associated with the topic (spouse, collaborator, band member), PLUS 1-2 prominent commentator/media handles that regularly cover this topic:
```
WebSearch("{RELATED_PERSON_OR_ENTITY} X twitter handle site:x.com")
```
For a music artist, find music commentary accounts (e.g., @PopBase, @HotFreestyle, @DailyRapFacts).
For a tech CEO, find tech media accounts (e.g., @TechCrunch, @TheInformation).
For a product, find reviewer accounts in that category.

From the results, extract their X/Twitter handles. Look for:
- **Verified profile URLs** like `x.com/{handle}` or `twitter.com/{handle}`
- Mentions like "@handle" in bios, articles, or social profiles
- "Follow @handle on X" patterns

**Verify accounts are real, not parody/fan accounts.** Check for:
- Verified/blue checkmark in the search results
- Official website linking to the X account
- Consistent naming (e.g., @thedorbrothers for "The Dor Brothers", not @DorBrosFan)
- If results only show fan/parody/news accounts (not the entity's own account), skip - the entity may not have an X presence

Pass handles to the CLI:
- Primary: `--x-handle={handle}` (without @)
- Related: `--x-related={handle1},{handle2},{company_handle},{commentator_handles}` (comma-separated, without @)

Example for "Kanye West":
- Primary: `--x-handle=kanyewest`
- Related: `--x-related=travisscott,PopBase,HotFreestyle`

Example for "Sam Altman":
- Primary: `--x-handle=sama`
- Related: `--x-related=OpenAI,TechCrunch`

Related handles are searched with lower weight (0.3) so they appear in results but don't dominate over the primary entity's content.

**Note about @grok:** Grok is Elon's AI on X (xAI). It often appears in search results with thoughtful, accurate analysis. When citing @grok in your synthesis, frame it as "per Grok's AI analysis of [article/topic]" rather than treating it as an independent human commentator.

**Skip this step if:**
- TOPIC is clearly a generic concept, not an entity (e.g., "best rap songs 2026", "how to use Docker", "AI ethics debate")
- TOPIC already contains @ (user provided the handle directly)
- Using `--quick` depth
- WebSearch shows no official X account exists for this entity

Store: `RESOLVED_HANDLE = {handle or empty}`, `RESOLVED_RELATED = {comma-separated handles or empty}`

### Step 0.5b: Resolve GitHub Username (if topic is a person) — MANDATORY FOR PERSON TOPICS

**MANDATORY when the topic is a person (developer, creator, CEO, founder, engineer, researcher) and WebSearch is available.** Resolving the X handle but NOT the GitHub handle is the documented Peter Steinberger failure mode (2026-04-18). Without `--github-user={handle}`, GitHub search becomes a keyword match across all of GitHub instead of person-mode scoped to `user:{handle}`. The result is typically 5-10 thin unrelated items instead of the person's actual commits, PRs, releases, and top-starred repos. Treat this as a peer step to Step 0.5 (X handle resolution), not an afterthought.

Do the WebSearch:

```
WebSearch("{TOPIC} github profile site:github.com")
```

From the results, extract their GitHub username from URLs like `github.com/{username}`.

**Verify the account is correct:** Check that the profile description or pinned repos match the person you're researching. Common names may return multiple profiles.

Pass to the CLI: `--github-user={username}` (without @)

Worked examples:
- For "Peter Steinberger", a WebSearch for `Peter Steinberger github profile site:github.com` returns @steipete. Pass `--github-user=steipete`.
- For "Matt Van Horn": `--github-user=mvanhorn`
- For "Garry Tan": `--github-user=garrytan`

**Person-mode GitHub tells a different story than keyword search.** Instead of "who mentioned this person in an issue body," it answers: "What are they shipping? Where are they getting merged? What do their own projects look like?" The engine fetches PR velocity, top repos with star counts, release notes, and README summaries.

**Skip this step if:**
- TOPIC is clearly NOT a person (products, concepts, events)
- TOPIC already has `--github-user` specified by the user
- Using `--quick` depth
- WebSearch shows no GitHub profile for this person (report "no GitHub handle found for this person" and proceed without `--github-user` rather than fabricating one)

Store: `RESOLVED_GITHUB_USER = {username or empty}`

**Checkpoint for person topics:** by the time you reach the Research Execution command, for a person topic you MUST have BOTH `RESOLVED_HANDLE` (from Step 0.5) AND `RESOLVED_GITHUB_USER` (from this step) OR an explicit "no X account" / "no GitHub profile" note. The Bash command that follows must include BOTH `--x-handle={handle}` AND `--github-user={handle}` when resolved. A person-topic run that shows only one of the two is a Step 0.5b regression.

### Step 0.5c: Resolve GitHub Repos (if topic is a product/project)

If TOPIC looks like a product, tool, or open source project (not a person), resolve its GitHub repo for project-mode search:

```
WebSearch("{TOPIC} github repo site:github.com")
```

From the results, extract `owner/repo` from URLs like `github.com/{owner}/{repo}`.

Pass to the CLI: `--github-repo={owner/repo}`

For comparisons ("X vs Y"), resolve repos for both topics: `--github-repo={repo_a},{repo_b}`

Example for "OpenClaw": `--github-repo=openclaw/openclaw`
Example for "OpenClaw vs Paperclip": `--github-repo=openclaw/openclaw,paperclipai/paperclip`

Project-mode GitHub fetches live star counts, README snippets, latest releases, and top issues directly from the API. This is always more accurate than blog posts or YouTube videos citing weeks-old numbers.

**Skip this step if:**
- TOPIC is a person (use `--github-user` instead)
- TOPIC has no GitHub presence (not a software project)
- WebSearch shows no GitHub repo for this topic

Store: `RESOLVED_GITHUB_REPOS = {comma-separated owner/repo or empty}`

### Step 0.5d: Resolve Trustpilot Domain (if topic is a company/brand and Trustpilot is active)

If the run includes the Trustpilot source (`INCLUDE_SOURCES=trustpilot` or an explicit `--search` list) and TOPIC is a company, brand, or service, resolve its Trustpilot review-page domain. Trustpilot pages are keyed by domain (`www.thriftbooks.com`), not company name — a bare name 404s.

**You usually already have it.** Step 0.55 item 6 (first-party positioning) fetches the official site — capture the bare hostname while you're there. When positioning wasn't fetched, one lookup covers it:

```
WebSearch("{TOPIC} official site")
```

Pass to the CLI: `--trustpilot-domain={domain}` (e.g., `--trustpilot-domain=www.thriftbooks.com`)

The flag is used verbatim and bypasses the engine's brand-shape gate, so it also unlocks Trustpilot for multi-word company names ("Stanley Steemer carpet cleaning"). For comparisons, put a per-entity `trustpilot_domain` in each PEER entity's `--competitors-plan` entry; the MAIN topic's domain must ride the outer `--trustpilot-domain` flag (the engine does not read a main-topic entry out of the plan).

**A miss is not fatal.** When the flag is absent, the engine resolves name → domain itself via the CLI's search (and headless `--auto-resolve` runs fill a hint the engine verifies). Resolve the flag when the domain is already in hand or the company name is ambiguous (lookalike or same-named companies) — an explicit domain is the only way to guarantee the right company.

**Skip this step if:**
- The Trustpilot source is not active for this run
- TOPIC is a person, event, or abstract concept (no company reviews to fetch)

Store: `RESOLVED_TRUSTPILOT_DOMAIN = {domain or empty}`

---

## Agent Mode (--agent flag)

If `--agent` appears in ARGUMENTS (e.g., `/last30days plaud granola --agent`):

1. **Skip** the intro display block ("I'll research X across Reddit...")
2. **Skip** any `AskUserQuestion` calls - use `TARGET_TOOL = "unknown"` if not specified
3. **Run** the research script and WebSearch exactly as normal
4. **Skip** the "WAIT FOR USER RESPONSE" pause
5. **Skip** the follow-up invitation ("I'm now an expert on X...")
6. **Output** the complete research report and stop - do not wait for further input

Agent mode saves raw research data to `LAST30DAYS_MEMORY_DIR` (defaults to `~/Documents/Last30Days`) automatically via `--save-dir` (handled by the script, no extra tool calls). Use `--output <file>` only when a caller needs the rendered stdout artifact at an exact path, with the format controlled by `--emit`.

**Machine-readable JSON exception:** If the user explicitly asks for structured JSON for an agent, script, or workflow, replace the normal `--emit=compact` engine invocation with `--emit=json` and pass the engine's stdout through verbatim instead of synthesizing the report format below. The default `--json-profile=agent` is the stable, versioned flat contract; use `--json-profile=raw` only when the user explicitly requests the full internal `Report` dump. `--preflight --emit=json` is a separate permission-preflight contract and is not affected by `--json-profile`. Full field documentation and the versioning policy live in `docs/reference/json-export.md` in the repository.

Agent mode report format:

```
## Research Report: {TOPIC}
Generated: {date} | Sources: Reddit, X, Bluesky, YouTube, TikTok, HN, Polymarket, Web

### Key Findings
[3-5 bullet points, highest-signal insights with citations]

### What I learned
{The full "What I learned" synthesis from normal output}

### Stats
{The standard stats block}
```

---

## If QUERY_TYPE = COMPARISON

When the user asks "X vs Y" (or "X vs Y vs Z"), the engine fans out N full `pipeline.run()` calls in parallel — one per entity — each with its own Step 0.55-grade targeting. This restored the old N-pass architecture (reverted the one-pass latency optimization that removed per-entity depth); parallel execution keeps wall clock ≈ a single pass.

**MANDATORY per-entity resolution.** For each entity, resolve the full Step 0.55 stack (X handle, subreddits, GitHub user/repos, news context). Then assemble a `--competitors-plan` JSON mapping each entity to its targeting, and invoke the engine ONCE with the vs-topic string.

**Output shape per run:**
- For `--emit=compact` / `--emit=md`, there is no separate merged Markdown raw file. The main topic saves to `{main-slug}-raw.md`; each peer saves to `{peer-slug}-raw.md`.
- For `--emit=html`, the main saved artifact is the merged comparison HTML at `{main-slug}-vs-{peer-slug}-raw-html[...].html`; each peer may also save its own per-entity HTML artifact.
- The engine logs every written file as `[last30days] Saved output to {path}` and, for comparison runs, follows with `[last30days] Comparison artifact set: main={path}; peers={path, ...}`. Treat that log line as authoritative instead of recomputing paths from slugs.
- Stdout shows a merged comparison with the `## Head-to-Head` scaffold + per-entity Resolved Entities block.

**Invocation:**
```bash
# SKILL_DIR = absolute path of the directory containing THIS SKILL.md you just Read.
# Substitute the actual path below — your harness told you where this file lives via
# the Read tool result. Examples:
#   Read ~/.claude/skills/last30days/SKILL.md      → SKILL_DIR=$HOME/.claude/skills/last30days
#   Read ~/.codex/skills/last30days/SKILL.md       → SKILL_DIR=$HOME/.codex/skills/last30days
#   Read ~/.claude/plugins/cache/last30days-skill/last30days/3.11.0/skills/last30days/SKILL.md
#     → SKILL_DIR=$HOME/.claude/plugins/cache/last30days-skill/last30days/3.11.0/skills/last30days
# scripts/last30days.py is always a direct child of SKILL_DIR (every install layout
# packages SKILL.md and scripts/ as siblings).
SKILL_DIR="<absolute path of the directory containing the SKILL.md you Read>"

if [ ! -f "$SKILL_DIR/scripts/last30days.py" ]; then
  echo "ERROR: scripts/last30days.py not found under SKILL_DIR=$SKILL_DIR" >&2
  echo "Re-check the directory of the SKILL.md you Read and substitute it as SKILL_DIR above." >&2
  exit 1
fi

# Write the per-entity plan to a tmpfile and pass the path to the engine.
# The engine's parse_competitors_plan() reads file paths transparently. This
# avoids the inline-single-quoted-JSON apostrophe trap (resolved context
# strings like "people's choice" or "McDonald's" otherwise close the outer
# single-quote and break shell parsing before the engine is even invoked).
# Trailing XXXXXX (no .json suffix) so BSD/macOS mktemp works the same as
# GNU; BSD only substitutes X's at the end of the template.
COMPETITORS_PLAN_FILE=$(mktemp "${TMPDIR:-/tmp}/last30days-competitors.XXXXXX")
trap 'rm -f "$COMPETITORS_PLAN_FILE"' EXIT
# >| not >: mktemp already created the file, so a plain > is refused under
# `set -o noclobber` (leaving the plan empty -> deterministic fallback).
cat >| "$COMPETITORS_PLAN_FILE" <<'PLAN_EOF'
{
  "{TOPIC_B}": {"x_handle":"{TOPIC_B_HANDLE}","subreddits":["{TOPIC_B_SUB_1}","{TOPIC_B_SUB_2}"],"github_user":"{TOPIC_B_GH}","context":"{TOPIC_B_CONTEXT}"},
  "{TOPIC_C}": {"x_handle":"{TOPIC_C_HANDLE}","subreddits":["{TOPIC_C_SUB_1}"],"github_user":"{TOPIC_C_GH}","context":"{TOPIC_C_CONTEXT}"}
}
PLAN_EOF

"${LAST30DAYS_PYTHON}" "${SKILL_DIR}/scripts/last30days.py" "{TOPIC_A} vs {TOPIC_B} vs {TOPIC_C}" \
  --emit=compact \
  --save-dir="${LAST30DAYS_MEMORY_DIR}" \
  --save-suffix=v3 \
  --x-handle={TOPIC_A_HANDLE} \
  --subreddits={TOPIC_A_SUBS} \
  --competitors-plan "$COMPETITORS_PLAN_FILE"
```

**Keep the heredoc marker quoted as `'PLAN_EOF'`.** Quoting suppresses shell interpolation so apostrophes, `$`, backticks, etc. pass through verbatim. If you ever switch to an unquoted `<<PLAN_EOF`, every variable reference and apostrophe inside the JSON becomes a parse hazard.

Topic A (the main topic, first in the vs-string) uses outer `--x-handle`, `--x-related`, `--subreddits`, `--github-user`, `--github-repo`, `--trustpilot-domain`, `--tiktok-*`, `--ig-creators` as usual. Topics B and C get their targeting from `--competitors-plan` entries (keyed by entity name, case-insensitive) — the engine does NOT read a main-topic entry out of the plan, so the main topic's Trustpilot domain must ride the outer flag.

**Step 0.55 for N entities.** The same pre-research protocol that applies to a single-entity topic applies to EACH entity in a vs-run. For N=3, that means 3 WebSearches for X handles, 3 for subreddits, 3 for GitHub, 3 for news context — or equivalent batched queries. A `## Resolved Entities` block with dashes for any entity means you skipped Step 0.55 for that one. Re-run with a corrected plan.

**Then do WebSearch supplements** for: `{TOPIC_A} vs {TOPIC_B} comparison {YEAR}` and `{TOPIC_A} vs {TOPIC_B} which is better` — these catch rivalry articles that per-entity passes might not surface.

**Use `RESOLVED_POSITIONING` per entity (Step 0.55 item 6) in two ways.** First, ground each entity's `What it is` cell in its CURRENT fetched pitch - describe the entity as it pitches itself today, never from memory. Second, if an entity's month of evidence directly bears on its pitch - SUPPORTS a specific claim, CUTS AGAINST one, or the conversation is squarely ABOUT the pitched ground - say so in ONE prose sentence inside that entity's section of the comparison synthesis (right after the Community Sentiment line - the template marks the slot), anchored to the real item with its engagement. When the pulse is orthogonal to the pitch (on-entity but about something the pitch doesn't speak to), say NOTHING about the pitch: omission is the correct output, and a manufactured connection is worse than silence. Match altitude: test SPECIFIC claims ("zero-config", "fastest", an uptime number) against specific threads; never grade a broad tagline ("financial infrastructure") against an individual thread - it is too broad to hit or miss. Keep claims windowed - "this month's conversation" - never trend verbs like "losing the narrative" that one 30-day window cannot support. If positioning was not actually fetched this run for an entity, skip both uses for that entity - never supply a pitch from memory.

**Skip the normal Step 1 below** - go directly to the comparison synthesis format (see "If QUERY_TYPE = COMPARISON" in the synthesis section).

**COMPARISON TABLE SCAFFOLD (engine-emitted, pass through verbatim):** For comparison topics, the engine's compact output includes a `## Head-to-Head` block with an empty markdown table (columns = entities, rows = axes like "What it is", "Philosophy", "Best for"). Your synthesis MUST include this block verbatim with filled cells, positioned between the narrative and the emoji-tree footer. Keep each cell to 5-15 words. Use ' - ' (hyphen with spaces) not em-dashes inside cells.

### Competitor mode (`--competitors`)

`--competitors` is a SKILL.md-level shortcut for vs-mode with auto-discovery. The engine flag itself just signals intent; YOU (the hosting reasoning model) do the discovery and Step 0.55 via your own WebSearch tool, then invoke the vs-topic path above.

**The four-step protocol:**
1. **Discover peers** via WebSearch: `"{topic} competitors"` / `"{topic} alternatives"`. Pick N=2 by default (match the flag's default), N=argument value if the user passed `--competitors=N`.
2. **Run Step 0.55 for the main topic AND each peer** — same protocol you use for a single-entity topic, just N times. X handle, subreddits, GitHub, news context, per entity.
3. **Build the vs-topic string**: `"{main} vs {peer1} vs {peer2}"`.
4. **Invoke the engine** with the vs-topic, `--competitors-plan` JSON covering both peers (and the main topic if you want to override the outer flags), and the outer `--x-handle`/`--subreddits`/`--github-*` for the main topic.

**Flag surface (engine):**
- `--competitors` (bare) - signals the hosting model to discover 2 peers (3-way total).
- `--competitors=N` - N peers (1..6; out-of-range clamps with stderr warning).
- `--competitors-list="A,B,C"` - minimum escape hatch; names only, no per-entity targeting. Peer sub-runs fall back to planner defaults (visibly thinner data).
- `--competitors-plan '{entity: {x_handle, subreddits, github_user, github_repos, trustpilot_domain, context}}'` - full per-entity targeting; implies vs-mode; preferred.
- `--polymarket-keywords "kw1,kw2"` - disambiguate Polymarket for ambiguous single-token topics ("Warriors" → `nba,gsw,golden-state`).
- `--hiring-signals` - deep-dive into public jobs/careers evidence for company focus signals. Use signal language only: leaning into, investing in, increasing focus, priority shift. Do NOT claim exact roadmap predictions from job postings.

**Why --competitors-plan over --competitors-list:** without per-entity handles/subs, peer sub-runs run with deterministic single-word planner queries and produce visibly thinner evidence than the main topic. The Resolved Entities block in stdout makes the gap visible — dashes for a peer = you skipped its Step 0.55.

**Engine-internal auto-resolve (headless fallback):** if the engine detects BRAVE_API_KEY / EXA_API_KEY / SERPER_API_KEY / PARALLEL_API_KEY / PERPLEXITY_API_KEY / OPENROUTER_API_KEY, it runs its own per-entity `resolve.auto_resolve()` before each sub-run. The hosting-model path does NOT need those keys — you are the WebSearch. The engine's auto-resolve is the cron/CI fallback for when no reasoning model is driving.

**Output:** for Markdown/compact runs, one `{slug}-raw.md` per entity in `--save-dir` plus the merged comparison on stdout. For HTML runs, the main saved artifact is merged comparison HTML and peer artifacts remain per-entity. Always use the `[last30days] Comparison artifact set: main=...; peers=...` log line as the source of truth. Synthesis contract identical to the vs-mode protocol above.

### Hiring Signals mode (`--hiring-signals`)

Use `--hiring-signals` when the user asks what a company's jobs page, careers page, LinkedIn jobs, or competitor hiring suggests about strategic focus. This is strongest for early-stage startups and weaker for large companies, where many unrelated roles are hiring noise.

**Hit the company's OWN job board - that is the entire point.** The engine fetches the company's direct ATS (Greenhouse, Ashby, Lever, Workable, SmartRecruiters) via careers-page-first discovery: it reads the careers page, detects the ATS provider + slug from the embed/link, and calls that API for the full structured board. Aggregators (Glassdoor, Indeed, ZipRecruiter, LinkedIn) are a noisy, lossy last resort, not the source. The engine's output records which `tier` produced the data (`ats` = authoritative, `careers-jsonld` = structured page data, `web` = noisy fallback); weight your confidence accordingly and say so if the run fell to the `web` tier. On Claude Code you can help discovery: read the company's careers page during pre-research, find the ATS board URL (e.g. `jobs.ashbyhq.com/{slug}`), and the engine will resolve the rest.

**Weight by novelty and departure-from-baseline, not raw role count.** A single strategic role can outweigh a department's worth of headcount. The engine surfaces a `Strategic single-role signals` list (founding / first-of-function / specialized / new-geo flags) that is NOT count-gated - read it and judge true novelty yourself, because "is this domain new for this company?" needs world knowledge a keyword map cannot encode. Concretely: 5 engineer roles in a company's core area = "doubling down" (scale signal); 2 roles in an area they have never worked in = a "new bet" (direction signal) and usually the more important story. A `Founding {Role}, {New Capability}` posting (e.g. "Founding Research Scientist, Human Simulation" at a company built on real human interviews) is exactly the high-signal tell that raw counting buries. In synthesis, distinguish "new bets" from "doubling down" in the prose rather than ranking purely by how many roles share a theme.

**Output title for a scoped `--hiring-signals` report.** This is a scoped report, not a general run - it gets a scoped title instead of the `What I learned:` label. Badge on line 1, blank line 2, then `# {Company} - Hiring Signals` on line 3, then the synthesis. Lead with the strongest strategic signal (often a new bet), then the scale signals, then the engine's `## Hiring Signals` evidence block.

**`--hiring-signals` is jobs-scoped - do not build a multi-source plan for it.** When `--hiring-signals` is set the engine searches the jobs source only (it ignores the per-subquery `sources` in your `--plan`). So for a pure hiring-signals run, skip the Step 0.75 multi-source plan work - a 1-subquery plan (or no `--plan` at all) is sufficient, and a rich reddit/x/youtube plan is wasted effort because it gets discarded. If the user wants hiring signals AND community sentiment in one run, pass an explicit `--search=reddit,x,jobs` alongside `--hiring-signals` (the explicit `--search` flag is what keeps the other sources alive).

The output must distinguish evidence from interpretation. Good: "3 current roles mention SSO, SOC 2, and procurement workflows, which signals increased enterprise-readiness focus." Bad: "They will ship enterprise SSO next quarter." In standard `/last30days Company` runs, include Hiring Signals only when the engine surfaces a strong signal; otherwise omit the topic entirely.

---

## Step 0.55: Pre-Research Intelligence (resolve communities + handles)

> **PLATFORM GATE:** If your platform does NOT support WebSearch (e.g., OpenClaw, raw CLI), **skip Steps 0.55 and 0.75** but add `--auto-resolve` to the Python command in the Research Execution section. The engine will do its own pre-research using configured web search backends (Brave, Exa, or Serper) to discover subreddits, X handles, and current events context before planning.

**MANDATORY on Claude Code (and any platform with WebSearch).** You MUST perform Step 0.55 before calling the Python engine. Skipping this step is the second-most-common failure mode of this skill, right after skipping the engine entirely. If your Bash call to `last30days.py` does NOT include a `--plan` flag with resolved handles and subreddits, that is a Step 0.55 skip and a failure. The engine's `[Resolve] No web search backend available, skipping resolve` log line means you, the model, did not do your job - it does NOT mean "the engine will handle it." Treat this step as non-skippable. Repeat invocations on the same topic still re-run Step 0.55 because Reddit/X/TikTok handles for breaking-news topics change week to week.

**Run 2-3 focused WebSearches (in parallel) to resolve platform-specific targeting. Do NOT search for every platform individually - that wastes time. Instead, use your knowledge of the topic to infer most targeting, and only WebSearch for what you can't infer.**

**1. X handles** - Already resolved in Step 0.5 above (including company handles and commentators). Reference your `RESOLVED_HANDLE` and `RESOLVED_RELATED` from that step.

**2. Reddit communities + YouTube channels + current events** - Run 1-2 searches that cover multiple platforms at once:

```
WebSearch("{TOPIC} subreddit reddit community")
WebSearch("{TOPIC} news {CURRENT_MONTH} {CURRENT_YEAR}")
```

The first search finds subreddits. The second gives you current events context (which helps you generate better subqueries in Step 0.75) and may surface YouTube channels or creators organically.

Extract 3-5 subreddit names from the results. Store as `RESOLVED_SUBREDDITS` (comma-separated, no r/ prefix).

**Dedicated vs broad subreddits.** Split the resolved subs into two buckets:
- **Dedicated** = subreddits whose entire purpose IS the topic (the entity's home: `r/Kanye` / `r/WestSubEver` / `r/GoodAssSub` for "Kanye West", `r/OpenClaw` for OpenClaw). Every post there is on-topic. Store as `RESOLVED_DEDICATED_SUBREDDITS` and pass via `--dedicated-subreddits`. The engine pulls these in full (top+hot+new) and skips the relevance floor for them, so an on-topic post whose title lacks the entity name (a "BULLY Deluxe" thread in r/Kanye) is not dropped.
- **Broad** = mixed-content communities where the topic is only sometimes discussed (`r/hiphopheads`, `r/Music`, category peers from 2a). Store as `RESOLVED_SUBREDDITS` and pass via `--subreddits`. These stay relevance-floored.
Label conservatively: only a sub clearly named for / dedicated to the entity goes in the dedicated bucket. Most topics have 0-3 dedicated subs (people and products often have one; generic concepts have none). When unsure, treat it as broad.

**2a. Category-peer expansion (MANDATORY for product topics).** If the topic is a product in a recognizable category (AI image generation, AI video generation, AI coding agents, AI music, AI chat models, SaaS screen recording, prediction markets, etc.), the brand-specific subreddits that WebSearch returned are INSUFFICIENT. Add 2-3 peer subreddits from the category. Peer subs are where cross-product technique discussion actually lives. Missing them is the 2026-04-22 `GPT Image 2` failure mode: the model resolved `r/OpenAI, r/ChatGPT, r/singularity, r/ChatGPTpromptengineering` (all OpenAI-brand) and missed `r/StableDiffusion, r/midjourney, r/dalle2, r/aiArt` where prompting techniques are actually shared. The user had to manually prompt "check image generation reddits too" to get a usable run.

Canonical category peers (single source of truth; `scripts/lib/categories.py` mirrors this for the `--auto-resolve` engine path):

| Category | Trigger keywords | Peer subs (priority order) |
|----------|------------------|---------------------------|
| `ai_image_generation` | image generation, text to image, GPT Image, Nano Banana, Midjourney, Stable Diffusion, DALL-E, Flux.1, Imagen, Seedance, Ideogram, Recraft | `StableDiffusion, midjourney, dalle2, aiArt, PromptEngineering, MediaSynthesis` |
| `ai_video_generation` | video generation, text to video, Sora, Veo 3, Runway Gen, Kling, Pika Labs, Luma Dream Machine, Hailuo | `aivideo, StableDiffusion, runwayml, singularity, MediaSynthesis` |
| `ai_music_generation` | music generation, ai music, Suno, Udio, Riffusion, Stable Audio | `SunoAI, udiomusic, aimusic, artificial` |
| `ai_coding_agent` | Claude Code, Cursor IDE, GitHub Copilot, Windsurf, Aider, Cline, OpenClaw, Hermes Agent, Continue.dev, Codeium, Devin | `ChatGPTCoding, LocalLLaMA, singularity, PromptEngineering` |
| `ai_agent_framework` | agent framework, LangChain, LangGraph, CrewAI, AutoGen, LlamaIndex, DSPy, smolagents | `LangChain, LocalLLaMA, AI_Agents, MachineLearning` |
| `ai_chat_model` | GPT-5/4, Claude Opus/Sonnet/Haiku, Gemini Pro/Flash, Llama 3/4, DeepSeek, Qwen, Mistral Large, Grok | `LocalLLaMA, ChatGPT, ClaudeAI, singularity, artificial` |
| `saas_screen_recording` | screen recording, screen recorder, Loom video, Tella screen, Vidyard | `SaaS, screenrecording, productivity, Entrepreneur` |
| `saas_productivity` | Notion app, Obsidian, Linear app, Asana, ClickUp, productivity app | `productivity, SaaS, ObsidianMD, Notion` |
| `prediction_markets` | Polymarket, Kalshi, prediction market, event contracts, Manifold Markets | `Polymarket, Kalshi, predictionmarkets` |
| `crypto_defi` | DeFi protocol, yield farming, liquidity pool, stablecoin, layer 2, L2 rollup | `defi, ethfinance, CryptoCurrency, ethereum` |

**Merging rule.** Start with WebSearch-returned subs. Append 2-3 category peers in the priority order shown. Dedupe case-insensitively (don't list `midjourney` twice if WebSearch already returned it). Cap total at 10: if adding all peers would exceed the cap, keep every WebSearch-returned sub (they are the freshest signal) and drop peers from the end of the priority list.

**Extrapolation.** If the topic is a product in a category NOT listed in the table (new AI tool, niche SaaS), use the same spirit: pick the 2-3 most active cross-product communities where technique discussion happens. A new image-gen tool still gets `r/StableDiffusion, r/midjourney, r/aiArt`. A new code editor still gets `r/ChatGPTCoding, r/LocalLLaMA`.

**Worked example — the failing query.** Topic: `Prompting GPT Image 2`.

Before (the 2026-04-22 failure mode):
```
Resolved:
- Reddit: r/OpenAI, r/ChatGPT, r/singularity, r/ChatGPTpromptengineering, r/artificial
```

After (with category-peer expansion):
```
Resolved:
- Reddit: r/OpenAI, r/ChatGPT, r/singularity, r/ChatGPTpromptengineering, r/StableDiffusion, r/midjourney, r/dalle2, r/aiArt (+ ai_image_generation peers)
```

The parenthetical `(+ ai_image_generation peers)` is the observable contract of the new Resolved block format. See Step 0.55 self-check below.

**3. TikTok hashtags + creators** - **INFER these from your topic knowledge. Do NOT WebSearch for "{PERSON} TikTok account" - most people/CEOs don't have TikTok, and the search is wasted.**

- **Hashtags:** Infer 2-3 from the topic name + category. Examples: "Kanye West" → `kanyewest,ye,bully`. "Claude Code" → `claudecode,aiagent,aicoding`. "Sam Altman" → `samaltman,openai,chatgpt`.
- **Creators:** Only search if the topic is a content creator, influencer, or brand that likely has TikTok presence. For CEOs, politicians, and non-creator people: skip.

Store as `RESOLVED_HASHTAGS` and `RESOLVED_TIKTOK_CREATORS`.

**4. Instagram creators** - **Same rule: INFER from topic knowledge.** If the topic is a celebrity, brand, or creator with obvious Instagram presence, use their handle directly. If the topic is a tech CEO or abstract concept, skip. Do NOT waste a WebSearch on "Dario Amodei Instagram account."

Store as `RESOLVED_IG_CREATORS`.

**5. YouTube content queries** - Infer 2-3 YouTube content-type queries from the topic without searching. The current events search (#2 above) may surface relevant YouTube channels.

- **For music artists:** `'{TOPIC} album review'`, `'{TOPIC} reaction'`
- **For products/SaaS:** `'{TOPIC} review'`, `'{TOPIC} tutorial'`
- **For comparisons:** `'{TOPIC_A} vs {TOPIC_B}'`
- **For people in the news:** `'{TOPIC} interview {YEAR}'`, `'{TOPIC} latest news'`

Store as `RESOLVED_YT_QUERIES`.

**6. First-party positioning** - **MANDATORY when WebSearch is available, for company / product / service topics.** If the topic (or, in a vs-run, an entity) is a company, product, or service with a public presence, fetch its CURRENT stated positioning. Do **NOT** rely on memory - homepages and positioning go stale as companies rewrite copy and pivot, and a stale claim produces a false gap. Anchor on first-party sources: the homepage tagline, docs, pricing, or a "compare/why-us" page. Fold this into the per-entity passes above where you can (e.g. add `official site` to a query); otherwise run one focused search per entity (`{TOPIC} official site`, `{TOPIC} pricing`). Capture the one-line value prop and any explicit claims ("zero-config", "fastest", "open source"). Store as `RESOLVED_POSITIONING`. This is what the entity *pitches*; the engine's community data is what people *actually talk about*. Use it three ways: ground `What it is` descriptions (describe the entity as it pitches itself TODAY, not as remembered), help reject unrelated brand-name noise (knowing what the entity is makes off-brand matches obvious), and feed the pitch-vs-pulse synthesis beat - a PROSE note that fires only when the month's evidence directly supports, cuts against, or is squarely about the pitch (see the synthesis section; orthogonal evidence gets silence, not a verdict). Skip (and omit `RESOLVED_POSITIONING`) for people, events, abstract concepts, and ownerless topics - they make no comparable public claim. The test is an identifiable first party with a fetchable pitch, and people NEVER pass it - not even founders/creators whose companies would qualify. The lens can apply to MrBeast (a company) but never to Jimmy Donaldson (a person); a person-vs-person run ("Garry Tan vs Sam Altman") gets no positioning research at all. Ownerless topics fail the same test: Bitcoin has no authoritative first party, and a foundation or fan site does not count.

**Concrete examples:**

| Topic | WebSearches needed | Reddit subs | TikTok hashtags | TikTok creators | IG creators | YT queries |
|-------|-------------------|-------------|-----------------|-----------------|-------------|------------|
| **Kanye West** | 2 (subreddit + BULLY news) | `Kanye,WestSubEver,hiphopheads,Music` | `kanyewest,ye,bully` | (inferred: `kanyewest`) | (inferred: `kanyewest`) | `kanye west bully review,kanye west bully reaction` |
| **Sam Altman vs Dario** | 2 (subreddit + AI CEO news) | `artificial,MachineLearning,OpenAI,ClaudeAI` | `samaltman,openai,anthropic` | (skip - CEOs don't TikTok) | (skip - CEOs don't Reel) | `sam altman interview 2026,dario amodei interview 2026` |
| **Tella** (SaaS) | 2 (subreddit + Tella news) | `SaaS,Entrepreneur,screenrecording,productivity` | `tella,tellaapp,screenrecording` | (search: `tella screen recorder TikTok`) | (inferred: `tella.tv`) | `tella screen recorder review,tella tutorial` |

**For comparison queries ("X vs Y" or "X vs Y vs Z") - MANDATORY per-entity resolution:**

For each entity in the comparison, resolve all four lookup types. For a 3-way comparison that is up to 12 lookups (3 entities x 4 types). Batch them into 3-4 WebSearch calls by combining entities per query - do NOT fire one search per entity per type (that produces 12 searches and burns 90 seconds).

Per-entity lookup types to resolve:

1. **Project X handle** - the project's official or primary X/Twitter account
2. **Project GitHub repo** - `owner/repo` format (e.g., `openai/openai-python`)
3. **Founder/maintainer X handle** - the person or team behind the project
4. **Relevant subreddits** - project-specific subreddits (e.g., `r/openclaw`) AND general-category subreddits (e.g., `r/LocalLLaMA`)
5. **Trustpilot domain** (only when the Trustpilot source is active and the entity is a company/brand/service) - the entity's Trustpilot review-page domain per Step 0.5d; peers carry it as `trustpilot_domain` in their `--competitors-plan` entry, the main topic via the outer `--trustpilot-domain` flag

Example batching for "OpenClaw vs Hermes vs Paperclip":

```
WebSearch("OpenClaw Hermes Paperclip github repos AI coding agent")
WebSearch("OpenClaw Hermes Paperclip founders twitter X handles")
WebSearch("OpenClaw Hermes Paperclip reddit subreddits community")
```

Three searches for 12 lookups. After resolving, display all 12 per-entity in the Resolved block before running the engine:

```
Resolved (comparison):
- OpenClaw: X @openclawai | GitHub openclaw/openclaw | Founder @steipete | Reddit r/openclaw, r/AI_Agents
- Hermes: X @hermesagent | GitHub nousresearch/hermes | Founder @NousResearch | Reddit r/hermesagent, r/LocalLLaMA
- Paperclip: X @paperclipai | GitHub dotta/paperclip | Founder @dotta | Reddit r/OpenClawInstall
```

Passing the resolved block visibly (per-entity, all 4 types each) is the observable check that Step 0.55 happened for this comparison. A Resolved block that only lists 3 project handles with no founders and no GitHub repos is a Step 0.55 regression. This was canonical behavior and must stay canonical.

**For non-comparison queries:** Resolve communities/handles for the single topic. Merging list logic does not apply.

**If you can't infer targeting for a platform, skip that flag -- the Python engine will fall back to keyword search.**

**Step 0.55 self-check: category-peer coverage.** Before emitting the Resolved block, re-read your resolved subreddit list. Does the topic match any category in the Section 2a table (or fit the spirit of one — AI image gen, AI coding, AI music, etc.)? If YES: does your list include AT LEAST 2 peer subs from that category? If NO, widen the list NOW — do not run the engine yet. The observable contract is the `(+ {category_id} peers)` annotation on the Reddit line in the Resolved block. Its absence on a product-in-a-known-category topic is a Step 0.55 regression — the named 2026-04-22 failure mode. Person topics, music artists, news stories, and topics outside any category are exempt; omit the annotation.

**After resolving all handles and communities, display what you found before moving on.** This shows the user that intelligent pre-research happened:

```
Resolved:
- X: @{HANDLE} (+ @{COMPANY}, @{COMMENTATOR})
- Reddit: r/{sub1}, r/{sub2}, r/{sub3}, r/{peer1}, r/{peer2} (+ {category_id} peers)
- TikTok: #{hashtag1}, #{hashtag2}
- YouTube: {query1}, {query2}
- Trustpilot: {domain}
- Positioning: "{one-line stated value prop}" (first-party)
```

Only show lines for platforms where something was resolved. Skip empty lines. On the Reddit line, the trailing `(+ {category_id} peers)` annotation appears when Step 0.55 Section 2a added category-peer subs. Omit the annotation when the topic had no matching category. The `Positioning:` line appears for company / product / service topics (from Step 0.55 item 6); omit it for people, events, abstract concepts, and ownerless topics. The `Trustpilot:` line appears only when Step 0.5d resolved a domain (company/brand topic with the Trustpilot source active). This display replaces the old "Parsed intent" block with something more useful.

---

## Step 0.75: Generate Query Plan (YOU are the planner)

> **PLATFORM GATE:** If you skipped Step 0.55 because WebSearch is unavailable, **also skip this step.** The Python engine will plan internally (enhanced by `--auto-resolve` if a web search backend is configured). Jump to Research Execution.

**If you have WebSearch and reasoning capability, YOU generate the query plan.** The Python script receives your plan via `--plan` and skips its internal planner entirely. This produces better results because you have full context about the topic.

**Generate a JSON query plan for the topic.** Think about:
1. What is the user's intent? (breaking_news, product, comparison, how_to, opinion, prediction, factual, concept)
2. What subqueries would find the best content across different platforms?
3. What related angles should be searched at lower weight?

**Output a JSON plan with this shape:**

```json
{
  "intent": "breaking_news",
  "freshness_mode": "strict_recent",
  "cluster_mode": "story",
  "subqueries": [
    {
      "label": "primary",
      "search_query": "kanye west",
      "ranking_query": "What notable events involving Kanye West happened in the last 30 days?",
      "sources": ["reddit", "x", "hackernews", "youtube", "tiktok", "instagram"],
      "weight": 1.0
    },
    {
      "label": "album",
      "search_query": "kanye west bully album",
      "ranking_query": "How was Kanye West's BULLY album received?",
      "sources": ["youtube", "reddit", "tiktok", "instagram"],
      "weight": 0.8
    },
    {
      "label": "reactions",
      "search_query": "kanye west bully review reaction",
      "ranking_query": "What are the reviews and reactions to Kanye West's BULLY?",
      "sources": ["youtube", "tiktok", "reddit"],
      "weight": 0.6
    }
  ]
}
```

**Rules for your plan:**
- Emit 1 to 4 subqueries (more for complex/multi-faceted topics, fewer for simple ones)
- **CRITICAL: Your PRIMARY subquery MUST include ALL of these sources: reddit, x, youtube, tiktok, instagram, hackernews, polymarket.** Never omit reddit (highest-signal discussion) or youtube (unique transcripts + official content). Secondary subqueries can target specific platforms.
- `search_query` should be concise and keyword-heavy - match how content is TITLED on platforms
- `ranking_query` should read like a natural language question
- **DISAMBIGUATION (mandatory for collision-prone names — the #1 cause of off-topic noise).** Anchor the `search_query` with the disambiguating context you resolved in Step 0.5 / 0.55 — the entity's company, role, or domain — when the topic name (a) is a common word or has non-product meanings ("Loom" = weaving tool, "Tella" = soccer player), OR (b) is a PERSON whose name collides with other public figures or common words. Apply the anchor to **EVERY subquery, not just the primary**, and mirror it in the `ranking_query`. Anchor on a SPECIFIC named entity (a company/product/firm), not a generic domain word. Examples: `"kevin rose digg founder"` not `"kevin rose"` (collides with Kevin Warsh / Leon Rose / Kevin Hart); `"lan xuezhao basis set ventures"` not `"lan xuezhao"` (collides with "Lanzhou" food, cdrama edits); `"trevin chow compound engineering"` not `"trevin chow"` (collides with Trevin Wax / Trevin Brown); `"tella screen recording"` not `"tella"`. The `ranking_query` carries the same anchor: `"ranking_query": "What has Kevin Rose, founder of Digg, been doing in the last 30 days?"`, not a bare `"...Kevin Rose..."`. A bare collision-prone name as a subquery is the named 2026-06-17 failure mode — "Kevin Rose" returned 55 items with ~0 about the actual founder until every subquery was anchored to "Digg founder". When the name is globally unambiguous (Kanye West, Nvidia, Peter Steinberger/OpenClaw), no anchor is needed.
- **For comparison queries**, each subquery should include the product category: "tella screen recorder review" not just "tella review", "loom video tool pricing" not just "loom pricing".
- NEVER include temporal phrases in search_query: no "last 30 days", "recent", month names, year numbers
- NEVER include meta-research phrases: no "news", "updates", "public appearances"
- Preserve exact proper nouns and entity strings from the topic
- For comparison ("X vs Y"): create per-entity subqueries at weight 0.8 + a head-to-head subquery at weight 1.0
- For product queries: route to YouTube (reviews), Reddit (discussions), TikTok (demos)
- For predictions: include Polymarket in sources
- For how_to: prioritize YouTube (tutorials) and Reddit (guides)
- Primary subquery weight = 1.0, secondary = 0.6-0.8, peripheral = 0.3-0.5

**Available sources (include ALL in primary subquery):** reddit, x, youtube, tiktok, instagram, hackernews, polymarket. Optional: bluesky, truthsocial, threads, pinterest, grounding (web search - only if user has Brave/Exa/Serper key), digg (Digg clusters - only if `digg-pp-cli` is on PATH)

**Intent → freshness_mode mapping:**
- breaking_news, prediction → `strict_recent`
- concept, how_to → `evergreen_ok`
- everything else → `balanced_recent`

**Intent → cluster_mode mapping:**
- breaking_news → `story`
- comparison, opinion → `debate`
- prediction → `market`
- how_to → `workflow`
- everything else → `none`

Store your plan as `QUERY_PLAN_JSON` - you'll pass it to the script in the next step.

---

