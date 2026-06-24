# Changelog

All notable changes to this project will be documented in this file.

## [1.1.0] - 2026-06-24

### Added
- **RSS Feed** — `feed.xml` auto-generated with each edition, keeps last 10 items
- **Sitemap** — `sitemap.xml` for SEO optimization
- **Social Sharing** — OG/Twitter meta tags for social media preview
- **Subscribe Page** — `subscribe.html` RSS subscription guide
- **PWA Enhancement** — Improved Service Worker with proper cache invalidation
- **Multi-language README** — 5 languages: zh/en/ja/de/ko

### Improved
- **Documentation** — Comprehensive README with tables, better structure
- **Scoring Algorithm** — New weighting: popularity×0.4 + timeliness×0.3 + source quality×0.3
- **Section Content** — Edition-specific content volumes (morning/noon/evening)
- **Architecture** — Complete pipeline documentation

## [1.0.0] - 2026-06-14

### Added
- Initial release
- **7 Content Sections** — Model Updates, Tools & Deploy, Policy & Compliance, Paper Spotlight, Real-World AI Cases, Open Source Pulse, Global Brief
- **3x Daily Editions** — Morning (08:00), Noon (12:00), Evening (20:00)
- **Apple-inspired Design** — Dark/light theme with dynamic orb background, glassmorphism cards
- **Calendar Archive** — Interactive calendar to browse past editions
- **Responsive Layout** — Desktop, tablet, mobile optimized
- **Zero Dependencies** — Pure HTML/CSS/JS, no build tools
- **Claude Code Native** — Slash commands for generation (`/ai-digest`)
- **Cron Scheduling** — Auto-registered scheduled tasks
- **PWA Support** — Add to home screen, offline-capable
- **Source Matrix** — 30+ platforms and 11 AI bloggers across 7 dimensions

---

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).