---
name: architecture-review
description: Review an existing backend architecture or RFC for boundary, ownership, security, operability, and evolution risks. Use for system-level assessment; use pr-review for defects in a specific code diff.
---

# Architecture review

Assess whether the system supports its stated requirements and can evolve
without disproportionate coordination. Review the supplied scope; do not launch
a rewrite or edit an RFC unless asked.

## Build a trustworthy system map

Read repository instructions, the RFC or ADRs, service entry points, schemas,
interfaces, deployment definitions, and relevant tests. Identify the system's
purpose and current pain. Trace a representative successful operation and one
failure path. Mark undocumented behavior and unavailable components as unknown.

Record the boundaries, state owners, callers, synchronous dependencies, and
deployment units. Distinguish the design described by documents from the behavior
implemented in code. A diagram is a hypothesis until its edges have evidence.

## Challenge the important seams

- **Ownership:** can more than one component write the same state? Who enforces
  each business invariant? Is cross-module access bypassing that owner?
- **Coupling:** can a common change or deployment happen independently? Cite an
  actual change path, shared schema, or call chain rather than counting services.
- **Trust:** where are identity, authorization, tenant separation, secrets, and
  data retention enforced? What crosses a trust boundary?
- **Failure:** which dependencies can exhaust threads, connections, or queues?
  How do callers see partial success, timeouts, and degraded operation?
- **Evolution:** do old/new clients and producers/consumers coexist safely? Can
  data and schema changes be rolled forward or recovered after a failed rollout?
- **Operations:** who owns alerts and recovery? Are goals, capacity limits, and
  critical-path signals measurable with the available telemetry?

Apply only checks relevant to the scope. Use workload evidence before making
performance claims. Missing evidence is a targeted investigation, not proof of a
broken design. Respect an existing ADR unless new evidence warrants reopening it.

## Prioritize a bounded response

Return an assessment with:

1. Scope, evidence sources, requirements, and important unknowns.
2. Risks ranked by likelihood and impact. Each includes a concrete failure or
   change scenario, the responsible boundary, and supporting source references.
3. A proportionate remedy for each major risk, its tradeoff, and a test or
   measurement that would confirm improvement.
4. A short sequence of incremental changes with compatibility and recovery
   considerations. Identify what already works and should be preserved.

Distinguish a requirement violation, an accepted tradeoff, and an optional
improvement. State whether the design is suitable, suitable with conditions, or
not yet assessable. Do not infer broad readiness from a diagram review alone.

Example: if billing and orders both update invoice status, trace conflicting
transitions and identify the invariant owner before recommending a service split.
