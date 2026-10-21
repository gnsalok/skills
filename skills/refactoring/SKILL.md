---
name: refactoring
description: Simplify or restructure working code while preserving observable behavior and compatibility. Use for reducing concrete change friction, duplication, or coupling; use architecture-design when the desired behavior or boundaries are still undecided.
---

# Refactor without losing behavior

Identify the concrete maintenance problem and the area in scope. Read local
instructions, callers, tests, and existing decisions. Describe the change that is
hard today and how the proposed structure makes it easier. Fewer lines alone are
not a sufficient outcome.

## Establish what must stay true

Record inputs/outputs, errors, effects and their order, resource lifetime, public
interfaces, and relevant timing/concurrency guarantees. Run existing behavior
checks. Add characterization cases only for meaningful behavior at risk, noting
when they preserve a known quirk rather than endorse it.

If an existing bug should change, separate that behavior change from the refactor
with its own criterion and evidence. Do not silently “clean up” compatibility
quirks that consumers rely on.

## Make the structure earn its cost

Choose a small transformation: name a concept clearly, isolate a responsibility,
remove an unnecessary layer, or consolidate truly shared logic. Compare a real
caller before/after. An abstraction should reduce what callers must know without
hiding control flow behind generic configuration or growing a hypothetical framework.

Preserve the order of validation and side effects. Watch for language-specific
changes in evaluation, laziness, exception timing, mutation, async cancellation,
and cleanup. Keep UI state identity and serialized/public names stable where they
form part of behavior. Work incrementally and test at stable public seams.

## Prove the result

Run the original checks and targeted regression cases without weakening expected
behavior to fit the new implementation. Use differential tests or representative
performance checks when those risks justify them. Inspect the diff for accidental
feature changes and generated-file churn.

Return the maintenance problem, structural improvement, preserved contract,
checks/results, and remaining risk. A review-only request returns candidates and
evidence instead of editing code. Stop when the scoped friction is resolved;
nearby imperfections do not automatically expand the task.
