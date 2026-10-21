---
name: frontend-design
description: Design or implement responsive, accessible user interfaces using an existing product language and real interaction states. Use for pages, components, visual hierarchy, and client-side interaction changes.
---

# Design a usable interface

Start from the user's task, audience, content, and available design references.
Inspect the current screen, components, tokens, framework, and routing conventions.
For a new product, state a coherent visual direction and the assumption behind it;
for an existing one, extend its language rather than introducing a second system.

## Model the interaction before polishing

Identify information priority, primary action, navigation, and state ownership.
Cover loading, empty, populated, error, disabled, and success states that the
task needs. Include slow responses, cancellation, duplicate submissions, and stale
async results. Decide which state belongs in the URL, component, or shared store
based on navigation and synchronization requirements.

Use realistic content lengths and narrow/wide layouts. Favor reusable project
components, semantic HTML, clear typography, and intentional spacing. Avoid adding
a component library, animation system, or global store merely to implement one
interaction. If exploring alternatives, keep prototypes visibly separate from
the production path and state which question they answer.

## Implement accessible behavior

When implementation is requested, build the smallest complete interaction.
Provide accessible names, labels, keyboard operation, visible focus, and useful
validation feedback. Manage dialog focus and return it to the invoking control.
Respect reduced motion and zoom; ensure information is not conveyed by color
alone. Prefer native elements to recreating their semantics manually.

Check responsive overflow and reflow with actual content. Preserve the user's
input during recoverable errors and explain the next action in product language.
Treat authorization as a server/resource boundary; hiding a control is not access
control. Keep secrets and unnecessary sensitive data out of client code.

## Verify and deliver

Run component tests and build checks that matter, then inspect the actual render
and exercise the journey in a browser when available. Check keyboard order,
focus, loading/error transitions, and representative viewport sizes. Record
browser/device limits. A screenshot alone does not prove interaction or assistive
technology behavior; a static code review does not prove visual quality.

Return the changed screen/flow, design reasoning, checks and observed states, and
remaining issues. If only design was requested, deliver an annotated proposal
or prototype rather than silently changing production UI.
