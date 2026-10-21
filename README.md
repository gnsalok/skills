# Engineering skills

A personal collection of practical workflows for working with coding agents across
applications, libraries, CLIs, services, and developer tooling. Use one skill for a
focused task, or connect them across the full development lifecycle. The methods
are evidence-based and portable across **Codex, Claude Code, and Kiro**.

## From an idea to a release

```text
DEFINE          PLAN                 BUILD        VERIFY       REVIEW       SHIP
Idea / spec  →  Spec / task slices →  Code      →  Test/debug →  QA gate   →  Release
/spec           /plan                /build       /test        /review      /ship
```

The slash labels describe the workflow. The installed skills are:

| Stage | Skill | Input → output |
| --- | --- | --- |
| Define | [spec](skills/spec/SKILL.md) | Chosen direction → scope, criterion IDs, assumptions, and a spec/PRD |
| Plan | [implementation-plan](skills/implementation-plan/SKILL.md) | Defined scope → ordered tasks, dependencies, acceptance checks |
| Build | [build](skills/build/SKILL.md) | Authorized task → implemented slices and verification evidence |
| Verify | [test](skills/test/SKILL.md) | Changed behavior → risk-based checks and observed outcomes |
| Review | [pr-review](skills/pr-review/SKILL.md) | Diff and criteria → actionable findings and merge recommendation |
| Ship | [ship](skills/ship/SKILL.md) | Exact candidate and evidence → readiness decision and authorized release |

`/plan` and `/review` are **not installed aliases**. Invoke `implementation-plan`
and `pr-review` by their real names; hosts may reserve these shorter commands.
Claude Code commonly exposes skills as `/spec`, `/implementation-plan`, etc.;
Codex supports explicit skill selection, commonly `$spec`; in Kiro, request the
skill by name. Use the host's selector if syntax differs. See [agent setup](docs/agent-setup.md).

The stages are useful boundaries, not a mandatory ceremony. Skip a separate spec
for a clear typo fix. Start at review for an existing PR. Continue already
authorized work across stages; stop for a genuinely missing decision, prerequisite,
or action outside scope. A readiness assessment does not itself authorize release.

See [worked workflows](docs/workflows.md) for a UI feature, a CLI change, and a
service change, including what each stage hands to the next.

## Find the right skill

Each folder is standalone. Install only what you need; another skill is never a
hidden prerequisite. The six lifecycle skills above form a useful starting set.

### Explore and design

| Skill | When to use it | Concrete result |
| --- | --- | --- |
| [idea-refinement](skills/idea-refinement/SKILL.md) | The problem or direction is still vague | Decision brief, alternatives, assumptions, smallest experiment |
| [research](skills/research/SKILL.md) | External facts or tool compatibility are uncertain | Versioned sources, findings, tradeoffs, unanswered questions |
| [architecture-design](skills/architecture-design/SKILL.md) | Choose a technical approach or module boundary | Realistic options, interface examples, recommendation |
| [architecture-review](skills/architecture-review/SKILL.md) | Assess an existing system or RFC | Structural risks, evidence, incremental remedies |
| [api-design](skills/api-design/SKILL.md) | Define a library, CLI, HTTP, RPC, or event contract | Caller-visible behavior, errors, compatibility cases |

### Build and improve

| Skill | When to use it | Concrete result |
| --- | --- | --- |
| [frontend-design](skills/frontend-design/SKILL.md) | Design or implement an interface | Responsive layout, interaction states, accessible behavior |
| [refactoring](skills/refactoring/SKILL.md) | Working code is costly to understand or change | Bounded structural improvement with preserved behavior |
| [developer-experience](skills/developer-experience/SKILL.md) | Setup, preview, build, or test loops are painful | Measured friction and a verified improvement |
| [technical-writing](skills/technical-writing/SKILL.md) | Explain a decision, procedure, or API | Sourced RFC, ADR, runbook, README, tutorial, or guide |

### Verify and operate

| Skill | When to use it | Concrete result |
| --- | --- | --- |
| [browser-verification](skills/browser-verification/SKILL.md) | Check an existing web journey in a browser | Repro steps, state/viewport evidence, runtime findings |
| [security-review](skills/security-review/SKILL.md) | Assess trust boundaries or threats | Credible abuse paths, findings, mitigations, validation limits |
| [performance-investigation](skills/performance-investigation/SKILL.md) | A measured latency/memory/rendering problem exists | Reproducible baseline, profiles, comparable results |
| [ci-cd](skills/ci-cd/SKILL.md) | Build or fix delivery automation | Reproducible jobs, appropriate permissions, verified gates |
| [observability](skills/observability/SKILL.md) | Behavior is hard to diagnose | Operating questions mapped to signals and actions |

### Keep the backend specialties

| Skill | When to use it | Concrete result |
| --- | --- | --- |
| [backend-debugging](skills/backend-debugging/SKILL.md) | Diagnose service errors or intermittent failures | Reproduction, hypotheses, causal evidence, fix or next probe |
| [distributed-systems-review](skills/distributed-systems-review/SKILL.md) | Check cross-process state and failure | Invariants, failure windows, recovery mechanisms, fault tests |
| [database-migration](skills/database-migration/SKILL.md) | Change persistent schema or data | Compatible stages, bounded backfill, validation and recovery limits |

### Maintain your agent workflow

| Skill | When to use it | Concrete result |
| --- | --- | --- |
| [agent-context](skills/agent-context/SKILL.md) | Agents repeatedly miss project facts or conventions | Focused instructions and reliable navigation pointers |
| [session-handoff](skills/session-handoff/SKILL.md) | Pause or transfer a long task | Current state, decisions, evidence, concrete next action |
| [workflow-retrospective](skills/workflow-retrospective/SKILL.md) | Learn from a session or tool/model change | Prioritized improvements and regression cases |

Select by the requested artifact: `spec` defines behavior; `architecture-design`
chooses a technical approach; `implementation-plan` sequences work. `test` owns
verification evidence; `pr-review` judges a diff; `ship` judges and, when authorized,
executes a specific release. The [workflow guide](docs/workflows.md) explains overlaps.

## Install in a project

The installer requires Python 3.10+ and the standard library. It copies complete
skill folders into the selected tool's project directory, with no network calls,
symlinks, or edits to your existing instruction files.

```bash
git clone https://github.com/gnsalok/skills.git
cd skills
python3 scripts/validate.py

# Replace /path/to/project with an existing application/library/tool checkout.
python3 scripts/install.py --agent codex --project /path/to/project --skill spec --skill implementation-plan --skill build --skill test --skill pr-review --skill ship
python3 scripts/install.py --agent claude --project /path/to/project --skill frontend-design --skill browser-verification
python3 scripts/install.py --agent kiro --project /path/to/project --skill agent-context --skill session-handoff
```

Add `--dry-run` to inspect paths, or use `--all` instead of `--skill` to install
everything. Existing destinations cause failure before any selected skill is
copied. The [setup guide](docs/agent-setup.md) covers manual installation, updates,
Kiro custom-agent resources, and explicit-file fallback when discovery is unavailable.
Start a new session in your project and verify the selected skill is available.

Codex, Claude Code, and Kiro are agent tools, not fixed model versions. Choose your
model in the host and evaluate the workflow on that combination. These skills do
not install a model, browser, MCP server, or runtime dependency; some tasks need
those capabilities supplied by the project or host.

## Example requests

```text
Use idea-refinement to challenge whether this reporting dashboard solves the
operator's problem. Compare a smaller intervention before proposing a platform.

Use spec to define searchable settings for this UI, including keyboard behavior,
empty results, and URL state. Then use implementation-plan to sequence the work.

Use build to implement the agreed CLI JSON-output feature. Preserve the existing
human-readable default and prove the output is usable by a real process consumer.

Use test to check the changed behavior, then pr-review to review the diff against
its acceptance criteria. Keep failed, skipped, and unrun checks visible.

Use ship to assess this package version for release. Prepare the consumer smoke
check and recovery plan; this request is readiness review only.

Use workflow-retrospective to identify one improvement after this session. Include
an example prompt that would catch the same failure after a model upgrade.
```

## Maintain it for yourself

Keep stable project facts in the application, using the [project context example](docs/project-context.md).
Keep reusable methods here. Capture a redacted failure from real work, change the
smallest relevant instruction, and rerun the case plus a neighboring/unrelated
prompt. Remove obsolete rules instead of continually appending more instructions.

Existing skill names remain stable, including `pr-review`, `implementation-plan`,
and `backend-debugging`. Installed copies do not auto-update: compare and preserve
customizations before replacing them. See [CONTRIBUTING](CONTRIBUTING.md), the
[evaluation guide](evals/README.md), and the [changelog](CHANGELOG.md).

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
python3 -m unittest discover -s evals/fixtures/report-cli/tests -v
```

CI checks metadata, packaged resource links, catalog/scenario coverage, and installer
behavior. These checks do not prove model quality or native skill activation.
Behavioral scenarios are manual and record the actual host/model/version and
results. A proposed experiment is never reported as an executed check.

## Inspiration

This collection draws on [Addy Osmani's agent-skills](https://github.com/addyosmani/agent-skills)
and [Matt Pocock's skills](https://github.com/mattpocock/skills). The workflows are
independently written for this collection. The [comparative review](docs/reference-review.md)
records source revisions, what was learned, and what was deliberately changed;
[design notes](docs/design.md) explain the collection's maintenance boundaries.
