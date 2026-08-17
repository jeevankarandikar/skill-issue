# global CLAUDE.md

@~/.claude/SOUL.md
@~/.claude/MEMORY.md

<!-- SOUL = how the agent behaves, MEMORY = what it knows about you. Both load
     every session in every project. Details: the universal-memory skill. -->

## routing

- fire the matching skill or command on intent. don't wait for a slash command,
  don't ask permission to use one.
- a command is the front door: when one fires it pulls in what it needs.
- commit, push, and PR wait for an explicit ask. always.
- never review code you just wrote - reviews go to a fresh-context subagent
  briefed with the diff and the requirement only, never your rationale.
