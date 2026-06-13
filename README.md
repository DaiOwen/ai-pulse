# AI 脉搏 · AI热点速览

面向中国 AI 开发工程师的每日 AI 新闻智能聚合页。基于 Claude Code 本地驱动，每天早中晚三次自动采集、整理、生成精美 HTML。

> **只需安装 Claude Code，clone 项目即可运行。零外部依赖，零手动配置。**

## 页面预览

### 暗色模式（默认）

> 打开 `index.html` 即可看到最新一期。深色渐变背景 + 动态光球 + 毛玻璃卡片，Apple 设计风格。

### 亮色模式

> 右上角滑块一键切换，自动记住偏好。

| 板块 | 说明 |
|------|------|
| 🤖 大模型动态 | 国产优先 + 国际重大模型发布/更新 |
| 🛠️ 工具 & 部署 | 框架更新、国产硬件适配、推理部署方案 |
| 📋 政策 & 合规 | 网信办备案、AI 安全审查、行业标准 |
| 📄 论文速递 | 每日精选一篇有落地价值的 arXiv 论文 |
| 💡 应用落地 | 企业 AI 集成案例、最佳实践 |
| ⭐ 开源热度 | GitHub/Gitee Stars 上升 Top10 + 关注度 Top10 |
| 🌍 海外参考 | 精选 3 条影响中国的海外动态 |

## 快速开始

### 1. 克隆项目

```bash
git clone https://github.com/DaiOwen/ai-pulse.git
cd ai-pulse
```

### 2. 生成第一期

进入项目目录后，Claude Code 自动加载配置。在终端运行：

```
/ai-digest morning
```

Claude 会：
- 从 6+ 信源搜索最新 AI 新闻（WebSearch）
- 深度抓取原文获取详情（WebFetch）
- 智能去重、评分、翻译、分类
- 生成完整 HTML 保存到 `archive/` 和 `index.html`

### 3. 查看结果

用浏览器打开 `index.html`：
```
双击项目根目录下的 index.html
```

### 4. 自动运行

首次运行后，自动注册三个定时任务：

| 任务 | 时间 | 说明 |
|------|------|------|
| 🌅 早间版 | 每天 07:49 | 覆盖昨夜海外 + 国内早间 |
| ☀️ 午间版 | 每天 12:17 | 增量更新上午新消息 |
| 🌙 晚间版 | 每天 20:13 | 全天汇总 + 开源全天数据 |

无需任何操作，每天自动更新。

## 手动命令

| 命令 | 说明 |
|------|------|
| `/ai-digest morning` | 生成早间版 |
| `/ai-digest noon` | 生成午间版（增量） |
| `/ai-digest evening` | 生成晚间版（全天汇总） |

## 技术架构

```
Cron 定时调度 (07:49 / 12:17 / 20:13)
       │
       ▼
Claude Code 启动
       │
       ├─ WebSearch（15-20 次多关键词搜索）
       ├─ WebFetch（Top5-8 结果深度抓取）
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
  • 保存 archive/YYYY-MM-DD-{edition}.html
  • 更新 index.html 为最新一期
```

## 设计特色

- 🇨🇳 为中国 AI 开发者定制 — 国产模型动态优先，政策合规重点关注
- ⚡ 四级信息深度 — TL;DR(3秒) → 标题(10秒) → 摘要(30秒) → 原文
- 🎨 Apple 设计美学 — 暗色科技风 + 深色/浅色模式切换 + 动态背景
- 📱 响应式布局 — 桌面/平板/手机均可流畅浏览
- 🔍 零依赖 — 纯 HTML/CSS/JS，无 npm/pip/外部服务

## 项目结构

```
ai-pulse/
├── index.html              # 主页（最新一期 + 日历导航）
├── archive/                # 历史归档
│   └── YYYY-MM-DD-{edition}.html
├── assets/
│   └── favicon.svg         # 站点图标
├── design/                 # 设计稿（参考）
│   ├── fusion-preview.html
│   └── bg-preview.html
├── .claude/                # Claude Code 配置
│   ├── settings.json       # 权限配置
│   └── scheduled_tasks.json # 定时任务（运行时）
├── CLAUDE.md               # 项目指令 + Skill 定义
├── .gitignore
└── README.md
```

## 常见问题

**Q: 为什么打开 index.html 没有内容？**
A: 首次 clone 后需要运行一次 `/ai-digest morning` 生成第一期内容。

**Q: 如何查看历史各期？**
A: 点击「往期回顾」按钮，日历弹窗展示当月所有日期和已生成的版次。

**Q: 定时任务没有运行？**
A: 在终端运行 `CronList` 检查任务状态。确认 Claude Code 处于运行状态。

**Q: 某天漏了生成？**
A: 手动运行对应版次的 `/ai-digest` 命令即可补生成。
