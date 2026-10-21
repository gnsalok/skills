# Reference study and review of the merged collection

Reviewed on 2026-10-21. Sources are inspiration and evidence for design choices,
not runtime dependencies. References below pin the revisions inspected.

- [Addy Osmani / agent-skills](https://github.com/addyosmani/agent-skills/tree/aeac41d4d005999432bb7312f7ff06383a91d59d)
- [Matt Pocock / skills](https://github.com/mattpocock/skills/tree/5beb35b040e3de97e54fa9e386d7e42d15c295c2)
- Local baseline: merged `main` at `03f6fa3`, containing the original ten skills.

## What was examined

The study covered the catalogs and packaging, Addy's six lifecycle command
wrappers, and substantive workflows for ideation/specification, incremental
implementation, testing, shipping, UI/browser work, security, performance,
observability, CI/CD, simplification, and context management. Matt's workflows
examined included specs, implementation/TDD and test-boundary references, module
design, domain vocabulary, prototypes, research, handoffs, retrospectives, and
writing for agents. This is a focused study of relevant workflows, not a claim
that every upstream experiment or script was executed.

## Findings from the references

| Area | What the sources contribute | Choice in this collection |
| --- | --- | --- |
| Lifecycle | Addy's command wrappers make define-to-ship discoverable | Four new standalone lifecycle skills join existing plan/review names; no host-specific wrappers |
| Requirements | Addy separates ideation and specs; Matt captures decisions and test seams | Separate the uncertain idea from the selected scope, with observable criterion IDs and bounded clarification |
| Implementation | Both favor small changes with feedback; Matt's implementation separates focused checks from final broader checks | Implement authorized scope in slices, discovering project commands and preserving user edits |
| Tests | Matt's TDD resources emphasize public behavior and independent expected values; Addy inspects the stack and regression failure | Check at the seam that exposes the risk; use real dependency semantics when needed and report test collection/skips |
| Architecture | Matt examines what callers must know and where change cost spreads | Compare concrete interfaces and state owners across UI, package, CLI, and service work |
| UI and browser | Addy distinguishes interface construction from runtime observation | Separate design/implementation from browser QA, with tool-independent instructions and honest blocked states |
| Release | Addy combines readiness, monitoring, and recovery | Tie evidence to an exact artifact, use project-specific thresholds, and separate readiness from authorized execution |
| Performance | Addy measures comparable workloads and records unsuccessful experiments | Keep baseline conditions, variance, correctness, and discarded experiments visible |
| Context | Both distinguish persistent guidance from task context; Matt stresses useful pointers and pruning | Keep durable facts, reusable methods, and temporary handoff state separate |
| Maintenance | Matt's retrospective classifies workflow/context/tooling problems | Add a regression-driven workflow retrospective and explicit host/model evaluation records |

Upstream choices are not universal requirements. This collection does not inherit
mandatory parallel agents, tracker configuration, fixed document locations, a
required browser MCP, repeated approval at every stage, or blanket release
thresholds. The user's scope and the project's actual constraints govern the work.
Supporting templates remain inside their skill folder so a single-folder install
does not lose resources referenced from a repository-level directory.

## Review of the old main branch

| Gap and evidence | Why it mattered | Resolution |
| --- | --- | --- |
| README handed implementation to “the coding workflow you already trust”; no spec/build/test/ship skill existed | The requested lifecycle stopped at design, planning, and review | Add explicit stage contracts and four missing lifecycle skills |
| Generic review/design/writing/planning descriptions explicitly said backend | Automatic selection could miss UI, CLI, and library tasks | Broaden seven existing skills with surface-specific guidance, retaining backend specialists |
| PR review covered code risks but did not explicitly separate requirement coverage | A clean implementation of the wrong feature could look acceptable | Map criteria independently from implementation-quality findings |
| Plans lacked stable task/criterion identifiers and resume evidence | Later sessions could lose the active scope or trust stale completion | Add traceable IDs, one canonical task list, and state rechecks |
| No UI, browser QA, security, performance, refactoring, research, or delivery-automation workflows | Common engineering tasks lacked a focused artifact and completion criterion | Add specialists with bounded triggers and outputs |
| Maintenance docs existed, but no workflow for using session evidence | Improvements could become accumulating prompt rules | Add context, handoff, and retrospective skills plus cross-domain evaluation cases |

Backend debugging, distributed failure analysis, and database migrations retain
their specialist focus. Broadening the collection should not erase useful depth.
Existing names remain valid; no compatibility aliases or duplicate skill bodies
are needed. Installed copies still require deliberate comparison and replacement.

## Provenance and limits

Both reference repositories publish under MIT licenses. The added instructions
and templates are independently written; no upstream code, skill bodies, or plugin
configuration were imported. Future adaptations must retain applicable notices.

This review informed the design; it does not establish model performance. Local
validation checks structure and installation. Native host discovery and behavioral
evaluation require recorded runs in those tools, with the actual model/context.
