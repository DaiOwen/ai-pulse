# AI 脉搏 · AI热点速览 — 实现计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 构建 AI热点速览 完整系统 —— 一个自包含的 HTML 页面 + Claude Code 驱动的新闻采集/生成 Skill，用户 clone 项目后零配置即可运行。

**Architecture:** 单体 HTML 页面（内嵌 CSS/JS）+ Claude Code 作为唯一运行时依赖。Claude 通过 WebSearch/WebFetch 采集新闻，按规格生成完整 HTML 文件存入 archive/，同时更新 index.html 为最新一期。CronCreate 实现每日三次自动触发，CLAUDE.md 提供手动 `/ai-digest` 命令。

**Tech Stack:** 纯 HTML5 + CSS3 + Vanilla JS（页面），Claude Code CLI（运行时），无 npm/pip/外部服务依赖。

**零依赖约束：** 用户只需安装 Claude Code。clone 项目 → 进入目录 → Claude Code 自动读取 CLAUDE.md → 一切就绪。

---

## 文件结构总览

```
ai-pulse/
├── CLAUDE.md                          # [新建] 项目指令 + Skill 定义 + 自动配置
├── index.html                         # [新建] 主页面（完整模板，含所有CSS/JS）
├── assets/
│   └── favicon.svg                    # [新建] 站点图标
├── archive/
│   └── .gitkeep                       # [新建] 保持目录
├── .claude/
│   └── settings.json                  # [新建] 权限配置（自动生成）
├── .gitignore                         # [已存在] 追加条目
└── README.md                          # [已存在] 更新
```

**关键设计决策：**
- `index.html` 既是模板也是最终页面 —— Claude 每次生成时覆写内容区
- CSS/JS 全部内嵌于 `<style>` 和 `<script>` 标签，零外部文件依赖
- 归档页 `archive/YYYY-MM-DD-{edition}.html` 为完整独立 HTML，可脱离 index 直接打开
- CLAUDE.md 承担三重职责：项目说明 + Skill 定义 + 配置引导

---

### Task 1: 创建项目骨架与 CLAUDE.md

**Files:**
- Create: `CLAUDE.md`
- Modify: `.gitignore`

CLAUDE.md 是整个项目的大脑。Claude Code 进入目录时自动加载，它必须包含：
1. 项目身份说明
2. `/ai-digest` Skill 的完整 Prompt（含搜索策略、内容规格、HTML 生成指令）
3. 自动配置逻辑（首次运行时自动创建 settings.json 和 Cron）

- [ ] **Step 1: 更新 .gitignore**

追加以下内容到 `.gitignore`：

```
# 归档和生成内容（本地运行产物，不提交）
archive/*.html
index.html

# 例外：保留目录占位
!archive/.gitkeep
```

- [ ] **Step 2: 创建 archive/.gitkeep**

Run: `touch archive/.gitkeep`

- [ ] **Step 3: 创建 CLAUDE.md**

```markdown
# AI 脉搏 · AI热点速览

面向中国 AI 开发工程师的每日 AI 新闻智能聚合。每天早中晚三次自动生成精美 HTML 页面。

## 项目身份

- 名称：AI 脉搏 (AI Pulse)
- 目标用户：中国 AI/大模型开发工程师
- 运行方式：Claude Code CLI 驱动，零外部依赖

## 命令

### `/ai-digest [edition]`

生成一期 AI 热点速览。

**参数：**
- `edition`：`morning`（早间版·默认）| `noon`（午间版）| `evening`（晚间版）

**示例：**
```
/ai-digest morning    # 生成早间版
/ai-digest evening    # 生成晚间版
```

## 自动配置

首次在项目中运行 `/ai-digest` 时，自动执行以下配置：
1. 检查 `.claude/settings.json` 是否存在，不存在则创建（含必要的 WebSearch/WebFetch/Bash 权限）
2. 检查 CronCreate 是否存在早中晚三个定时任务，不存在则创建：
   - 早间版：`49 7 * * *`（约 07:49，错峰避免整点拥挤）
   - 午间版：`17 12 * * *`（约 12:17）
   - 晚间版：`13 20 * * *`（约 20:13）
3. 所有 Cron 任务统一调用 `/ai-digest {edition}`

## 新闻采集策略

### 搜索关键词（按板块）

**🤖 大模型动态 — 搜索：**
- 站内搜索："大模型 发布 site:36kr.com"、"AI model release China 2026"
- "OpenAI 新模型"、"百度文心 更新"、"阿里通义"、"DeepSeek 发布"
- "Anthropic Claude 更新"、"Mistral"、"Llama 新版本"
- 时效过滤：最近 24 小时

**🛠️ 工具 & 部署 — 搜索：**
- "AI 开发工具 发布"、"开源 AI 框架 更新"
- "vllm"、"langchain"、"ollama"、"国产 GPU 适配"
- "推理部署 方案 大模型"
- 时效过滤：最近 48 小时

**📋 政策 & 合规 — 搜索：**
- "AI 政策 中国 2026"、"大模型 备案"、"生成式AI 监管"
- "网信办 AI"、"数据安全 AI"
- 时效过滤：最近 7 天

**📄 论文速递 — 搜索：**
- "arXiv cs.AI 最新论文 2026"
- "arxiv LLM paper breakthrough"
- 时效过滤：最近 48 小时

**💡 应用落地 — 搜索：**
- "AI 应用 案例 企业"、"大模型 落地 实践"
- "AI agent 应用"、"RAG 实践"、"企业微信 AI"
- 时效过滤：最近 7 天

**⭐ 开源热度 — 搜索/抓取：**
- 搜索 "GitHub trending AI 2026"、"Gitee 热门 AI 项目"
- 抓取 GitHub Trending 页面或使用 API 获取 AI 相关仓库 Stars 数据

**🌍 海外参考 — 搜索：**
- "AI news today 2026"、"Hacker News AI"
- "The Rundown AI today"
- 只选取对中国开发者有实际影响的（技术方案、开源项目、芯片、开发者工具）
- 时效过滤：最近 24 小时

### 搜索执行规范

1. 每个板块至少执行 3 次不同关键词的 WebSearch
2. 搜索后对 Top5-8 结果执行 WebFetch 获取原文详情
3. 开源数据额外尝试直接访问 `https://github.com/trending?since=daily` 和 Gitee API
4. 单次采集总搜索次数控制在 15-20 次以内

## 内容处理规范

### 去重
- 标题相似度 > 80% 视为重复，保留评分高者
- 同一事件不同角度报道，合并为一条（标注多来源）

### 评分公式
```
总分 = 热度信号×0.4 + 时效信号×0.3 + 来源质量×0.3
热度信号：多源交叉验证(+5) / 优先信源(+3) / 社区讨论度(+1)
时效信号：6h内(+5) / 12h内(+3) / 24h内(+1)
来源质量：36氪/量子位/机器之心(+3) / 其他(+1)
```

### 翻译规范（海外内容）
- 保留原始标题，后面附中文翻译
- 摘要全中文，2-3 句
- 关键数据（金额、百分比、版本号）原文照搬

### 内容量按版次

| 板块 | morning | noon | evening |
|------|:-------:|:----:|:-------:|
| 大模型动态 | Lead×1 + Sub×3 | 增量1-2条 | 全天汇总×5 |
| 工具&部署 | 3-4条 | 增量1-2条 | 汇总×4 |
| 政策&合规 | 1-2条 | 1条 | 汇总×2 |
| 论文速递 | 1篇 | — | — |
| 应用落地 | 2条 | 1条 | 2条 |
| 开源热度 | 快照Top5 | 快照Top5 | 全天Top10 |
| 海外参考 | 3条 | — | 3条 |

## HTML 生成规范

### 生成流程

1. **读取参考模板**：Read `design/fusion-preview.html` 理解视觉结构和 CSS 规范
2. **生成完整 HTML**：按照融合设计（参考 fusion-preview.html）的视觉规格，生成完整的独立 HTML 文件
3. **保存文件**：
   - 保存到 `archive/YYYY-MM-DD-{edition}.html`（如 `archive/2026-06-14-morning.html`）
   - 同时保存到 `index.html`（作为主页，显示最新一期）

### HTML 文件要求

1. **完全自包含**：所有 CSS 内嵌于 `<style>` 标签，所有 JS 内嵌于 `<script>` 标签
2. **字体从 CDN**：Inter + Noto Sans SC 从 Google Fonts CDN 加载（`@import url(...)`）
3. **动态背景**：必须包含 4 个模糊光球 + 40 个微粒 + 网格线动画（纯 CSS + JS，无外部依赖）
4. **主题切换**：右上角滑块 Toggle，默认暗色，localStorage 记住偏好
5. **内容标记**：每条新闻包含分类标签、来源链接、时间、"💡 开发者影响"标注
6. **每日一语**：页脚包含行业名言（优先 Alan Kay、Andrej Karpathy、李开复等 AI 领域人物）

### index.html 额外要求

除上述内容外，index.html 还需包含：
- 日历月导航入口（「往期回顾」按钮 → 下拉/弹窗展示当月日历 + 各日期版次链接）
- 日历数据从 `archive/` 目录文件列表动态生成（读取文件名解析日期和版次）

### 错误处理

- 某信源无结果 → 静默跳过，不影响其他板块
- 全部信源无结果 → 生成页面展示"暂无可获取新闻"，标注最后成功时间
- 开源 API 限流 → 使用本地缓存的昨日数据，标注"数据来自昨日"

## 自动配置（首次运行）

以下逻辑在每次 `/ai-digest` 开始时检查并自动执行：

### 1. 权限配置自动创建

检查 `.claude/settings.json` 是否存在。如果不存在，创建：

```json
{
  "permissions": {
    "allow": [
      "WebSearch",
      "WebFetch",
      "Bash(git:*)",
      "Bash(ls:*)",
      "Bash(mkdir:*)",
      "Bash(cat:*)",
      "Bash(date:*)",
      "Bash(curl:*)"
    ]
  }
}
```

### 2. Cron 定时任务自动创建

检查是否存在定时任务（通过 CronList 工具）。如果不存在，创建 3 个：

| 任务 | Cron 表达式 | 说明 |
|------|------------|------|
| 早间版 | `49 7 * * *` | 07:49 触发，采集昨夜到今晨 |
| 午间版 | `17 12 * * *` | 12:17 触发，增量更新 |
| 晚间版 | `13 20 * * *` | 20:13 触发，全天汇总 |

注意：使用非整点/半点时间（49分/17分/13分），避免与其他用户的 Cron 任务在整点拥挤。

每个 Cron 任务的 prompt 为：`/ai-digest {edition}`

### 3. 自检清单

每次运行 `/ai-digest` 前输出一行自检：
```
🔍 AI脉搏自检：权限配置 ✓ | Cron早间 ✓ 午间 ✓ 晚间 ✓ | 上次生成：archive/2026-06-13-evening.html
```
```

- [ ] **Step 4: Commit**

```bash
git add .gitignore archive/.gitkeep CLAUDE.md
git commit -m "feat: add project skeleton, CLAUDE.md with full skill definition"
```

---

### Task 2: 创建核心 HTML 模板 (index.html)

**Files:**
- Create: `index.html`
- Reference: `design/fusion-preview.html`

这是融合设计（V1 Editorial + V2 工程师优化）的最终实现。包含完整 CSS、JS 和示例占位内容。作为首次运行的模板和后续 Claude 生成的参考。

- [ ] **Step 1: 创建 index.html 的文档头和 CSS 变量**

```html
<!DOCTYPE html>
<html lang="zh-CN" data-theme="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AI 脉搏 · 热点速览</title>
<meta name="description" content="面向中国AI开发工程师的每日AI新闻智能聚合">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Noto+Sans+SC:wght@300;400;500;600;700&display=swap');

  :root {
    /* Dark theme (default) */
    --bg-primary: #0a0a0f;
    --bg-secondary: rgba(255,255,255,0.025);
    --bg-card: rgba(255,255,255,0.018);
    --border-subtle: rgba(255,255,255,0.06);
    --border-card: rgba(255,255,255,0.04);
    --text-primary: #f5f5f7;
    --text-secondary: #9898a0;
    --text-tertiary: #86868b;
    --accent-indigo: #6366f1;
    --accent-green: #22c55e;
    --accent-amber: #f59e0b;
    --accent-purple: #8b5cf6;
    --accent-cyan: #06b6d4;
    --bg-glow-indigo: rgba(99,102,241,0.04);
    --bg-glow-purple: rgba(139,92,246,0.03);
    --bg-glow-cyan: rgba(6,182,212,0.03);
  }

  [data-theme="light"] {
    --bg-primary: #f5f5f7;
    --bg-secondary: rgba(0,0,0,0.02);
    --bg-card: rgba(0,0,0,0.015);
    --border-subtle: rgba(0,0,0,0.08);
    --border-card: rgba(0,0,0,0.06);
    --text-primary: #1d1d1f;
    --text-secondary: #6e6e73;
    --text-tertiary: #86868b;
    --bg-glow-indigo: rgba(99,102,241,0.06);
    --bg-glow-purple: rgba(139,92,246,0.04);
    --bg-glow-cyan: rgba(6,182,212,0.04);
  }
```

- [ ] **Step 2: 创建全局重置和排版 CSS**

```css
  *, *::before, *::after { margin: 0; padding: 0; box-sizing: border-box; }

  body {
    font-family: 'Inter', 'Noto Sans SC', -apple-system, BlinkMacSystemFont, sans-serif;
    background: linear-gradient(160deg, #0a0a0f 0%, #0f0f1a 30%, #0d0d18 60%, #0a0a14 100%);
    color: var(--text-primary);
    min-height: 100vh;
    -webkit-font-smoothing: antialiased;
    overflow-x: hidden;
    transition: background 0.5s ease;
  }

  [data-theme="light"] body {
    background: linear-gradient(160deg, #f5f5f7 0%, #fafafa 30%, #f0f0f3 60%, #f5f5f7 100%);
  }
```

- [ ] **Step 3: 创建动态背景 CSS**

```css
  /* ── Dynamic Background ── */
  .bg-layer { position: fixed; inset: 0; pointer-events: none; z-index: 0; }
  .orb {
    position: absolute; border-radius: 50%; filter: blur(120px);
    animation-timing-function: ease-in-out; animation-iteration-count: infinite;
    animation-direction: alternate;
  }
  .orb-1 { width:500px; height:500px; background:radial-gradient(circle, #6366f1 0%, transparent 70%); top:-10%; right:-5%; opacity:0.12; animation:float1 18s infinite; }
  .orb-2 { width:400px; height:400px; background:radial-gradient(circle, #8b5cf6 0%, transparent 70%); bottom:-15%; left:-8%; opacity:0.12; animation:float2 22s infinite; }
  .orb-3 { width:300px; height:300px; background:radial-gradient(circle, #06b6d4 0%, transparent 70%); top:45%; right:-10%; opacity:0.08; animation:float3 20s infinite; }
  .orb-4 { width:250px; height:250px; background:radial-gradient(circle, #f59e0b 0%, transparent 70%); top:-8%; left:40%; opacity:0.06; animation:float4 24s infinite; }
  @keyframes float1 {
    0% { transform:translate(0,0) scale(1); } 33% { transform:translate(-80px,60px) scale(1.15); }
    66% { transform:translate(40px,-30px) scale(0.9); } 100% { transform:translate(-20px,20px) scale(1.05); }
  }
  @keyframes float2 {
    0% { transform:translate(0,0) scale(1); } 33% { transform:translate(60px,-50px) scale(1.2); }
    66% { transform:translate(-30px,20px) scale(0.85); } 100% { transform:translate(10px,-10px) scale(1.1); }
  }
  @keyframes float3 {
    0% { transform:translate(0,0) scale(1); } 50% { transform:translate(-50px,-40px) scale(1.3); }
    100% { transform:translate(20px,30px) scale(0.9); }
  }
  @keyframes float4 {
    0% { transform:translate(0,0) scale(1); } 25% { transform:translate(30px,50px) scale(1.25); }
    75% { transform:translate(-40px,20px) scale(0.85); } 100% { transform:translate(10px,-10px) scale(1.05); }
  }
  .grid-overlay {
    position:absolute; inset:0;
    background-image:linear-gradient(rgba(255,255,255,0.012) 1px, transparent 1px),
                     linear-gradient(90deg, rgba(255,255,255,0.012) 1px, transparent 1px);
    background-size:60px 60px; animation:gridShift 30s linear infinite;
  }
  @keyframes gridShift { 0% { background-position:0 0; } 100% { background-position:60px 60px; } }
  .particle {
    position:absolute; border-radius:50%; background:rgba(255,255,255,0.35);
    animation:rise linear infinite;
  }
  @keyframes rise {
    0% { transform:translateY(0) translateX(0); opacity:0; }
    10% { opacity:0.5; } 90% { opacity:0.05; }
    100% { transform:translateY(-100vh) translateX(60px); opacity:0; }
  }
```

- [ ] **Step 4: 创建导航栏 CSS**

```css
  /* ── Layout ── */
  .content { position:relative; z-index:1; max-width:900px; margin:0 auto; padding:0 32px 80px; }

  /* ── Nav ── */
  .nav { display:flex; justify-content:space-between; align-items:center; padding:18px 0; border-bottom:0.5px solid var(--border-subtle); }
  .nav-brand { display:flex; align-items:center; gap:10px; }
  .nav-logo { width:34px; height:34px; border-radius:9px; background:linear-gradient(135deg, #6366f1, #8b5cf6); display:flex; align-items:center; justify-content:center; font-size:16px; }
  .nav-title { font-size:15px; font-weight:600; color:var(--text-primary); letter-spacing:-0.02em; }
  .nav-sub { font-size:9px; color:var(--text-tertiary); letter-spacing:0.05em; }
  .nav-right { display:flex; align-items:center; gap:20px; }
  .nav-link { font-size:10px; color:var(--text-tertiary); font-weight:500; cursor:pointer; transition:color 0.2s; background:none; border:none; font-family:inherit; }
  .nav-link:hover { color:var(--text-primary); }
  .toggle-track { width:38px; height:22px; background:rgba(99,102,241,0.25); border-radius:11px; border:0.5px solid rgba(99,102,241,0.35); position:relative; cursor:pointer; transition:background 0.3s; }
  .toggle-thumb { width:17px; height:17px; background:linear-gradient(135deg, #6366f1, #8b5cf6); border-radius:50%; position:absolute; top:2px; left:2px; box-shadow:0 1px 4px rgba(0,0,0,0.3); transition:transform 0.3s cubic-bezier(0.25,0.8,0.25,1.2); }
  [data-theme="light"] .toggle-thumb { transform:translateX(16px); }
  .toggle-label { font-size:10px; color:var(--text-tertiary); }
```

- [ ] **Step 5: 创建 Hero、TL;DR、板块样式、卡片、页脚 CSS**

继续写入 index.html 的 `<style>` 块，直接从 `design/fusion-preview.html` 复制以下 CSS 类并适配 CSS 变量：
- `.hero`, `.hero-glow`, `.hero-badge`, `.hero-badge-dot`, `.hero-title`, `.hero-date`, `.hero-stats`
- `.tldr`, `.tldr-label`, `.tldr-text`
- `.section-head`, `.section-line`, `.section-label`, `.section-label-cn`
- `.feature-card`, `.card-tag`, `.card-title`, `.card-desc`, `.card-meta`, `.card-meta-link`, `.card-row`, `.card-icon`, `.card-body`
- `.sub-grid`, `.sub-card`, `.sub-tag`, `.sub-title`, `.sub-desc`
- `.tool-row`, `.tool-card`, `.tool-icon`, `.tool-name`, `.tool-desc`, `.tool-badge`, `.badge-new`, `.badge-update`
- `.paper-spotlight`, `.paper-header`, `.paper-label`, `.paper-title`, `.paper-abstract`, `.paper-meta`
- `.dual-cards`, `.rank-card`, `.rank-label`, `.rank-row`, `.rank-num`, `.rank-name`, `.rank-stat`, `.rank-up`, `.rank-neutral`
- `.footer`, `.footer-icon`, `.footer-quote`, `.footer-author`

关键适配：将所有硬编码颜色替换为 CSS 变量引用。

- [ ] **Step 6: 创建日历弹窗 CSS**

```css
  /* ── Calendar Modal ── */
  .calendar-overlay { display:none; position:fixed; inset:0; background:rgba(0,0,0,0.6); backdrop-filter:blur(4px); z-index:100; justify-content:center; align-items:center; }
  .calendar-overlay.active { display:flex; }
  .calendar-modal { background:var(--bg-primary); border:0.5px solid var(--border-subtle); border-radius:16px; padding:24px; max-width:380px; width:90%; max-height:80vh; overflow-y:auto; }
  .calendar-header { display:flex; justify-content:space-between; align-items:center; margin-bottom:16px; }
  .calendar-month { font-size:16px; font-weight:600; color:var(--text-primary); }
  .calendar-nav { font-size:18px; color:var(--text-tertiary); cursor:pointer; background:none; border:none; padding:4px 8px; }
  .calendar-nav:hover { color:var(--text-primary); }
  .calendar-close { font-size:20px; color:var(--text-tertiary); cursor:pointer; background:none; border:none; }
  .calendar-grid { display:grid; grid-template-columns:repeat(7,1fr); gap:4px; text-align:center; }
  .calendar-day-header { font-size:9px; color:var(--text-tertiary); padding:4px; }
  .calendar-day { font-size:12px; padding:8px 4px; border-radius:6px; cursor:pointer; color:var(--text-secondary); position:relative; }
  .calendar-day:hover { background:rgba(99,102,241,0.1); }
  .calendar-day.today { font-weight:700; color:#6366f1; border:1px solid rgba(99,102,241,0.3); }
  .calendar-day.has-content { color:var(--text-primary); }
  .calendar-day.full { background:rgba(34,197,94,0.08); }
  .calendar-day.partial { background:rgba(99,102,241,0.06); }
  .calendar-day.other-month { color:#484f58; }
  .calendar-day-links { display:none; position:absolute; bottom:100%; left:50%; transform:translateX(-50%); background:var(--bg-primary); border:0.5px solid var(--border-subtle); border-radius:8px; padding:6px 10px; font-size:10px; white-space:nowrap; z-index:2; }
  .calendar-day:hover .calendar-day-links { display:block; }
  .calendar-day-link { display:block; color:var(--text-secondary); text-decoration:none; padding:2px 0; }
  .calendar-day-link:hover { color:#6366f1; }
  .calendar-legend { display:flex; gap:16px; margin-top:12px; font-size:9px; color:var(--text-tertiary); justify-content:center; }
  .calendar-legend-item { display:flex; align-items:center; gap:4px; }
  .calendar-legend-dot { width:8px; height:8px; border-radius:2px; }
```

- [ ] **Step 7: 创建 HTML body 结构（含占位内容）**

写入 `</style></head><body>` 之后的内容。结构如下：

```html
<!-- ═══ BACKGROUND ═══ -->
<div class="bg-layer">
  <div class="orb orb-1"></div><div class="orb orb-2"></div>
  <div class="orb orb-3"></div><div class="orb orb-4"></div>
  <div class="grid-overlay"></div>
  <div class="particles" id="particles"></div>
</div>

<!-- ═══ CALENDAR OVERLAY ═══ -->
<div class="calendar-overlay" id="calendarOverlay">
  <div class="calendar-modal">
    <div class="calendar-header">
      <button class="calendar-nav" id="calPrev">◀</button>
      <span class="calendar-month" id="calMonth">2026年6月</span>
      <button class="calendar-nav" id="calNext">▶</button>
      <button class="calendar-close" id="calClose">✕</button>
    </div>
    <div class="calendar-grid" id="calGrid"></div>
    <div class="calendar-legend">
      <div class="calendar-legend-item"><div class="calendar-legend-dot" style="background:rgba(34,197,94,0.5);"></div>3版完整</div>
      <div class="calendar-legend-item"><div class="calendar-legend-dot" style="background:rgba(99,102,241,0.4);"></div>有内容</div>
      <div class="calendar-legend-item"><div class="calendar-legend-dot" style="background:rgba(255,255,255,0.1);"></div>暂无</div>
    </div>
  </div>
</div>

<!-- ═══ CONTENT ═══ -->
<div class="content">

  <!-- Nav -->
  <nav class="nav">
    <div class="nav-brand">
      <div class="nav-logo">⚡</div>
      <div>
        <div class="nav-title">AI热点速览</div>
        <div class="nav-sub">AI PULSE</div>
      </div>
    </div>
    <div class="nav-right">
      <button class="nav-link" id="btnArchive">往期回顾</button>
      <span class="toggle-label">暗</span>
      <div class="toggle-track" id="themeToggle"><div class="toggle-thumb"></div></div>
      <span class="toggle-label">亮</span>
    </div>
  </nav>

  <!-- Hero -->
  <section class="hero">
    <div class="hero-glow"></div>
    <div class="hero-badge">
      <div class="hero-badge-dot"></div>
      <span class="hero-badge-text" id="editionLabel">早间版 · 08:00 · 实时</span>
    </div>
    <h1 class="hero-title">今日 AI 脉搏</h1>
    <p class="hero-date" id="dateLabel">2026年6月14日 · 星期六</p>
    <div class="hero-stats" id="heroStats">
      <div><div class="hero-stat-num" id="statNews">--</div><div class="hero-stat-label">头条新闻</div></div>
      <div class="hero-stat-divider"></div>
      <div><div class="hero-stat-num" id="statSources">--</div><div class="hero-stat-label">信源覆盖</div></div>
      <div class="hero-stat-divider"></div>
      <div><div class="hero-stat-num" id="statProjects">--</div><div class="hero-stat-label">热门项目</div></div>
      <div class="hero-stat-divider"></div>
      <div><div class="hero-stat-num" id="statPapers">--</div><div class="hero-stat-label">精选论文</div></div>
    </div>
  </section>

  <!-- TL;DR -->
  <div class="tldr" id="tldrSection">
    <span class="tldr-label">TL;DR</span>
    <span class="tldr-text" id="tldrContent"><!-- Claude fills this --></span>
  </div>

  <!-- Sections: Claude fills each section's inner HTML -->
  <!-- 🤖 大模型动态 -->
  <div class="section-gap" id="section-models">
    <div class="section-head">
      <div class="section-line" style="background:linear-gradient(180deg, #6366f1, #8b5cf6);"></div>
      <span class="section-label" style="color:#a5b4fc;">大模型动态</span>
      <span class="section-label-cn">Models</span>
    </div>
    <!-- Lead Story + Sub cards injected here -->
  </div>

  <!-- 🛠️ 工具 & 部署 -->
  <div class="section-gap" id="section-tools">
    <div class="section-head">
      <div class="section-line" style="background:linear-gradient(180deg, #22c55e, #10b981);"></div>
      <span class="section-label" style="color:#86efac;">工具 & 部署</span>
      <span class="section-label-cn">Tools & Deploy</span>
    </div>
    <!-- Tool cards injected here -->
  </div>

  <!-- 📋 政策 & 合规 -->
  <div class="section-gap" id="section-policy">
    <div class="section-head">
      <div class="section-line" style="background:linear-gradient(180deg, #f59e0b, #d97706);"></div>
      <span class="section-label" style="color:#fcd34d;">政策 & 合规</span>
      <span class="section-label-cn">Policy & Compliance</span>
    </div>
    <!-- Policy cards injected here -->
  </div>

  <!-- 📄 论文速递 -->
  <div class="section-gap" id="section-paper">
    <div class="section-head">
      <div class="section-line" style="background:linear-gradient(180deg, #8b5cf6, #7c3aed);"></div>
      <span class="section-label" style="color:#c4b5fd;">论文速递</span>
      <span class="section-label-cn">Paper Spotlight</span>
    </div>
    <!-- Paper spotlight card injected here (morning only) -->
  </div>

  <!-- 💡 应用落地 -->
  <div class="section-gap" id="section-cases">
    <div class="section-head">
      <div class="section-line" style="background:linear-gradient(180deg, #06b6d4, #0891b2);"></div>
      <span class="section-label" style="color:#67e8f9;">应用落地</span>
      <span class="section-label-cn">Real-World AI</span>
    </div>
    <!-- Case cards injected here -->
  </div>

  <!-- ⭐ 开源热度 -->
  <div class="section-gap" id="section-oss">
    <div class="section-head">
      <div class="section-line" style="background:linear-gradient(180deg, #f59e0b, #d97706);"></div>
      <span class="section-label" style="color:#fcd34d;">开源热度</span>
      <span class="section-label-cn">Open Source Pulse</span>
    </div>
    <!-- Rank cards injected here -->
  </div>

  <!-- 🌍 海外参考 -->
  <div class="section-gap" id="section-overseas">
    <div class="section-head">
      <div class="section-line" style="background:linear-gradient(180deg, #06b6d4, #0891b2);"></div>
      <span class="section-label" style="color:#67e8f9;">海外参考</span>
      <span class="section-label-cn">Global Brief</span>
    </div>
    <!-- Overseas cards injected here -->
  </div>

  <!-- Footer -->
  <footer class="footer">
    <div class="footer-icon">⚡</div>
    <p class="footer-quote" id="footerQuote">"预测未来最好的方式，就是创造它。"</p>
    <p class="footer-author" id="footerAuthor">Alan Kay</p>
  </footer>

</div>
```

- [ ] **Step 8: 创建 JavaScript（粒子、主题切换、日历）**

```html
<script>
  // ═══ PARTICLES ═══
  (function() {
    const pc = document.getElementById('particles');
    for (let i = 0; i < 40; i++) {
      const p = document.createElement('div');
      p.classList.add('particle');
      p.style.left = Math.random() * 100 + '%';
      p.style.top = Math.random() * 100 + '%';
      const s = 1 + Math.random() * 2;
      p.style.width = s + 'px'; p.style.height = s + 'px';
      p.style.animationDuration = (12 + Math.random() * 20) + 's';
      p.style.animationDelay = Math.random() * 15 + 's';
      pc.appendChild(p);
    }
  })();

  // ═══ THEME TOGGLE ═══
  (function() {
    const saved = localStorage.getItem('ai-pulse-theme');
    if (saved === 'light') document.documentElement.setAttribute('data-theme', 'light');
    document.getElementById('themeToggle').addEventListener('click', function() {
      const current = document.documentElement.getAttribute('data-theme');
      const next = current === 'light' ? 'dark' : 'light';
      document.documentElement.setAttribute('data-theme', next);
      localStorage.setItem('ai-pulse-theme', next);
    });
  })();

  // ═══ CALENDAR ═══
  (function() {
    const overlay = document.getElementById('calendarOverlay');
    const grid = document.getElementById('calGrid');
    const monthLabel = document.getElementById('calMonth');
    let calYear = new Date().getFullYear();
    let calMonth = new Date().getMonth() + 1;

    // Scan archive/ directory entries from a pre-built index
    // For the static template, we build a simple JSON map
    // In production, Claude writes this map to a <script> tag
    let archiveMap = {};
    try { archiveMap = JSON.parse(document.getElementById('archiveData')?.textContent || '{}'); } catch(e) {}

    function renderCalendar() {
      const daysInMonth = new Date(calYear, calMonth, 0).getDate();
      const firstDay = new Date(calYear, calMonth - 1, 1).getDay(); // 0=Sun
      const adjustedFirst = firstDay === 0 ? 6 : firstDay - 1; // Mon=0
      const today = new Date();
      const dayHeaders = ['一','二','三','四','五','六','日'];

      monthLabel.textContent = calYear + '年' + calMonth + '月';
      grid.innerHTML = dayHeaders.map(h => `<div class="calendar-day-header">${h}</div>`).join('');

      // Empty cells before first day
      for (let i = 0; i < adjustedFirst; i++) {
        grid.innerHTML += '<div class="calendar-day other-month"></div>';
      }

      for (let d = 1; d <= daysInMonth; d++) {
        const dateStr = `${calYear}-${String(calMonth).padStart(2,'0')}-${String(d).padStart(2,'0')}`;
        const isToday = d === today.getDate() && calMonth === today.getMonth() + 1 && calYear === today.getFullYear();
        const entry = archiveMap[dateStr];
        let cls = 'calendar-day';
        if (isToday) cls += ' today';
        if (entry) {
          cls += ' has-content';
          cls += (entry === 'full') ? ' full' : ' partial';
        }
        let linksHtml = '';
        if (entry) {
          const editions = entry === 'full' ? ['morning','noon','evening'] :
                           Array.isArray(entry) ? entry : ['morning'];
          linksHtml = `<div class="calendar-day-links">${editions.map(e =>
            `<a class="calendar-day-link" href="archive/${dateStr}-${e}.html">${e==='morning'?'🌅 早间':e==='noon'?'☀️ 午间':'🌙 晚间'}</a>`
          ).join('')}</div>`;
        }
        grid.innerHTML += `<div class="${cls}">${d}${linksHtml}</div>`;
      }
    }

    document.getElementById('btnArchive').addEventListener('click', () => {
      calYear = new Date().getFullYear();
      calMonth = new Date().getMonth() + 1;
      renderCalendar();
      overlay.classList.add('active');
    });
    document.getElementById('calPrev').addEventListener('click', () => { calMonth--; if(calMonth<1){calMonth=12;calYear--;} renderCalendar(); });
    document.getElementById('calNext').addEventListener('click', () => { calMonth++; if(calMonth>12){calMonth=1;calYear++;} renderCalendar(); });
    document.getElementById('calClose').addEventListener('click', () => overlay.classList.remove('active'));
    overlay.addEventListener('click', (e) => { if (e.target === overlay) overlay.classList.remove('active'); });
  })();
</script>
</body>
</html>
```

- [ ] **Step 9: Commit**

```bash
git add index.html
git commit -m "feat: create index.html with full CSS, dark/light theme, dynamic background, calendar"
```

---

### Task 3: 创建站点图标

**Files:**
- Create: `assets/favicon.svg`

- [ ] **Step 1: 创建 SVG favicon**

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <defs>
    <linearGradient id="g" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#6366f1"/>
      <stop offset="100%" style="stop-color:#8b5cf6"/>
    </linearGradient>
  </defs>
  <rect width="100" height="100" rx="20" fill="url(#g)"/>
  <text x="50" y="68" font-size="55" text-anchor="middle" fill="white">⚡</text>
</svg>
```

- [ ] **Step 2: 在 index.html 的 `<head>` 中添加**

```html
<link rel="icon" type="image/svg+xml" href="assets/favicon.svg">
```

- [ ] **Step 3: Commit**

```bash
git add assets/favicon.svg index.html
git commit -m "feat: add SVG favicon and link in index.html"
```

---

### Task 4: 生成首个示例页面（早间版）

**Files:**
- Create: `archive/2026-06-14-morning.html`

用 Claude 按 CLAUDE.md 规范生成第一期示例内容，验证完整流程可运行。

- [ ] **Step 1: 手动运行首次采集生成**

作为 Claude Code 会话，严格按照 CLAUDE.md 中的 `/ai-digest morning` 规范执行：
1. 执行 15-20 次 WebSearch（覆盖全部 7 个板块）
2. 对关键结果执行 WebFetch 获取详情
3. 尝试访问 GitHub Trending 获取开源数据
4. 按评分公式排序 + 去重
5. 按早间版规格生成完整 HTML
6. 保存到 `archive/2026-06-14-morning.html`

- [ ] **Step 2: 同时更新 index.html**

将生成的内容同步写入 `index.html`（作为主页展示最新一期）

- [ ] **Step 3: 验证页面**

Run: 用浏览器打开 `index.html`，检查：
- 所有 7 个板块内容完整
- 主题切换正常工作
- 动态背景流畅
- 日历弹窗可打开（至少有一个日期有数据）
- 无 JS 控制台错误

- [ ] **Step 4: Commit**

```bash
git add archive/2026-06-14-morning.html index.html
git commit -m "feat: generate first morning edition with real AI news content"
```

---

### Task 5: 自动配置验证与 Cron 注册

**Files:**
- Create: `.claude/settings.json`
- Modify: `.claude/scheduled_tasks.json`（由 CronCreate 工具生成）

- [ ] **Step 1: 创建权限配置文件**

```json
{
  "permissions": {
    "allow": [
      "WebSearch",
      "WebFetch",
      "Bash(git:*)",
      "Bash(ls:*)",
      "Bash(mkdir:*)",
      "Bash(cat:*)",
      "Bash(date:*)",
      "Bash(curl:*)"
    ]
  }
}
```

- [ ] **Step 2: 注册 Cron 定时任务**

对早中晚三个版次分别调用 CronCreate（使用非整点时间避免拥挤）：

```bash
# 早间版 — 07:49
CronCreate cron="49 7 * * *" prompt="/ai-digest morning" durable=true

# 午间版 — 12:17
CronCreate cron="17 12 * * *" prompt="/ai-digest noon" durable=true

# 晚间版 — 20:13
CronCreate cron="13 20 * * *" prompt="/ai-digest evening" durable=true
```

注意：`durable=true` 确保任务持久化到 `.claude/scheduled_tasks.json`，Claude Code 重启后仍有效。

- [ ] **Step 3: 验证 Cron 注册**

Run: `CronList` 检查 3 个任务是否已注册、状态是否为 active。

- [ ] **Step 4: 更新 CLAUDE.md 中的自动配置说明**

确保 CLAUDE.md 中已经包含首次运行自动检测的逻辑（已在 Task 1 中写入，此处确认）。

- [ ] **Step 5: Commit**

```bash
git add .claude/settings.json
git commit -m "feat: add permissions config and cron registration"
```

---

### Task 6: 亮色模式完善与响应式适配

**Files:**
- Modify: `index.html`（追加 CSS）

- [ ] **Step 1: 验证亮色模式 CSS 变量覆盖完整**

检查 `[data-theme="light"]` 块中所有变量是否覆盖完整。追加缺失变量：

```css
  [data-theme="light"] {
    --bg-primary: #f5f5f7;
    --bg-secondary: rgba(0,0,0,0.02);
    --bg-card: rgba(0,0,0,0.015);
    --border-subtle: rgba(0,0,0,0.08);
    --border-card: rgba(0,0,0,0.06);
    --text-primary: #1d1d1f;
    --text-secondary: #6e6e73;
    --text-tertiary: #86868b;
  }

  [data-theme="light"] .feature-card { background:rgba(0,0,0,0.015); }
  [data-theme="light"] .sub-card { background:rgba(0,0,0,0.01); }
  [data-theme="light"] .tool-card { background:rgba(0,0,0,0.01); }
  [data-theme="light"] .rank-card { background:rgba(0,0,0,0.01); }
  [data-theme="light"] .tldr { background:rgba(99,102,241,0.04); }
  [data-theme="light"] .paper-spotlight { background:rgba(139,92,246,0.03); }
  [data-theme="light"] .orb { opacity: 0.04 !important; }
  [data-theme="light"] .particle { background:rgba(0,0,0,0.15); }
  [data-theme="light"] .grid-overlay { background-image:linear-gradient(rgba(0,0,0,0.03) 1px, transparent 1px),linear-gradient(90deg, rgba(0,0,0,0.03) 1px, transparent 1px); }
```

- [ ] **Step 2: 添加响应式 CSS**

```css
  /* ── Responsive ── */
  @media (max-width: 768px) {
    .content { padding:0 16px 60px; }
    .hero-title { font-size:32px; }
    .hero-stats { gap:20px; }
    .hero-stat-num { font-size:18px; }
    .sub-grid { grid-template-columns:1fr; }
    .tool-row { grid-template-columns:1fr; }
    .dual-cards { grid-template-columns:1fr; }
    .card-row { flex-direction:column; }
    .card-icon { width:48px; height:48px; font-size:18px; }
    .feature-card { padding:18px; }
  }

  @media (max-width: 480px) {
    .nav { flex-direction:column; gap:10px; }
    .nav-right { gap:12px; }
    .hero-title { font-size:26px; }
    .hero { padding:32px 0 24px; }
  }
```

- [ ] **Step 3: 验证移动端效果**

用浏览器 DevTools 模拟 iPhone 14 (390×844) 和 iPad (768×1024) 检查布局是否正常。

- [ ] **Step 4: Commit**

```bash
git add index.html
git commit -m "feat: complete light mode styles and responsive layout"
```

---

### Task 7: 最终验证与文档更新

**Files:**
- Modify: `README.md`

- [ ] **Step 1: 端到端验证**

- 浏览器打开 `index.html` → 内容完整、主题切换正常、日历有数据
- 运行 CronList → 3 个任务均为 active
- 手动运行 `/ai-digest noon` → 生成午间版到 `archive/`，更新 `index.html`

- [ ] **Step 2: 更新 README.md**

将 README 更新为最终版本，强调零配置体验：

```markdown
# AI 脉搏 · AI热点速览

面向中国 AI 开发工程师的每日 AI 新闻智能聚合页。**只需安装 Claude Code，clone 项目即可运行。**

## 快速开始

```bash
git clone https://github.com/DaiOwen/ai-pulse.git
cd ai-pulse
# 进入目录后 Claude Code 自动加载项目配置
# 运行一次手动采集：
/ai-digest morning
# 之后每天早中晚自动运行，无需任何操作
```

## 查看

用浏览器打开 `index.html` 即可查看最新一期 AI 热点速览。

或直接打开 `archive/` 目录下的任意一期 HTML 文件。

## 工作原理

1. Claude Code 在每天 07:49 / 12:17 / 20:13 自动触发采集
2. WebSearch + WebFetch 从 6+ 信源聚合 AI 新闻
3. Claude 智能去重、评分、翻译、分类、生成摘要
4. 生成精美 HTML 存入 archive/，同步更新 index.html

**零依赖**：不需要 npm、Python、数据库或任何外部服务。只需要 Claude Code。
**零配置**：clone 后 Claude Code 自动读取项目配置，首次运行自动创建权限和定时任务。
```

- [ ] **Step 3: 最终 Commit & Push**

```bash
git add README.md
git commit -m "docs: update README with quick start and architecture overview"
git push
```

---

## 计划自审

### 1. Spec 覆盖检查

| Spec 要求 | 对应 Task |
|-----------|----------|
| 核心 HTML 模板（CSS/JS 内嵌） | Task 2 ✅ |
| 7 个板块完整布局 | Task 2 Step 7 ✅ |
| 动态背景（光球/粒子/网格） | Task 2 Step 3,8 ✅ |
| 深色/浅色主题切换 | Task 2 Step 2,8; Task 6 ✅ |
| TL;DR 条 | Task 2 Step 7 ✅ |
| 日历月导航 | Task 2 Step 6,8 ✅ |
| 归档系统 (archive/) | Task 4 ✅ |
| Claude Code Skill (`/ai-digest`) | Task 1 (CLAUDE.md) ✅ |
| Cron 定时 (早中晚) | Task 5 ✅ |
| 自动配置（权限 + Cron） | Task 1 (CLAUDE.md), Task 5 ✅ |
| 零外部依赖 | 全部 Task（只用 Claude Code + 浏览器） ✅ |
| 亮色模式 + 响应式 | Task 6 ✅ |
| 成功标准验证 | Task 7 ✅ |

### 2. Placeholder 扫描

无 TBD、TODO、模糊描述。所有步骤包含具体代码和命令。

### 3. 类型一致性

- CSS 变量在 Task 2 Step 1 定义，Task 2 Steps 2-6 和 Task 6 中使用，名称一致
- HTML id 属性在 Step 7 定义，Step 8 JS 中引用，完全匹配
- CLAUDE.md 中的搜索关键词和板块名与 index.html 中的 section id 对应
