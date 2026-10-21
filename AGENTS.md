# Working on this collection

Read [CONTRIBUTING.md](CONTRIBUTING.md) before editing skills and
[docs/design.md](docs/design.md) for the maintenance decisions.

The product is the workflow inside each `skills/<name>/SKILL.md`. Keep names
stable, triggers distinct, and each folder independently installable. Supporting
resources stay inside the skill that uses them. Host-specific setup belongs in
[docs/agent-setup.md](docs/agent-setup.md), not copied into every skill.

Update the README catalog and `evals/scenarios.json` when adding a skill. Use
synthetic cases and preserve attribution when adapting external material.

Validation from the repository root:

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
python3 -m unittest discover -s evals/fixtures/report-cli/tests -v
```

Structural checks and installer tests do not prove native discovery or model
behavior. Report those outcomes separately, with actual evidence when available.
