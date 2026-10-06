# Interface text

Load this when writing or reviewing labels, buttons, errors, empty states and alerts. The Writing section of the project's `DESIGN.md` decides voice and capitalization. Where the project follows a platform canon, that canon's writing guidance wins on any conflict.

## Buttons and links

- A button label starts with a verb and names the outcome: "Save changes", "Create account", "Download PDF". "OK", "Submit" and a bare "Yes" say nothing.
- A confirmation repeats the consequence in its button, such as "Delete project" beside "Cancel".
- "Delete" is permanent and "Remove" implies the thing can come back. Use the one that is true.
- Link text describes the destination and makes sense read alone.
- A toggle is labeled with the state it turns on: "Send read receipts".
- Use one word per flow and keep it at every step, either "Continue" or "Next".

## Labels

Check whether the value can carry its own label before adding one.

| Labeled | Folded |
| --- | --- |
| Price: $49 | $49 |
| Due date: Mar 4 | Due Mar 4 |
| Members: 1,204 | 1,204 members |
| In stock: 12 | 12 left in stock |

Keep explicit labels on form fields and table columns.

## Errors

- An error says what happened, why, and how to fix it: "Email address needs an @ symbol", where "Invalid input" helps no one.
- Describe the field's need and leave the person out of it: "Enter a date as MM/DD/YYYY".
- For a failure on the product's side, say so and offer another route.
- No humor in errors. The person is already stuck.

| Situation | Shape |
| --- | --- |
| Wrong format | The field needs this format, with an example |
| Missing | Enter the thing that is missing |
| No permission | You do not have access to this, and what to do about it |
| Network | The product could not reach the service, check the connection and retry |
| Server | Something failed on the product's side, with an alternative |

## Tone and consistency

- Voice stays the same everywhere. Tone shifts with the moment: brief on success, helpful on an error, plain and serious before a destructive action.
- Choose one term for each concept and use it everywhere, such as "Delete", "Settings", "Sign in" and "Create". Keep the list in `DESIGN.md`.
- Address the reader as "you".
- If the heading explains the screen, an introduction under it is redundant. Say a thing once.
- Capitalize buttons, headings and labels the same way throughout.
- Store text in natural case and let the presentation layer change its case.
- Truncated text keeps its full value reachable.

## Access and translation

- Alternative text gives the information an image carries, such as "Revenue rose 40% in the fourth quarter". A decorative image gets empty alternative text.
- An icon-only button has an accessible name that states its action.
- Leave room for growth. German and Finnish run about 30% longer than English.
- Keep each sentence as one whole string, since word order changes between languages. Keep numbers outside the sentence where a language's plural rules would break it.
- Avoid abbreviations, and tell translators where each string appears.

## Sources

Adapted from the UX writing reference of the impeccable skill by Paul Bakaus (github.com/pbakaus/impeccable, Apache 2.0) and Rauno Freiberg's interface guidelines at interfaces.dev.
