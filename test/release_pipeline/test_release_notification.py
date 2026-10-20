"""Protect release notification and replay without accessing GitHub."""

import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


WORKFLOWS = Path(__file__).resolve().parents[2] / ".github/workflows"
NOTIFY = (WORKFLOWS / "notify-sdk-release.yml").read_text()


class ReleaseNotificationTests(unittest.TestCase):
    """Release-please must call the notifier explicitly instead of relying on events."""

    def test_release_please_chains_only_new_releases(self):
        """Pass the actual created tag to the reusable notification job."""
        workflow = (WORKFLOWS / "release-please.yml").read_text()
        self.assertIn("release_created: ${{ steps.release.outputs.release_created }}", workflow)
        self.assertIn("if: needs.release-please.outputs.release_created == 'true'", workflow)
        self.assertIn("uses: ./.github/workflows/notify-sdk-release.yml", workflow)
        self.assertIn("tag: ${{ needs.release-please.outputs.tag_name }}", workflow)
        self.assertIn("  workflow_call:\n", NOTIFY)
        self.assertIn("  workflow_dispatch:\n", NOTIFY)
        self.assertIn("types: [published]", NOTIFY)

    def run_notification(self, **environment):
        """Run notification shell with a recording GitHub CLI double."""
        script = NOTIFY.split("        run: |\n", 1)[1]
        script = "\n".join(line[10:] for line in script.splitlines())
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            gh = root / "gh"
            gh.write_text(f"""#!{sys.executable}
import json, os, sys
with open(os.environ["COMMAND_LOG"], "a") as output:
    output.write(json.dumps(sys.argv[1:]) + "\\n")
if sys.argv[-1] == ".draft":
    if os.environ.get("RELEASE_MISSING") == "true":
        sys.exit(1)
    print(os.environ.get("DRAFT", "false"))
""")
            gh.chmod(0o755)
            log = root / "commands.jsonl"
            result = subprocess.run(
                ["bash", "-e", "-c", script],
                env={
                    **os.environ,
                    "PATH": f"{root}:{os.environ['PATH']}",
                    "COMMAND_LOG": str(log),
                    "GH_TOKEN": "test-dispatch-token",
                    "RELEASE_READ_TOKEN": "test-read-token",
                    "GITHUB_REPOSITORY": "kangaroorewards/api-docs",
                    "TAG": "v0.0.685",
                    **environment,
                },
                capture_output=True, text=True,
            )
            commands = [json.loads(line) for line in log.read_text().splitlines()] if log.exists() else []
            return result, commands

    def test_existing_published_release_dispatches_without_recreating_it(self):
        """A replay sends only the release lookup and SDK dispatch requests."""
        result, commands = self.run_notification()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(commands, [
            ["api", "repos/kangaroorewards/api-docs/releases/tags/v0.0.685", "--jq", ".draft"],
            ["api", "repos/kangaroorewards/Kangaroo-App-SDK/dispatches",
             "-f", "event_type=api-docs-release", "-f", "client_payload[tag]=v0.0.685"],
        ])

    def test_invalid_or_unpublished_releases_and_missing_token_fail(self):
        """Do not notify the SDK after invalid input or a failed release lookup."""
        for environment in (
            {"TAG": "master"},
            {"DRAFT": "true"},
            {"RELEASE_MISSING": "true"},
            {"GH_TOKEN": ""},
        ):
            with self.subTest(environment=environment):
                result, commands = self.run_notification(**environment)
                self.assertNotEqual(result.returncode, 0)
                self.assertFalse(any("event_type=api-docs-release" in command for command in commands))


if __name__ == "__main__":
    unittest.main()
