# zcode-cli-dispatch

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-3776AB?logo=python&logoColor=white)
![ZCode App or CLI](https://img.shields.io/badge/ZCode-App%20or%20CLI-5B5BD6)

[简体中文](README.zh-CN.md)

An unofficial bridge for **Codex and other coding agents** to delegate project-local code edits to ZCode Agent. The calling agent runs the bundled `scripts/zcode-edit`, then reviews the changed files and verifies the result. This wrapper does not replace ZCode.

## Requirements

- Python 3.9 or newer.
- A configured ZCode Agent. **If ZCode.app is installed at `/Applications/ZCode.app`, no separate ZCode CLI installation is needed**; this path also requires `node` on `PATH`.
- Alternatively, an official standalone `zcode` command on `PATH`.

The wrapper uses the standalone `zcode` command when available. Otherwise, it starts the Agent CLI bundled in ZCode.app without changing the app or its provider configuration. It always passes `--mode yolo`, so ZCode tools run without approval prompts. `WebFetch` and `WebSearch` are disabled, but this does not block network access through other tools such as `Bash` or configured MCP servers.

## Install

Copy this to your coding agent to install:

```text
Install the zcode-cli-dispatch Codex skill from https://github.com/Ethereal49/zcode-cli-dispatch.
```

Manual install (from this repository):

```sh
mkdir -p "$HOME/.codex/skills" && cp -R skills/zcode-cli-dispatch "$HOME/.codex/skills/"
```

No separate `zcode-edit` installation is needed. Other coding agents can run `skills/zcode-cli-dispatch/scripts/zcode-edit` directly from a clone of this repository.

## Use

In Codex, send your agent:

```text
Use $zcode-cli-dispatch to fix the parsing bug in this project and add a focused test. Review the changes and run the test afterward.
```

The Codex skill routes only code changes and test writing to ZCode. Browser, desktop, messaging, upload, and deployment work stays with the calling agent.

### Direct script (optional)

Other coding agents can invoke the bundled script directly:

```sh
ZCODE_HEADLESS_CWD=/path/to/project ./skills/zcode-cli-dispatch/scripts/zcode-edit "Fix the parsing bug and add a focused test."
```

Set `ZCODE_HEADLESS_CWD` to choose a project without changing directories. Set `ZCODE_HEADLESS_TIMEOUT` to change the default 300-second limit. The command prints only ZCode's final reply and returns a nonzero status on CLI failure. In the tested ZCode.app setup, headless sessions are stored by ZCode but do not appear as Desktop tasks. Review the actual diff and run relevant tests after ZCode finishes.

## Check

```sh
python3 -m unittest discover -s tests -v
```

## License

MIT. See [LICENSE](LICENSE). ZCode is a separate project and is not bundled here.
