# Behavioral evaluation

The cases in [scenarios.json](scenarios.json) are synthetic, manual regression
scenarios. They cover every skill and two unrelated prompts. They are not stored
model transcripts, automated model grades, or claims that a host/model has passed.
Structural CI checks ensure the cases stay well formed and cover the catalog.

## Run a case

Use a disposable project/session with no production credentials. Install the
selected skill for a focused test, or all skills when testing routing. Keep the
host's usual repository instructions but record them, since they affect results.

1. Record the collection commit, agent host/version, model identifier, date,
   tool permissions, and available repository context. Start a fresh session.
2. For **routing**, supply the case's `context` and `prompt` without naming a
   skill. Check whether the host selects the expected `skill`. `null` means no
   skill in this collection is needed. Record routing as unobservable if the host
   does not expose selection; do not infer activation from a plausible answer.
3. For **behavior**, explicitly request the expected skill and supply the same
   context/prompt. The supplied excerpts are the entire synthetic source of
   truth, not files claimed to exist in the current repository. If the host needs
   files, materialize the excerpts in the disposable project and record that setup.
4. Compare the output against each `expected` criterion and every `avoid` item.
   Save a redacted excerpt supporting each result. Do not award credit for merely
   repeating words from the checklist without addressing the scenario.
5. Repeat the changed cases and adjacent skills under the same configuration.
   For an upgrade or uncertain result, use at least three fresh runs; report the
   variation rather than picking the best answer.

For `null` cases, run routing only. Do not explicitly activate a skill and then
score it for declining to activate itself.

## Score and record

Use [the result template](result-template.md), one record per run:

- **Pass:** all expected criteria are supported and no forbidden behavior occurs.
- **Partial:** useful output with one or more missing criteria; list them.
- **Fail:** the central risk is missed, evidence is invented, or an avoid item occurs.
- **Blocked:** the evaluation cannot run because of missing host/access/context.
- **Not run:** no evaluation was attempted.

Track routing and behavior separately. An explicit-file prompt can test reasoning
but does not verify native discovery. Do not treat tests proposed by the agent as
tests executed, or mark a blocked case as a pass.

Before changing a model/tool default, run at least review-tenant-scope,
design-slow-exports, distributed-charge-unknown, and both negative controls.
When changing one skill, run its case and the closest neighboring workflow.
For project-specific tuning, add a redacted reproduction from real work and keep
the portable synthetic case as a baseline.

## Current baseline

No live Codex, Claude Code, or Kiro behavioral runs are recorded in this initial
collection. Installer and structural checks verify packaging only. Use this suite
to establish your baseline on the actual tools and models you use day to day.
