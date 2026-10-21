---
name: ci-cd
description: Design or fix automated build, test, artifact, and deployment pipelines. Use for CI failures, workflow setup, cache correctness, and delivery automation; use ship for a specific release decision or execution.
---

# Build dependable automation

Read existing workflows, project commands, version pins, branch protections when
visible, and release requirements. Establish the triggering event, trust level,
target platforms, and failure symptom. Prefer running the same checked-in commands
locally and in CI over creating a second implementation of the build.

## Model the pipeline

Order jobs by real dependencies and artifacts. Separate fast feedback from costly
integration/platform coverage without silently dropping required gates. Ensure
selected tests actually collect and run. Preserve the failing command's exit code;
avoid allowing a successful upload or cleanup step to hide failed verification.

Pin appropriate runtime/tool versions and use frozen dependency installation.
Make caches depend on actual inputs, including lockfiles, toolchain, platform,
and relevant configuration. Verify a cold run and invalidation; a warm green run
alone does not prove reproducibility.

## Respect trust boundaries

Give jobs the permissions they need. Treat PR code, workflow inputs, and downloaded
artifacts as untrusted. Do not run an external contributor's code with publication
secrets or write privileges merely because a privileged event can access them.
Keep test artifacts free of credentials and sensitive environment dumps.

For delivery, identify the tested artifact and promote that artifact through
environments rather than rebuilding unknown bits at each stage. Preserve signing,
checksum, and TLS checks. State protected environments, concurrency controls,
release authorization, and recovery behavior supported by the project.

## Validate the change

Use available workflow validators and run the underlying commands locally.
Inspect the triggered CI run when access exists: exact commit, event, matrix,
job statuses, test counts, and artifact freshness. A valid YAML file or locally
passing command does not prove the remote workflow ran successfully.

Report the failure or missing gate, change, local versus remote results, and
remaining configuration such as branch protection or registry access. Do not
claim required checks are enforced just because a workflow file was committed.
