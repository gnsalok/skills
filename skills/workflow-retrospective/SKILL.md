---
name: workflow-retrospective
description: Review a completed development or agent session to identify small, evidence-based improvements to skills, context, tooling, or checks. Use to maintain a personal workflow after repeated friction or a model/tool upgrade.
---

# Improve the workflow from real evidence

Use the requested session or the current one. Read task outcomes, corrections,
diffs, command results, and available redacted notes. Identify what the user
wanted, what happened, and where time or correctness was lost. Do not attribute
every mistake to the model without inspecting missing facts or tool limitations.

## Classify the failure

- Missing project fact: improve the authoritative project guide/navigation.
- Weak workflow: adjust the relevant skill's trigger, step, or completion criterion.
- Mechanical error: consider the existing linter/test/CI gate before adding prose.
- Unavailable tool/access: fix the environment or report the precise prerequisite.
- Product ambiguity: record the decision needed, rather than encoding a guessed
  requirement as permanent agent behavior.

Include what worked and should be retained. Rank a few changes by observed impact,
repeatability, confidence, and maintenance cost. A repeated failure with a small
reproduction is stronger evidence than a preference about wording.

## Make one change testable

For each recommendation, name the evidence, smallest intervention, source file
or tool, regression prompt, expected improvement, and possible downside. When
implementation is requested, apply the bounded change and rerun the relevant
checks; otherwise return a proposal.

For skill changes, replay the failure and an adjacent/unrelated prompt to catch
over-triggering. Compare under the same host, model, permissions, and context when
possible. Record multiple runs for variable behavior. Do not claim a prompt is
better merely because it is longer or one answer sounded more confident.

## Keep the collection maintainable

Remove superseded rules and duplicate instructions when evidence supports it.
Keep project-specific facts private and reusable methods portable. Record the
reason for the change and the scenario that protects it. Preserve untested ideas
as proposals, not permanent rules.

Deliver prioritized findings, changes made or proposed, validation outcomes, and
one next experiment. A model/tool upgrade should trigger representative reevaluation,
not an automatic rewrite of every skill.
