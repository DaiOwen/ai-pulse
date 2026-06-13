🌐 **Read this in:** [English](README.md) · [中文](README.zh-CN.md) · [日本語](README.ja.md) · [Deutsch](README.de.md) · [한국어](README.ko.md)

<p align="center">
  <img src="assets/favicon.svg" width="64" alt="AI Pulse logo" />
</p>

<h1 align="center">AI Pulse · Daily AI News Digest</h1>

<p align="center">
  <em>AI-powered daily news aggregation for developers. Zero deps. Claude Code native.</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/license-MIT-blue" alt="License">
  <img src="https://img.shields.io/badge/dependencies-zero-brightgreen" alt="Zero Dependencies">
  <img src="https://img.shields.io/badge/PRs-welcome-orange" alt="PRs Welcome">
</p>

---

**AI Pulse** is a daily AI news aggregation HTML page for AI developers, powered by [Claude Code](https://claude.ai). It auto-generates beautiful, responsive HTML pages 3 times daily by scraping and synthesizing news from 6+ sources. No npm, no Python, no external services — just Claude Code and a terminal.

## Features

- 🤖 **7 curated sections** — Model Updates, Tools & Deploy, Policy & Compliance, Paper Spotlight, Real-World AI Cases, Open Source Pulse, Global Brief
- ⚡ **Four-level information depth** — TL;DR (3s) → Headlines (10s) → Summaries (30s) → Full articles
- 🎨 **Apple-inspired design** — Dark/light theme with dynamic animated background, glassmorphism cards
- 📱 **Responsive layout** — Works beautifully on desktop, tablet, and mobile
- 📅 **Archive calendar** — Browse past editions with an interactive calendar
- 🔍 **Zero dependencies** — Pure HTML/CSS/JS, no build step, no package manager
- 🇨🇳 **Chinese AI ecosystem focus** — Priority coverage of domestic models and compliance policies
- ⏰ **Auto-scheduled** — Generates at 07:49, 12:17, and 20:13 daily

## Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/DaiOwen/ai-pulse.git
cd ai-pulse

# 2. Generate your first edition
# (Claude Code loads the project config automatically)
/ai-digest morning

# 3. Open index.html in your browser
```

On first run, Claude Code will:
- Search 6+ sources for the latest AI news (WebSearch)
- Deep-fetch top articles for full content (WebFetch)
- Deduplicate, score, translate, and classify all items
- Generate a complete standalone HTML page saved to `archive/` and `index.html`

### Scheduled Tasks

After the first manual run, three cron jobs are registered automatically:

| Task | Time | Coverage |
|------|------|----------|
| 🌅 Morning | 07:49 | Overnight global + morning domestic news |
| ☀️ Noon | 12:17 | Incremental updates from the morning |
| 🌙 Evening | 20:13 | Full-day summary + all-day open source data |

### Manual Commands

| Command | Description |
|---------|-------------|
| `/ai-digest morning` | Generate morning edition |
| `/ai-digest noon` | Generate noon edition (incremental) |
| `/ai-digest evening` | Generate evening edition (full-day summary) |

## Content Sections

| Section | Description |
|---------|-------------|
| 🤖 Model Updates | Priority on Chinese domestic + major global model releases |
| 🛠️ Tools & Deploy | Framework updates, hardware adaptation, inference deployment |
| 📋 Policy & Compliance | CAC filings, AI safety reviews, industry standards |
| 📄 Paper Spotlight | One curated arXiv paper daily with practical value |
| 💡 Real-World AI Cases | Enterprise AI integration stories & best practices |
| ⭐ Open Source Pulse | GitHub/Gitee Stars rising Top 10 + attention Top 10 |
| 🌍 Global Brief | 3 curated international stories impacting China |

## Architecture

```
Cron Schedule (07:49 / 12:17 / 20:13)
       │
       ▼
Claude Code Launches
       │
       ├─ WebSearch (15-20 multi-keyword searches)
       ├─ WebFetch (deep-fetch top 5-8 results)
       └─ GitHub/Gitee API (open source trending data)
       │
       ▼
Processing Pipeline
  ① Dedup (title similarity + URL normalization)
  ② Scoring (popularity×0.4 + timeliness×0.3 + source quality×0.3)
  ③ Translation (global news → localized summaries)
  ④ Classification (7 sections)
  ⑤ Summary generation (2-3 sentences + developer impact note)
       │
       ▼
HTML Generation & Archive
  • Generates fully self-contained HTML
  • Saves to archive/YYYY-MM-DD-{edition}.html
  • Updates index.html to latest edition
```

## Project Structure

```
ai-pulse/
├── index.html              # Main page (latest issue + calendar nav)
├── archive/                # Historical archive
│   └── YYYY-MM-DD-{edition}.html
├── assets/
│   └── favicon.svg         # Site icon
├── design/                 # Design references
├── .claude/                # Claude Code config
│   ├── settings.json       # Permission config
│   └── scheduled_tasks.json # Scheduled tasks (runtime)
├── CLAUDE.md               # Project instructions & Skill definitions
├── .gitignore
└── README.md
```

## Screenshots

### 🌙 Dark Mode (default)

![AI Pulse Dark Mode](screenshots/dark-mode.png)

### ☀️ Light Mode

![AI Pulse Light Mode](screenshots/light-mode.png)

## FAQ

**Q: Why is index.html blank?**
A: You need to run `/ai-digest morning` first to generate content.

**Q: How do I browse past editions?**
A: Click the "Archive" button to open the calendar modal showing all dates and editions.

**Q: Scheduled tasks aren't running?**
A: Run `CronList` in the terminal to check task status. Ensure Claude Code is running.

**Q: Missed a generation?**
A: Manually run the corresponding `/ai-digest` command to backfill.

**Q: Can I customize the content sections?**
A: Yes — edit the classification rules in `CLAUDE.md` to adjust section priorities.

---

<p align="center">
  Built with <a href="https://claude.ai">Claude Code</a> · 
  <a href="https://github.com/DaiOwen/ai-pulse">GitHub</a>
</p>
