# Specification outline

Use only the sections this change needs. Match an existing project template first.

- Identity: title, status, related issue/brief, source of accepted decisions.
- Problem and audience: current task, limitation, desired outcome.
- Scope: included capability, non-goals, constraints, dependencies.
- Behavior: examples and important state transitions; defined domain terms.
- Acceptance: stable criterion ID, input/precondition, observable result, failure case.
- Interfaces: existing public boundaries, compatibility, trust and data ownership.
- Verification: observable test boundary and existing commands or missing tooling.
- Delivery: rollout/distribution concerns and recovery limits if relevant.
- Questions: decision, why it matters, who can resolve it if known.

Example criterion for a CLI: `AC-2` — given a nonexistent input file, exit nonzero,
write a useful diagnostic to stderr, and leave stdout empty for pipeline callers.
It specifies caller behavior without prescribing the parser implementation.
