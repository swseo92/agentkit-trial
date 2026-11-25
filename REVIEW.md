# Review criteria
- Kind: guideline
- Topic: review
- Readers: review
- Status: adopted

Its reader is the review run (`plugins/dev/devkit/skills/review-run/SKILL.md`, step 3), which reads this file as it stands on the PR's base branch before reading the change. It is the one place for what a review raises and what blocks (user decision 206, 2026-11-19, card 5169); the skill holds the order, the shape of a finding and the verdict file.

## What is raised as a defect
Only what meets all of these:
1. It has a real effect on correctness, operation, security or maintenance.
2. It is one thing and can be fixed (not a complaint about the codebase).
3. This PR made it (a defect that was already there is not raised).
4. The author would fix it on learning of it, and it is not an intended change.
5. Not a guess. To say it reaches another part, show **one concrete path** (which code is affected, and how).

Besides defects, look at:
- Does the change meet the card's goal and done criteria? Find the evidence for each criterion (a test's name, a file).
- Does it touch what is out of scope? Does it change a contract document (`CONTRACT.md`, `ports`) the brief did not ask for?
- **A fence path without the mark**: when the change touches a path listed in `.github/CODEOWNERS` and the PR title does not start with `[fence]`, that is a blocking finding (P1, `contract`).
- **Tests deleted or weakened** (a dropped assertion, a looser expected value): kind `test-weakening`.
- **A replacing PR** (it deletes or rewrites existing test files wholesale): hold the PR body's **table of what the tests kept** against the contract. For each deleted test: the name of the new test that keeps the same thing, or "no longer kept: why" (the contract sentence is gone). Count the deleted tests in the diff against the table's rows. **No table: do not pass** (P1, "no table of what the tests kept"). Counting is the author's work; you check that the table is true. In the same PR: are the declaration's resources (memory, job counts) as before, or is there a measured value for the change?
- Do contract and code disagree? Did the change do what the piece's `AGENTS.md` says it does not do?
- **Does new code assume an OS**: an OS name newly outside an adapter (`fcntl`, `/proc/`, `systemctl`, `killpg`, signals, process groups, file modes)? P1 (root `AGENTS.md`). Only what this PR adds.
- **Does Zuul already do this?** If yes, it goes in Zuul config, not our code (decision 217): new code that rebuilds what the merge line's Zuul already does is a finding (kind `contract`).
- Wrong behaviour: edge cases, what happens on failure, going on where it must stop and reveal.
- **Say everything you saw in the first round.** Do not hold a finding back for a later round.

## What blocks (decision 206)
- **Blocking = a confirmed P0 or P1 with evidence.** Re-read the code for each P0 and P1 before the verdict and set `status`: only `confirmed` ones block; a `possible` one is listed and does not block.
- **Evidence** is the finding's `scenario` (input, state or environment → what goes wrong; or a failing test named) together with its `file` and `line`. A finding whose scenario you cannot write is not raised.
- **Correctness only**: style, naming, wording and taste never block. Give such a finding the kind `style`, `naming`, `wording` or `taste`; `dev flow` never counts it as blocking, so a `back` whose only P0/P1 are of these kinds is no verdict. A typo or wording point is a defect only when it breaks a written rule; then its kind is `docs` or `contract` and that rule is its `rule`.
- **CI is evidence, not a reviewer's job**: `dev flow` marks a head reviewed only when its required check is green, so a running check is never a reason to bounce, and a review runs no checks or tests (root `AGENTS.md`). A finished failure caused by this change is a finding (P0 or P1; read the failed step with `gh run view --log-failed`); an unrelated one (another piece's test, the runner) is not: name it in the verdict's `line`.
- **Only the delta from round 2**: the earlier blocking findings first, then the change since the last reviewed head (the skill's step 2); a merge of the base into the branch brings no new finding on code the base already had.
