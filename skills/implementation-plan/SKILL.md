---
name: implementation-plan
description: Turn an agreed backend change into small, dependency-ordered implementation slices with acceptance tests, rollout gates, and recovery steps. Use after the goal is clear and before coding a multi-step change.
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

Trace every acceptance criterion to at least one slice and check for work that
serves no criterion. Keep optional enhancements out of the required path. Use
coarse effort/risk estimates only if helpful; do not invent precise delivery dates.

## Deliver a usable handoff

Return the scope, ordered slices, dependency map if needed, verification plan,
and remaining decisions. End with the first executable step. If saving a plan is
requested, follow local conventions and include the relevant code/design refs.

State that proposed checks have not run. A plan is complete when an engineer can
start a bounded slice and know how to tell it works, not when every possible
future concern has a task.
