---
name: paulgraham
description: >-
  Stress-test a startup idea before a month goes into building it. Five frameworks - pressure-
  test, validate-problem, map-competition, first-ten, mvp-2-weeks. Use for "is this idea any
  good", "should we pivot", "who are we competing with". Ends on a verdict: strong, weak, or
  pivot.
version: 1.0.0
user-invocable: true
argument-hint: "[pressure-test|validate-problem|map-competition|first-ten|mvp-2-weeks|all]"
---

# Paul Graham-style startup validation

Five frameworks adapted from Paul Graham's YC evaluation method.
Apply them before spending a month building the wrong thing. Each
framework is a brutal-honesty audit; the goal is not to feel good
about the idea, it's to find the flaws before the market does.

## When to use

- Before starting a new startup or product initiative.
- Mid-build, when considering whether to pivot or push through.
- When auditing an in-flight product for product-market fit.
- When a new contributor is asked "why does this business work?" and
  can't answer crisply.

## How to use

The skill accepts one argument:

- `pressure-test` - Framework 1 only
- `validate-problem` - Framework 2 only
- `map-competition` - Framework 3 only
- `first-ten` - Framework 4 only
- `mvp-2-weeks` - Framework 5 only
- `all` or no argument - Run all five in sequence

For each framework the skill:
1. Asks for the startup idea + target customer if not already in context.
2. Runs the framework's role / task / steps / rules.
3. Returns the specified output format.

## The shared procedure

1. Get the idea and the target customer once. If either is missing, ask - one
   question, then proceed.
2. Run the named framework's five moves.
3. Return its output sections, in order, and nothing else.

Across all five: every flaw is specific to this idea, because generic startup advice
is the tell that you did not engage with it. Verdicts are direct - strong, weak, or
pivot, never "it has potential but." Rank by what kills the company soonest. Don't pad
to a number. Every assumption you surface has to be testable before anything gets
built.

**Verdict anchors.** STRONG = the core assumption is testable in two weeks or less
AND a named early adopter is currently paying money or hours for a workaround AND it
reads as a painkiller. WEAK = testable, but the early-adopter evidence is hypothetical,
or it leans vitamin, or the differentiation is only a price or quality claim. PIVOT =
untestable before building, OR a fatal flaw with no mitigation, OR no concrete answer
to "why would they switch from what they do today."

---

## The five frameworks

| # | Name | The five moves | Output sections |
|---|---|---|---|
| 1 | `pressure-test` | core assumption -> most likely failures, ranked -> real pain or nice-to-have -> founder-market fit -> verdict | Core Assumption / Fatal Flaws / Problem Validation / Founder-Market / Brutal Verdict |
| 2 | `validate-problem` | the specific pain and when it hits -> who feels it most acutely (a person, not a demographic) -> 5 discovery questions about past behavior, never hypothetical intent -> validation criteria -> vitamin or painkiller | Specific Pain / Early Adopter / 5 Questions / Validation Criteria / Vitamin-or-Painkiller |
| 3 | `map-competition` | what they do today -> direct -> indirect -> the real enemy (the habit) -> genuine differentiation | Current Behavior / Direct / Indirect / Real Enemy / Differentiation |
| 4 | `first-ten` | where those ten people already are -> manual outreach -> the actual first message -> behavioral success criteria -> week-by-week to ten | Where They Are / Approach / First Message / Success Criteria / Milestones |
| 5 | `mvp-2-weeks` | the single riskiest assumption -> minimum feature set to test it -> what gets cut -> behavioral test criteria -> day-by-day to real users | Core Assumption / Minimum Set / What Gets Cut / Test Criteria / 2-Week Plan |

### Framework-specific deltas

- **3:** "we have no competition" is always wrong - flag it on sight. Current behavior
  is always a competitor, and usually the one that wins.
- **4:** manual only. No ads, no automation. The first message asks for a
  conversation, never a sale.
- **5:** every feature that does not test the core assumption gets cut. The plan ends
  with real users, not internal testing.

---

## Running all five in sequence

When called with `all` or no argument:

1. Ask ONCE for the idea + target customer (use those across all five).
2. Run Framework 1 (Pressure Test). Share verdict.
3. If verdict is "pivot required", STOP. Do not continue. Report that
   the idea needs rethinking before further validation.
4. If verdict is "strong" or "weak", continue with Framework 2
   (Validate Problem).
5. If Framework 2 verdict is "vitamin", STOP. Flag that the business
   is a nice-to-have and further validation will waste effort until
   the problem is reframed.
6. Continue with Framework 3 (Map Competition).
7. Run Framework 4 (First 10) and Framework 5 (MVP).
8. Deliver a consolidated summary:

```
## Consolidated verdict

- Pressure test: {strong | weak | pivot}
- Problem type: {painkiller | vitamin}
- Real enemy: {current behavior or direct competitor to replace}
- First 10 path: {specific channel + week-1 action}
- MVP test: {single assumption + behavioral success criterion}

## Go / no-go: {GO | PAUSE | PIVOT}

## If GO, next 7 days:
1. {action}
2. {action}
3. {action}

## If PAUSE, what to fix first:
{specific missing evidence}

## If PIVOT, suggested reframing:
{one-sentence new direction}
```

---

## What this skill will NOT do

- Write the product. This is validation, not construction.
- Recommend a tech stack. Orthogonal to PMF.
- Design the UI. Use `/design` for that.
- Raise money for you. PG can pressure-test your YC application, this
  skill tries to keep you from wasting a month. It is not a VC.

## When NOT to use

- Post-launch when you already have 100 paying customers. You've
  validated. Go operate.
- Consulting engagements where the product is already defined and
  your job is just to build.
- Problems where the "business" is actually an open-source side
  project or a personal tool. PMF isn't the right frame.
