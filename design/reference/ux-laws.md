# UX Laws

Cognitive and interaction laws that should inform the Shape phase and the critique. Not trivia — each one forces a concrete design decision. Cite the law when you make the call (it's a named prior; see also [design-priors.md](design-priors.md)).

## The Laws That Earn Their Keep

| Law | What it means | The decision it forces |
|---|---|---|
| **Hick's Law** | Decision time grows with the number and complexity of choices. | Cap primary nav/CTAs; progressive-disclose advanced options. Don't show 8 where 3 will do. |
| **Fitts's Law** | Time-to-target depends on its distance and size. | Primary action large and near where the eye lands. Min 44×44pt targets. Don't strand the CTA in a corner. |
| **Jakob's Law** | Users expect your site to work like the others they know. | Keep interaction conventions (logo top-left, cart top-right). Be visually distinct, not behaviorally surprising. |
| **Miller's Law** | Working memory holds ~7±2 items. | Chunk into ≤7 groups; group long lists/menus before they overflow. |
| **Tesler's Law** | Every system has irreducible complexity — someone absorbs it. | Decide *who*: push it onto the system (smart defaults), not the user. |
| **Doherty Threshold** | Productivity soars when response is <400ms. | Every interaction responds <400ms; skeletons + optimistic UI to stay under it. |
| **Peak-End Rule** | People judge an experience by its peak and its end. | Spend the signature-detail budget at the emotional peak; design the success/end state deliberately. |
| **Aesthetic-Usability Effect** | Pretty designs are *perceived* as more usable. | Polish earns trust — but pair it with real usability checks so it doesn't mask friction. |
| **Von Restorff (Isolation)** | The thing that differs is the thing remembered. | One visually distinct primary CTA per view; don't dilute with competing emphasis. |
| **Serial Position** | First and last items are best remembered. | Put the most important nav/list items first and last. |
| **Goal-Gradient** | Motivation rises near the goal. | Show progress (steppers, % complete) to pull users through multi-step flows. |
| **Law of Proximity** | Near things read as grouped. | Carry grouping with spacing before reaching for borders. |
| **Law of Common Region** | A shared bounded area reads as a group. | Use a card/container only when proximity alone is ambiguous. |
| **Law of Similarity** | Similar-looking elements read as related. | Style same-function elements identically (all primary buttons match). |
| **Postel's Law** | Be liberal in what you accept, conservative in what you send. | Forgiving inputs (accept messy formats, autoformat); precise, predictable output states. |
| **Prägnanz** | The eye resolves complexity to the simplest form. | Favor simple, regular layouts; cut visual noise. |

Secondary (reach for when relevant): Choice Overload, Zeigarnik Effect, Flow, Occam's Razor, Pareto Principle, Law of Uniform Connectedness.

---

**Avoid**: citing a law as decoration without applying it · using "Jakob's Law" to justify a generic, undifferentiated *look* (it governs interaction conventions, not visual sameness) · optimizing one law in isolation — they trade off (Hick's restraint vs Miller's chunking vs the brief). Source: lawsofux.com (Jon Yablonski).
