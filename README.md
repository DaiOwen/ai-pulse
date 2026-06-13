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
</p>

---

**AI Pulse** 是一款面向 AI 开发者的每日新闻智能聚合页，基于 [Claude Code](https://claude.ai) 自动驱动。每天早中晚三次自动采集 6+ 信源，智能去重、分类、生成精美的 HTML 页面。无需 npm、无需 Python、无需任何外部服务，仅需 Claude Code 和一个终端。

## 功能特色

- 🤖 **7 大内容板块** — 大模型动态、工具与部署、政策合规、论文速递、应用落地、开源热度、海外参考
- ⚡ **四级信息深度** — TL;DR(3秒) → 标题(10秒) → 摘要(30秒) → 原文全文
- 🎨 **Apple 设计美学** — 暗色/亮色双主题 + 动态光球背景 + 毛玻璃卡片
- 📱 **响应式布局** — 桌面端、平板、手机均流畅浏览
- 📅 **日历归档导航** — 交互式日历查看历史各期
- 🔍 **零依赖** — 纯 HTML/CSS/JS，无需构建工具或包管理器
- 🇨🇳 **中国 AI 生态优先** — 国产模型动态优先，政策合规重点追踪
- ⏰ **定时自动生成** — 每天 07:49 / 12:17 / 20:13 三次自动更新

## 快速开始

```bash
# 1. 克隆项目
git clone https://github.com/DaiOwen/ai-pulse.git
cd ai-pulse

# 2. 生成第一期
（Claude Code 自动加载项目配置）
/ai-digest morning

# 3. 用浏览器打开 index.html
```

首次运行时，Claude Code 将自动：
- 从 6+ 信源搜索最新 AI 新闻（WebSearch）
- 深度抓取 Top 文章全文（WebFetch）
- 智能去重、评分、翻译、分类
- 生成完整 HTML 保存到 `archive/` 和 `index.html`

### 定时任务

首次手动运行后，自动注册三个定时任务：

| 任务 | 时间 | 覆盖范围 |
|------|------|----------|
| 🌅 早间版 | 07:49 | 昨夜海外动态 + 国内早间新闻 |
| ☀️ 午间版 | 12:17 | 上午增量更新 |
| 🌙 晚间版 | 20:13 | 全天汇总 + 开源数据 |

### 手动命令

| 命令 | 说明 |
|------|------|
| `/ai-digest morning` | 生成早间版 |
| `/ai-digest noon` | 生成午间版（增量） |
| `/ai-digest evening` | 生成晚间版（全天汇总） |

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
Cron 定时调度 (07:49 / 12:17 / 20:13)
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
│   ├── favicon.svg         # 站点图标
│   └── social-preview.svg  # 社交媒体预览图
├── design/                 # 设计稿参考
├── .github/                # GitHub 配置
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md   # Bug 报告模板
│   │   └── feature_request.md # 功能建议模板
│   └── PULL_REQUEST_TEMPLATE.md # PR 模板
├── .claude/                # Claude Code 配置
│   ├── settings.json       # 权限配置
│   └── scheduled_tasks.json # 定时任务（运行时）
├── CLAUDE.md               # 项目指令 + Skill 定义
├── CONTRIBUTING.md         # 贡献指南（中英双语）
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

---

## 贡献指南 / Contributing

我们欢迎所有形式的贡献 — 报告 Bug、建议新功能、提交代码、改进文档。

请参阅 [CONTRIBUTING.md](CONTRIBUTING.md) 了解详细指南。

We welcome all forms of contributions — bug reports, feature requests, code submissions, and documentation improvements. See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

## 许可证 / License

本项目基于 MIT 许可证开源 — 详见 [LICENSE](LICENSE) 文件。

This project is open-sourced under the MIT License — see the [LICENSE](LICENSE) file for details.

---

<p align="center">
  基于 <a href="https://claude.ai">Claude Code</a> 构建 ·
  <a href="https://github.com/DaiOwen/ai-pulse">GitHub</a> ·
  <a href="https://github.com/DaiOwen/ai-pulse/blob/main/CHANGELOG.md">更新日志</a>
</p>
