# Changelog

## Unreleased — engineering lifecycle expansion

- Expand the collection from 10 to 27 standalone skills for general software
  engineering, preserving the existing backend specialties and all skill names.
- Add `spec`, `build`, `test`, and `ship` to complete the lifecycle with
  `implementation-plan` and `pr-review`.
- Add idea refinement, research, frontend design, browser verification, security
  review, performance investigation, refactoring, CI/CD, observability, agent
  context, skill review, session handoff, and workflow retrospective.
- Broaden review, architecture, API design, planning, writing, and DX guidance
  for application, library, CLI, and tooling work.
- Add stage handoffs, packaged templates, and
  behavioral scenarios for general engineering and release boundaries.
- Add a concise cross-host quick start for installing and invoking the collection
  in Codex, Claude Code, and Kiro.
- Include a runnable synthetic CLI fixture for repeatable build-skill evaluations;
  its baseline contract is checked in CI independently of model behavior.

Installed skills are copies. Compare local customizations before updating them;
the installer refuses overwrites. `/plan` and `/review` remain lifecycle labels,
not new aliases replacing host commands.

## Initial collection — 2026-10-17

- Ten backend-oriented workflows, three-host setup documentation, a project
  installer, structural validation, and manual behavioral evaluation scenarios.
