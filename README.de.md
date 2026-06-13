🌐 **Sprache wählen:** [English](README.en.md) · [中文](README.md) · [日本語](README.ja.md) · [Deutsch](README.de.md) · [한국어](README.ko.md)

<p align="center">
  <img src="assets/favicon.svg" width="64" alt="AI Pulse Logo" />
</p>

<h1 align="center">AI Pulse · Taglicher KI-Nachrichtenuberblick</h1>

<p align="center">
  <em>KI-gestutzte tagliche Nachrichtenaggregation fur Entwickler. Keine Abhangigkeiten. Claude Code nativ.</em>
</p>

<p align="center">
  <img src="https://img.shields.io/github/stars/DaiOwen/ai-pulse?style=flat&color=yellow" alt="GitHub Stars">
  <img src="https://img.shields.io/badge/license-MIT-blue" alt="Lizenz">
  <img src="https://img.shields.io/badge/dependencies-zero-brightgreen" alt="Keine Abhangigkeiten">
  <img src="https://img.shields.io/github/contributors/DaiOwen/ai-pulse?color=orange" alt="Mitwirkende">
  <img src="https://img.shields.io/badge/PRs-welcome-orange" alt="PRs willkommen">
  <a href="https://daiowen.github.io/ai-pulse/"><img src="https://img.shields.io/badge/demo-live%20preview-6366f1?style=flat" alt="Live Demo"></a>
</p>

---

**AI Pulse** ist eine tagliche KI-Nachrichtenseite fur KI-Entwickler, betrieben durch [Claude Code](https://claude.ai). Sie generiert dreimal taglich automatisch wunderschone, responsive HTML-Seiten aus 6+ Quellen. Kein npm, kein Python, keine externen Dienste — nur Claude Code und ein Terminal.

## 🔗 Live-Demo

**[https://daiowen.github.io/ai-pulse/](https://daiowen.github.io/ai-pulse/)**

Keine Installation erforderlich — offnen Sie es in Ihrem Browser, um die neueste KI-Nachrichtenubersicht zu sehen.

## Funktionen

- 🤖 **7 kuratierte Bereiche** — Modell-Updates, Tools & Deployment, Richtlinien & Compliance, Paper-Spotlight, reale KI-Anwendungsfalle, Open-Source-Trends, globaler Uberblick
- ⚡ **Vierstufige Informationstiefe** — TL;DR (3s) → Schlagzeilen (10s) → Zusammenfassungen (30s) → Volltexte
- 🎨 **Apple-inspiriertes Design** — Dunkles/helles Theme mit dynamischem animiertem Hintergrund, Glas-Morphismuskarten
- 📱 **Responsives Layout** — Optimiert fur Desktop, Tablet und Mobilgerate
- 📅 **Archiv-Kalender** — Vergangene Ausgaben uber einen interaktiven Kalender durchsuchen
- 🔍 **Keine Abhangigkeiten** — Reines HTML/CSS/JS, kein Build-Schritt, kein Paketmanager
- 🇨🇳 **Fokus auf das chinesische KI-Okosystem** — Prioritare Abdeckung chinesischer Modelle und Compliance-Richtlinien
- ⏰ **Automatische Zeitplanung** — Generierung um 07:49, 12:17 und 20:13 Uhr

## Schnellstart

```bash
# 1. Repository klonen
git clone https://github.com/DaiOwen/ai-pulse.git
cd ai-pulse

# 2. Erste Ausgabe generieren
（Claude Code lad die Projektkonfiguration automatisch）
/ai-digest morning

# 3. index.html im Browser offnen
```

Beim ersten Durchlauf fuhrt Claude Code automatisch folgende Schritte aus:
- Durchsucht 6+ Quellen nach den neuesten KI-Nachrichten (WebSearch)
- Ruft Top-Artikel detailliert ab (WebFetch)
- Entfernt Duplikate, bewertet, ubersetzt und klassifiziert alle Eintrage
- Generiert eine vollstandige, eigenstandige HTML-Seite und speichert sie in `archive/` und `index.html`

### Geplante Aufgaben

Nach der ersten manuellen Ausführung werden automatisch drei Cron-Jobs registriert:

| Aufgabe | Zeit | Abdeckung |
|---------|------|-----------|
| 🌅 Morgen | 07:49 | Nachrichten uber Nacht + fruhe Neuigkeiten |
| ☀️ Mittag | 12:17 | Inkrementelle Aktualisierungen vom Vormittag |
| 🌙 Abend | 20:13 | Zusammenfassung des gesamten Tages + Open-Source-Daten |

### Manuelle Befehle

| Befehl | Beschreibung |
|--------|--------------|
| `/ai-digest morning` | Morgenausgabe generieren |
| `/ai-digest noon` | Mittagsausgabe generieren (inkrementell) |
| `/ai-digest evening` | Abendausgabe generieren (Tageszusammenfassung) |

## Inhaltsbereiche

| Bereich | Beschreibung |
|---------|--------------|
| 🤖 Modell-Updates | Prioritare Berucksichtigung chinesischer Modelle + globale Releases |
| 🛠️ Tools & Deployment | Framework-Updates, Hardware-Anpassung, Inferenz-Deployment |
| 📋 Richtlinien & Compliance | CAC-Meldungen, KI-Sicherheitsprufungen, Industriestandards |
| 📄 Paper-Spotlight | Ein taglich kuratiertes arXiv-Paper mit praktischem Wert |
| 💡 Reale KI-Anwendungsfalle | Unternehmensintegrationen & Best Practices |
| ⭐ Open-Source-Trends | GitHub/Gitee Stars Top 10 + Aufmerksamkeit Top 10 |
| 🌍 Globaler Uberblick | 3 kuratierte internationale Meldungen mit China-Bezug |

## Architektur

```
Cron-Zeitplan (07:49 / 12:17 / 20:13)
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
  ① Deduplizierung (Titel-Ahnlichkeit + URL-Normalisierung)
  ② Bewertung (Popularitat×0.4 + Aktualitat×0.3 + Quellenqualitat×0.3)
  ③ Ubersetzung (globale Nachrichten → lokalisierte Zusammenfassungen)
  ④ Klassifizierung (7 Bereiche)
  ⑤ Zusammenfassung (2-3 Satze + Entwicklerwirkungsvermerk)
       │
       ▼
HTML-Generierung & Archivierung
  • Erzeugt vollstandig eigenstandiges HTML
  • Speichert in archive/YYYY-MM-DD-{edition}.html
  • Aktualisiert index.html auf die neueste Ausgabe
```

## Projektstruktur

```
ai-pulse/
├── index.html              # Hauptseite (aktuelle Ausgabe + Kalendernavigation)
├── archive/                # Historisches Archiv
│   └── YYYY-MM-DD-{edition}.html
├── assets/
│   └── favicon.svg         # Seitenicon
├── design/                 # Design-Referenzen
├── screenshots/            # Screenshots
├── .github/                # GitHub-Konfiguration
│   ├── ISSUE_TEMPLATE/
│   └── PULL_REQUEST_TEMPLATE.md
├── .claude/                # Claude Code Konfiguration
│   ├── settings.json
│   └── scheduled_tasks.json
├── CLAUDE.md               # Projektanweisungen & Skill-Definitionen
├── CONTRIBUTING.md         # Beitragsleitfaden
├── CODE_OF_CONDUCT.md      # Verhaltenskodex
├── ROADMAP.md              # Fahrplan
├── SECURITY.md             # Sicherheitsrichtlinie
├── CHANGELOG.md            # Anderungsprotokoll
├── LICENSE                 # MIT-Lizenz
├── .gitignore
└── README.md
```

## Screenshots

### 🌙 Dark Mode (Standard)

![AI Pulse Dark Mode](screenshots/dark-mode.png)

### ☀️ Light Mode

![AI Pulse Light Mode](screenshots/light-mode.png)

## Sicherheit

**Datenschutz und Sicherheit sind grundlegende Designprinzipien.** AI Pulse wird 100% lokal ausgefuhrt — Ihre Daten verlassen niemals Ihren Rechner.

- 🏠 Reine lokale Ausfuhrung, kein Daten-Upload
- 🔌 Generiertes HTML stellt keine externen Anfragen (kein Tracking, keine Telemetrie, keine Werbung)
- 🔑 Keine API-Schlussel oder Tokens von Drittanbietern erforderlich
- 👁️ MIT Open Source, vollstandig uberprufbarer Code

Die vollstandige Sicherheitsrichtlinie finden Sie in [SECURITY.md](SECURITY.md).

## Haufig gestellte Fragen (FAQ)

**F: Warum ist index.html leer?**
A: Sie mussen zuerst `/ai-digest morning` ausfuhren, um Inhalte zu generieren.

**F: Wie kann ich fruhere Ausgaben durchsuchen?**
A: Klicken Sie auf die Schaltflache "Archiv", um den Kalender zu offnen, der alle Daten und Ausgaben anzeigt.

**F: Geplante Aufgaben werden nicht ausgefuhrt?**
A: Fuhren Sie `CronList` im Terminal aus, um den Aufgabenstatus zu prufen. Stellen Sie sicher, dass Claude Code lauft.

**F: Eine Generierung wurde verpasst?**
A: Fuhren Sie den entsprechenden `/ai-digest` Befehl manuell aus, um die Ausgabe nachzuholen.

**F: Kann ich die Inhaltsbereiche anpassen?**
A: Ja — bearbeiten Sie die Klassifizierungsregeln in `CLAUDE.md`, um die Bereichsprioritaten anzupassen.

## Beitragen

Wir heißen alle Formen von Beitragen willkommen — Fehlerberichte, Funktionswunsche, Code-Einreichungen und Dokumentationsverbesserungen.

Ausfuhrliche Richtlinien finden Sie in [CONTRIBUTING.md](CONTRIBUTING.md).

## Fahrplan

Den zukunftigen Entwicklungsplan des Projekts finden Sie in [ROADMAP.md](ROADMAP.md).

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert — siehe [LICENSE](LICENSE) fur Details.

---

<p align="center">
  Erstellt mit <a href="https://claude.ai">Claude Code</a> ·
  <a href="https://github.com/DaiOwen/ai-pulse">GitHub</a> ·
  <a href="https://daiowen.github.io/ai-pulse/">Live-Demo</a> ·
  <a href="CHANGELOG.md">Anderungsprotokoll</a>
</p>
