# Report CLI evaluation fixture

This is synthetic baseline code for a build-skill evaluation, not a production
tool. It intentionally has no `--json` mode. Copy the whole directory into a
disposable project before asking an agent to implement the feature; keep this
baseline unchanged so future evaluations start from the same behavior.

Requires Python 3.10+ with no third-party dependencies. From this directory:

```bash
python3 report.py --count 3
python3 -m unittest discover -s tests -v
```

The first command prints `Items: 3` and exits zero. Invalid or negative counts
exit nonzero with diagnostics on stderr and no stdout. Default count is zero.

The evaluation task is to add optional `--json` output containing a JSON object
with integer field `count`, followed by a newline. Keep the human-readable
default and error behavior compatible. Tests added during an evaluation should
exercise the process as a consumer and verify failure behavior in both modes.

For the user-edit preservation case, add a personal note below in the disposable
copy before running the agent. Record the initial tree/diff and ensure the agent
does not remove or absorb that note into an unrelated change.

## Personal note

Leave the baseline blank here; customize only the disposable copy.
