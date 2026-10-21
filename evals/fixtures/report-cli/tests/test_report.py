import subprocess
import sys
import unittest
from pathlib import Path

REPORT = Path(__file__).resolve().parents[1] / "report.py"


class ReportTests(unittest.TestCase):
    def run_report(self, *arguments):
        return subprocess.run(
            [sys.executable, str(REPORT), *arguments],
            capture_output=True,
            text=True,
            check=False,
        )

    def test_default_output(self):
        result = self.run_report()
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "Items: 0\n")
        self.assertEqual(result.stderr, "")

    def test_explicit_count(self):
        result = self.run_report("--count", "3")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "Items: 3\n")
        self.assertEqual(result.stderr, "")

    def test_invalid_integer(self):
        result = self.run_report("--count", "many")
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "")
        self.assertIn("count must be an integer", result.stderr)

    def test_negative_count(self):
        result = self.run_report("--count", "-1")
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "")
        self.assertIn("count must be nonnegative", result.stderr)


if __name__ == "__main__":
    unittest.main()
