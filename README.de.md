🌐 **Sprache wählen:** [English](README.en.md) · [中文](README.md) · [日本語](README.ja.md) · [Deutsch](README.de.md) · [한국어](README.ko.md)

<p align="center">
  <img src="assets/favicon.svg" width="64" alt="AI Pulse Logo" />
</p>

<h1 align="center">AI Pulse · Täglicher KI-Nachrichtenüberblick</h1>

<p align="center">
  <em>KI-gestützte tägliche Nachrichtenaggregation für Entwickler. Keine Abhängigkeiten. Claude Code nativ.</em>
</p>

<p align="center">
  <img src="https://img.shields.io/github/stars/DaiOwen/ai-pulse?style=flat&color=yellow" alt="GitHub Stars">
  <img src="https://img.shields.io/badge/license-MIT-blue" alt="Lizenz">
  <img src="https://img.shields.io/badge/dependencies-zero-brightgreen" alt="Keine Abhängigkeiten">
  <img src="https://img.shields.io/github/contributors/DaiOwen/ai-pulse?color=orange" alt="Mitwirkende">
  <img src="https://img.shields.io/badge/PRs-welcome-orange" alt="PRs willkommen">
  <a href="https://daiowen.github.io/ai-pulse/"><img src="https://img.shields.io/badge/demo-live%20preview-6366f1?style=flat" alt="Live Demo"></a>
  <img src="https://img.shields.io/badge/edition-3x%20daily-22c55e" alt="3x täglich">
</p>

---

**AI Pulse** ist eine tägliche KI-Nachrichtenseite für KI-Entwickler, betrieben durch [Claude Code](https://claude.ai). Sie generiert dreimal täglich automatisch wunderschöne, responsive HTML-Seiten aus 30+ Plattformen und 11 notable KI-Bloggern über 7 Dimensionen — Aggregator, Medien, Communitys, Forschung, offizielle Blogs, Newsletter und KOLs. Kein npm, kein Python, keine externen Dienste — nur Claude Code und ein Terminal.

## 🔗 Live-Demo

**[https://daiowen.github.io/ai-pulse/](https://daiowen.github.io/ai-pulse/)**

Keine Installation erforderlich — öffnen Sie es in Ihrem Browser, um die neueste KI-Nachrichtenübersicht zu sehen.

> 💡 **Nur hier, um zu lesen?** Öffnen Sie die Live-Demo oben — 3x täglich aktualisiert, zero Setup. Updates per [RSS](https://daiowen.github.io/ai-pulse/feed.xml) verfügbar.

## ✨ Funktionen

| Funktion | Beschreibung |
|----------|--------------|
| 🤖 **7 kuratierte Bereiche** | Modell-Updates, Tools & Deployment, Richtlinien & Compliance, Paper-Spotlight, reale KI-Anwendungsfälle, Open-Source-Trends, globaler Überblick |
| ⚡ **Vierstufige Informationstiefe** | TL;DR (3s) → Schlagzeilen (10s) → Zusammenfassungen (30s) → Volltexte |
| 🎨 **Apple-inspiriertes Design** | Dunkles/helles Theme + dynamische animierte Orbs + Glas-Morphismuskarten + Grid-Animation |
| 📱 **Responsives Layout** | Optimiert für Desktop, Tablet und Mobilgeräte |
| 📅 **Archiv-Kalender** | Vergangene Ausgaben über interaktiven Kalender durchsuchen, Editionswechsel |
| 🔍 **Keine Abhängigkeiten** | Reines HTML/CSS/JS, kein Build-Schritt, kein Paketmanager |
| 🇨🇳 **Fokus auf chinesisches KI-Ökosystem** | Prioritäre Abdeckung chinesischer Modelle und Compliance-Richtlinien |
| ⏰ **Automatische Zeitplanung** | Generierung um 08:00, 12:00 und 20:00 Uhr |
| 📡 **RSS-Feed** | RSS-Reader-Abonnement für tägliche automatische Updates |
| 📲 **PWA-Ready** | Zum Home-Screen hinzufügen, offline-fähig |
| 🔗 **Social Sharing** | OG/Twitter Meta-Tags für Social-Media-Preview |
| 🗺️ **Sitemap** | Auto-generierte sitemap.xml für SEO-Optimierung |
| 🩺 **Health-Check** | `/ai-digest status` diagnose Cron, Berechtigungen, letzte Generierung |

## 🚀 Schnellstart

> **Voraussetzungen:** Installiere die [Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview) CLI und führe die erste Anmeldung durch (`claude login`).

### 1. Repository klonen

```bash
git clone https://github.com/DaiOwen/ai-pulse.git
cd ai-pulse
```

### 2. Claude Code starten und erste Ausgabe generieren

Starte die Claude Code Oberfläche aus dem Projektverzeichnis:

```bash
claude
```

Claude Code lädt automatisch die Projektkonfiguration (`CLAUDE.md`). Gib im Chat den Slash-Befehl ein:

```
/ai-digest morning
```

Die KI führt automatisch den gesamten Ablauf aus:
- Durchsucht 6+ Quellen nach den neuesten KI-Nachrichten (WebSearch)
- Ruft Top-Artikel detailliert ab (WebFetch)
- Entfernt Duplikate, bewertet, übersetzt und klassifiziert alle Einträge
- Generiert eine vollständige HTML-Seite und speichert sie in `archive/` und `index.html`
- Aktualisiert `feed.xml` RSS-Feed
- Aktualisiert `sitemap.xml` für SEO

### 3. Generierte Seite öffnen

```bash
open index.html    # macOS
start index.html   # Windows
```

Oder doppelklicke auf `index.html`, um sie im Browser zu öffnen.

Nach der ersten Ausführung werden Cron-Jobs automatisch registriert (täglich 08:00 / 12:00 / 20:00) – keine weiteren manuellen Schritte erforderlich.

> 💡 **Was ist `/ai-digest`?** Es ist kein Terminal-Befehl, sondern ein **Claude Code Slash-Befehl** – er funktioniert nur im Claude Code Chat. Zum Vergleich: `git clone` führst du im Terminal aus, `/ai-digest morning` gibst du im Claude Code Gespräch ein. Die `CLAUDE.md` im Projektverzeichnis dient als "KI-Betriebsanleitung" – Claude Code liest sie und führt die Anweisungen automatisch aus. Du musst keine einzige Zeile Code schreiben.

## ⏰ Geplante Aufgaben

Nach der ersten manuellen Ausführung werden automatisch drei Cron-Jobs registriert:

| Aufgabe | Zeit | Abdeckung |
|---------|------|-----------|
| 🌅 Morgen | 08:00 | Nachrichten über Nacht + frühe Neuigkeiten + arXiv-Paper |
| ☀️ Mittag | 12:00 | Inkrementelle Aktualisierungen vom Vormittag |
| 🌙 Abend | 20:00 | Zusammenfassung des gesamten Tages + Open-Source-Daten |

> ⚠️ **Wichtig: Cron feuert nur, wenn Claude Code läuft.** Wenn du das Terminal schließt oder Claude Code beendest, werden geplante Aufgaben nicht ausgeführt. Halte ein Terminal-Fenster offen oder nutze `tmux` / `screen`. Mit `/ai-digest status` kannst du jederzeit prüfen, ob alles funktioniert.

## 🎮 Manuelle Befehle

| Befehl | Beschreibung |
|--------|--------------|
| `/ai-digest now` | **Sofort-Update** — auto-wählt Edition, use anytime |
| `/ai-digest morning` | Morgenausgabe generieren (inkl. Paper-Spotlight) |
| `/ai-digest noon` | Mittagsausgabe generieren (inkrementell) |
| `/ai-digest evening` | Abendausgabe generieren (Tageszusammenfassung + Open-Source Top 10) |
| `/ai-digest update` | Neuesten Upstream-Code pullen für Projekt-Updates |
| `/ai-digest status` | Projekt-Health diagnose — Cron, Berechtigungen, letzte Generierung |

## 🔄 Update-Mechanismus

### Live-Demo (GitHub Pages)

Vollautomatisch, kein manueller Eingriff:

```
Cron feuert (08:00 / 12:00 / 20:00)
  → Claude Code sucht & generiert HTML + RSS + Sitemap
  → git add & commit & push
  → GitHub Pages deployt automatisch (~1-2 Min später)
```

### Self-hosting-Nutzer

Drei Wege für aktuelle Inhalte:

| Methode | Beschreibung |
|---------|--------------|
| `/ai-digest update` | **Empfohlen.** One-Click Pull des neuesten Upstream-Codes |
| `git pull` | Manuelles Terminal-Pull — kein Claude Code nötig |
| `/ai-digest morning` | Befehl selbst ausführen, um aktuelle Nachrichten zu sammeln |

Wenn du das Repository geforkt hast und deine eigenen GitHub Pages automatisch aktualisieren möchtest, halte Claude Code einfach lokal am Laufen (Cron-Jobs + Git Push erledigen alles). Siehe [CLAUDE.md](CLAUDE.md) für Details.

## 📰 Inhaltsbereiche

| Bereich | Morgen | Mittag | Abend | Beschreibung |
|---------|:------:|:------:|:------:|--------------|
| 🤖 Modell-Updates | 4-5 | 1-2 | 5 | Prioritäre Berücksichtigung chinesischer Modelle + globale Releases |
| 🛠️ Tools & Deployment | 3-4 | 1-2 | 4 | Framework-Updates, Hardware-Anpassung, Inferenz-Deployment |
| 📋 Richtlinien & Compliance | 1-2 | 1 | 2 | CAC-Meldungen, KI-Sicherheitsprüfungen, Industriestandards |
| 💡 Reale KI-Anwendungsfälle | 2 | 1 | 2 | Unternehmensintegrationen & Best Practices |
| ⭐ Open-Source-Trends | Top5 | Top5 | Top10 | GitHub/Gitee Stars Top 10 + Aufmerksamkeit Top 10 |
| 🌍 Globaler Überblick | 3 | — | 3 | 3 kuratierte internationale Meldungen mit China-Bezug |
| 📄 Paper-Spotlight | 1 | — | — | Ein täglich kuratiertes arXiv-Paper mit praktischem Wert |

### Quellmatrix

Inhalte aus 30+ Plattformen und 11 KI-Vordenkern über 7 Dimensionen:

| Dimension | Repräsentative Quellen |
|-----------|------------------------|
| 🎯 Aggregatoren | RadarAI, AIHOT, AIbase, Digg AI |
| 📰 Medien | 36Kr, TMTPost, Synced, QbitAI, GeekPark, VentureBeat, The Verge, MIT Technology Review |
| 💬 Communitys | Reddit r/ML, Hacker News, Zhihu AI, ModelScope |
| 🔬 Forschung | arXiv, Papers with Code, Hugging Face |
| 🏢 Offizielle Blogs | OpenAI, DeepMind, Anthropic, Microsoft, Meta, Alibaba Tongyi, ByteDance Doubao, Baidu Wenxin, Zhipu GLM |
| 📧 Newsletter | The Decoder, Import AI |
| 👤 KOLs | Karpathy, Lilian Weng, Jim Fan, Simon Willison, Chip Huyen, Andrew Ng + 5 chinesische Blogger |

> Kernregel: Eine Story muss in 2+ unabhängigen Quellen erscheinen, um als verifizierter Hot-Topic zu gelten.

### Bewertungsalgorithmus

```
Gesamtpunkte = Popularität×0.4 + Aktualität×0.3 + Quellenqualität×0.3

Popularität: Cross-verifiziert(+5) / Erst-berichtet(+3) / Hohe Community-Engagement(+1)
Aktualität: Innerhalb 6h(+5) / Innerhalb 12h(+3) / Innerhalb 24h(+1) / Über 48h(+0)
Quellenqualität: 36Kr/VentureBeat/TheVerge(+3) / MIT Tech Review/People.cn/cnblogs(+2) / Andere(+1)
```

## 🏗️ Architektur

```
Cron-Zeitplan (08:00 / 12:00 / 20:00)
       │
       ▼
Claude Code wird gestartet
       │
       ├─ WebSearch (15-20 Mehrwort-Suchen)
       ├─ WebFetch (Top 5-8 Ergebnisse detailliert abrufen)
       └─ GitHub/Gitee API (Open-Source-Trenddaten)
       │
       ▼
Verarbeitungspipeline
  ① Deduplizierung (Titel-Ähnlichkeit > 80% + URL-Normalisierung)
  ② Bewertung (Popularität×0.4 + Aktualität×0.3 + Quellenqualität×0.3)
  ③ Übersetzung (globale Nachrichten → lokalisierte Zusammenfassungen, Zahlen original)
  ④ Klassifizierung (7 Bereiche)
  ⑤ Zusammenfassung (2-3 Sätze + Entwicklerwirkungsvermerk)
       │
       ▼
HTML-Generierung & Archivierung
  • Erzeugt vollständig eigenständiges HTML (dunkel/hell Themes)
  • Speichert in archive/YYYY-MM-DD-{edition}.html
  • Aktualisiert index.html auf die neueste Ausgabe
  • Aktualisiert feed.xml RSS-Feed (hält letzte 10 Items)
  • Aktualisiert sitemap.xml für SEO
  • git commit & push → GitHub Pages auto-deploy
```

## 📁 Projektstruktur

```
ai-pulse/
├── index.html              # Hauptseite (aktuelle Ausgabe + Kalendernavigation)
├── feed.xml                # RSS-Feed
├── sitemap.xml             # SEO-Sitemap
├── manifest.json           # PWA-Konfiguration
├── subscribe.html          # RSS-Abonnement-Guide
├── archive/                # Historisches Archiv
│   └── YYYY-MM-DD-{edition}.html
├── assets/
│   ├── favicon.svg         # Seitenicon
│   └── og-image.svg        # Social-Sharing-Preview-Bild
├── design/                 # Design-Referenzen
├── screenshots/            # Screenshots
├── .github/                # GitHub-Konfiguration
│   ├── workflows/          # GitHub Actions Automatisierung
│   ├── ISSUE_TEMPLATE/
│   └── PULL_REQUEST_TEMPLATE.md
├── .claude/                # Claude Code Konfiguration
│   ├── commands/           # Slash-Befehl-Definitionen
│   │   └── ai-digest.md
│   ├── settings.json
│   └── scheduled_tasks.json
├── CLAUDE.md               # Projektanweisungen & Skill-Definitionen
├── CONTRIBUTING.md         # Beitragsleitfaden
├── CODE_OF_CONDUCT.md      # Verhaltenskodex
├── ROADMAP.md              # Fahrplan
├── SECURITY.md             # Sicherheitsrichtlinie
├── CHANGELOG.md            # Änderungsprotokoll
├── LICENSE                 # MIT-Lizenz
├── .gitignore
└── README.{md,en.md,ja.md,de.md,ko.md}  # Multi-Language Docs
```

## 📸 Screenshots

### 🌙 Dark Mode (Standard)

![AI Pulse Dark Mode](screenshots/dark-mode.png)

### ☀️ Light Mode

![AI Pulse Light Mode](screenshots/light-mode.png)

### 📅 Archiv-Kalender

![AI Pulse Calendar](screenshots/calendar.png)

## 🔒 Sicherheit

**Datenschutz und Sicherheit sind grundlegende Designprinzipien.** AI Pulse wird 100% lokal ausgeführt — Ihre Daten verlassen niemals Ihren Rechner.

| Merkmal | Beschreibung |
|---------|--------------|
| 🏠 Reine lokale Ausführung | Kein Daten-Upload zu Drittanbieter-Servern |
| 🔌 Null externe Anfragen | Generiertes HTML ohne Tracking, Telemetrie oder Werbung |
| 🔑 Keine API-Schlüssel erforderlich | Keine Drittanbieter-API-Tokens benötigt |
| 👁️ MIT Open Source | Vollständig überprüfbarer Code |

Die vollständige Sicherheitsrichtlinie finden Sie in [SECURITY.md](SECURITY.md).

## ❓ Häufig gestellte Fragen (FAQ)

**F: Die Live-Demo zeigt immer alte Inhalte, außer ich aktualisiere manuell?**
A: Der alte Service Worker hat die Seite zwischengespeichert. **Einmalige Lösung:** Seite öffnen → F12 → Application → Service Workers → "Unregister" klicken → aktualisieren. Der neue SW (v2) hat das Problem bereits behoben — jeder weitere Besuch zeigt die neuesten Inhalte.

**F: Warum ist index.html leer?**
A: Sie müssen zuerst `/ai-digest morning` ausführen, um Inhalte zu generieren.

**F: Wie kann ich frühere Ausgaben durchsuchen?**
A: Klicken Sie auf die Schaltfläche "Archiv" oben rechts, um den Kalender zu öffnen, der alle Daten und Ausgaben (Morgen/Mittag/Abend) anzeigt.

**F: Geplante Aufgaben werden nicht ausgeführt?**
A: Führen Sie `CronList` im Claude Code Chat aus, um den Aufgabenstatus zu prüfen. Stellen Sie sicher, dass Claude Code läuft.

**F: Eine Generierung wurde verpasst?**
A: Führen Sie den entsprechenden `/ai-digest` Befehl manuell aus, um die Ausgabe nachzuholen.

**F: Kann ich die Inhaltsbereiche anpassen?**
A: Ja — bearbeiten Sie die Klassifizierungsregeln in `CLAUDE.md`, um die Bereichsprioritäten und Quellen anzupassen.

**F: Kosten Claude Code Geld?**
A: Claude Code bietet eine kostenlose Nutzung (~50-100 Tool-Aufrufe/Tag). Ein `/ai-digest` Lauf verwendet ~20-30 Aufrufe (Suche + Fetch), sodass die kostenlose Nutzung für den täglichen Gebrauch ausreichend ist. Für intensivere Nutzung sind [Claude Pro](https://claude.ai/pricing) ($20/Monat) oder Max ($100-200/Monat) verfügbar.

**F: Kann ich nur die Nachrichten lesen ohne Claude Code zu installieren?**
A: Absolut. Zwei Optionen:
- Live-Demo besuchen: **[https://daiowen.github.io/ai-pulse/](https://daiowen.github.io/ai-pulse/)** — keine Installation nötig
- Repo klonen und `git pull` die neueste `index.html`, dann im Browser öffnen

**F: Wie lange dauert eine Generierung? Warum scheint sie festzuhängen?**
A: Ein vollständiger `/ai-digest` Lauf dauert 3-5 Minuten (15-20 Web-Suchen + 8-10 Deep-Fetches). Er ist nicht festgehangen — bitte haben Sie Geduld. Führen Sie zuerst `/ai-digest status` aus, um zu überprüfen, ob Ihre Einrichtung korrekt ist.

**F: Wie verwende ich RSS-Abonnement?**
A: Abonnieren Sie `https://daiowen.github.io/ai-pulse/feed.xml` mit einem beliebigen RSS-Reader (Feedly, Inoreader, NetNewsWire). Updates werden nach jeder Edition automatisch gepusht.

## 🤝 Beitragen

Wir heißen alle Formen von Beitragen willkommen — Fehlerberichte, Funktionswünsche, Code-Einreichungen und Dokumentationsverbesserungen.

Ausführliche Richtlinien finden Sie in [CONTRIBUTING.md](CONTRIBUTING.md).

## 🗺️ Fahrplan

Den zukünftigen Entwicklungsplan des Projekts finden Sie in [ROADMAP.md](ROADMAP.md).

## 📄 Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert — siehe [LICENSE](LICENSE) für Details.

---

<p align="center">
  Erstellt mit <a href="https://claude.ai">Claude Code</a> ·
  <a href="https://github.com/DaiOwen/ai-pulse">GitHub</a> ·
  <a href="https://daiowen.github.io/ai-pulse/">Live-Demo</a> ·
  <a href="feed.xml">RSS-Feed</a> ·
  <a href="CHANGELOG.md">Änderungsprotokoll</a>
</p>