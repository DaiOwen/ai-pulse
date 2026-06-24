🌐 **言語を選択:** [English](README.en.md) · [中文](README.md) · [日本語](README.ja.md) · [Deutsch](README.de.md) · [한국어](README.ko.md)

<p align="center">
  <img src="assets/favicon.svg" width="64" alt="AI Pulse ロゴ" />
</p>

<h1 align="center">AI Pulse · 日次 AI ニュースダイジェスト</h1>

<p align="center">
  <em>AI 開発者のための日次ニュース自動集約。ゼロ依存。Claude Code ネイティブ。</em>
</p>

<p align="center">
  <img src="https://img.shields.io/github/stars/DaiOwen/ai-pulse?style=flat&color=yellow" alt="GitHub Stars">
  <img src="https://img.shields.io/badge/license-MIT-blue" alt="ライセンス">
  <img src="https://img.shields.io/badge/dependencies-zero-brightgreen" alt="依存関係ゼロ">
  <img src="https://img.shields.io/github/contributors/DaiOwen/ai-pulse?color=orange" alt="貢献者">
  <img src="https://img.shields.io/badge/PRs-welcome-orange" alt="PR 歓迎">
  <a href="https://daiowen.github.io/ai-pulse/"><img src="https://img.shields.io/badge/demo-live%20preview-6366f1?style=flat" alt="Live Demo"></a>
  <img src="https://img.shields.io/badge/edition-3x%20daily-22c55e" alt="毎日3回">
</p>

---

**AI Pulse** は、[Claude Code](https://claude.ai) で動作する AI 開発者向け日次ニュース集約ページです。30以上のプラットフォームと11名の著名AIブロガーから、1日3回自動でニュースを収集・整理し、美しいHTMLページを生成します。npm、Python、外部サービスは一切不要。Claude Codeとターミナルだけで完結します。

## 🔗 ライブデモ

**[https://daiowen.github.io/ai-pulse/](https://daiowen.github.io/ai-pulse/)**

インストール不要 — ブラウザで開くだけで最新の AI ニュースダイジェストをご覧いただけます。

> 💡 **ニュースを読むだけ？** 上記のライブデモリンクを開くだけ — 毎日3回自動更新、セットアップ不要。RSSリーダーで[RSS購読](https://daiowen.github.io/ai-pulse/feed.xml)も可能です。

## ✨ 機能

| 機能 | 説明 |
|------|------|
| 🤖 **7つのセクション** | モデルアップデート、ツール&デプロイ、ポリシー&コンプライアンス、論文スポットライト、実世界のAI事例、オープンソース動向、グローバルブリーフ |
| ⚡ **4段階の情報深度** | TL;DR(3秒) → 見出し(10秒) → 要約(30秒) → 全文 |
| 🎨 **Appleデザイン美学** | ダーク/ライトテーマ + 動的アニメーション光球 + ガラスモーフィズムカード + グリッドアニメーション |
| 📱 **レスポンシブレイアウト** | デスクトップ、タブレット、モバイルで快適に表示 |
| 📅 **アーカイブカレンダー** | インタラクティブカレンダーで過去のエディションを閲覧、版次切替対応 |
| 🔍 **ゼロ依存** | 純粋なHTML/CSS/JS、ビルドツール不要 |
| 🇨🇳 **中国AIエコシステム重視** | 中国国内モデルの動向とコンプライアンス情報を優先 |
| ⏰ **定期自動実行** | 毎日 08:00 / 12:00 / 20:00 に自動生成 |
| 📡 **RSSフィード** | RSSリーダーで購読可能、毎日自動更新 |
| 📲 **PWA対応** | ホーム画面に追加可能、オフライン閲覧対応 |
| 🔗 **ソーシャル共有** | OG/Twitterメタタグでソーシャルメディアプレビュー対応 |
| 🗺️ **サイトマップ** | sitemap.xml自動生成、SEO最適化 |
| 🩺 **ヘルスチェック** | `/ai-digest status` でCron、権限、最終生成時刻を診断 |

## 🚀 クイックスタート

> **前提条件：** [Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview) CLI をインストールし、初回ログイン（`claude login`）を完了してください。

### 1. リポジトリをクローン

```bash
git clone https://github.com/DaiOwen/ai-pulse.git
cd ai-pulse
```

### 2. Claude Code を起動して初号を生成

プロジェクトディレクトリで Claude Code の対話画面を起動します：

```bash
claude
```

Claude Code がプロジェクト設定（`CLAUDE.md`）を自動的に読み込みます。チャットでスラッシュコマンドを入力してください：

```
/ai-digest morning
```

AI が以下の全工程を自動実行します：
- 6以上の情報源から最新 AI ニュースを検索（WebSearch）
- トップ記事を詳細取得（WebFetch）
- 重複除去、スコアリング、翻訳、分類
- 完全な HTML を生成し `archive/` と `index.html` に保存
- `feed.xml` RSSフィードを更新
- `sitemap.xml` を更新

### 3. 生成されたページを開く

```bash
open index.html    # macOS
start index.html   # Windows
```

または `index.html` をダブルクリックしてブラウザで開きます。

初回実行後、定期タスクが自動登録されます（毎日 08:00 / 12:00 / 20:00）。以降の手動操作は不要です。

> 💡 **`/ai-digest` とは？** これはターミナルコマンドではなく、**Claude Code のスラッシュコマンド**です。Claude Code のチャット画面でのみ機能します。`git clone` はターミナルで実行し、`/ai-digest morning` は Claude Code との会話の中で入力します。プロジェクト直下の `CLAUDE.md` が「AIの取り扱い説明書」となり、Claude Code がそれを読み取って自動的に指示に従います。コードを一行も書く必要はありません。

## ⏰ 定期実行タスク

初回手動実行後、以下の3つのスケジュールタスクが自動登録されます：

| タスク | 時刻 | 対象範囲 |
|--------|------|----------|
| 🌅 朝刊 | 08:00 | 昨夜の海外 + 国内朝のニュース + arXiv論文 |
| ☀️ 昼刊 | 12:00 | 午前中の更新を差分反映 |
| 🌙 夕刊 | 20:00 | 終日サマリー + オープンソース完全版 |

> ⚠️ **重要：Cron は Claude Code 実行中のみ動作します。** ターミナルを閉じたり Claude Code を終了すると、スケジュールタスクは実行されません。ターミナルウィンドウを開いたままにするか、`tmux` / `screen` を使用してください。`/ai-digest status` でいつでも状態を確認できます。

## 🎮 手動コマンド

| コマンド | 説明 |
|----------|------|
| `/ai-digest now` | **即時更新** — 自動で版次を選択、Cronを待ちたくない場合に使用 |
| `/ai-digest morning` | 朝刊を生成（論文スポットライト含む） |
| `/ai-digest noon` | 昼刊を生成（差分更新） |
| `/ai-digest evening` | 夕刊を生成（終日サマリー + オープンソースTop10） |
| `/ai-digest update` | 上流の最新コードを取得してプロジェクトを同期 |
| `/ai-digest status` | プロジェクト状態を診断 — Cron、権限、最終生成時刻 |

## 🔄 更新メカニズム

### ライブデモ（GitHub Pages）

完全自動化、人手不要：

```
Cron 実行 (08:00 / 12:00 / 20:00)
  → Claude Code がニュース検索 & HTML + RSS + Sitemap 生成
  → git add & commit & push
  → GitHub Pages が自動デプロイ（約 1～2 分後に更新）
```

### セルフホストユーザー

最新コンテンツを取得する3つの方法：

| 方法 | 説明 |
|------|------|
| `/ai-digest update` | **推奨。** ワンクリックで上流の最新コードを取得 |
| `git pull` | 手動でターミナルからプル（Claude Code 不要） |
| `/ai-digest morning` | 生成コマンドを自分で実行して最新ニュースを収集 |

リポジトリをフォークして自分の GitHub Pages を自動更新したい場合は、ローカルで Claude Code を起動したままにするだけです（Cron ジョブ + git push がすべて自動実行）。詳細は [CLAUDE.md](CLAUDE.md) をご覧ください。

## 📰 コンテンツセクション

| セクション | 朝刊 | 昼刊 | 夕刊 | 説明 |
|------------|:----:|:----:|:----:|------|
| 🤖 モデルアップデート | 4-5 | 1-2 | 5 | 中国国内モデル優先 + 国際的な主要リリース |
| 🛠️ ツール & デプロイ | 3-4 | 1-2 | 4 | フレームワーク更新、ハードウェア適応、推論デプロイ |
| 📋 ポリシー & コンプライアンス | 1-2 | 1 | 2 | CAC届出、AI安全審査、業界標準 |
| 💡 実世界のAI事例 | 2 | 1 | 2 | 企業AI統合事例、ベストプラクティス |
| ⭐ オープンソース動向 | Top5 | Top5 | Top10 | GitHub/Gitee Stars上昇ランキング |
| 🌍 グローバルブリーフ | 3 | — | 3 | 中国に影響を与える海外動向 |
| 📄 論文スポットライト | 1 | — | — | 実用価値のあるarXiv論文を日替わりで厳選 |

### 情報源マトリックス

7つの次元、30以上のプラットフォームと11名のAI思想リーダーから情報を収集：

| 次元 | 代表的情報源 |
|------|-------------|
| 🎯 アグリゲーター | RadarAI, AIHOT, AIbase, Digg AI |
| 📰 メディア | 36Kr, TMTPost, Synced, QbitAI, GeekPark, VentureBeat, The Verge, MIT Technology Review |
| 💬 コミュニティ | Reddit r/ML, Hacker News, 知乎 AI, ModelScope |
| 🔬 研究 | arXiv, Papers with Code, Hugging Face |
| 🏢 公式ブログ | OpenAI, DeepMind, Anthropic, Microsoft, Meta, 阿里通義, 字節豆包, 百度文心, 智譜GLM |
| 📧 ニュースレター | The Decoder, Import AI |
| 👤 KOL | Karpathy, Lilian Weng, Jim Fan, Simon Willison, Chip Huyen, Andrew Ng + 中国人ブロガー5名 |

> コアルール：ニュースは2つ以上の独立した情報源で確認されたもののみを掲載。

### スコアリングアルゴリズム

```
総合スコア = 人気度×0.4 + 新規性×0.3 + 情報源品質×0.3

人気度：複数ソース確認済み(+5) / 最初の報道(+3) / コミュニティ盛り上がり(+1)
新規性：6時間以内(+5) / 12時間以内(+3) / 24時間以内(+1) / 48時間超過(+0)
情報源品質：36Kr/VentureBeat/TheVerge(+3) / MIT Tech Review/人民網/cnblogs(+2) / その他(+1)
```

## 🏗️ アーキテクチャ

```
Cron スケジュール (08:00 / 12:00 / 20:00)
       │
       ▼
Claude Code 起動
       │
       ├─ WebSearch（15-20 回の複数キーワード検索）
       ├─ WebFetch（上位 5-8 件を深堀り取得）
       └─ GitHub/Gitee API（オープンソース動向データ）
       │
       ▼
処理パイプライン
  ① 重複除去（タイトル類似度 > 80% + URL 正規化）
  ② スコアリング（人気×0.4 + 新規性×0.3 + 品質×0.3）
  ③ 翻訳（海外ニュース → 日本語/中国語要約、数値は原文維持）
  ④ 分類（7 セクション）
  ⑤ 要約生成（各 2-3 文 + 開発者影響度の注釈）
       │
       ▼
HTML 生成 & アーカイブ
  • 完全自己完結型 HTML を生成（ダーク/ライトテーマ）
  • archive/YYYY-MM-DD-{edition}.html に保存
  • index.html を最新版に更新
  • feed.xml RSSフィードを更新（直近10件を保持）
  • sitemap.xml を更新
  • git commit & push → GitHub Pages 自動デプロイ
```

## 📁 プロジェクト構造

```
ai-pulse/
├── index.html              # メインページ（最新号 + カレンダーナビ）
├── feed.xml                # RSSフィード
├── sitemap.xml             # SEOサイトマップ
├── manifest.json           # PWA設定
├── subscribe.html          # RSS購読ガイド
├── archive/                # 履履歴アーカイブ
│   └── YYYY-MM-DD-{edition}.html
├── assets/
│   ├── favicon.svg         # サイトアイコン
│   └── og-image.svg        # ソーシャル共有プレビュー画像
├── design/                 # デザイン参考
├── screenshots/            # スクリーンショット
├── .github/                # GitHub 設定
│   ├── workflows/          # GitHub Actions自動化
│   ├── ISSUE_TEMPLATE/
│   └── PULL_REQUEST_TEMPLATE.md
├── .claude/                # Claude Code 設定
│   ├── commands/           # スラッシュコマンド定義
│   │   └── ai-digest.md
│   ├── settings.json
│   └── scheduled_tasks.json
├── CLAUDE.md               # プロジェクト指示 + Skill定義
├── CONTRIBUTING.md         # 貢献ガイド
├── CODE_OF_CONDUCT.md      # 行動規範
├── ROADMAP.md              # ロードマップ
├── SECURITY.md             # セキュリティポリシー
├── CHANGELOG.md            # 変更履歴
├── LICENSE                 # MIT ライセンス
├── .gitignore
└── README.{md,en.md,ja.md,de.md,ko.md}  # 多言語ドキュメント
```

## 📸 スクリーンショット

### 🌙 ダークモード（デフォルト）

![AI Pulse Dark Mode](screenshots/dark-mode.png)

### ☀️ ライトモード

![AI Pulse Light Mode](screenshots/light-mode.png)

### 📅 アーカイブカレンダー

![AI Pulse Calendar](screenshots/calendar.png)

## 🔒 セキュリティ

**データプライバシーとセキュリティは基本設計原則です。** AI Pulse は 100% ローカルで実行され、データが外部に出ることはありません。

| 特徴 | 説明 |
|------|------|
| 🏠 純粋なローカル実行 | サードパーティサーバーへのデータアップロードなし |
| 🔌 ゼロ外部リクエスト | 生成されたHTMLはトラッキング、テレメトリ、広告なし |
| 🔑 APIキー不要 | サードパーティのAPIトークンが不要 |
| 👁️ MITオープンソース | 完全に監査可能なコード |

完全なセキュリティポリシーについては [SECURITY.md](SECURITY.md) をご覧ください。

## ❓ よくある質問（FAQ）

**Q: ライブデモが毎回古いコンテンツを表示し、手動更新が必要？**
A: 旧バージョンの Service Worker がページをキャッシュしていました。**一度だけの修正：** ページを開く → F12 → Application → Service Workers → "Unregister" をクリック → 更新。新しい SW（v2）はこの問題を修正済みで、以降は常に最新コンテンツが表示されます。

**Q: index.html が空白で表示されます。**
A: 初回は `/ai-digest morning` を実行してコンテンツを生成してください。

**Q: 過去のエディションを閲覧するには？**
A: 右上の「アーカイブ」ボタンをクリックし、カレンダーモーダルから過去の日付と版（朝/昼/夕）を選択します。

**Q: 定期タスクが実行されません。**
A: Claude Code チャットで `CronList` を実行してタスク状態を確認してください。Claude Code が起動していることを確認します。

**Q: 生成を逃した日があります。**
A: 該当する `/ai-digest` コマンドを手動実行してバックフィルできます。

**Q: コンテンツセクションをカスタマイズできますか？**
A: はい — `CLAUDE.md` の分類ルールを編集することでセクションの優先順位と情報源を調整できます。

**Q: Claude Code は有料ですか？**
A: Claude Code には無料枠（約50-100回/日のツール呼び出し）があります。1回の `/ai-digest` は約20-30回（検索 + 取得）を消費するため、日常利用には無料枠で十分です。より高頻度の利用には [Claude Pro](https://claude.ai/pricing)（$20/月）または Max（$100-200/月）がご利用いただけます。

**Q: Claude Code をインストールせずにニュースだけ読めますか？**
A: もちろん。2つの方法があります：
- ライブデモにアクセス：**[https://daiowen.github.io/ai-pulse/](https://daiowen.github.io/ai-pulse/)** — インストール不要
- リポジトリをクローンして `git pull` で最新の `index.html` を取得、ブラウザで開く

**Q: 1回の生成にどれくらいかかりますか？止まっているようですが？**
A: 完全な `/ai-digest` は3-5分かかります（15-20回のWeb検索 + 8-10回の深堀り取得）。止まっているわけではありません — お待ちください。まず `/ai-digest status` を実行して設定が正しいか確認してください。

**Q: RSS購読の使い方は？**
A: 任意のRSSリーダー（Feedly、Inoreader、NetNewsWireなど）で `https://daiowen.github.io/ai-pulse/feed.xml` を購読してください。各エディション更新後に自動でプッシュされます。

## 🤝 貢献

バグ報告、機能リクエスト、コード提出、ドキュメント改善など、あらゆる形式の貢献を歓迎します。

詳細なガイドラインについては [CONTRIBUTING.md](CONTRIBUTING.md) をご覧ください。

## 🗺️ ロードマップ

プロジェクトの将来の開発計画については [ROADMAP.md](ROADMAP.md) をご覧ください。

## 📄 ライセンス

このプロジェクトは MIT ライセンスの下で公開されています。詳細は [LICENSE](LICENSE) ファイルをご覧ください。

---

<p align="center">
  <a href="https://claude.ai">Claude Code</a> で構築 ·
  <a href="https://github.com/DaiOwen/ai-pulse">GitHub</a> ·
  <a href="https://daiowen.github.io/ai-pulse/">ライブデモ</a> ·
  <a href="feed.xml">RSSフィード</a> ·
  <a href="CHANGELOG.md">変更履歴</a>
</p>