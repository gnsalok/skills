---
name: observability
description: Design or improve logs, metrics, traces, and alerts around concrete operating questions. Use when behavior is hard to diagnose or new functionality needs signals; use backend-debugging for an active backend defect.
---

# Make behavior diagnosable

Read the feature's boundaries, existing telemetry conventions, runtime limits,
and operating goals. Identify the questions an engineer or operator needs to
answer: which step failed, how many users are affected, where time went, or whether
work is stuck. Each new signal should answer a question.

## Pick signals and semantics

Use metrics for aggregate trends, structured events/logs for specific outcomes,
and traces for causality and timing across boundaries. For client software,
consider local diagnostics and consent-aware error reporting; not every tool
needs a remote telemetry service.

Define event names, units, denominators, success/failure categories, and where
measurement starts/stops. Include cancellations, timeouts, partial success, and
retries so success rates do not count attempts as users or operations accidentally.
Propagate correlation through async boundaries without exposing sensitive IDs.

Bound cardinality and volume. Do not use raw user IDs, URLs with arbitrary values,
or request payloads as metric dimensions. Redact secrets and personal data before
collection, respect retention/sampling rules, and ensure telemetry failure does
not break the primary operation. Sampling can hide rare events; describe that limit.

## Make signals actionable

Connect important alerts to user impact, an evaluation window, known baseline or
SLO, and a diagnosis/response path. Mark thresholds and owners as proposed when
not established. Avoid alerts for every internal error without a human action.

For implementation work, exercise success and failure locally and inspect the
emitted signal. Verify label bounds, missing/duplicate events, trace propagation,
and behavior when the collector is unavailable. Keep test telemetry isolated
from production alerting.

Return question → signal → interpretation → action, changed instrumentation,
verification evidence, and gaps in collection or dashboards. A configured exporter
is not proof that signals arrived or that an alert can fire.
