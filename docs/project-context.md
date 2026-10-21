# Project context example

Skills supply methods. Your application supplies facts. Put a short version of
the following in the instruction mechanism your team uses (`AGENTS.md` for
Codex, `CLAUDE.md` for Claude Code, or Kiro steering). If several hosts share a
project, point their instructions at one canonical project guide and confirm
each host can read it; file-import syntax is host-specific.

```text
Domain: [what this application, library, or tool does; link to the glossary]
Boundaries: [state owners and component/module entry points]
Local setup: [documented commands, working directories, pinned runtimes]
Tests: [one-test command, relevant integration tests, full CI gate]
Contracts: [schema locations, consumers, compatibility policy]
Decisions: [ADR/RFC directory and naming/status convention]
Runtime: [databases/brokers and versions; local substitutes and their limits]
Operations: [SLO/runbook locations, data handling and production-access rules]
Delivery: [deployment or package process, artifact identity, release authority]
UI/platform: [design system, accessibility goals, supported runtimes/devices]
Workflow: [spec/task location, active scope, stage entry points you use]
Writing: [audience, document location, preferred terminology]
```

Replace placeholders with verified project facts. Keep credentials in your
existing secure configuration. Do not invent an SLO, owner, or policy to fill a
line. Remove unused fields rather than maintaining a large stale instruction file.

Personalize one skill only after noticing a repeated need. For example, add a
review check for your transaction boundary convention or adapt migration gates
to your database engine. Keep employer-specific information in your private
project, and reduce any public regression case to synthetic data.
