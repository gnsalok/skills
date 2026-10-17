# Collection design and implementation plan

## Intent

Build a personal, maintainable backend workflow collection for Codex, Claude Code,
and Kiro. Optimize for useful engineering artifacts and fewer repeated mistakes,
not the number of skills or lines of instruction.

## Initial plan

1. Inspect the existing PR review skill and the two requested reference projects.
2. Retain `pr-review` and add nine standalone workflows covering architecture,
   distributed behavior, contracts, data changes, writing, DX, debugging, and planning.
3. Document native discovery and a safe project installer for the three tools.
4. Add dependency-free structural checks, installer regression tests, and manual
   behavioral scenarios. Distinguish structural success from model performance.
5. Review the complete diff, run the checks, and submit the change as one PR.

## Decisions

- **One source, three hosts.** Use portable front matter and plain instructions;
  keep tool installation details in documentation. No model-version branching.
- **Independent folders.** A single skill install must work without sibling
  skills or repository-root resources. Future supporting files live inside the
  relevant skill directory and load only when useful.
- **Focused scope.** Design chooses an approach; architecture review assesses a
  system; PR review assesses a diff. Specialized failure and migration workflows
  cover areas where generic advice misses important state transitions.
- **Evidence before prescription.** Require triggers, sources, assumptions,
  tradeoffs, and observable checks. Avoid mandatory interviews for facts already
  available in the repository, fixed output lengths, and forced service patterns.
- **Small maintenance surface.** Standard-library Python tooling, no package
  lockfile or runtime dependency, and no automatic plugin/hooks installation.
- **Preserve the existing entry point.** `pr-review` remains the name. Its review
  output now leads with evidence and distinguishes an unassessable change from
  a change with no blocking findings. Positive observations remain optional.

## Inspiration record

These revisions were inspected on 2026-10-17; they are provenance, not dependencies.

| Repository | Revision | Ideas considered | Local choices |
| --- | --- | --- | --- |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | `aeac41d4d005999432bb7312f7ff06383a91d59d` | Engineering workflows, verification, documentation of decisions | Backend failure windows, contract evolution, and explicit recovery limits |
| [mattpocock/skills](https://github.com/mattpocock/skills) | `49dd158d1076134a641b33efb035946536778336` | Repository context, testable feedback loops, architecture change costs | Bounded clarification and standalone skills without required tracker setup or subagents |

Both reference projects publish under MIT licenses. No source text, scripts,
templates, or plugin configuration were imported. If future contributions adapt
material from either project, preserve the applicable license and attribution
with the adapted material.

Agent paths and Kiro custom-agent resource guidance were also inspected in the
[skills CLI](https://github.com/vercel-labs/skills) source. See the
[setup guide](agent-setup.md) for primary vendor links and validation limits.

## Future changes should follow observed work

Potential additions include a performance investigation workflow, incident
postmortems, and threat modeling. Add one when a repeated task needs a distinct
trigger and artifact; avoid expanding a generic checklist for every new topic.

When a model or host changes, rerun the scenarios before adding compatibility
instructions. Prefer deleting obsolete workarounds over stacking new ones.
Keep a brief record of the failure case, change, and result in the PR or eval log.
