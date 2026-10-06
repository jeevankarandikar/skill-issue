# writing-guard

A Claude Code hook that blocks machine-sounding prose before it lands. The rules are in [RULES.md](RULES.md). The guard enforces the ones a pattern can catch, in prose files as they are written and in chat replies before they are sent.

It is one Python file with no dependencies. It reads no paths of its own and writes nothing.

## How it behaves

- On a Write or Edit to a prose file that breaks a rule, the tool call is refused and the model gets the offending snippet back, so it rewrites and tries again.
- On a reply that breaks a rule, the stop is refused once with the snippet. The second attempt always goes through, so a reply that has to discuss a banned phrase cannot loop.
- An Edit is judged on what it adds. A file that already holds an em dash can still be edited, as long as the edit does not add another.
- A malformed hook event is allowed through.

## Exemptions

Files that must quote what the rules ban, such as a style guide, are skipped when their path contains a fragment listed in `WRITING_GUARD_EXEMPT`. Separate fragments with colons and set the variable in the `env` block of `~/.claude/settings.json`:

```json
"WRITING_GUARD_EXEMPT": "/docs/style-guide.md:/quotes/"
```

This folder is always exempt.

## Check it

```bash
python3 writing_guard.py --selftest
```

Install steps are in [SETUP.md](../SETUP.md).
