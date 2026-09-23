# zcode-cli-dispatch

An unofficial Codex skill and small Python wrapper for delegating project-local code edits to ZCode Agent. ZCode performs the edit; the calling agent reviews the changed files and runs the relevant checks.

## Requirements

- Python 3.9 or newer.
- A configured `zcode` CLI on `PATH`, or ZCode.app at `/Applications/ZCode.app` with `node` on `PATH` (macOS fallback).

The wrapper uses the standalone `zcode` command when available. Otherwise, it starts the Agent CLI bundled in ZCode.app without changing the app or its provider configuration. It always passes `--mode yolo`, so ZCode tools run without approval prompts. `WebFetch` and `WebSearch` are disabled, but this does not block network access through other tools such as `Bash` or configured MCP servers.

## Install

```sh
mkdir -p "$HOME/.local/bin" "$HOME/.codex/skills"
install -m 755 bin/zcode-edit "$HOME/.local/bin/zcode-edit"
cp -R skills/zcode-cli-dispatch "$HOME/.codex/skills/"
```

If `zcode-cli-dispatch` is already installed as a Codex skill, replace its old files with the files in `skills/zcode-cli-dispatch/`.

## Use

```sh
cd /path/to/project
zcode-edit "Fix the parsing bug and add a focused test."
```

Set `ZCODE_HEADLESS_CWD` to choose a project without changing directories. Set `ZCODE_HEADLESS_TIMEOUT` to change the default 300-second limit. The command prints only ZCode's final reply and returns a nonzero status on CLI failure. In the tested ZCode.app setup, headless sessions are stored by ZCode but do not appear as Desktop tasks.

The Codex skill routes only code changes and test writing to this command. Browser, desktop, messaging, upload, and deployment work stays with the calling agent. Review the actual diff and run relevant tests after ZCode finishes.

## Check

```sh
python3 -m unittest discover -s tests -v
```

## License

MIT. See [LICENSE](LICENSE). ZCode is a separate project and is not bundled here.
