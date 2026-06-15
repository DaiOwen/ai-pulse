🌐 **多语言版本:** [English](README.en.md) · [中文](README.md) · [日本語](README.ja.md) · [Deutsch](README.de.md) · [한국어](README.ko.md)

<p align="center">
  <img src="assets/favicon.svg" width="64" alt="AI Pulse 标志" />
</p>

<h1 align="center">AI Pulse · AI 热点速览</h1>

<p align="center">
  <em>面向 AI 开发者的每日新闻智能聚合。零依赖，Claude Code 原生驱动。</em>
</p>

<p align="center">
  <img src="https://img.shields.io/github/stars/DaiOwen/ai-pulse?style=flat&color=yellow" alt="GitHub Stars">
  <img src="https://img.shields.io/badge/license-MIT-blue" alt="开源协议">
  <img src="https://img.shields.io/badge/dependencies-zero-brightgreen" alt="零依赖">
  <img src="https://img.shields.io/github/contributors/DaiOwen/ai-pulse?color=orange" alt="贡献者">
  <img src="https://img.shields.io/badge/PRs-welcome-orange" alt="欢迎 PR">
  <a href="https://daiowen.github.io/ai-pulse/"><img src="https://img.shields.io/badge/demo-live%20preview-6366f1?style=flat" alt="Live Demo"></a>
</p>

---

**AI Pulse** 是一款面向 AI 开发者的每日新闻智能聚合页，基于 [Claude Code](https://claude.ai) 自动驱动。每天早中晚三次自动采集 6+ 信源，智能去重、分类、生成精美的 HTML 页面。无需 npm、无需 Python、无需任何外部服务，仅需 Claude Code 和一个终端。

## 🔗 在线演示

**[https://daiowen.github.io/ai-pulse/](https://daiowen.github.io/ai-pulse/)**

无需安装，直接浏览器打开即可查看最新一期 AI 热点速览。

## 功能特色

- 🤖 **7 大内容板块** — 大模型动态、工具与部署、政策合规、论文速递、应用落地、开源热度、海外参考
- ⚡ **四级信息深度** — TL;DR(3秒) → 标题(10秒) → 摘要(30秒) → 原文全文
- 🎨 **Apple 设计美学** — 暗色/亮色双主题 + 动态光球背景 + 毛玻璃卡片
- 📱 **响应式布局** — 桌面端、平板、手机均流畅浏览
- 📅 **日历归档导航** — 交互式日历查看历史各期
- 🔍 **零依赖** — 纯 HTML/CSS/JS，无需构建工具或包管理器
- 🇨🇳 **中国 AI 生态优先** — 国产模型动态优先，政策合规重点追踪
- ⏰ **定时自动生成** — 每天 08:00 / 12:00 / 20:00 三次自动更新

## 快速开始

> **前提条件：** 安装 [Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview) CLI 并完成首次登录（`claude login`）。

**1. 克隆项目**

```bash
git clone https://github.com/DaiOwen/ai-pulse.git
cd ai-pulse
```

**2. 启动 Claude Code 并生成第一期**

在项目目录下启动 Claude Code 交互界面：
```bash
claude
```

Claude Code 会自动加载项目配置（`CLAUDE.md`）。在对话中输入斜杠命令：

```
/ai-digest morning
```

AI 将自动完成以下全流程：
- 从 6+ 信源搜索最新 AI 新闻（WebSearch）
- 深度抓取 Top 文章全文（WebFetch）
- 智能去重、评分、翻译、分类
- 生成完整 HTML 保存到 `archive/` 和 `index.html`

**3. 打开生成的主页**

```bash
open index.html    # macOS
start index.html   # Windows
```

或直接双击 `index.html` 在浏览器中打开。

首次运行后，定时任务自动注册（每天 08:00 / 12:00 / 20:00），后续无需手动操作。

> 💡 **`/ai-digest` 是什么？** 它不是终端命令，而是 **Claude Code 斜杠命令**——只在 Claude Code 对话里有效。打个比方：`git clone` 在终端里跑，`/ai-digest morning` 在 Claude Code 聊天框里输入。项目根目录的 `CLAUDE.md` 就像一份"AI 操作手册"，Claude Code 读取后自动按指令执行——不需要你写任何代码。

### 定时任务

首次手动运行后，自动注册三个定时任务：

| 任务 | 时间 | 覆盖范围 |
|------|------|----------|
| 🌅 早间版 | 08:00 | 昨夜海外动态 + 国内早间新闻 |
| ☀️ 午间版 | 12:00 | 上午增量更新 |
| 🌙 晚间版 | 20:00 | 全天汇总 + 开源数据 |

### 手动命令

| 命令 | 说明 |
|------|------|
| `/ai-digest morning` | 生成早间版 |
| `/ai-digest noon` | 生成午间版（增量） |
| `/ai-digest evening` | 生成晚间版（全天汇总） |
| `/ai-digest update` | 拉取上游最新代码，同步项目更新 |

### 更新机制

**在线演示（GitHub Pages）** — 全程自动化，无需人工干预：

```
Cron 触发 (08:00/12:00/20:00)
  → Claude Code 搜索采集 → 生成 HTML
  → git add & commit & push
  → GitHub Pages 自动部署（约 1-2 分钟后更新）
```

**自部署用户** — 两种方式获取最新内容：

| 方式 | 说明 |
|------|------|
| `git pull` | 拉取上游仓库已生成的最新 `index.html`，无需安装 Claude Code |
| `/ai-digest morning` | 自行运行生成命令，采集此刻最新新闻（需 Claude Code） |

如果 fork 了仓库并希望自己的 GitHub Pages 也自动更新，只需在本地保持 Claude Code 运行（Cron 定时任务 + git push 自动完成）。详见 [CLAUDE.md](CLAUDE.md)。

## 内容板块

| 板块 | 说明 |
|------|------|
| 🤖 大模型动态 | 国产优先 + 国际重大模型发布/更新 |
| 🛠️ 工具 & 部署 | 框架更新、国产硬件适配、推理部署方案 |
| 📋 政策 & 合规 | 网信办备案、AI 安全审查、行业标准 |
| 📄 论文速递 | 每日精选一篇有落地价值的 arXiv 论文 |
| 💡 应用落地 | 企业 AI 集成案例、最佳实践 |
| ⭐ 开源热度 | GitHub/Gitee Stars 上升 Top 10 + 关注度 Top 10 |
| 🌍 海外参考 | 精选 3 条影响国内的海外动态 |

## 技术架构

```
Cron 定时调度 (08:00 / 12:00 / 20:00)
       │
       ▼
Claude Code 启动
       │
       ├─ WebSearch（15-20 次多关键词搜索）
       ├─ WebFetch（Top 5-8 结果深度抓取）
       └─ GitHub/Gitee API（开源热度数据）
       │
       ▼
智能处理 Pipeline
  ① 去重（标题相似度 + URL 归一化）
  ② 评分（热度×0.4 + 时效×0.3 + 来源质量×0.3）
  ③ 翻译（海外新闻 → 中文摘要）
  ④ 分类（7 大板块）
  ⑤ 摘要生成（每条 2-3 句 + 开发者影响标注）
       │
       ▼
HTML 生成 & 归档
  • 生成完整自包含 HTML
  • 保存至 archive/YYYY-MM-DD-{edition}.html
  • 更新 index.html 为最新一期
```

## 项目结构

```
ai-pulse/
├── index.html              # 主页（最新一期 + 日历导航）
├── archive/                # 历史归档
│   └── YYYY-MM-DD-{edition}.html
├── assets/
│   └── favicon.svg         # 站点图标
├── design/                 # 设计稿参考
├── screenshots/            # 截图
├── .github/                # GitHub 配置
│   ├── ISSUE_TEMPLATE/
│   └── PULL_REQUEST_TEMPLATE.md
├── .claude/                # Claude Code 配置
│   ├── settings.json
│   └── scheduled_tasks.json
├── CLAUDE.md               # 项目指令 + Skill 定义
├── CONTRIBUTING.md         # 贡献指南
├── CODE_OF_CONDUCT.md      # 行为准则
├── ROADMAP.md              # 路线图
├── SECURITY.md             # 安全策略
├── CHANGELOG.md            # 更新日志
├── LICENSE                 # MIT 开源许可证
├── .gitignore
└── README.md
```

## 截图预览

### 🌙 暗色模式（默认）

![AI Pulse Dark Mode](screenshots/dark-mode.png)

### ☀️ 亮色模式

![AI Pulse Light Mode](screenshots/light-mode.png)

## 安全性 / Security

**数据和隐私安全是本项目的设计基石。** AI Pulse 100% 在本地运行，数据永不出户。

- 🏠 纯本地运行，无任何数据上传
- 🔌 生成的 HTML 页面零外部请求（无埋点、无遥测、无广告）
- 🔑 无需任何第三方 API 密钥或 Token
- 👁️ MIT 开源协议，代码完全透明可审计

详见 [SECURITY.md](SECURITY.md) 查看完整安全策略。

## 常见问题

**Q: 打开 index.html 没有内容？**
A: 需要先运行 `/ai-digest morning` 生成第一期内容。

**Q: 如何查看历史各期？**
A: 点击「往期回顾」按钮，日历弹窗展示当月所有日期和已生成的版次。

**Q: 定时任务没有运行？**
A: 在终端运行 `CronList` 检查任务状态，确保 Claude Code 处于运行状态。

**Q: 某天漏了生成？**
A: 手动运行对应版次的 `/ai-digest` 命令即可补生成。

**Q: 可以自定义内容板块吗？**
A: 可以——编辑 `CLAUDE.md` 中的分类规则即可调整板块优先级。

## 贡献指南 / Contributing

我们欢迎所有形式的贡献 — 报告 Bug、建议新功能、提交代码、改进文档。

请参阅 [CONTRIBUTING.md](CONTRIBUTING.md) 了解详细指南。

We welcome all forms of contributions — bug reports, feature requests, code submissions, and documentation improvements. See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

## 路线图 / Roadmap

请参阅 [ROADMAP.md](ROADMAP.md) 了解项目未来发展计划。

See [ROADMAP.md](ROADMAP.md) for the project's future development plans.

## 许可证 / License

本项目基于 MIT 许可证开源 — 详见 [LICENSE](LICENSE) 文件。

This project is open-sourced under the MIT License — see the [LICENSE](LICENSE) file for details.

---

<p align="center">
  基于 <a href="https://claude.ai">Claude Code</a> 构建 ·
  <a href="https://github.com/DaiOwen/ai-pulse">GitHub</a> ·
  <a href="https://daiowen.github.io/ai-pulse/">在线演示</a> ·
  <a href="CHANGELOG.md">更新日志</a>
</p>
