---
name: test
description: Design, add, or run meaningful verification for a change using observable behavior and risk. Use for test requests, coverage gaps, regression checks, or QA evidence; use build when feature implementation is the primary task.
---

# Verify behavior

Determine what could fail, then collect evidence that distinguishes correct from
incorrect behavior. Read the task, changed code, existing tests, runner config,
and CI. State the target revision or working-tree scope and relevant criteria.

## Choose a test boundary

Map each material risk to the cheapest check that can actually expose it:

- Pure rules and transformations: deterministic examples, edge cases, properties.
- Libraries/CLIs: exported interfaces, supported runtimes, process exit/output,
  resource lifetime, and installation from the produced package when relevant.
- Storage and service integration: real representative transactions, protocol
  contracts, authorization failures, and concurrency at the appropriate boundary.
- UI: component behavior and browser journeys, keyboard/focus, responsive states,
  loading/error paths. Screenshots and DOM checks answer different questions.

Prefer established seams and public behavior. Use isolated real dependencies when
their semantics matter; use fakes at costly/nondeterministic boundaries and state
what they cannot prove. Avoid asserting private call order unless it is itself
part of the contract. Keep expected values independent of implementation logic.

## Execute and interpret

For a regression test, demonstrate that the original behavior fails for the
reported reason and the corrected behavior passes when a fix is in scope. Do not
count syntax errors or missing imports as a useful red phase. Keep seeds, clocks,
fixtures, and concurrency controlled; replace arbitrary sleeps with conditions.

Use actual repository commands in their documented directories. Preserve exit
status when capturing output. Inspect collected test counts and fresh reports;
zero collected tests, filtered-out cases, expected failures, and skips are not
passing coverage. Confirm a targeted test genuinely executed.

Classify failures as product, test, infrastructure, or uncertain. Investigate
within scope; keep a discovered product failure visible when only verification
was requested. Do not remove assertions or retry until green to conceal flakes.
Bound repeated runs and report failure frequency when nondeterminism matters.

## Deliver verification evidence

Return criterion/risk → check → observed result, runner counts when available,
commands and environment, and gaps requiring a different boundary or capability.
State pass, fail, skipped, blocked, and not run separately. A QA recommendation
depends on required checks and unresolved risk, not coverage percentage alone.
Do not approve release solely because a unit suite is green.
