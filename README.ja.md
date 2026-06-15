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
</p>

---

**AI Pulse** は、[Claude Code](https://claude.ai) で動作する AI 開発者向け日次ニュース集約ページです。6 以上の情報源から 1 日 3 回自動でニュースを収集・整理し、美しい HTML ページを生成します。npm、Python、外部サービスは一切不要。Claude Code とターミナルだけで完結します。

## 🔗 ライブデモ

**[https://daiowen.github.io/ai-pulse/](https://daiowen.github.io/ai-pulse/)**

インストール不要 — ブラウザで開くだけで最新の AI ニュースダイジェストをご覧いただけます。

## 機能

- 🤖 **7 つのセクション** — モデルアップデート、ツール & デプロイ、ポリシー & コンプライアンス、論文スポットライト、実世界の AI 事例、オープンソース動向、グローバルブリーフ
- ⚡ **4 段階の情報深度** — TL;DR(3秒) → 見出し(10秒) → 要約(30秒) → 全文
- 🎨 **Apple デザイン美学** — ダーク/ライトテーマ切替、動的アニメーション背景、ガラスモーフィズムカード
- 📱 **レスポンシブレイアウト** — デスクトップ、タブレット、モバイルで快適に表示
- 📅 **アーカイブカレンダー** — 過去のエディションをインタラクティブカレンダーで閲覧
- 🔍 **ゼロ依存** — 純粋な HTML/CSS/JS、ビルドツール不要
- 🇨🇳 **中国 AI エコシステム重視** — 中国国内モデルの動向とコンプライアンス情報を優先
- ⏰ **定期自動実行** — 毎日 07:49 / 12:17 / 20:13 に自動生成

## クイックスタート

> **前提条件：** [Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview) CLI をインストールし、初回ログイン（`claude login`）を完了してください。

**1. リポジトリをクローン**

```bash
git clone https://github.com/DaiOwen/ai-pulse.git
cd ai-pulse
```

**2. Claude Code を起動して初号を生成**

プロジェクトディレクトリで Claude Code の対話画面を起動します：
```bash
claude
```

Claude Code がプロジェクト設定（`CLAUDE.md`）を自動的に読み込みます。チャットでスラッシュコマンドを入力してください：

```
/ai-digest morning
```

AI が以下の全工程を自動実行します：
- 6 以上の情報源から最新 AI ニュースを検索（WebSearch）
- トップ記事を詳細取得（WebFetch）
- 重複除去、スコアリング、翻訳、分類
- 完全な HTML を生成し `archive/` と `index.html` に保存

**3. 生成されたページを開く**

```bash
open index.html    # macOS
start index.html   # Windows
```

または `index.html` をダブルクリックしてブラウザで開きます。

初回実行後、定期タスクが自動登録されます（毎日 07:49 / 12:17 / 20:13）。以降の手動操作は不要です。

> 💡 **`/ai-digest` とは？** これはターミナルコマンドではなく、**Claude Code のスラッシュコマンド**です。Claude Code のチャット画面でのみ機能します。`git clone` はターミナルで実行し、`/ai-digest morning` は Claude Code との会話の中で入力します。プロジェクト直下の `CLAUDE.md` が「AI の取り扱い説明書」となり、Claude Code がそれを読み取って自動的に指示に従います。コードを一行も書く必要はありません。

### 定期実行タスク

初回手動実行後、以下の 3 つのスケジュールタスクが自動登録されます：

| タスク | 時刻 | 対象範囲 |
|--------|------|----------|
| 🌅 朝刊 | 07:49 | 昨夜の海外 + 国内朝のニュース |
| ☀️ 昼刊 | 12:17 | 午前中の更新を差分反映 |
| 🌙 夕刊 | 20:13 | 終日サマリー + オープンソースデータ |

### 手動コマンド

| コマンド | 説明 |
|----------|------|
| `/ai-digest morning` | 朝刊を生成 |
| `/ai-digest noon` | 昼刊を生成（差分更新） |
| `/ai-digest evening` | 夕刊を生成（終日サマリー） |
| `/ai-digest update` | 上流の最新コードを取得してプロジェクトを同期 |

### 更新メカニズム

**ライブデモ（GitHub Pages）** — 完全自動化、人手不要：

```
Cron 実行 (07:49 / 12:17 / 20:13)
  → Claude Code がニュースを検索・HTML を生成
  → git add & commit & push
  → GitHub Pages が自動デプロイ（約 1～2 分後に更新）
```

**セルフホストユーザー** — 最新コンテンツを取得する 2 つの方法：

| 方法 | 説明 |
|------|------|
| `git pull` | 上流リポジトリの最新 `index.html` を取得（Claude Code 不要） |
| `/ai-digest morning` | 生成コマンドを自分で実行して最新ニュースを収集（Claude Code 必要） |

リポジトリをフォークして自分の GitHub Pages を自動更新したい場合は、ローカルで Claude Code を起動したままにするだけです（Cron ジョブ + git push がすべて自動実行）。詳細は [CLAUDE.md](CLAUDE.md) をご覧ください。

## コンテンツセクション

| セクション | 説明 |
|------------|------|
| 🤖 モデルアップデート | 中国国内モデル優先 + 国際的な主要リリース |
| 🛠️ ツール & デプロイ | フレームワーク更新、ハードウェア適応、推論デプロイ |
| 📋 ポリシー & コンプライアンス | ネット情報弁公室（CAC）届出、AI 安全審査、業界標準 |
| 📄 論文スポットライト | 実用価値のある arXiv 論文を日替わりで厳選 |
| 💡 実世界の AI 事例 | 企業 AI 統合事例、ベストプラクティス |
| ⭐ オープンソース動向 | GitHub/Gitee Stars 上昇 Top 10 + 注目度 Top 10 |
| 🌍 グローバルブリーフ | 中国に影響を与える海外動向を 3 件厳選 |

## アーキテクチャ

```
Cron スケジュール (07:49 / 12:17 / 20:13)
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
  ① 重複除去（タイトル類似度 + URL 正規化）
  ② スコアリング（人気×0.4 + 新規性×0.3 + 情報源品質×0.3）
  ③ 翻訳（海外ニュース → 中国語または英語要約）
  ④ 分類（7 セクション）
  ⑤ 要約生成（各 2-3 文 + 開発者影響度の注釈）
       │
       ▼
HTML 生成 & アーカイブ
  • 完全自己完結型 HTML を生成
  • archive/YYYY-MM-DD-{edition}.html に保存
  • index.html を最新版に更新
```

## プロジェクト構造

```
ai-pulse/
├── index.html              # メインページ（最新号 + カレンダーナビ）
├── archive/                # 履歴アーカイブ
│   └── YYYY-MM-DD-{edition}.html
├── assets/
│   └── favicon.svg         # サイトアイコン
├── design/                 # デザイン参考
├── screenshots/            # スクリーンショット
├── .github/                # GitHub 設定
│   ├── ISSUE_TEMPLATE/
│   └── PULL_REQUEST_TEMPLATE.md
├── .claude/                # Claude Code 設定
│   ├── settings.json
│   └── scheduled_tasks.json
├── CLAUDE.md               # プロジェクト指示 + Skill 定義
├── CONTRIBUTING.md         # 貢献ガイド
├── CODE_OF_CONDUCT.md      # 行動規範
├── ROADMAP.md              # ロードマップ
├── SECURITY.md             # セキュリティポリシー
├── CHANGELOG.md            # 変更履歴
├── LICENSE                 # MIT ライセンス
├── .gitignore
└── README.md
```

## スクリーンショット

### 🌙 ダークモード（デフォルト）

![AI Pulse Dark Mode](screenshots/dark-mode.png)

### ☀️ ライトモード

![AI Pulse Light Mode](screenshots/light-mode.png)

## セキュリティ

**データプライバシーとセキュリティは基本設計原則です。** AI Pulse は 100% ローカルで実行され、データが外部に出ることはありません。

- 🏠 純粋なローカル実行、データのアップロードは一切なし
- 🔌 生成された HTML は外部リクエストを行いません（トラッキング、テレメトリ、広告なし）
- 🔑 サードパーティの API キーやトークンは不要
- 👁️ MIT オープンソース、完全に監査可能なコード

完全なセキュリティポリシーについては [SECURITY.md](SECURITY.md) をご覧ください。

## よくある質問（FAQ）

**Q: index.html が空白で表示されます。**
A: 初回は `/ai-digest morning` を実行してコンテンツを生成してください。

**Q: 過去のエディションを閲覧するには？**
A: 「アーカイブ」ボタンをクリックし、カレンダーモーダルから過去の日付と版を選択します。

**Q: 定期タスクが実行されません。**
A: ターミナルで `CronList` を実行してタスク状態を確認してください。Claude Code が起動していることを確認します。

**Q: 生成を逃した日があります。**
A: 該当する `/ai-digest` コマンドを手動実行してバックフィルできます。

**Q: コンテンツセクションをカスタマイズできますか？**
A: はい — `CLAUDE.md` の分類ルールを編集することでセクションの優先順位を調整できます。

## 貢献

バグ報告、機能リクエスト、コード提出、ドキュメント改善など、あらゆる形式の貢献を歓迎します。

詳細なガイドラインについては [CONTRIBUTING.md](CONTRIBUTING.md) をご覧ください。

## ロードマップ

プロジェクトの将来の開発計画については [ROADMAP.md](ROADMAP.md) をご覧ください。

## ライセンス

このプロジェクトは MIT ライセンスの下で公開されています。詳細は [LICENSE](LICENSE) ファイルをご覧ください。

---

<p align="center">
  <a href="https://claude.ai">Claude Code</a> で構築 ·
  <a href="https://github.com/DaiOwen/ai-pulse">GitHub</a> ·
  <a href="https://daiowen.github.io/ai-pulse/">ライブデモ</a> ·
  <a href="CHANGELOG.md">変更履歴</a>
</p>
