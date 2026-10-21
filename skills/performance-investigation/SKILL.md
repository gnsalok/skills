---
name: performance-investigation
description: Investigate measured latency, throughput, memory, startup, or rendering problems across apps, libraries, services, and tools. Use for profiling and optimization with comparable before-and-after evidence.
---

# Performance investigation

Define the user-visible symptom, workload, metric, and acceptable target from
existing requirements. Mark proposed targets and missing measurements. Read
project instructions and relevant prior experiments before choosing a profiler
or changing code.

## Measure the current behavior

Capture version, environment, input sizes/distribution, concurrency, cache state,
and command. Repeat enough samples to expose variance and warm-up effects. Report
the statistic that matters: a tail latency, startup duration, memory trend, frame
responsiveness, or throughput at a stated load. Avoid invented p95s from tiny samples.

Use the tool that can locate the cost: browser traces/network waterfall for UI,
CPU/allocation profiles for compute, query plans and wait time for storage,
dependency spans for distributed calls, or build traces for tooling. Limit profiling
overhead and avoid running mutating analysis or load against production without scope.

## Test one causal explanation

Rank likely bottlenecks from the measurements. Choose one intervention with a
prediction and a correctness check. Reduce work, contention, or transfer before
adding caches or concurrency without evidence. For caching, include all relevant
identity/permission inputs, invalidation, size bounds, and consistency costs.

Re-measure under the same conditions. Changing data size, machine, or cache warmth
invalidates a simple before/after claim. If the difference is within noise, say so
and collect better evidence or remove the added complexity. Keep a short record
of unsuccessful experiments so the next session does not repeat them.

## Keep correctness and context

Run affected behavior checks: an optimization that skips required work or changes
output ordering is a regression. Explain memory, complexity, operating cost, or
freshness tradeoffs. Restore only your own unsuccessful experimental changes.

Deliver baseline/result with units, variability, reproduction command, supporting
profile evidence, and the chosen next step. Add a proportionate regression budget
or monitoring signal where useful. Separate local benchmark improvements from
field/user outcomes that still need observation.
