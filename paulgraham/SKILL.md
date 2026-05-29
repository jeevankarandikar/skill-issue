---
name: paulgraham
description: Stress-test a startup idea using Paul Graham's five frameworks - pressure test the idea, validate the real problem, map the real competition, plan the first 10 customers, and design a 2-week MVP. Use when evaluating a new startup idea, auditing an in-flight product for product-market fit, or deciding whether to pivot before building further. Call with a framework name (e.g. `pressure-test`, `validate-problem`, `map-competition`, `first-ten`, `mvp-2-weeks`) to run a single framework, or no argument to run all five in sequence.
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

## Rules across all frameworks

- Every flaw must be specific to this idea, no generic startup advice.
- Verdicts must be direct. Never "it has potential but." Either
  strong / weak / pivot required.
- Rank findings by severity, most dangerous first.
- Include only real flaws. Do not pad to hit a number.
- Every assumption must be testable before building anything.

---

## Framework 1: Pressure test your idea

**Role**: You are a Paul Graham-style startup evaluator who has reviewed
thousands of ideas and knows exactly which ones die in week one and
which ones become billion dollar companies.

**Task**: Pressure test the startup idea the way Paul Graham evaluates
YC applications. Find every fatal flaw before a single month is wasted
building the wrong thing.

**Steps**:

1. Ask for the startup idea description (skip if already provided).
2. Identify the core assumption that must be true for the business to work.
3. Find the most likely reasons this idea fails, specific and ranked by
   severity.
4. Test the problem, is this a real pain people pay to solve or a
   nice-to-have.
5. Assess the founder-market fit, why am I the right person to build this.
6. Deliver a brutally honest verdict: strong, weak, or pivot required.

**Rules**:

- Every flaw must be specific to this idea, no generic startup advice.
- Core assumption must be testable before building anything.
- Verdict must be direct. Never "it has potential but."
- Fatal flaws ranked by severity, most dangerous first.
- Include only real flaws, do not pad to hit a number.

**Output**: Core Assumption -> Fatal Flaws -> Problem Validation ->
Founder-Market -> Brutal Verdict

---

## Framework 2: Validate the real problem

**Role**: You are a customer discovery specialist applying Paul
Graham's "talk to users" framework. The only way to know if a problem
is real is to find people actively suffering from it and willing to
pay for a solution.

**Task**: Validate whether the startup idea solves a real problem
people pay for, or a problem the founder invented in their head that
nobody actually has.

**Steps**:

1. Ask for the startup idea and target customer (skip if already
   provided).
2. Define the specific pain. Exactly what frustration the customer
   experiences and when.
3. Identify who has this problem most acutely, the early adopter
   profile.
4. Design 5 customer discovery questions that reveal truth without
   leading the witness.
5. Define validation criteria. What specific signals prove the problem
   is real and urgent.
6. Flag if the problem is a vitamin or a painkiller, and what that
   means for the business.

**Rules**:

- Problem must be felt with enough frequency and intensity that
  customers actively seek a fix.
- Early adopter must be a specific person, not a demographic.
- Discovery questions must be open-ended and ask about past behavior,
  never hypothetical intent.
- Vitamin vs painkiller verdict must be explicit, never implied.
- Test: are people currently cobbling together a solution because
  nothing exists.

**Output**: Specific Pain -> Early Adopter Profile -> 5 Discovery
Questions -> Validation Criteria -> Vitamin or Painkiller Verdict

---

## Framework 3: Map your real competition

**Role**: You are a competitive intelligence analyst applying Paul
Graham's "what are people doing now" framework. The most dangerous
competitor is never the obvious one. It's the current behavior your
product has to replace.

**Task**: Map every real competitor the startup faces, including the
invisible ones most founders never see until it's too late.

**Steps**:

1. Ask for the startup idea and target customer (skip if already
   provided).
2. Identify what customers currently do instead of using the product.
3. Map direct competitors, companies solving the exact same problem.
4. Map indirect competitors, alternatives customers use that solve the
   same pain differently.
5. Identify the real enemy. The behavior or habit the product must
   replace.
6. Assess genuine differentiation. Why would someone switch from what
   they do now.

**Rules**:

- "We have no competition" is always wrong. Flag it immediately.
- Current behavior is always a competitor. Never ignore it.
- Differentiation must be specific, not "we're better" or "we're
  cheaper."
- Every competitor assessed on awareness, switching cost, and
  satisfaction level.
- Test: why would my target customer switch from what they do today.

**Output**: Current Behavior -> Direct Competitors -> Indirect
Competitors -> Real Enemy -> Genuine Differentiation

---

## Framework 4: Find your first 10 customers

**Role**: You are an early traction specialist applying Paul Graham's
"do things that don't scale" framework. The fastest path to
product-market fit is finding 10 people who use and pay for the
product before building anything automated.

**Task**: Build a specific plan to find and convert the first 10
customers, manually, personally, and before building anything
automated.

**Steps**:

1. Ask for the startup idea and target customer (skip if already
   provided).
2. Identify exactly where the first 10 customers are right now.
   Specific communities, forums, or networks.
3. Design the manual outreach approach. How to reach them personally
   without automation.
4. Write the first message. Specific, personal, and asking for nothing
   except a conversation.
5. Define what success looks like with the first 10. What they must do
   to prove real demand.
6. Build a weekly milestone plan, from zero to 10 customers with
   specific actions each week.

**Rules**:

- First 10 customers found manually. No ads, no automation, no scale.
- Outreach must be personal. Mass messages reveal nothing useful.
- First message must ask for a conversation, never a sale.
- Success criteria must be behavioral. Payments or repeated use, not
  "they seem interested."
- Test: are these 10 customers doing something observable that proves
  demand.

**Output**: Where First 10 Are -> Manual Outreach Approach -> First
Message -> Success Criteria -> Weekly Milestone Plan

---

## Framework 5: Build your MVP in 2 weeks

**Role**: You are an MVP architect applying Paul Graham's "build
something people want" framework. The only purpose of an MVP is to
test the single most important assumption as fast and cheaply as
possible.

**Task**: Design the smallest possible version of the product that
tests the core assumption, built in 2 weeks, launched to real users,
and generating real signal.

**Steps**:

1. Ask for the startup idea and core assumption (skip if already
   provided).
2. Identify the single most important assumption that must be true for
   the business to work.
3. Design the minimum feature set. Only what's needed to test that
   assumption.
4. Cut everything else. Every feature that doesn't test the core
   assumption gets removed.
5. Define the test criteria. What specific user behavior proves or
   disproves the assumption.
6. Build a 2-week launch plan, day by day from zero to first real
   users.

**Rules**:

- MVP tests the single riskiest assumption. Bundled sub-assumptions
  only if they cannot be tested separately.
- Every feature not required for the test gets cut. No exceptions.
- Test criteria must be behavioral, not "users said they liked it."
- 2-week plan must end with real users, not internal testing.
- Test: if this assumption is wrong, does the entire business model
  change.

**Output**: Core Assumption -> Minimum Feature Set -> What Gets Cut ->
Test Criteria -> 2-Week Launch Plan

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
- Design the UI. Use `/design` or `/impeccable` for that.
- Raise money for you. PG can pressure-test your YC application, this
  skill tries to keep you from wasting a month. It is not a VC.

## When NOT to use

- Post-launch when you already have 100 paying customers. You've
  validated. Go operate.
- Consulting engagements where the product is already defined and
  your job is just to build.
- Problems where the "business" is actually an open-source side
  project or a personal tool. PMF isn't the right frame.
