---
name: implementation-plan
description: Turn an agreed software change or spec into dependency-ordered implementation slices with acceptance checks and delivery gates. Use after scope is defined and before coding multi-step work.
---

# Implementation plan

Make the next coding session executable. Read repository instructions, the task,
relevant code/tests, and accepted design records. Reuse an existing plan if one
already describes this change. Planning does not authorize creating tracker
tickets, changing infrastructure, or implementing a plan by itself.

## Bound the outcome

Restate the observable result, acceptance criteria, invariants, non-goals, and
constraints. Identify interfaces and state that change, plus old clients or
workers that must keep working. Distinguish settled decisions from assumptions.

Resolve what can be learned from the repository. Ask for a missing decision only
when it changes the plan materially. If architecture is undecided, describe the
smallest investigation that can settle it before detailed implementation tasks.

## Slice by verifiable behavior

Prefer a thin end-to-end capability over completing every layer in isolation.
Each slice should be reviewable and leave the main branch in a coherent state.
Keep pure refactors separate when that makes behavior changes easier to assess.

For each slice provide:

- A stable task ID, criterion IDs it satisfies, dependencies, and status. Keep
  one canonical task list and reference existing specs or tickets rather than
  duplicating their requirements. Preserve unfinished plans for other work.
- Outcome and affected modules/paths discovered in the repository.
- Dependencies and prerequisites, including credentials or external decisions.
- Implementation steps with enough detail to locate the seam, without inventing
  symbols or file paths that have not been verified.
- Acceptance cases: success, relevant error/failure path, and compatibility or
  concurrency checks. State the expected behavior, not merely “add tests.”
- Validation commands from the project and what result should demonstrate.
- Deployment/feature-flag gate and recovery path where the slice changes runtime
  behavior. Mark destructive transitions and the point rollback stops being safe.

Use explicit dependencies instead of assuming every task can run in parallel.
Do not prescribe subagents, a worktree, a specific model, or a cloud service as a
prerequisite unless the repository or user requires it.

## Check the whole sequence

Walk the mixed-version rollout and data lifecycle. Put compatible schema changes
before new writers, and cleanup after consumers and rollback windows have moved.
Include observability required to decide whether to continue rollout.

Adapt delivery to the product: browser interaction and accessibility checks for
UI work, consumer/runtime compatibility for libraries, and output/installation
checks for CLIs. Deployment gates apply only to deployable changes. A simple
local fix can have a two-step plan without a separate PRD or release ceremony.

Trace every acceptance criterion to at least one slice and check for work that
serves no criterion. Keep optional enhancements out of the required path. Use
coarse effort/risk estimates only if helpful; do not invent precise delivery dates.

## Deliver a usable handoff

Return the scope, ordered slices, dependency map if needed, verification plan,
and remaining decisions. End with the first executable step. If saving a plan is
requested, follow local conventions and include the relevant code/design refs.

Name the active spec or scope explicitly so a later session cannot resume the
wrong initiative. Completed tasks link to their evidence; blocked tasks name the
missing input. A resumed session should recheck state before trusting old marks.

State that proposed checks have not run. A plan is complete when an engineer can
start a bounded slice and know how to tell it works, not when every possible
future concern has a task.
