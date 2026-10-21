import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from install import AGENTS, install
from validate import validate_collection, validate_links, validate_skill


def make_skill(root, name="demo"):
    folder = root / "skills" / name
    folder.mkdir(parents=True)
    path = folder / "SKILL.md"
    path.write_text(
        f"---\nname: {name}\ndescription: Use when a synthetic development task needs review.\n---\n\n# Demo\n\nInspect evidence and return a result.\n",
        encoding="utf-8",
    )
    return path


class ToolTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.source = self.root / "source"
        self.path = make_skill(self.source)
        self.project = self.root / "project"
        self.project.mkdir()

    def test_valid_skill(self):
        self.assertEqual(validate_skill(self.path), [])

    def test_missing_metadata(self):
        self.path.write_text("# Only a heading\n")
        self.assertTrue(validate_skill(self.path))

    def test_name_must_match_directory(self):
        text = self.path.read_text().replace("name: demo", "name: wrong")
        self.path.write_text(text)
        self.assertTrue(any("name must match" in e for e in validate_skill(self.path)))

    def test_duplicate_metadata_rejected(self):
        self.path.write_text("---\nname: demo\nname: demo\n---\n# Demo\n")
        self.assertTrue(any("duplicate" in e for e in validate_skill(self.path)))

    def test_yaml_significant_description_rejected(self):
        self.path.write_text(self.path.read_text().replace("Use when", "Task: use when"))
        self.assertTrue(any("plain single-line" in e for e in validate_skill(self.path)))

    def test_instruction_budget(self):
        self.path.write_text(self.path.read_text() + "line\n" * 201)
        self.assertTrue(any("budget" in e for e in validate_skill(self.path)))

    def test_broken_resource_link(self):
        self.path.write_text(self.path.read_text() + "\n[Guide](references/missing.md)\n")
        self.assertTrue(any("missing local link" in e for e in validate_links(self.path, self.path.parent)))

    def test_skill_cannot_link_outside_package(self):
        other = make_skill(self.source, "other")
        self.path.write_text(self.path.read_text() + "\n[Other](../other/SKILL.md)\n")
        self.assertTrue(other.is_file())
        self.assertTrue(any("escapes its package" in e for e in validate_links(self.path, self.path.parent)))

    def test_valid_packaged_resource_and_external_link(self):
        (self.path.parent / "guide.md").write_text("# Guide\n")
        self.path.write_text(self.path.read_text() + "\n[Guide](guide.md#section) [Web](https://example.com)\n")
        self.assertEqual(validate_links(self.path, self.path.parent), [])

    def test_installs_complete_folders_for_all_hosts(self):
        (self.path.parent / "reference.txt").write_text("resource")
        references = self.path.parent / "references"
        references.mkdir()
        (references / "outline.md").write_text("# Packaged outline\n")
        self.path.write_text(self.path.read_text() + "\n[Outline](references/outline.md)\n")
        for agent, directory in AGENTS.items():
            with self.subTest(agent=agent):
                targets = install(self.source, self.project, agent, ["demo"])
                target = self.project.resolve() / directory / "demo"
                self.assertEqual(targets, [target])
                self.assertEqual((target / "SKILL.md").read_bytes(), self.path.read_bytes())
                self.assertEqual((target / "reference.txt").read_text(), "resource")
                self.assertEqual((target / "references/outline.md").read_text(), "# Packaged outline\n")
                self.assertEqual(validate_links(target / "SKILL.md", target), [])
                self.assertFalse(target.is_symlink())

    def test_repeat_install_preserves_personalization(self):
        target = install(self.source, self.project, "codex", ["demo"])[0]
        (target / "SKILL.md").write_text("personalized")
        with self.assertRaisesRegex(ValueError, "already exists"):
            install(self.source, self.project, "codex", ["demo"])
        self.assertEqual((target / "SKILL.md").read_text(), "personalized")

    def test_all_selections_preflight_before_copy(self):
        make_skill(self.source, "other")
        install(self.source, self.project, "codex", ["other"])
        with self.assertRaisesRegex(ValueError, "already exists"):
            install(self.source, self.project, "codex", ["demo", "other"])
        self.assertFalse((self.project / AGENTS["codex"] / "demo").exists())

    def test_unknown_skill_prevents_any_copy(self):
        with self.assertRaises(ValueError):
            install(self.source, self.project, "codex", ["demo", "missing"])
        self.assertEqual(list(self.project.iterdir()), [])

    def test_dry_run_does_not_create_directories(self):
        targets = install(self.source, self.project, "claude", ["demo"], dry_run=True)
        self.assertEqual(len(targets), 1)
        self.assertEqual(list(self.project.iterdir()), [])

    def test_rejects_symlinked_destination_ancestor(self):
        external = self.root / "elsewhere"
        external.mkdir()
        (self.project / ".agents").symlink_to(external, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, "ancestor"):
            install(self.source, self.project, "codex", ["demo"])
        self.assertEqual(list(external.iterdir()), [])

    def test_rejects_dangling_destination_symlink(self):
        parent = self.project / AGENTS["codex"]
        parent.mkdir(parents=True)
        (parent / "demo").symlink_to(self.root / "missing")
        with self.assertRaisesRegex(ValueError, "already exists"):
            install(self.source, self.project, "codex", ["demo"])

    def test_rejects_symlinked_source_resource(self):
        (self.path.parent / "external.txt").symlink_to(self.path)
        with self.assertRaisesRegex(ValueError, "symlinks"):
            install(self.source, self.project, "codex", ["demo"])

    def test_rejects_path_traversal(self):
        with self.assertRaisesRegex(ValueError, "invalid skill name"):
            install(self.source, self.project, "codex", ["../demo"])

    def test_missing_project_is_not_created(self):
        missing = self.root / "absent"
        with self.assertRaisesRegex(ValueError, "existing directory"):
            install(self.source, missing, "codex", ["demo"])
        self.assertFalse(missing.exists())

    def make_collection(self):
        (self.source / "README.md").write_text("# Skills\n\n[Demo](skills/demo/SKILL.md)\n")
        (self.source / "CONTRIBUTING.md").write_text("# Contributing\n")
        (self.source / "evals").mkdir()
        cases = [
            {"id": "demo", "skill": "demo", "prompt": "Review it", "context": "An example", "expected": ["Cite evidence"], "avoid": ["Invent facts"]},
            {"id": "negative", "skill": None, "prompt": "Say hello", "context": "No task", "expected": ["Say hello"], "avoid": ["Review code"]},
        ]
        (self.source / "evals/scenarios.json").write_text(json.dumps(cases))
        return cases

    def test_collection_coverage(self):
        self.make_collection()
        self.assertEqual(validate_collection(self.source), [])

    def test_optional_root_document_links_are_checked(self):
        self.make_collection()
        (self.source / "AGENTS.md").write_text("# Instructions\n\n[Missing guide](docs/missing.md)\n")
        errors = validate_collection(self.source)
        self.assertTrue(any("AGENTS.md" in e and "missing local link" in e for e in errors))

    def test_missing_catalog_entry(self):
        self.make_collection()
        (self.source / "README.md").write_text("# No catalog\n")
        self.assertTrue(any("catalog entry" in e for e in validate_collection(self.source)))

    def test_missing_skill_scenario(self):
        cases = self.make_collection()
        (self.source / "evals/scenarios.json").write_text(json.dumps(cases[1:]))
        self.assertTrue(any("no behavioral scenario" in e for e in validate_collection(self.source)))

    def test_duplicate_scenario_ids(self):
        cases = self.make_collection()
        cases[1]["id"] = cases[0]["id"]
        (self.source / "evals/scenarios.json").write_text(json.dumps(cases))
        self.assertTrue(any("unique" in e for e in validate_collection(self.source)))

    def test_missing_negative_control(self):
        cases = self.make_collection()
        (self.source / "evals/scenarios.json").write_text(json.dumps(cases[:1]))
        self.assertTrue(any("negative control" in e for e in validate_collection(self.source)))


if __name__ == "__main__":
    unittest.main()
