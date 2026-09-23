# zcode-cli-dispatch

[![许可证：MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-3776AB?logo=python&logoColor=white)
![ZCode App 或 CLI](https://img.shields.io/badge/ZCode-App%20or%20CLI-5B5BD6)

[English](README.md)

这是一个非官方的轻量桥接工具，供 **Codex 和其他 coding agent** 将项目内的代码修改任务交给 ZCode Agent。调用方运行技能内附的 `scripts/zcode-edit`，随后检查实际改动并独立验收。它不替代 ZCode。

## 运行条件

- Python 3.9 或更新版本。
- 已配置可用的 ZCode Agent。**如果已将 ZCode.app 安装在 `/Applications/ZCode.app`，无需额外安装独立版 ZCode CLI**；这种方式还需要 `node` 在 `PATH` 中。
- 另一种方式是在 `PATH` 中安装官方独立版 `zcode` 命令。

脚本优先使用 `PATH` 中的 `zcode`；找不到时，调用 ZCode.app 内附的 Agent CLI，不修改应用及其 provider 配置。它固定传入 `--mode yolo`，ZCode 工具运行时不会逐项请求批准。内置 `WebFetch` 和 `WebSearch` 被禁用，但 `Bash` 或已配置的 MCP 工具仍可能访问网络。

## 安装

把这段话复制给你的 Agent 安装：

```text
请从 https://github.com/Ethereal49/zcode-cli-dispatch 安装 zcode-cli-dispatch Codex 技能。
```

手动安装（在本仓库目录执行）：

```sh
mkdir -p "$HOME/.codex/skills" && cp -R skills/zcode-cli-dispatch "$HOME/.codex/skills/"
```

无需另装 `zcode-edit` 命令。其他 coding agent 可以直接运行仓库中的 `skills/zcode-cli-dispatch/scripts/zcode-edit`。

## 使用

```sh
ZCODE_HEADLESS_CWD=/path/to/project ./skills/zcode-cli-dispatch/scripts/zcode-edit "修复解析错误，并添加一个针对性的测试。"
```

可用 `ZCODE_HEADLESS_CWD` 指定项目目录，用 `ZCODE_HEADLESS_TIMEOUT` 调整默认的 300 秒超时。命令只输出 ZCode 的最终答复；CLI 失败时返回非零状态。在已测试的 ZCode.app 环境中，headless 会话由 ZCode 保存，但不会作为桌面任务出现。

Codex 技能只把代码修改和测试编写分派给这个脚本；其他 coding agent 可以直接调用。浏览器、桌面、消息、上传和部署任务由调用方处理。ZCode 返回后，应检查实际 diff 并运行相关测试。

## 检查

```sh
python3 -m unittest discover -s tests -v
```

## 许可证

MIT，详见 [LICENSE](LICENSE)。ZCode 是独立项目，本仓库不打包 ZCode。
