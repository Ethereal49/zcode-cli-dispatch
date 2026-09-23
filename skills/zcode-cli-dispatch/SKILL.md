---
name: zcode-cli-dispatch
description: Use when delegating self-contained project-local code changes or test writing to ZCode headless CLI. Excludes browser, desktop, messaging, uploads, and deployment tasks.
---

# ZCode CLI Dispatch

Route project-local code changes to the local ZCode CLI. Use it for edits, refactors, and test writing; handle standalone planning, analysis, and review here. Anything that needs a browser, desktop app, GUI interaction, external service login, or system-level action stays here. The wrapper requires an existing working ZCode provider configuration; it does not change provider settings. Task scope is an eligibility rule, not a filesystem sandbox.

## Eligibility check

Before dispatching, confirm the request:

- operates only on files and commands inside a project workspace;
- does not require opening or controlling a browser, desktop app, terminal emulator, or OS window;
- does not need screenshots, clipboard, notifications, messaging, email, uploads, deployments, or account authentication;
- has a clear deliverable (code change or test file).

If any condition fails, handle it in the current environment instead.

## How to dispatch

Use `~/.local/bin/zcode-edit`. It accepts the prompt as arguments and returns only the final assistant reply.

```bash
cd /path/to/project
~/.local/bin/zcode-edit "Fix the off-by-one in src/parser.ts and add a focused test."
```

To target a project without changing directory:

```bash
ZCODE_HEADLESS_CWD=/path/to/project ~/.local/bin/zcode-edit "Refactor auth middleware into a shared helper."
```

Optional environment variables:

| Variable | Default | Meaning |
|----------|---------|---------|
| `ZCODE_HEADLESS_CWD` | current directory | Project directory the task runs in |
| `ZCODE_HEADLESS_TIMEOUT` | `300` | Maximum runtime in seconds |

The wrapper always runs ZCode in `yolo` mode. `Agent` and `Task` are available when the CLI exposes them; `WebFetch` and `WebSearch` remain disabled. `yolo` skips tool approvals and is not a filesystem sandbox. The caller runs relevant tests and verifies the diff after ZCode returns.

## Result handling

- The command exits `0` on success and prints the final reply. It does not edit the user's ZCode provider configuration.
- Non-zero exit means the CLI failed; treat stderr as the error and do not retry automatically. Timeout exits `124`.
- The reply is plain text. If it includes a code change, verify it yourself by reading the diff or running the relevant test before reporting completion.
- ZCode sessions created this way are stored in `~/.zcode/cli/db/db.sqlite` but do not appear in the Desktop app's task list.
