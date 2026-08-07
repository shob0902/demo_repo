# Demo repo: toy Flask signup endpoint

This is the small, real repo used to demo the agent swarm end-to-end
(Build Order step 10 in the project brief). It's intentionally tiny: one
route with a real bug and a test suite that already encodes the fix.

`POST /signup` currently accepts any payload -- no email format check, no
required-password check. Two of the three tests in `test_app.py` fail
against the current `app.py`.

## Demo task

Submit this task against this repo's path from the Agent Swarm UI:

> **Description:** Add input validation to the /signup endpoint: reject
> requests with an invalid email format or a missing password with a 400
> response.
>
> **Repo path:** the absolute path to this `demo_repo` folder.

Expected result: the pipeline runs Planner → Coder → Tester (retrying up
to `MAX_TEST_RETRIES` times if the first attempt doesn't pass) → Reviewer,
and finishes `done` with all three tests in `test_app.py` passing.

## Running the tests yourself (outside the swarm)

```
pip install -r requirements.txt
python -m pytest -q
```
