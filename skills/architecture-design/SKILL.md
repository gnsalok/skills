---
name: architecture-design
description: Explore a backend architecture idea and compare viable designs against workload, invariants, team constraints, and operating cost. Use before implementation; produces a recommendation or a bounded experiment.
---

# Architecture design

Turn an idea into a decision a team can challenge. Start with the existing
system, not a preferred technology. This workflow proposes a design; implementing
it or provisioning infrastructure requires that scope from the user.

## Establish the problem

Read local instructions, existing design records, relevant code, and deployment
configuration. Follow one representative request or event through storage and
downstream effects. Cite the evidence for the current behavior.

Write a compact design brief:

- User outcome and the limitation that motivates a change.
- Workload: request/event rate, burst shape, payload size, data growth, and hot
  keys. Label estimates and assumptions; do not invent traffic measurements.
- Invariants: what must remain true about ownership, money, permissions, order,
  or state transitions, including under failure.
- Constraints: latency and availability goals, acceptable data loss/staleness,
  team capacity, budget, residency, and existing platform commitments.
- Non-goals and decisions still reversible within this task.

Infer routine details from the repository. Ask only for an unknown that could
change the recommendation. Continue with explicit assumptions where useful.

## Compare realistic options

Consider keeping the current design with a smaller improvement, plus one or two
credible alternatives. Reject options that cannot satisfy a hard constraint.
For each remaining option describe:

1. Boundaries and who owns each piece of state. Show a small component or sequence
   diagram only if it makes the critical path clearer.
2. Reads, writes, synchronous dependencies, and the exact points where work can
   partially succeed. Include tenant isolation and authorization boundaries.
3. Expected bottleneck, rough capacity/cost arithmetic with units and inputs, and
   operating burden. An unknown input should produce a range or an experiment.
4. Evolution: compatibility with current clients, migration steps, mixed-version
   behavior, and what remains recoverable after new writes begin.

Choose technology only after these differences are clear. Do not prescribe
microservices, a broker, caching, or multi-region deployment without a workload
or failure requirement that pays for the complexity.

## Deliver the decision

Return a brief proposal with problem, evidence, constraints, option comparison,
recommendation, and consequences. Separate accepted facts from assumptions and
open decisions. A recommendation may be “keep the current boundary.”

List the smallest experiment that could overturn the recommendation, its success
and failure thresholds, and a first independently verifiable implementation
slice. Include a rollout signal and a recovery path. When the user requests a
saved document, follow the repository's RFC/ADR location and template; leave its
status proposed until the decision owner accepts it.

Example: for slow exports, compare query/index improvements, an async job in the
existing service, and a separate worker. Decide using duration, memory pressure,
freshness needs, and operational ownership rather than “we need a queue.”
