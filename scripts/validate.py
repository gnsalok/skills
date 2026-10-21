#!/usr/bin/env python3
"""Dependency-free checks for this repository's intentionally small skill format."""

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")
LINK = re.compile(r"!?\[[^\]]*\]\(([^\s)]+)\)")


def validate_skill(path):
    errors = []
    if path.is_symlink() or any(p.is_symlink() for p in path.parent.rglob("*")):
        return [f"{path}: skill folders must not contain symlinks"]
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        return [f"{path}: {exc}"]
    lines = text.splitlines()
    if len(lines) < 5 or lines[0] != "---" or lines[3] != "---":
        return [f"{path}: expected name and description in four-line front matter"]
    fields = {}
    for line in lines[1:3]:
        match = re.fullmatch(r"(name|description): (\S.*)", line)
        if not match or match[1] in fields:
            errors.append(f"{path}: invalid or duplicate metadata field")
            continue
        value = match[2]
        if ": " in value or " #" in value or value[0] in "[]{}&*!|>'\"%@`":
            errors.append(f"{path}: use plain single-line metadata values")
        fields[match[1]] = value
    if set(fields) != {"name", "description"}:
        errors.append(f"{path}: name and description are required")
    name = fields.get("name", "")
    if not NAME.fullmatch(name) or len(name) > 64 or name != path.parent.name:
        errors.append(f"{path}: name must match its lowercase-hyphenated directory")
    if not 20 <= len(fields.get("description", "")) <= 1024:
        errors.append(f"{path}: description must contain 20–1024 characters")
    if not any(line.startswith("# ") for line in lines[4:]):
        errors.append(f"{path}: missing body heading")
    if len(lines) > 200:
        errors.append(f"{path}: exceeds the 200-line instruction budget")
    return errors


def validate_links(path, boundary):
    errors = []
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        return [f"{path}: {exc}"]
    # Fenced examples are not rendered links. This is not a general Markdown parser.
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    for target in LINK.findall(text):
        url = urlsplit(target)
        if url.scheme or url.netloc or not url.path:
            continue
        destination = (path.parent / unquote(url.path)).resolve()
        if not destination.is_relative_to(boundary.resolve()):
            errors.append(f"{path}: local link escapes its package: {target}")
        elif not destination.exists():
            errors.append(f"{path}: missing local link target: {target}")
    return errors


def validate_collection(root):
    errors = []
    skills_dir = root / "skills"
    skill_dirs = sorted(p for p in skills_dir.iterdir() if p.is_dir()) if skills_dir.is_dir() else []
    if not skill_dirs:
        return [f"{root}: no skill folders found"]
    for directory in skill_dirs:
        if directory.is_symlink():
            errors.append(f"{directory}: skill directory must not be a symlink")
        else:
            errors.extend(validate_skill(directory / "SKILL.md"))
    markdown = sorted({root / "README.md", root / "CONTRIBUTING.md", *root.glob("*.md")})
    for directory in (skills_dir, root / "docs", root / "evals"):
        markdown.extend(directory.rglob("*.md"))
    for path in markdown:
        if not path.is_file():
            errors.append(f"{path}: required document missing")
            continue
        boundary = root
        if path.is_relative_to(skills_dir):
            boundary = skills_dir / path.relative_to(skills_dir).parts[0]
        errors.extend(validate_links(path, boundary))
    readme = root / "README.md"
    if readme.is_file():
        catalog = readme.read_text(encoding="utf-8")
        for directory in skill_dirs:
            if f"(skills/{directory.name}/SKILL.md)" not in catalog:
                errors.append(f"{readme}: missing catalog entry for {directory.name}")
    try:
        scenarios = json.loads((root / "evals/scenarios.json").read_text(encoding="utf-8"))
        if not isinstance(scenarios, list) or not scenarios:
            raise ValueError("expected a nonempty scenario list")
        ids, covered = set(), set()
        names = {p.name for p in skill_dirs}
        for case in scenarios:
            if not isinstance(case, dict):
                raise ValueError("each scenario must be an object")
            case_id = case.get("id")
            if not isinstance(case_id, str) or not case_id or case_id in ids:
                raise ValueError("scenario IDs must be unique nonempty strings")
            ids.add(case_id)
            skill = case.get("skill")
            if skill is not None and skill not in names:
                raise ValueError(f"{case_id}: unknown skill {skill}")
            for field in ("prompt", "context"):
                if not isinstance(case.get(field), str) or not case[field].strip():
                    raise ValueError(f"{case_id}: missing {field}")
            for field in ("expected", "avoid"):
                values = case.get(field)
                if not isinstance(values, list) or not values or not all(isinstance(x, str) and x.strip() for x in values):
                    raise ValueError(f"{case_id}: {field} must list concrete criteria")
            covered.add(skill)
        for name in sorted(names - covered):
            errors.append(f"{root}: no behavioral scenario for {name}")
        if None not in covered:
            errors.append(f"{root}: add an unrelated-prompt negative control")
    except (OSError, UnicodeError, ValueError, TypeError) as exc:
        errors.append(f"{root}/evals/scenarios.json: {exc}")
    return errors


def main():
    errors = validate_collection(ROOT)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    count = len(list((ROOT / "skills").glob("*/SKILL.md")))
    print(f"PASS: {count} skills; metadata, local links, catalog, and scenario coverage")
    return 0


if __name__ == "__main__":
    sys.exit(main())
