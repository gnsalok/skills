# Collection design

## Intent

Maintain a personal engineering workflow collection across Codex, Claude Code,
and Kiro: define, plan, build, verify, review, ship, and improve how the work gets
done. Serve applications, libraries, CLIs, services, and tooling while retaining
useful backend depth. Prefer a smaller useful method over a generic checklist.

## Organization and compatibility

The six lifecycle entry points are `spec`, `implementation-plan`, `build`, `test`,
`pr-review`, and `ship`. Specialists answer narrower questions and produce their
own artifacts. They are optional additions, never hidden prerequisites.

Names from the original collection remain stable. In particular, `pr-review`
and `implementation-plan` are not renamed merely to match `/review` and `/plan`.
Those short labels can already have meanings in a host. Documentation maps the
lifecycle to actual skill names instead of shipping conflicting wrappers.

Use portable `name` and `description` front matter and plain instructions. Keep
host-specific discovery/configuration in the setup guide. No model version,
mandatory subagents, tracker integration, or plugin command system is required.

## Scope and stage boundaries

A stage produces something the next stage can verify: criterion IDs, dependent
tasks, implemented behavior, test evidence, findings, or a release record. Use
one canonical scope/task record and links rather than duplicate specifications.
Continue work already authorized by the user; a stage boundary does not mandate
another permission prompt. Missing decisions and external action scope still matter.

Generic skills adapt to the actual surface: browser state and accessibility,
consumer/runtime compatibility, CLI outputs and resource effects, or service
transactions and recovery. Specialized distributed-system and database workflows
retain concrete failure analysis rather than being diluted into every review.

## Context and maintenance budget

Keep the main skill under 200 lines. Put optional templates or deeper references
inside that skill's directory and link them from the point where they are useful.
A copied folder must work by itself; there are no dependencies on root-level
resources or another installed skill.

Keep runtime tooling small: standard-library Python, no new package dependencies,
and no automatic hooks or host configuration rewrites. The installer preserves
existing destinations. The catalog is organized by work rather than a second
nested folder taxonomy that would change install paths.

## Evidence and evolution

Every new workflow has a trigger, bounded steps, observable result, and a manual
regression scenario. Changes to broad descriptions need adjacent-task and negative
routing cases. Automated checks validate packaging and coverage, not model quality.
Record host/model/context for behavioral runs and distinguish not run from blocked.

Use real friction to guide future additions. Test the smallest instruction change,
then remove obsolete rules and duplicate guidance. A model upgrade is an occasion
to rerun representative cases, not a reason to fork every skill by model name.
See [CONTRIBUTING](../CONTRIBUTING.md) and [evaluation guidance](../evals/README.md).
