---
name: worker-dev
description: Call right after taking a card on the dev board, and when coming back to that card after a note. Not for the manager who adds cards.
---
# Worker steps on a trial-dev card (flow board)
This is the trial repository's copy of sushilife-agentkit's `docs/skills/worker-dev/SKILL.md`: the two skills it links live in that repository's main checkout on this host, so they are named by absolute path here.
- Kind: skill
- Topic: dev worker steps
- Readers: worker
- Status: adopted

Read `/home/swseo-agent-2/personal/sushilife-agentkit/docs/skills/worker/SKILL.md` now and follow it (the common worker steps), with these changes. This board has no `dev submit`, no `dev review` and no review or merging column: where the common skill says submit or submitting, read "push and open or update the PR", and where it leaves a card in merging or submitted, leave the PR open. Its "Finishing: card with a PR" and "When returned" are replaced by the lines below. `dev done` is one of the commands you call; do not move a card that has PRs to done yourself. Everything else in it holds, the no-local-check rule included.
Read `/home/swseo-agent-2/personal/sushilife-agentkit/third_party/ponytail/SKILL.md` now and follow it; this repository's root `AGENTS.md` wins over it.

- One card is one goal. Split the work into as many small PRs as its context boundaries need, and give independent parts to subagents.
- Open each PR yourself with plain `git` and `gh`. Put `Card: <n>` (your card's number) alone on a line of the PR body: that line is how the system finds the PR, and without it nothing reviews or merges it.
- Order between PRs: `Depends-On: <PR URL>` in the body, or a stacked branch. After the PR under a stacked one merges, merge the default branch into yours and push.
- Do not merge a PR and do not post the `reviewed` status: the line merges once the independent review and the check pass.
- Results come as notes on your card (review verdict with findings, check failure, line failure, merged and installed). Act on the note. A fix is a new commit pushed to the same branch (no rebase, amend or force push: the next review reads the delta). A finding you do not fix is answered in a commit message or a PR comment; a fixed one needs no words.
- A PR that touches a path listed in `.github/CODEOWNERS` (a fence path) starts its title with this repository's fence mark (`[울타리]`, root `AGENTS.md`): without the mark you get a note, and the review counts it against the PR.
- Goal reached: `dev done <n> --result "<what, where, how confirmed>"`. It may be called while PRs are in flight: the card moves to done when the last one is merged and installed.
- Needs a decision: "When blocked" of the common skill.

