---
name: session-handoff
description: Capture the current task's decisions, implementation state, verification, and next step for a fresh session or another engineer. Use when pausing, switching context, or resuming long work without repeating discovery.
---

# Leave a resumable handoff

Read the active goal and recent decisions, then verify current repository state.
Capture the branch/commit and working-tree changes; identify edits owned by the
user versus this task when known. A handoff describes state, not a transcript.

## Preserve what the next session cannot infer cheaply

Record the accepted scope and corrections, canonical spec/plan paths, important
constraints, decisions with reasons, completed work, and outstanding tasks. Link
to durable artifacts rather than copying them. Mark temporary paths explicitly;
they may disappear between machines or sessions.

For verification, include command, working directory, revision/state tested,
observed result, and relevant failure evidence. Separate successful checks from
skipped or proposed ones. Record external actions actually completed, such as a
PR URL, without inventing their status from an attempted command.

List unresolved hypotheses, unsuccessful approaches worth avoiding, missing
credentials/access by name only, and the smallest next action. Authorization is
scoped: record an existing release instruction accurately, but do not expand it
or treat an old approval as applying to a different artifact or destination.

## Save and resume deliberately

Use the requested location or existing project convention, preserving other
handoffs. If none is given, provide the handoff in the response and suggest a
durable path when cross-session persistence matters. Consult the optional
[outline](references/handoff-outline.md) for a long task.

Exclude credentials, customer data, hidden instructions, and unnecessary personal
information. Do not send the handoff to another person or service unless requested.

Tell the next session to recheck status, artifact availability, and external state
before continuing. Completion means it can identify the active task, trust the
scope of recorded evidence, and take one concrete next step without redoing the
whole investigation.
