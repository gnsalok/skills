# Release record outline

- Candidate: commit, artifact identifier/digest, version, relevant configuration.
- Destination and audience: environment/registry, selected release scope.
- Authority: requested action or existing release agreement; unresolved decisions.
- Evidence: required check, candidate tested, result and evidence location.
- Compatibility: consumers, flags, mixed versions, migration ordering if applicable.
- Rollout: stage, observed signal, advance/hold/stop condition, responsible role.
- Recovery: reversible steps, persistent effects, restore/forward-repair prerequisites.
- Outcome: ready/not ready/insufficient evidence; deployed/published only if verified.
- Follow-up: observation window, residual risks, cleanup, ownership to confirm.

For a package release, “rollback” may mean stopping adoption and publishing a
fixed version. Do not promise that deleting a tag removes already downloaded code.
