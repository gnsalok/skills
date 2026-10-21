---
name: spec
description: Turn a chosen idea or change request into a scoped specification or PRD with observable acceptance criteria. Use for unclear feature requirements or a requested spec before implementation; skip for trivial edits with explicit behavior.
---

# Specify the change

Translate intent into a shared definition of done. Read local instructions,
existing specs/issues, domain terms, and relevant code. Identify the active
initiative; preserve unrelated or unfinished specifications.

## Establish the contract

Describe the user/caller, current limitation, desired outcome, constraints, and
non-goals. Resolve terms with examples: “archive” might hide an item, make it
read-only, or remove it permanently. Distinguish the requested future behavior
from the behavior currently implemented.

Use supplied decisions and repository evidence. Ask about unresolved choices
that change acceptance criteria; proceed with labeled assumptions for details
that can remain provisional. Do not manufacture stakeholder approval, product
research, latency targets, or a preferred stack.

For a large initiative, identify independently useful capabilities, their owners
or consumers, and dependencies. Specify the selected capability with explicit
links to the rest. A small feature needs no artificial module hierarchy.

## Make requirements observable

Give important criteria stable IDs. Each states a precondition/input, observable
result, and relevant failure/edge case. Cover permissions, invalid input, state
transitions, compatibility, accessibility, and performance only where applicable.
Make clear which criteria are required and which are optional.

Record existing interfaces and verification entry points that the implementation
will use. Keep implementation guesses separate from requirements. For example,
“filtering preserves keyboard focus and can be cleared” is behavior; “use a global
state library” is a technical choice requiring its own justification.

Use the repository's document format. If none exists, consult the optional
[spec outline](references/spec-outline.md). Scale it to the task and use a
descriptive filename when saving, rather than overwriting a root `SPEC.md`.

## Hand off the scope

Return the spec, source references, assumptions, and blocking versus nonblocking
questions. A spec is ready for planning when the required behavior is observable
and unresolved decisions are explicit. Keep its status proposed unless already
accepted in the session. If the user requested specification only, finish there;
if implementation was also authorized, continue once its prerequisites are met.
This skill does not publish tickets or documents to external services by itself.
