---
name: technical-writing
description: Write or revise technical RFCs, ADRs, runbooks, READMEs, tutorials, and onboarding guides from evidence. Use for a durable document or substantive documentation edit, not a one-line copy correction.
---

# Technical writing

Write for the next engineer trying to decide or do something. Match existing
document locations and conventions. Draft in the response unless the user asks
for a file or editing a file is already part of the task; do not publish to a
wiki, tracker, or chat without that scope.

## Establish the reader and source of truth

Read local instructions, nearby documentation, implementation/configuration, and
relevant decisions. Identify the reader's task and choose the smallest useful
document. Preserve established domain vocabulary; define unfamiliar terms once.

Separate implemented behavior, a proposed decision, and an assumption. Cite code
or authoritative documentation for claims that matter. Ask for a missing fact
only when it prevents a useful draft; otherwise mark a precise open question.
Never invent benchmarks, incident history, owners, approvals, or test results.

## Match the document to the work

- **RFC:** problem, constraints, non-goals, current behavior, viable alternatives,
  recommendation, consequences, rollout/recovery, and open decisions. Keep it
  proposed until the responsible person accepts it.
- **ADR:** status, context, decision, rejected alternatives with reasons,
  consequences, and conditions for revisiting it. Reference a superseding record
  rather than silently rewriting the history of an accepted decision.
- **Runbook:** symptom and impact, safe read-only diagnosis, interpretation of
  each signal, scoped mitigation, stop conditions, escalation role, and recovery
  verification. Identify destructive or shared-environment steps explicitly.
- **README/onboarding:** purpose, prerequisites and versions, working directory,
  setup, one useful invocation, expected result, common failures, and maintenance
  pointers. Keep secrets in secure configuration; show placeholder names only.
- **Tutorial/how-to:** a reader goal, prior knowledge, a minimal runnable example,
  expected intermediate results, common mistakes, and a way to verify completion.
  Keep API reference facts separate from the teaching sequence.

Use these as content checks, not mandatory headings. Omit sections that do not
help the reader. Prefer a concrete example over an abstract paragraph.

## Validate the instructions

Check paths, local links, flags, configuration names, units, and compatibility
claims against the sources. Execute safe local examples when practical, using
the stated working directory and prerequisites. Do not execute destructive or
production runbook actions just to verify documentation.

Show expected output or a success criterion so readers can detect a wrong state.
Explain environment-specific substitutions. Mark commands not executed and facts
that still need confirmation. Redact credentials, tokens, and customer data from
examples and captured output.

## Edit and deliver

Lead with the decision or task. Remove repetition and promotional language while
preserving qualifications, failure cases, and numeric units. Use tables for
comparisons and diagrams only when they clarify ownership or sequence.

Return the document or changed path, source references, validation performed, and
remaining questions. If the document is a proposal, make that status visible.

Example: a queue-lag runbook should distinguish a slow consumer from a poison
message and explain when replay is safe; “restart the workers” alone is unsafe.
