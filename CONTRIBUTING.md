# Contributing to AI Pulse / 贡献指南

🎉 Welcome! Thank you for your interest in contributing to AI Pulse.
🎉 欢迎！感谢您对 AI Pulse 的关注和贡献。

## Table of Contents / 目录

- [Code of Conduct / 行为准则](#code-of-conduct--行为准则)
- [How to Contribute / 如何贡献](#how-to-contribute--如何贡献)
- [Development Setup / 开发环境](#development-setup--开发环境)
- [Code Style / 代码风格](#code-style--代码风格)
- [Adding News Sources / 添加新闻源](#adding-news-sources--添加新闻源)
- [Customizing Sections / 自定义板块](#customizing-sections--自定义板块)
- [Pull Request Process / PR 流程](#pull-request-process--pr-流程)

---

## Code of Conduct / 行为准则

Please be respectful and constructive in all interactions. This project welcomes contributors of all backgrounds.
请在所有交流中保持尊重和建设性。本项目欢迎来自各种背景的贡献者。

## How to Contribute / 如何贡献

### Reporting Bugs / 报告 Bug

1. Check existing [Issues](https://github.com/DaiOwen/ai-pulse/issues) to avoid duplicates.
2. Use the **Bug Report** template when creating a new issue.
3. Provide clear steps to reproduce and your environment details.

---

1. 先查看已有的 [Issues](https://github.com/DaiOwen/ai-pulse/issues) 避免重复。
2. 新建 Issue 时请使用 **Bug Report** 模板。
3. 提供清晰的复现步骤和环境信息。

### Suggesting Features / 建议功能

1. Use the **Feature Request** template.
2. Describe the use case and why it would benefit the project.
3. If possible, suggest an implementation approach.

---

1. 请使用 **Feature Request** 模板。
2. 描述使用场景及其对项目的价值。
3. 如有可能，请提出实现思路。

### Submitting Code / 提交代码

1. **Fork** the repository.
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Make your changes.
4. Test your changes locally.
5. Commit with clear messages (see style below).
6. Push to your fork and open a **Pull Request**.

---

1. **Fork** 本仓库。
2. 创建新分支：`git checkout -b feature/your-feature-name`
3. 进行修改。
4. 本地测试修改。
5. 提交清晰的 commit 信息（见下方规范）。
6. Push 到您的 Fork 并提交 **Pull Request**。

## Development Setup / 开发环境

AI Pulse requires only:
- [Claude Code](https://claude.ai) (latest version)
- A terminal (bash, zsh, PowerShell, etc.)

No npm, Python, or build tools needed.

### Quick Start

```bash
git clone https://github.com/DaiOwen/ai-pulse.git
cd ai-pulse
# Claude Code will auto-load the project config
# Run /ai-digest morning to generate the first edition
```

## Code Style / 代码风格

### Commit Messages / 提交信息

- Use English for commit messages
- Follow the [Conventional Commits](https://www.conventionalcommits.org/) format:
  - `feat:` — new feature
  - `fix:` — bug fix
  - `docs:` — documentation
  - `chore:` — maintenance
  - `refactor:` — code refactoring
  - `perf:` — performance improvement

Examples:
```
feat: add WeChat official accounts as news source
fix: resolve date format issue in archive calendar
docs: update README with new screenshots
```

### HTML / CSS / JS

- Follow existing patterns in `index.html`
- Use semantic HTML5 elements
- Keep CSS classes descriptive and consistent
- Prefer vanilla JS — no external dependencies
- Comment complex logic in Chinese (for maintainability)

### CLAUDE.md

- All feature instructions go in `CLAUDE.md`
- Keep section headings clear
- Update the skill definition when adding new commands

## Adding News Sources / 添加新闻源

To add a new news source to the daily aggregation:

1. Open `.claude/settings.json` or `CLAUDE.md`
2. Add the source URL + description to the search configuration
3. Update the relevant section in `CLAUDE.md` if needed
4. Test by running `/ai-digest morning`

**Guidelines:**
- Prefer sources with good API or stable HTML structure
- Chinese-language sources are prioritized for domestic sections
- Add RSS/Atom feeds when available for more reliable fetching
- Verify the source is still active periodically

---

要添加新的新闻源到每日聚合：

1. 打开 `.claude/settings.json` 或 `CLAUDE.md`
2. 在搜索配置中添加源 URL 和描述
3. 如有需要，更新 `CLAUDE.md` 中的相关板块
4. 运行 `/ai-digest morning` 测试

**指南：**
- 优先选择有良好 API 或稳定 HTML 结构的源
- 国内板块优先使用中文源的新闻
- 可用时优先添加 RSS/Atom 订阅源以提升抓取可靠性
- 定期验证源是否仍然可用

## Customizing Sections / 自定义板块

The 7 content sections are defined in `CLAUDE.md`. To customize:

1. Edit the section definitions in `CLAUDE.md`
2. Adjust the classification rules if needed
3. Update the HTML generation logic in `CLAUDE.md`
4. Test by running `/ai-digest morning`

You can:
- Change section names and descriptions
- Adjust the number of items per section
- Reorder sections
- Add or remove sections entirely

---

7 个内容板块在 `CLAUDE.md` 中定义。要自定义：

1. 编辑 `CLAUDE.md` 中的板块定义
2. 根据需要调整分类规则
3. 更新 `CLAUDE.md` 中的 HTML 生成逻辑
4. 运行 `/ai-digest morning` 测试

您可以：
- 修改板块名称和描述
- 调整每个板块的文章数量
- 重排板块顺序
- 增加或删除板块

## Pull Request Process / PR 流程

1. Ensure your code builds cleanly (no errors or warnings).
2. Update documentation if your changes affect usage.
3. Fill out the **Pull Request Template** completely.
4. Request review from maintainers.
5. Address review feedback promptly.
6. Once approved, a maintainer will merge your PR.

---

1. 确保代码无报错或警告。
2. 如果更改影响使用，请更新文档。
3. 完整填写 **Pull Request Template**。
4. 请求维护者进行 Review。
5. 及时处理 Review 反馈。
6. 审核通过后，维护者会合并您的 PR。

---

<p align="center">
  <strong>Thank you for contributing! / 感谢您的贡献！</strong>
</p>
