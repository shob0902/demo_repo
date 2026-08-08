# Demo repo: toy Flask signup API

The target repo used to demo the agent swarm end-to-end. Intentionally tiny —
the Coder agent rewrites whole files, so every file here stays small enough to
regenerate inside the provider's output-token budget.

- `app.py` — `POST /signup` (validates email + password) and `GET /users`
- `validators.py` — pure validation helpers, no Flask import
- `test_app.py`, `test_validators.py` — the suite the Tester agent runs

**All tests pass as-is.** That's on purpose: the swarm never pushes its changes
back, so this repo is byte-identical on every run. A failing test here would
stay failing and sink every subsequent demo. Demo tasks are therefore additive
or behaviour-preserving, and "done" means *the change didn't break anything* —
read the diff to check the new behaviour itself.

For the red→green retry-loop demo, use the companion repo with a deliberately
failing suite instead.

## Submitting a task

The swarm takes a **public GitHub URL**, not a local path. Paste this repo's
URL into the dashboard along with a description that **names the file to
change** (e.g. "add a GET /health endpoint to app.py") — the Planner passes
that filename through to the Coder's file selection.

## Running the tests yourself

```
pip install -r requirements.txt
python -m pytest -q
```
