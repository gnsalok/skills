# Quick start for Codex, Claude Code, and Kiro

This collection provides reusable engineering workflows. Install a skill into a
project when it should travel with that repository, or into the user directory
when it should be available across local projects.

## 1. Clone and validate the collection

Python 3.10 or newer is required by the installer and validation scripts.

```bash
git clone https://github.com/gnsalok/skills.git
cd skills
python3 scripts/validate.py
```

The six lifecycle skills are a practical starting set:

```text
spec → implementation-plan → build → test → pr-review → ship
```

Install only the stages and specialist skills useful to the project. A small,
explicit selection is easier to evaluate than installing every skill at once.

## 2. Install skills into a project

Set `/path/to/project` to an existing repository. Preview the copy first:

```bash
python3 scripts/install.py --agent codex --project /path/to/project --skill spec --skill implementation-plan --skill build --skill test --skill pr-review --skill ship --dry-run
python3 scripts/install.py --agent claude --project /path/to/project --skill spec --skill implementation-plan --skill build --skill test --skill pr-review --skill ship --dry-run
python3 scripts/install.py --agent kiro --project /path/to/project --skill spec --skill implementation-plan --skill build --skill test --skill pr-review --skill ship --dry-run
```

Run the one command for the intended host again without `--dry-run` after
checking its destinations. The installer refuses to overwrite an existing skill.

| Host | Project location | Personal location | Explicit invocation |
| --- | --- | --- | --- |
| Codex | `.agents/skills/<name>/SKILL.md` | `~/.agents/skills/<name>/SKILL.md` | Select with `/skills` or mention `$<name>` |
| Claude Code | `.claude/skills/<name>/SKILL.md` | `~/.claude/skills/<name>/SKILL.md` | `/<name>` |
| Kiro | `.kiro/skills/<name>/SKILL.md` | `~/.kiro/skills/<name>/SKILL.md` | `/<name>` |

The installer supports project locations. For a personal installation, first
confirm that the destination does not already exist, then copy the complete
`skills/<name>/` folder into the host's personal location. Keep references,
scripts, templates, and other files alongside `SKILL.md`.

## 3. Start a fresh session and verify discovery

Open the target project in a new agent session, then explicitly invoke one skill:

```text
Codex:      $pr-review Review this branch against origin/main.
Claude Code: /pr-review Review this branch against origin/main.
Kiro:        /pr-review Review this branch against origin/main.
```

Confirm that the host shows or loads `pr-review`, rather than merely producing a
similar-looking answer. Codex and Claude Code can also select a skill automatically
from its description. Kiro supports automatic activation as well as slash commands.

If a skill is missing, check the folder name, front matter, installation scope,
and active project. Restart the session after installation when the host does not
detect the change immediately.

## 4. Use the skills as a flexible lifecycle

Invoke only the workflow needed for the current task. For example:

```text
/spec Define searchable settings, including keyboard behavior and URL state.
/implementation-plan Break the accepted scope into reviewable slices.
/build Implement the first agreed slice and run focused checks.
/test Verify the acceptance criteria and keep blocked checks visible.
/pr-review Review the exact diff against the accepted criteria.
/ship Assess this exact candidate for release readiness. Do not publish it.
```

Use the host's syntax from the table above. The stages are not mandatory ceremony:
a small fix may need only `build`, a focused check, and `pr-review`. Specialist
skills such as `frontend-design`, `database-migration`, or `security-review` can
be used independently when their trigger matches the work.

Skills provide instructions; they do not grant shell, browser, repository,
deployment, or network access. Existing host permissions and user authorization
still control every action.

## 5. Update carefully

Installed skills are copies and do not update automatically. Record the source
revision with `git rev-parse HEAD`. After pulling a newer collection revision,
compare the installed folder with its source, preserve local customizations, move
the old copy outside the discovery directory, and reinstall it. Restart the host
and rerun a representative scenario from [the evaluation guide](../evals/README.md).

For host-specific configuration, custom Kiro agents, nested repositories, cloud
sessions, and troubleshooting, read the longer [agent setup guide](agent-setup.md).

Official documentation:

- [Codex skills](https://developers.openai.com/codex/skills)
- [Claude Code skills](https://code.claude.com/docs/en/skills)
- [Kiro skills](https://kiro.dev/docs/skills/)
