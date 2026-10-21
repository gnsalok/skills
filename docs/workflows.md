# Working across the lifecycle

Use the smallest workflow that matches the task. Skills operate within the user's
existing scope and local instructions. They do not impose approval after every
stage or silently authorize later external actions.

## Stage contracts

| Stage label | Installed skill | Evidence needed | Artifact handed forward |
| --- | --- | --- | --- |
| `/spec` | `spec` | User/caller problem, chosen direction, constraints | Scope, criterion IDs, assumptions, open decisions |
| `/plan` | `implementation-plan` | Defined behavior and relevant repository seams | Task IDs, dependencies, criterion mapping, verification commands |
| `/build` | `build` | Authorized scope and next bounded task | Implementation, task status, checks tied to the current state |
| `/test` | `test` | Candidate and acceptance risks | Check/result matrix, failures and gaps |
| `/review` | `pr-review` | Exact comparison and intended behavior | Findings, requirement coverage, recommendation |
| `/ship` | `ship` | Exact artifact, required evidence, target and release scope | Readiness decision; release outcome only after authorized execution and verification |

These labels are a mental model, not portable slash-command aliases. For example,
ask “Use implementation-plan” or select that skill in your host. This repository
does not install a `/plan` or `/review` wrapper that could shadow a built-in command.

For long work, keep one canonical task/spec record with criterion and task IDs.
Link to code, check results, decisions, and releases rather than duplicating them
in every artifact. A resumed session rechecks Git status and external state before
continuing; an old checked box does not prove the current code still passes.

## Example: searchable settings UI

This is an illustrative workflow, not a recorded execution.

1. **Define:** `idea-refinement` first if the user problem is unclear. `spec`
   defines `AC-1` filtering by label, `AC-2` keyboard navigation/focus preservation,
   and `AC-3` clearing a filter restores results. Decide URL persistence explicitly.
2. **Plan:** `implementation-plan` identifies the current settings component and
   state owner, then slices one working filter path before adding empty/error states.
3. **Build:** `frontend-design` handles state/layout/accessibility decisions;
   `build` implements the authorized slices and focused regression checks.
4. **Verify:** `test` checks matching and state transitions; `browser-verification`
   exercises keyboard use, narrow layouts, reload, and empty results on the actual build.
5. **Review:** `pr-review` checks the diff against all three criteria and looks for
   stale async responses, focus loss, and unrelated changes.
6. **Ship:** `ship` uses the project's hosting workflow, validates the actual
   version and journey if deployment is authorized, and records rollback limits.

If browser tools are absent, runtime QA stays blocked or unrun; a screenshot
description or source inspection does not replace the missing check.

## Example: JSON output for a CLI

Use `api-design` to define `--json`, stdout/stderr separation, exit codes, and
compatibility with the existing human-readable output. `spec` records these as
criteria; `implementation-plan` sequences serialization, failure behavior, and
consumer tests. `build` implements the change; `test` invokes the built executable
with valid input, invalid input, and a pipeline consumer.

`pr-review` checks default-output compatibility and resource cleanup. For
distribution, `ship` checks the actual package contents, version, supported
platforms, and clean consumer install. Publishing an immutable package version
may require a follow-up release rather than deletion for recovery.

## Example: reliable background work

Keep the existing backend depth. `architecture-design` compares feasible approaches;
`distributed-systems-review` traces partial failure and duplicate delivery;
`database-migration` plans compatible schema/backfill stages. Feed their concrete
decisions into the spec and plan rather than running every skill on every task.

`build` implements the path, `test` exercises the relevant transaction and crash
boundaries, and `observability` verifies operating signals. `ship` distinguishes
rolling code back from reversing writes or external effects.

## Pick between neighboring skills

| If the uncertainty is… | Start with… |
| --- | --- |
| Is this the right problem/idea? | `idea-refinement` |
| What is actually supported in this version? | `research` |
| What should users/callers observe? | `spec` or `api-design` for the public contract |
| Which technical approach fits? | `architecture-design` |
| What is wrong with these existing boundaries? | `architecture-review` |
| How do we sequence known work? | `implementation-plan` |
| Does the candidate work? | `test`, with `browser-verification` for browser evidence |
| What must change before this diff merges? | `pr-review` |
| Can this exact candidate be released? | `ship` |
| Why is this measured workload slow? | `performance-investigation` |
| How can working code be easier to change? | `refactoring` |
| Are development commands slow or fragile? | `developer-experience` |
| Are agent instructions/navigation unreliable? | `agent-context` |
| What should the next session know? | `session-handoff` |
| What should we improve after this session? | `workflow-retrospective` |

For small clear changes, use `build` → relevant checks → `pr-review` as needed.
For a research-only question, finish with the answer and sources. For an existing
incident, use the established incident process; this lifecycle is not a reason to
delay an already authorized mitigation with a new PRD.
