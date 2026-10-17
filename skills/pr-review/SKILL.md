---
name: pr-review
description: Review a backend PR, branch, or working diff for actionable defects, contract changes, and missing verification. Use before merge; use architecture-review for system boundaries beyond the diff.
---

# PR review

Find changes that could hurt a caller, operator, or future maintainer. Prefer a
short, defensible review over hypothetical problems. Review only; do not change
code or post comments unless the user asks.

## Establish the comparison

1. Read repository instructions and the task or acceptance criteria. Inspect Git
   status before running commands; preserve the user's work.
2. Resolve the requested base and head to commits and record them. For a branch
   review, compare its merge base with the target branch to head. Do not assume
   `HEAD~1` captures a PR. If the target is unknown, inspect repository defaults;
   ask only if the choice changes the review.
3. For working changes, include staged and unstaged diffs and inspect relevant
   untracked files separately. State which changes were reviewed. An empty diff
   means there is nothing to review, not that the system is correct.
4. Read changed tests, then the implementation and its callers. Follow affected
   transaction boundaries, consumers, configuration, and migrations beyond the
   changed lines when needed to establish impact.

## Trace the behavior

For each meaningful change, ask what input or interleaving would break it:

- **Correctness:** error paths, cancellation, timeouts, resource cleanup, races,
  and transaction isolation. Can an effect commit before a retryable error?
- **Contracts:** old clients, mixed deployment versions, event schemas, nullable
  fields, pagination, and schema compatibility during rollout and rollback.
- **Trust:** authorization on the actual resource and tenant, unsafe queries,
  exposed secrets, and untrusted input crossing a privilege boundary.
- **Operations:** bounded work, query count, connection pools, retry budgets,
  logging sensitive data, and enough telemetry to diagnose the changed path.
- **Maintainability:** a concrete increase in change cost or hidden coupling.
  Label taste as optional; do not turn a preferred pattern into a defect.

Read the surrounding implementation before reporting a missing safeguard. Try a
targeted existing test or safe local reproduction when it can distinguish a
defect from a suspicion. Do not run destructive commands or use production data.

## Return a review someone can act on

Lead with findings, ordered by impact. Each finding contains:

- Severity: **blocker** (data loss, security breach, or core path broken),
  **important** (credible behavioral regression), or **suggestion** (optional).
- Exact file and line, triggering input or sequence, observed or reasoned
  consequence, and a specific correction or regression test.
- Evidence and confidence. Put an unresolved assumption under open questions,
  rather than presenting it as a confirmed failure.

Finish with the reviewed commits/scope, checks actually executed and their
results, unverified risks, and a merge recommendation. Distinguish **no blocking
findings** from **not enough evidence to assess**. Never imply tests passed when
they were skipped or unavailable. Deduplicate findings with the same root cause.

Example: a retry after a payment-provider timeout may duplicate a charge if the
first attempt committed. Cite the call and retry path, identify the unknown
outcome, and recommend a stable operation identity plus reconciliation; “add
error handling” is not a useful finding.
