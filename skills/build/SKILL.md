---
name: build
description: Implement an agreed feature, fix, or plan in small verified slices across apps, libraries, services, or tools. Use when coding is requested; an existing task description can supply scope without a separate spec file.
---

# Build a working change

Deliver the requested behavior through a short implementation/feedback loop.
Read local instructions, the active task/spec, relevant implementation and tests,
and Git status. Preserve unrelated edits. Record acceptance criteria and the
smallest useful next slice; do not require a separate plan for a small clear fix.

## Establish the baseline

Discover project commands, versions, generated files, and test conventions from
the repository. Run the relevant existing check to separate pre-existing failures
from new regressions. Record unavailable dependencies and keep independent work
moving. A failing baseline is evidence to diagnose, not permission to weaken tests.

Trace the affected public boundary and callers. Choose the simplest design that
fits established patterns. Identify compatibility, accessibility, authorization,
and persistent-state implications before changing those behaviors.

## Implement one observable slice

1. Define the intended result at the user's or caller's interface. For a bug or
   meaningful new behavior, add a focused test that fails for the right reason
   before the fix where practical. For static copy/docs, inspect the actual output
   or validate links rather than inventing an implementation-mirroring test.
2. Make the smallest complete change. Preserve existing interfaces unless scope
   includes changing them. Avoid unrelated rewrites or new dependencies for a
   capability the project already provides.
3. Run the focused check. Diagnose failures using output and one falsifiable
   hypothesis at a time. For asynchronous or intermittent bugs, exercise the
   competing operations; a single green run is weak evidence.
4. Clean up temporary probes, then run relevant regression/build/type checks.
   For UI changes, verify the actual interaction/rendering when tools are available;
   for libraries/CLIs, exercise a real consumer or invocation.
5. Update task status with evidence and continue the authorized scope. Reopen
   the plan if a discovery changes requirements or dependencies materially.

## Finish the whole requested outcome

Inspect the final diff for accidental files, weakened assertions, leaked data,
and missing documentation. Run required project checks once at the relevant end
boundary; do not rerun every unrelated suite after each tiny edit.

Report criteria delivered, important design choices, commands/results, and any
remaining failures or unverified behavior. Distinguish code written from behavior
verified. Commit or push when requested or established by the working agreement,
staging only intended files. Implementation alone does not authorize deployment,
package publication, or messages to other people.
