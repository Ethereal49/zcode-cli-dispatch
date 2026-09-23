import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


WRAPPER = Path(__file__).resolve().parents[1] / "bin/zcode-edit"


class ZCodeEditTests(unittest.TestCase):
    def test_standalone_cli_receives_fixed_edit_settings(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            cli = root / "zcode"
            capture = root / "args.json"
            cli.write_text(
                "#!/usr/bin/env python3\n"
                "import json, os, sys\n"
                "from pathlib import Path\n"
                "Path(os.environ['ZCODE_CAPTURE']).write_text(json.dumps(sys.argv[1:]))\n"
                "print(json.dumps({'response': 'done'}))\n"
            )
            cli.chmod(0o755)
            env = os.environ.copy()
            env.update(
                PATH=f"{root}{os.pathsep}{env.get('PATH', '')}",
                ZCODE_CAPTURE=str(capture),
            )
            run = subprocess.run(
                [sys.executable, str(WRAPPER), "Fix", "it"],
                cwd=root,
                env=env,
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(run.returncode, 0, run.stderr)
            self.assertEqual(run.stdout.strip(), "done")
            self.assertEqual(
                json.loads(capture.read_text()),
                [
                    "--prompt", "Fix it", "--cwd", str(root.resolve()),
                    "--mode", "yolo", "--json", "--disallowed-tools", "WebFetch,WebSearch",
                ],
            )


if __name__ == "__main__":
    unittest.main()
