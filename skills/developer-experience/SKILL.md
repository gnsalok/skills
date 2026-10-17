---
name: developer-experience
description: Investigate slow or unreliable backend development loops such as setup, local services, tests, CI, and agent context. Use to propose or implement measured, incremental DX improvements without weakening correctness checks.
---

# Developer experience

Improve the path from checkout to a trustworthy change. Inspect the actual
workflow before adding another tool. For a DX review, return recommendations;
implement a bounded improvement when the user asks for changes.

## Reproduce the friction

Read local instructions, setup docs, version pins, package scripts, service
definitions, and CI. Follow the documented path from a clean checkout when an
isolated environment is available. Preserve existing files and user services.

Choose a concrete loop: first setup, one test, full suite, code generation,
debugging a request, or getting an agent to locate the right code. Record the
command, environment/tool versions, elapsed time, success rate, and manual steps.
Label a single observation; do not present it as a stable benchmark.

Identify the developer affected and the frequency of the problem. Separate
missing documentation, avoidable work, nondeterminism, and a real external
dependency. A cache miss and a broken environment need different remedies.

## Choose one intervention

Rank a few candidates by time saved × frequency, confidence, implementation
cost, and ongoing maintenance. State assumptions in rough estimates. Prefer
repository-supported scripts and pinned tools over new orchestration.

Possible fixes include deterministic fixtures, isolated test databases, health
checks for local services, incremental test selection with a reliable full CI
gate, cache keys that include true inputs, and concise navigation instructions.
Use the smallest change that addresses the measured bottleneck.

Do not hide failures, remove security checks, disable tests to get green CI,
cache secret-bearing outputs, or rely on a warm cache as proof setup works.
Never put a local credential into a helper script or tracked configuration.

## Verify the improved loop

If implementation is requested:

1. Establish the baseline, then make the bounded change using project conventions.
2. Re-run the same command and representative correctness checks. For caching,
   verify invalidation after a real input change as well as a warm run.
3. Verify first-run behavior, repeatability, and useful errors when a dependency
   is missing. Start/stop only services belonging to this experiment.
4. Record the new entry point and prerequisites; keep CI and local instructions
   aligned. Include a way to bypass or revert the optimization for diagnosis.

For agent friction, improve repository facts and navigation first. Put durable
project rules in the host's instruction file and task-specific methods in skills.
Do not paste the whole codebase or every skill into always-loaded context.

## Deliver a measured result

Return the friction, evidence, chosen change or ranked proposal, before/after
observations, correctness checks, and remaining costs. State if gains are local,
cache-dependent, or not yet measured in CI. A shorter command alone does not
prove the workflow is faster or more reliable.
