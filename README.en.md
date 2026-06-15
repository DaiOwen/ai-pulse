🌐 **Read this in:** [English](README.en.md) · [中文](README.md) · [日本語](README.ja.md) · [Deutsch](README.de.md) · [한국어](README.ko.md)

<p align="center">
  <img src="assets/favicon.svg" width="64" alt="AI Pulse logo" />
</p>

<h1 align="center">AI Pulse · Daily AI News Digest</h1>

<p align="center">
  <em>AI-powered daily news aggregation for developers. Zero deps. Claude Code native.</em>
</p>

<p align="center">
  <img src="https://img.shields.io/github/stars/DaiOwen/ai-pulse?style=flat&color=yellow" alt="GitHub Stars">
  <img src="https://img.shields.io/badge/license-MIT-blue" alt="License">
  <img src="https://img.shields.io/badge/dependencies-zero-brightgreen" alt="Zero Dependencies">
  <img src="https://img.shields.io/github/contributors/DaiOwen/ai-pulse?color=orange" alt="Contributors">
  <img src="https://img.shields.io/badge/PRs-welcome-orange" alt="PRs Welcome">
  <a href="https://daiowen.github.io/ai-pulse/"><img src="https://img.shields.io/badge/demo-live%20preview-6366f1?style=flat" alt="Live Demo"></a>
</p>

---

**AI Pulse** is a daily AI news aggregation HTML page for AI developers, powered by [Claude Code](https://claude.ai). It auto-generates beautiful, responsive HTML pages 3 times daily by scraping and synthesizing news from 6+ sources. No npm, no Python, no external services — just Claude Code and a terminal.

## 🔗 Live Demo

**[https://daiowen.github.io/ai-pulse/](https://daiowen.github.io/ai-pulse/)**

No installation needed — open in your browser to see the latest AI news digest.

> 💡 **Just here to read?** Open the live demo link above — updated 3x daily, zero setup. Want updates delivered? Subscribe via [RSS](feed.xml).

## Features

- 🤖 **7 curated sections** — Model Updates, Tools & Deploy, Policy & Compliance, Paper Spotlight, Real-World AI Cases, Open Source Pulse, Global Brief
- ⚡ **Four-level information depth** — TL;DR (3s) → Headlines (10s) → Summaries (30s) → Full articles
- 🎨 **Apple-inspired design** — Dark/light theme with dynamic animated background, glassmorphism cards
- 📱 **Responsive layout** — Works beautifully on desktop, tablet, and mobile
- 📅 **Archive calendar** — Browse past editions with an interactive calendar
- 🔍 **Zero dependencies** — Pure HTML/CSS/JS, no build step, no package manager
- 🇨🇳 **Chinese AI ecosystem focus** — Priority coverage of domestic models and compliance policies
- ⏰ **Auto-scheduled** — Generates at 07:49, 12:17, and 20:13 daily
- 📡 **RSS Feed** — Subscribe via RSS reader for daily automatic updates
- 📲 **PWA Ready** — Add to home screen, offline-capable with cached content
- 🩺 **Health Check** — `/ai-digest status` diagnoses Cron, permissions, last generation

## Quick Start

> **Prerequisites:** Install [Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview) CLI and complete the first-time login (`claude login`).

**1. Clone the repository**

```bash
git clone https://github.com/DaiOwen/ai-pulse.git
cd ai-pulse
```

**2. Launch Claude Code and generate your first edition**

Start the Claude Code interactive interface from the project directory:
```bash
claude
```

Claude Code automatically loads the project config (`CLAUDE.md`). In the chat, enter the slash command:

```
/ai-digest morning
```

The AI will automatically complete the full pipeline:
- Search 6+ sources for the latest AI news (WebSearch)
- Deep-fetch top articles for full content (WebFetch)
- Deduplicate, score, translate, and classify all items
- Generate a complete standalone HTML page saved to `archive/` and `index.html`

**3. Open the generated page**

```bash
open index.html    # macOS
start index.html   # Windows
```

Or double-click `index.html` to open it in your browser.

After the first run, cron jobs are auto-registered (07:49 / 12:17 / 20:13 daily) — no further manual steps needed.

> 💡 **What is `/ai-digest`?** It is not a terminal command — it's a **Claude Code slash command** that only works inside a Claude Code chat. Think of it this way: `git clone` runs in your terminal, `/ai-digest morning` is typed into the Claude Code conversation. The `CLAUDE.md` file in the project root acts as an "AI instruction manual" — Claude Code reads it and follows the instructions automatically. You don't write a single line of code.

### Scheduled Tasks

After the first manual run, three cron jobs are registered automatically:

| Task | Time | Coverage |
|------|------|----------|
| 🌅 Morning | 07:49 | Overnight global + morning domestic news |
| ☀️ Noon | 12:17 | Incremental updates from the morning |
| 🌙 Evening | 20:13 | Full-day summary + all-day open source data |

> ⚠️ **Important: Cron only fires when Claude Code is running.** If you close your terminal or exit Claude Code, scheduled tasks will not execute. Keep a terminal window open, or use `tmux` / `screen`. You can always run `/ai-digest status` to check if everything is healthy.

### Manual Commands

| Command | Description |
|---------|-------------|
| `/ai-digest now` | **Instant update** — auto-picks edition, use anytime outside cron |
| `/ai-digest morning` | Generate morning edition |
| `/ai-digest noon` | Generate noon edition (incremental) |
| `/ai-digest evening` | Generate evening edition (full-day summary) |
| `/ai-digest update` | Pull latest upstream code to sync project updates |
| `/ai-digest status` | Diagnose project health — Cron, permissions, last generation |

### Update Mechanism

**Live Demo (GitHub Pages)** — fully automated, zero human intervention:

```
Cron fires (07:49 / 12:17 / 20:13)
  → Claude Code searches & generates HTML
  → git add & commit & push
  → GitHub Pages auto-deploys (~1-2 min later)
```

**Self-hosted users** — three ways to get the latest:

| Method | Description |
|--------|-------------|
| `/ai-digest update` | **Recommended.** One-click pull of latest upstream code to sync features and design |
| `git pull` | Manual terminal pull — no Claude Code needed |
| `/ai-digest morning` | Run the generation command yourself to collect real-time news |

If you forked the repo and want your own GitHub Pages to auto-update, simply keep Claude Code running locally (cron jobs + git push handle everything). See [CLAUDE.md](CLAUDE.md) for details.

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
├── screenshots/            # Screenshots
├── .github/                # GitHub configuration
│   ├── ISSUE_TEMPLATE/
│   └── PULL_REQUEST_TEMPLATE.md
├── .claude/                # Claude Code config
│   ├── settings.json
│   └── scheduled_tasks.json
├── CLAUDE.md               # Project instructions & Skill definitions
├── CONTRIBUTING.md         # Contribution guide
├── CODE_OF_CONDUCT.md      # Code of conduct
├── ROADMAP.md              # Project roadmap
├── SECURITY.md             # Security policy
├── CHANGELOG.md            # Changelog
├── LICENSE                 # MIT license
├── .gitignore
└── README.md
```

## Screenshots

### 🌙 Dark Mode (default)

![AI Pulse Dark Mode](screenshots/dark-mode.png)

### ☀️ Light Mode

![AI Pulse Light Mode](screenshots/light-mode.png)

## Security

**Data privacy and security are foundational design principles.** AI Pulse runs 100% locally — your data never leaves your machine.

- 🏠 Pure local execution, zero data upload
- 🔌 Generated HTML makes no external requests (no tracking, no telemetry, no ads)
- 🔑 No third-party API keys or tokens required
- 👁️ MIT open source, fully auditable code

See [SECURITY.md](SECURITY.md) for the complete security policy.

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

**Q: Does Claude Code cost money?**
A: Claude Code includes a free tier (~50-100 tool calls/day). One `/ai-digest` run uses ~20-30 calls (search + fetch), so the free tier is sufficient for daily use. For heavier usage, [Claude Pro](https://claude.ai/pricing) ($20/mo) or Max ($100-200/mo) are available.

**Q: Can I just read the news without installing Claude Code?**
A: Absolutely. Two options:
- Visit the live demo: **[https://daiowen.github.io/ai-pulse/](https://daiowen.github.io/ai-pulse/)** — no installation needed
- Clone the repo and `git pull` the latest `index.html`, then open it in your browser

**Q: How long does a generation take? Why does it seem stuck?**
A: A full `/ai-digest` run takes 3-5 minutes (15-20 web searches + 8-10 deep fetches). It's not stuck — please be patient. Run `/ai-digest status` first to verify your setup is correct.

## Contributing

We welcome all forms of contributions — bug reports, feature requests, code submissions, and documentation improvements.

Please see [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

## Roadmap

See [ROADMAP.md](ROADMAP.md) for the project's future development plans.

## License

This project is open-sourced under the MIT License — see the [LICENSE](LICENSE) file for details.

---

<p align="center">
  Built with <a href="https://claude.ai">Claude Code</a> ·
  <a href="https://github.com/DaiOwen/ai-pulse">GitHub</a> ·
  <a href="https://daiowen.github.io/ai-pulse/">Live Demo</a> ·
  <a href="CHANGELOG.md">Changelog</a>
</p>
