---
name: ship
description: Assess release readiness and prepare or execute an authorized deployment, package publication, or distribution change. Use for go-live decisions, release checklists, rollout gates, and recovery planning after implementation.
---

# Ship with verifiable release evidence

Identify the exact commit/artifact, target environment or registry, intended
audience, and requested action. Read the project's release process and current
authorization. A readiness request produces a decision and procedure; deploy or
publish only when that action and destination are already authorized. Do all
independent preparation before asking for a genuinely missing release decision.

## Assess the candidate

Tie test/build/review results to this candidate, not a nearby branch or stale CI
run. Verify required criteria and unresolved findings. Passing tests alone do not
establish approval, environment readiness, or successful deployment.

Select relevant checks for the artifact:

- Application: configuration presence, credentials usable through supported
  routes, dependencies, compatibility of mixed versions, migration ordering,
  user journey and telemetry needed to observe the rollout.
- Package/CLI: intended version/tag, included files, clean consumer install,
  supported runtimes/platforms, release notes, registry and artifact identity.
- Static site/docs: generated output, links/assets, accessibility/navigation,
  hosting configuration, and a functional request to the deployed version.

Inspect credential names/status only; keep values out of output and documents.
Preserve checksum, signature, and TLS verification. A scanner's absence or failed
registry request is a validation gap, not a clean security report.

## Define rollout and recovery

Use the existing deployment path. State stages, responsible role if known,
success/hold/stop signals, observation window, and recovery procedure. Derive
thresholds from existing goals/baselines or mark them proposed; arbitrary rollout
percentages or waiting periods are not universal policy.

Differentiate undoing code from undoing effects: database writes, notifications,
and published package versions may require forward repair or a new release.
Identify the last reversible step and recovery prerequisites before proceeding.
Use the optional [release record](references/release-record.md) when useful.

## Decide and, when authorized, execute

Return **ready**, **not ready**, or **insufficient evidence**, with blockers and
accepted risks attributed to actual decisions. If release is authorized and the
candidate is ready, use project commands, observe completion, and verify the
deployed artifact/version through a representative operation. A queued CI job,
PID, open port, or success banner alone is not evidence the user journey works.

Record what was released, evidence, remaining monitoring, and any recovery taken.
If execution is blocked, report the exact missing prerequisite and leave the
prepared procedure usable. Never say “live” for a proposal or an unverified job.
