# AI 脉搏 · AI热点速览

面向中国 AI 开发工程师的每日 AI 新闻智能聚合页。**只需安装 Claude Code，clone 项目即可运行。**

## 快速开始

```bash
git clone https://github.com/DaiOwen/ai-pulse.git
cd ai-pulse
```

进入目录后 Claude Code 自动加载项目配置。运行一次手动采集：

```
/ai-digest morning
```

之后每天早中晚自动运行（07:49 / 12:17 / 20:13），无需任何操作。

用浏览器打开 `index.html` 即可查看最新一期。

## 工作原理

1. Claude Code 在每天 07:49 / 12:17 / 20:13 自动触发采集
2. WebSearch + WebFetch 从 6+ 信源聚合 AI 新闻
3. Claude 智能去重、评分、翻译、分类、生成摘要
4. 生成精美 HTML 存入 `archive/`，同步更新 `index.html`

**零依赖**：不需要 npm、Python、数据库或任何外部服务。只需要 Claude Code。
**零配置**：clone 后 Claude Code 自动读取项目配置，首次运行自动创建权限和定时任务。

## 板块结构

| 板块 | 说明 |
|------|------|
| 🤖 大模型动态 | 国产优先 + 国际重大模型发布/更新 |
| 🛠️ 工具 & 部署 | 框架更新、国产硬件适配、推理部署方案 |
| 📋 政策 & 合规 | 网信办备案、AI 安全审查、行业标准 |
| 📄 论文速递 | 每日精选一篇有落地价值的 arXiv 论文 |
| 💡 应用落地 | 企业 AI 集成案例、最佳实践 |
| ⭐ 开源热度 | GitHub/Gitee Stars 上升 Top10 + 关注度 Top10 |
| 🌍 海外参考 | 精选 3 条影响中国的海外动态 |

## 项目结构

```
├── index.html           # 主页（最新一期）
├── archive/             # 历史归档
├── assets/              # CSS / 图标
├── design/              # 设计稿预览
├── .claude/             # 权限 + 定时任务配置
├── CLAUDE.md            # 项目指令 + Skill 定义
└── README.md
```

## 设计

- 🇨🇳 为中国 AI 开发者定制
- ⚡ 30 秒扫读全貌（TL;DR 条 + 分层信息架构）
- 🎨 Apple 设计美学（暗色科技风 + 深色/浅色模式切换）
- 🤖 Claude Code 驱动，纯 HTML/CSS/JS 输出
