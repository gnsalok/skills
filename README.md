# Backend engineering skills

Practical workflows for a senior backend engineer working with coding agents.
Use them to review a change, explore a design, trace a failure, or leave a useful
document for the next engineer. They ask for evidence, make tradeoffs explicit,
and keep the next action small enough to verify.

The same skill files work with **Codex, Claude Code, and Kiro**. These are agent
tools, not fixed model versions: choose the model in your tool, then evaluate the
workflow with your repository. No API key, MCP server, or paid service is required
by this collection; your agent still needs its usual authentication and tools.

## Choose a skill

| Work | Skill | Result |
| --- | --- | --- |
| Review a PR or working diff | [pr-review](skills/pr-review/SKILL.md) | Prioritized findings with triggers, locations, fixes, and verification |
| Explore an architecture idea | [architecture-design](skills/architecture-design/SKILL.md) | Constraint-based options, recommendation, and a falsifiable experiment |
| Assess a system or RFC | [architecture-review](skills/architecture-review/SKILL.md) | Evidence-backed boundary and evolution risks, with incremental remedies |
| Check cross-process correctness | [distributed-systems-review](skills/distributed-systems-review/SKILL.md) | Invariants, failure windows, recovery mechanisms, and fault tests |
| Define or evolve a contract | [api-design](skills/api-design/SKILL.md) | Consumer behavior, errors, authorization, retries, and compatibility |
| Change persistent data | [database-migration](skills/database-migration/SKILL.md) | Staged migration/backfill plan, gates, and recovery limits |
| Write a durable explanation | [technical-writing](skills/technical-writing/SKILL.md) | A sourced RFC, ADR, runbook, README, or onboarding guide |
| Improve the development loop | [developer-experience](skills/developer-experience/SKILL.md) | Measured friction, a bounded improvement, and before/after evidence |
| Diagnose an error or slowdown | [backend-debugging](skills/backend-debugging/SKILL.md) | Reproduction, tested hypotheses, and a fix or next experiment |
| Break down an agreed change | [implementation-plan](skills/implementation-plan/SKILL.md) | Dependency-ordered slices with acceptance checks and rollout gates |

Start with one skill. Architecture design chooses an approach; architecture
review assesses an existing one; PR review examines a concrete change. A
distributed-systems review is useful when the risk is in partial failure or
concurrency rather than the shape of a module.

## Install in a project

Clone this repository outside the application you want to work on. The included
installer uses Python 3.10+ and the standard library. It copies complete skill
folders into the chosen project's native discovery directory, without symlinks,
network calls, or edits to your existing instruction files.

```bash
git clone https://github.com/gnsalok/skills.git
cd skills
python3 scripts/validate.py

# Replace /path/to/backend with an existing application directory.
python3 scripts/install.py --agent codex --project /path/to/backend --skill pr-review
python3 scripts/install.py --agent claude --project /path/to/backend --skill architecture-design
python3 scripts/install.py --agent kiro --project /path/to/backend --skill distributed-systems-review
```

Repeat `--skill` to select several, or use `--all` to install the collection.
Add `--dry-run` to inspect the paths first. Existing destination folders cause a
failure before any selected skill is copied; nothing is overwritten. See
[agent setup](docs/agent-setup.md) for discovery paths, invocation, updates,
Kiro custom-agent configuration, and a manual install alternative.

Start a new agent session in your application after installing. A prompt you can
use in all three tools is:

```text
Use the pr-review skill to review this branch against origin/main.
The goal is to make export retries safe. Focus on duplicate work and tenant
authorization. Review only, and report which tests you actually ran.
```

Codex also supports explicitly selecting a skill (commonly `$pr-review`), and
Claude Code exposes project skills as `/pr-review`. In Kiro, name the skill in
your request and confirm it is available to the selected agent. Explicit picker
syntax can change between tool versions; the path-based fallback is in the setup
guide. This repository does not install plugin commands or change your model.

## Use it in daily work

Give the agent a scope, the desired artifact, and any constraints it cannot infer.
It should read the repository before asking you to restate facts already there.

```text
Use architecture-design to explore async exports. Compare improving the current
request path with a background job. Keep the current database and include the
cost of operating either option. Draft a proposal; do not implement it yet.

Use distributed-systems-review on the invoice consumer. Check crash-after-charge,
concurrent redelivery, and replay after the dedupe retention period. Return a
failure-window table and local test cases.

Use technical-writing to create a runbook for queue lag from the worker config
and existing dashboards. Mark proposed thresholds and commands you cannot verify.

Use developer-experience to improve the single-test loop. Measure the current
path first, make one small change, and keep the full correctness checks intact.
```

For a larger change, use architecture-design → implementation-plan → the coding
workflow you already trust → pr-review. Bring in the narrower API, database, or
distributed-systems skill at the relevant seam. No skill requires installing or
automatically invoking another skill.

Skills guide reasoning; repository instructions and the user's scope still
apply. A review does not authorize a rewrite, deployment, incident intervention,
or publishing a document. Findings should cite evidence, and proposed checks
must stay distinct from checks that ran.

## Make the collection fit your workflow

Keep stable project facts in the application's instruction files: test commands,
service boundaries, glossary, ADR location, and operating constraints. Start with
the [project context example](docs/project-context.md). Keep reusable methods in
these skills; avoid copying every skill into always-loaded context.

When an agent misses something in real work, capture a redacted regression case,
change the smallest relevant instruction, and rerun that case on the tools/models
you use. Remove rules that no longer earn their context cost. See
[CONTRIBUTING](CONTRIBUTING.md) and the [evaluation guide](evals/README.md).

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

CI runs these dependency-free structural and installer checks. They do not prove
model behavior. The behavioral scenarios are a manual evaluation suite; record
the actual host, model, version, and outcomes when you run them. Native discovery
and behavior in Claude Code and Kiro still need a run in those tools; a copied
folder is not evidence of successful activation.

## Inspiration and direction

Inspired by [Addy Osmani's agent-skills](https://github.com/addyosmani/agent-skills)
and [Matt Pocock's skills](https://github.com/mattpocock/skills): explicit working
methods, repository context, and feedback that can prove or disprove a result.
The instructions here are independently written for backend engineering, without
importing their skill packs or command systems. The [design notes](docs/design.md)
record the source revisions considered, the initial plan, and future directions.
