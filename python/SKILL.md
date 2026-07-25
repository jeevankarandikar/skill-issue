---
name: python
description: Python conventions for this user's repos - uv-managed projects, the script-oriented layout he actually uses, ruff, and the FastAPI service shape he ships. Use when starting a Python project, when the layout or toolchain is undecided, or when reviewing Python against his conventions rather than against PEP 8 in the abstract. Invoke with `fastapi` for the service patterns - app factory, schemas, DI, async routes, test overrides, security. Generic idiom and style review belongs to the python-reviewer agent, not here.
version: 3.0.0
user-invocable: true
argument-hint: "[fastapi]"
---

# Python

This file holds only what is specific to these repos. General Python idiom - EAFP,
comprehensions, dataclasses, decorators, `__slots__`, mutable default arguments - used
to live here and was cut: enumerating what the model already knows costs context on
every load and quietly narrows the search space to the listed items.

## What a project should look like

uv, always: `pyproject.toml` + `uv.lock`, `uv run` to execute, `uv add` to add. Not
pip, not poetry, not a bare venv, and never a `requirements.txt` in a new repo.

Layout follows the work, not a template. Data and AI tooling here is script-oriented -
top-level `build_*.py`, `embed.py`, `query.py`, `server.py` sitting next to one
package directory. `src/` layout is for something published to PyPI; using it for a
personal tool adds a directory level that buys nothing. Match whatever the repo
already does over either of these.

## The stack actually reached for

- Services: FastAPI + uvicorn.
- Storage: SQLite with `sqlite-vec` and FTS5 before reaching for Postgres. The
  single-file database is a feature on a personal machine, not a compromise.
- HTTP: `httpx`, not `requests`.
- Embeddings and local inference: `sentence-transformers`, `ollama`, `mlx-lm` on
  Apple silicon. Local-first by default - this runs on a daily-use laptop, so don't
  assume a spare GPU or an always-on API budget.
- Multi-provider LLM work: `anthropic` + `openai` + `google-generativeai`,
  `jsonlines`, `python-dotenv`, YAML configs.

Check what is already installed before adding anything. A dependency is permanent code
you don't control.

## Tooling and tests

`ruff` for lint and format. `mypy` where the types earn it, not everywhere.

`pytest` for domain logic. For anything model-shaped, an eval harness rather than unit
tests - a pass/fail assertion on a generated string measures the wrong thing. See the
`test` skill. Research and one-off analysis code is normally untested and that is
fine; don't manufacture scaffolding there unless asked.

## The one review check worth making every time

Every `except` retries, degrades, or re-raises with context. `except: pass` and
`except Exception: log; continue` hide the failure instead of handling it, and they
are how a Python bug becomes undiagnosable. This is the rule that gets broken.

## FastAPI

Service patterns - app factory, Pydantic schemas, dependency injection, async routes,
test dependency overrides, auth and CORS: reference/fastapi.md - read when running
`/python fastapi`.
