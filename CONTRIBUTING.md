# Maintaining these skills

Treat a skill as a small engineering workflow with a testable purpose. Favor
changes based on actual development friction over general advice or longer
checklists. Use synthetic examples rather than private code or incident data.

## Change a skill

1. Capture the prompt, repository context, and observed failure or missing result.
2. Add or update a case in [evals/scenarios.json](evals/scenarios.json). Include
   expected behavior and a failure to avoid; test the nearest adjacent skill too.
3. Change the smallest relevant instruction. Keep the distinction between facts,
   assumptions, proposed checks, and executed results.
4. Run the structural/installer checks, then the relevant manual scenarios in your
   host. Compare the old and new skill under the same model and context when possible.
5. Include evidence and limitations in the PR. Record host/model/version when
   behavior is evaluated; “better response” without an example is not enough.

Do not retune the collection after one unexplained model output. Reproduce the
failure, inspect the supplied context, and check whether a missing project fact
belongs in the application instructions instead of the reusable skill.

## Add a skill

Use `skills/<lowercase-hyphenated-name>/SKILL.md`. The repository deliberately
uses a restricted front matter format: exactly two unquoted, single-line fields,
`name` and `description`. The name matches the directory; the description says
what the skill does and when it should be selected. Avoid YAML-significant `: `
or ` #` in those values. The validator enforces this convention, not all YAML.

Describe the evidence to inspect, the sequence of work, decisions that depend on
context, expected artifact, validation, and stopping condition. Use only sections
that serve that workflow. Keep a skill under 200 lines; move supporting material
into its own `references/`, `templates/`, or `scripts/` directory when needed.

A copied skill folder must be sufficient. Use relative Markdown links for local
resources and keep them inside the same skill. Do not require another skill,
host-specific tools, subagents, automatic publishing, or a particular model.
New skill-owned scripts need meaningful tests and should preserve authentication,
TLS, artifact checks, and the user's existing files.

Add the skill to the README and evaluation scenarios. Document a new trigger
rather than making several descriptions match the same everyday request.

## Validate

From the repository root, with Python 3.10+:

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
python3 -m unittest discover -s evals/fixtures/report-cli/tests -v
```

The validator checks skill metadata, size, self-contained resource links, local
Markdown link targets, catalog coverage, and evaluation coverage. It is a
repository-specific check, not a full Markdown/YAML renderer or a model judge.
CI runs the same commands without vendor API credentials.

Use [the evaluation guide](evals/README.md) to assess activation and output.
After changing a description, also run routing cases with all skills installed.
After changing installation paths, test native discovery in the affected host;
an installer unit test cannot establish that the host loaded a skill.

## Compatibility and evolution

Keep the `pr-review` entry point stable. Prefer retaining other names too; if a
rename is necessary, document how installed copies should be removed or migrated.
Copies do not update automatically, and a rename can leave an old skill installed.

For a host/model upgrade, rerun one review, one design, one failure-analysis case,
and the negative controls. Record what ran and what did not. Revisit the directory
mappings against official host documentation before changing installation logic.

Do not import upstream skill packs as a substitute for a focused workflow. If
adapting any source material, include the source, revision, license, and required
notices. Keep attribution separate from a claim of behavioral verification.

## Review the collection as it grows

Start with the requested artifact, not a new topic keyword. Check the catalog for
an existing workflow before adding one. A distinct trigger, decision sequence,
and result justify a new skill; extra background reading can be a packaged reference.
Keep the six lifecycle entry points useful on their own and preserve existing names.

For broad skills, include at least one non-service scenario (UI, library, CLI, or
tooling). When adding a release or external-action workflow, include a readiness-only
case and a missing-evidence case. Test that unrelated prompts do not activate a
large workflow. When skills overlap, state the boundary in their descriptions and
in the workflow guide rather than adding circular instructions to call each other.

After a host/model upgrade or repeated failure, use `workflow-retrospective` to
classify the issue before editing prompts. Record source revision/date for new
external inspiration in the comparative review; keep imported material's license
when directly adapting it. Update the changelog for new skills or behavior changes.
