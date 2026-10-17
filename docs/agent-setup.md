# Agent setup

Each `skills/<name>/SKILL.md` has portable `name` and `description` front matter.
The body contains the workflow. There are no host-specific tool names, mandatory
subagents, plugin manifests, or hidden shared files to install.

## Project discovery paths

| Tool | Project path | User-level path for manual installation |
| --- | --- | --- |
| Codex | `.agents/skills/<name>/SKILL.md` | `~/.agents/skills/<name>/SKILL.md` |
| Claude Code | `.claude/skills/<name>/SKILL.md` | `~/.claude/skills/<name>/SKILL.md` |
| Kiro IDE / default CLI agent | `.kiro/skills/<name>/SKILL.md` | `~/.kiro/skills/<name>/SKILL.md` |

Use project scope first to keep the workflow associated with a repository. The
included installer supports project scope only. For global installation, copy
the selected complete folder to the user-level path after checking for an
existing skill with the same name. Avoid multiple copies of the same skill in
global and project scope; resolution rules differ by host/version.

From the root of this collection:

```bash
python3 scripts/install.py --agent codex --project /path/to/backend --skill pr-review --dry-run
python3 scripts/install.py --agent codex --project /path/to/backend --skill pr-review
```

Use `--agent claude` or `--agent kiro` for the other hosts. `--all` and `--skill`
are mutually exclusive. The project must already exist. The installer refuses
destination conflicts and symlinked destination directories; inspect those paths
manually instead of letting an install write outside the selected project.

For a manual install, first confirm that the destination skill does not exist.
Create the parent discovery directory, then copy the complete skill folder:

```text
<clone>/skills/pr-review/ → <application>/.agents/skills/pr-review/
```

Choose `.claude` or `.kiro` for the other hosts. Copy resources inside the folder
as well if a future skill includes them. You can also ask the host to read the
absolute path to a `SKILL.md` for one session without installing it. That is an
explicit-file workflow, not a native discovery test.

## Codex

Start a new session in the target application and check its skill selector. Select
`pr-review` or ask “Use the pr-review skill to review this branch against
origin/main.” Explicit skill mentions commonly use `$pr-review`; follow the
selector presented by your installed client if its syntax differs.

Keep project commands and invariants in `AGENTS.md`, without pasting all of these
skill bodies into it. Do not assume installing a skill grants a tool, network
access, GitHub permissions, or a runtime service.

Official reference: [Codex skills](https://developers.openai.com/codex/skills).

## Claude Code

Start a new Claude Code session in the target application. Use `/pr-review` or
ask for the skill by name. Confirm the skill appears in the available skills
before relying on automatic selection. Do not assume Claude.ai uploads or API
skill APIs use the same local directory installation.

Keep local project conventions in `CLAUDE.md` or the instruction mechanism your
team already maintains. These skills need no `allowed-tools` expansion or hooks.

Official reference: [Claude Code skills](https://code.claude.com/docs/en/skills).

## Kiro IDE and CLI

Install under `.kiro/skills/` and start a new session in the project. Ask “Use the
distributed-systems-review skill on the invoice consumer.” Check the active
agent's loaded skills if it does not pick up the request.

The default CLI agent discovers the standard skills directory. For a **custom
CLI agent**, merge an entry like this into its existing `resources` array in
`.kiro/agents/<agent>.json`; preserve its other resources and settings:

```json
{
  "resources": ["skill://.kiro/skills/**/SKILL.md"]
}
```

This is a configuration fragment, not a complete replacement custom-agent file.
Use the corresponding user-directory pattern if installing globally. Kiro
steering files hold durable project context; leave task methods in the skills.

Official references: [Kiro skills](https://kiro.dev/docs/skills/) and
[CLI skill resources](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#skill-resources).

## Verify activation, then evaluate behavior

1. Check that the installed file exists at the native path and restart the session.
2. Confirm the skill is discoverable in the host, not just readable as a file.
3. In a disposable project, explicitly request one skill with a concrete task.
   Check its characteristic output, such as cited review findings or failure windows.
4. Run the matching [evaluation scenario](../evals/README.md). Include an adjacent
   skill and an unrelated prompt to check routing as well as answer quality.

The directory mappings and Kiro custom-agent fragment were cross-checked against
the skills CLI's agent registry and guidance. Direct vendor documentation access
was blocked in the authoring environment; the links above are the primary source
to recheck when upgrading. Local copy/validation checks are automated; native
activation and model behavior are not claimed as verified by those checks.

## Updating or removing a skill

Installations are copies. Record the source commit with `git rev-parse HEAD` when
installing. After pulling an update, compare your installed folder with the new
source (`diff -ru` is useful on Unix). Preserve local changes, move the old folder
to a backup outside the host's discovery directory, then reinstall. The installer
has no overwrite flag, so an update cannot silently discard personalization.

Restart the agent and rerun a representative scenario after an update. To remove
a skill, remove only its installed folder after preserving local customizations;
leave other skills and host configuration alone.
