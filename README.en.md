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
  <img src="https://img.shields.io/badge/edition-3x%20daily-22c55e" alt="3x Daily">
</p>

---

**AI Pulse** is a daily AI news aggregation HTML page for AI developers, powered by [Claude Code](https://claude.ai). It auto-generates beautiful, responsive HTML pages 3 times daily by scraping and synthesizing news from 30+ platforms and 11 notable AI bloggers across 7 dimensions — aggregators, media, communities, research, official blogs, newsletters, and KOLs. No npm, no Python, no external services — just Claude Code and a terminal.

## 🔗 Live Demo

**[https://daiowen.github.io/ai-pulse/](https://daiowen.github.io/ai-pulse/)**

No installation needed — open in your browser to see the latest AI news digest.

> 💡 **Just here to read?** Open the live demo link above — updated 3x daily, zero setup. Want updates delivered? Subscribe via [RSS](https://daiowen.github.io/ai-pulse/feed.xml).

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🤖 **7 curated sections** | Model Updates, Tools & Deploy, Policy & Compliance, Paper Spotlight, Real-World AI Cases, Open Source Pulse, Global Brief |
| ⚡ **Four-level info depth** | TL;DR (3s) → Headlines (10s) → Summaries (30s) → Full articles |
| 🎨 **Apple-inspired design** | Dark/light theme + dynamic animated orbs + glassmorphism cards + grid animation |
| 📱 **Responsive layout** | Works beautifully on desktop, tablet, and mobile |
| 📅 **Archive calendar** | Browse past editions with an interactive calendar, switch between editions |
| 🔍 **Zero dependencies** | Pure HTML/CSS/JS, no build step, no package manager |
| 🇨🇳 **Chinese AI ecosystem focus** | Priority coverage of domestic models and compliance policies |
| ⏰ **Auto-scheduled** | Generates at 08:00, 12:00, and 20:00 daily |
| 📡 **RSS Feed** | Subscribe via RSS reader for daily automatic updates |
| 📲 **PWA Ready** | Add to home screen, offline-capable with cached content |
| 🔗 **Social sharing** | OG/Twitter meta tags for social media preview |
| 🗺️ **Sitemap** | Auto-generated sitemap.xml for SEO optimization |
| 🩺 **Health Check** | `/ai-digest status` diagnoses Cron, permissions, last generation |

## 🚀 Quick Start

> **Prerequisites:** Install [Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview) CLI and complete the first-time login (`claude login`).

### 1. Clone the repository

```bash
git clone https://github.com/DaiOwen/ai-pulse.git
cd ai-pulse
```

### 2. Launch Claude Code and generate your first edition

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
- Update `feed.xml` RSS feed
- Update `sitemap.xml` for SEO

### 3. Open the generated page

```bash
open index.html    # macOS
start index.html   # Windows
```

Or double-click `index.html` to open it in your browser.

After the first run, cron jobs are auto-registered (08:00 / 12:00 / 20:00 daily) — no further manual steps needed.

> 💡 **What is `/ai-digest`?** It is not a terminal command — it's a **Claude Code slash command** that only works inside a Claude Code chat. Think of it this way: `git clone` runs in your terminal, `/ai-digest morning` is typed into the Claude Code conversation. The `CLAUDE.md` file in the project root acts as an "AI instruction manual" — Claude Code reads it and follows the instructions automatically. You don't write a single line of code.

## ⏰ Scheduled Tasks

After the first manual run, three cron jobs are registered automatically:

| Task | Time | Coverage |
|------|------|----------|
| 🌅 Morning | 08:00 | Overnight global + morning domestic news + arXiv paper |
| ☀️ Noon | 12:00 | Incremental updates from the morning |
| 🌙 Evening | 20:00 | Full-day summary + complete open source data |

> ⚠️ **Important: Cron only fires when Claude Code is running.** If you close your terminal or exit Claude Code, scheduled tasks will not execute. Keep a terminal window open, or use `tmux` / `screen`. You can always run `/ai-digest status` to check if everything is healthy.

## 🎮 Manual Commands

| Command | Description |
|---------|-------------|
| `/ai-digest now` | **Instant update** — auto-picks edition, use anytime outside cron |
| `/ai-digest morning` | Generate morning edition (includes Paper Spotlight) |
| `/ai-digest noon` | Generate noon edition (incremental) |
| `/ai-digest evening` | Generate evening edition (full-day summary + Open Source Top 10) |
| `/ai-digest update` | Pull latest upstream code to sync project updates |
| `/ai-digest status` | Diagnose project health — Cron, permissions, last generation |

## 🔄 Update Mechanism

### Live Demo (GitHub Pages)

Fully automated, zero human intervention:

```
Cron fires (08:00 / 12:00 / 20:00)
  → Claude Code searches & generates HTML + RSS + Sitemap
  → git add & commit & push
  → GitHub Pages auto-deploys (~1-2 min later)
```

### Self-hosted users

Three ways to get the latest:

| Method | Description |
|--------|-------------|
| `/ai-digest update` | **Recommended.** One-click pull of latest upstream code to sync features and design |
| `git pull` | Manual terminal pull — no Claude Code needed |
| `/ai-digest morning` | Run the generation command yourself to collect real-time news |

If you forked the repo and want your own GitHub Pages to auto-update, simply keep Claude Code running locally (cron jobs + git push handle everything). See [CLAUDE.md](CLAUDE.md) for details.

## 📰 Content Sections

| Section | morning | noon | evening | Description |
|---------|:-------:|:----:|:-------:|-------------|
| 🤖 Model Updates | 4-5 | 1-2 | 5 | Priority on Chinese domestic + major global releases |
| 🛠️ Tools & Deploy | 3-4 | 1-2 | 4 | Framework updates, hardware adaptation, inference deployment |
| 📋 Policy & Compliance | 1-2 | 1 | 2 | CAC filings, AI safety reviews, industry standards |
| 💡 Real-World AI Cases | 2 | 1 | 2 | Enterprise AI integration stories & best practices |
| ⭐ Open Source Pulse | Top5 | Top5 | Top10 | GitHub/Gitee Stars rising leaderboard |
| 🌍 Global Brief | 3 | — | 3 | Curated international stories impacting China |
| 📄 Paper Spotlight | 1 | — | — | One curated arXiv paper daily with practical value |

### Source Matrix

Content drawn from 30+ platforms and 11 AI thought leaders across 7 dimensions:

| Dimension | Representative Sources |
|-----------|----------------------|
| 🎯 Aggregators | RadarAI, AIHOT, AIbase, Digg AI |
| 📰 Media | 36Kr, TMTPost, Synced, QbitAI, GeekPark, VentureBeat, The Verge, MIT Technology Review |
| 💬 Communities | Reddit r/ML, Hacker News, Zhihu AI, ModelScope |
| 🔬 Research | arXiv, Papers with Code, Hugging Face |
| 🏢 Official Blogs | OpenAI, DeepMind, Anthropic, Microsoft, Meta, Alibaba Tongyi, ByteDance Doubao, Baidu Wenxin, Zhipu GLM |
| 📧 Newsletters | The Decoder, Import AI |
| 👤 KOLs | Karpathy, Lilian Weng, Jim Fan, Simon Willison, Chip Huyen, Andrew Ng + 5 Chinese bloggers |

> Core rule: a story must appear in 2+ independent sources to be considered a verified hot topic.

### Scoring Algorithm

```
Total Score = Popularity×0.4 + Timeliness×0.3 + Source Quality×0.3

Popularity: Cross-verified(+5) / First-reported(+3) / High community engagement(+1)
Timeliness: Within 6h(+5) / Within 12h(+3) / Within 24h(+1) / Beyond 48h(+0)
Source Quality: 36Kr/VentureBeat/TheVerge(+3) / MIT Tech Review/People.cn/cnblogs(+2) / Others(+1)
```

## 🏗️ Architecture

```
Cron Schedule (08:00 / 12:00 / 20:00)
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
  ① Dedup (title similarity > 80% + URL normalization)
  ② Scoring (popularity×0.4 + timeliness×0.3 + source quality×0.3)
  ③ Translation (global news → localized summaries, preserve key data)
  ④ Classification (7 sections)
  ⑤ Summary generation (2-3 sentences + developer impact note)
       │
       ▼
HTML Generation & Archive
  • Generates fully self-contained HTML (dark/light themes)
  • Saves to archive/YYYY-MM-DD-{edition}.html
  • Updates index.html to latest edition
  • Updates feed.xml RSS feed (keeps last 10 items)
  • Updates sitemap.xml for SEO
  • git commit & push → GitHub Pages auto-deploy
```

## 📁 Project Structure

```
ai-pulse/
├── index.html              # Main page (latest issue + calendar nav)
├── feed.xml                # RSS feed
├── sitemap.xml             # SEO sitemap
├── manifest.json           # PWA config
├── subscribe.html          # RSS subscription guide
├── archive/                # Historical archive
│   └── YYYY-MM-DD-{edition}.html
├── assets/
│   ├── favicon.svg         # Site icon
│   └ og-image.svg          # Social sharing preview image
├── design/                 # Design references
├── screenshots/            # Screenshots
├── .github/                # GitHub configuration
│   ├── workflows/          # GitHub Actions automation
│   ├── ISSUE_TEMPLATE/
│   └── PULL_REQUEST_TEMPLATE.md
├── .claude/                # Claude Code config
│   ├── commands/           # Slash command definitions
│   │   └── ai-digest.md
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
└── README.{md,en.md,ja.md,de.md,ko.md}  # Multi-language docs
```

## 📸 Screenshots

### 🌙 Dark Mode (default)

![AI Pulse Dark Mode](screenshots/dark-mode.png)

### ☀️ Light Mode

![AI Pulse Light Mode](screenshots/light-mode.png)

### 📅 Archive Calendar

![AI Pulse Calendar](screenshots/calendar.png)

## 🔒 Security

**Data privacy and security are foundational design principles.** AI Pulse runs 100% locally — your data never leaves your machine.

| Feature | Description |
|---------|-------------|
| 🏠 Pure local execution | No data upload to third-party servers |
| 🔌 Zero external requests | Generated HTML has no tracking, telemetry, or ads |
| 🔑 No API keys required | No third-party API tokens needed |
| 👁️ MIT open source | Fully auditable code |

See [SECURITY.md](SECURITY.md) for the complete security policy.

## ❓ FAQ

**Q: The live demo keeps showing old content unless I refresh?**
A: Old Service Worker cached the page. **One-time fix:** Open the page → F12 → Application → Service Workers → click "Unregister" → refresh. The new SW (v2) has already fixed this — every visit after unregister will show the latest content.

**Q: Why is index.html blank?**
A: You need to run `/ai-digest morning` first to generate content.

**Q: How do I browse past editions?**
A: Click the "Archive" button in the top-right to open the calendar modal showing all dates and editions (morning/noon/evening).

**Q: Scheduled tasks aren't running?**
A: Run `CronList` in the Claude Code chat to check task status. Ensure Claude Code is running.

**Q: Missed a generation?**
A: Manually run the corresponding `/ai-digest` command to backfill.

**Q: Can I customize the content sections?**
A: Yes — edit the classification rules in `CLAUDE.md` to adjust section priorities and sources.

**Q: Does Claude Code cost money?**
A: Claude Code includes a free tier (~50-100 tool calls/day). One `/ai-digest` run uses ~20-30 calls (search + fetch), so the free tier is sufficient for daily use. For heavier usage, [Claude Pro](https://claude.ai/pricing) ($20/mo) or Max ($100-200/mo) are available.

**Q: Can I just read the news without installing Claude Code?**
A: Absolutely. Two options:
- Visit the live demo: **[https://daiowen.github.io/ai-pulse/](https://daiowen.github.io/ai-pulse/)** — no installation needed
- Clone the repo and `git pull` the latest `index.html`, then open it in your browser

**Q: How long does a generation take? Why does it seem stuck?**
A: A full `/ai-digest` run takes 3-5 minutes (15-20 web searches + 8-10 deep fetches). It's not stuck — please be patient. Run `/ai-digest status` first to verify your setup is correct.

**Q: How do I use RSS subscription?**
A: Subscribe to `https://daiowen.github.io/ai-pulse/feed.xml` with any RSS reader (Feedly, Inoreader, NetNewsWire). Updates are pushed automatically after each edition.

## 🤝 Contributing

We welcome all forms of contributions — bug reports, feature requests, code submissions, and documentation improvements.

Please see [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

## 🗺️ Roadmap

See [ROADMAP.md](ROADMAP.md) for the project's future development plans.

## 📄 License

This project is open-sourced under the MIT License — see the [LICENSE](LICENSE) file for details.

---

<p align="center">
  Built with <a href="https://claude.ai">Claude Code</a> ·
  <a href="https://github.com/DaiOwen/ai-pulse">GitHub</a> ·
  <a href="https://daiowen.github.io/ai-pulse/">Live Demo</a> ·
  <a href="feed.xml">RSS Feed</a> ·
  <a href="CHANGELOG.md">Changelog</a>
</p>