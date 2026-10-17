#!/usr/bin/env python3
"""Copy selected skills into a project's native agent directory, without overwrite."""

import argparse
import shutil
import sys
from pathlib import Path

from validate import NAME, ROOT, validate_collection, validate_skill

AGENTS = {"codex": ".agents/skills", "claude": ".claude/skills", "kiro": ".kiro/skills"}


def install(source_root, project, agent, names, dry_run=False):
    if not project.is_dir():
        raise ValueError(f"project must be an existing directory: {project}")
    project = project.resolve()
    if agent not in AGENTS:
        raise ValueError(f"unknown agent: {agent}")
    if not names or len(names) != len(set(names)):
        raise ValueError("select at least one skill, without duplicates")
    parent = project
    for part in Path(AGENTS[agent]).parts:
        parent = parent / part
        if parent.is_symlink() or (parent.exists() and not parent.is_dir()):
            raise ValueError(f"destination ancestor must be a real directory: {parent}")
    operations = []
    for name in names:
        if not NAME.fullmatch(name):
            raise ValueError(f"invalid skill name: {name}")
        source = source_root / "skills" / name
        if source.is_symlink():
            raise ValueError(f"source must not be a symlink: {source}")
        errors = validate_skill(source / "SKILL.md")
        if errors:
            raise ValueError("\n".join(errors))
        target = parent / name
        if target.exists() or target.is_symlink():
            raise ValueError(f"destination already exists; preserve and compare it before updating: {target}")
        operations.append((source, target))
    # Preflight every selection before creating directories or copying any files.
    if not dry_run:
        for source, target in operations:
            shutil.copytree(source, target)
    return [target for _, target in operations]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--agent", required=True, choices=AGENTS)
    parser.add_argument("--project", required=True, type=Path)
    selection = parser.add_mutually_exclusive_group(required=True)
    selection.add_argument("--skill", action="append", dest="names")
    selection.add_argument("--all", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    try:
        errors = validate_collection(ROOT)
        if errors:
            raise ValueError("\n".join(errors))
        names = sorted(p.parent.name for p in (ROOT / "skills").glob("*/SKILL.md")) if args.all else args.names
        targets = install(ROOT, args.project, args.agent, names, args.dry_run)
    except (OSError, ValueError) as exc:
        parser.exit(1, f"error: {exc}\n")
    for target in targets:
        print(f"{'Would install' if args.dry_run else 'Installed'}: {target}")
    if not args.dry_run:
        print("Start a new agent session in the project and verify skill discovery.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
