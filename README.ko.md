🌐 **언어 선택:** [English](README.en.md) · [中文](README.md) · [日本語](README.ja.md) · [Deutsch](README.de.md) · [한국어](README.ko.md)

<p align="center">
  <img src="assets/favicon.svg" width="64" alt="AI Pulse 로고" />
</p>

<h1 align="center">AI Pulse · 일일 AI 뉴스 다이제스트</h1>

<p align="center">
  <em>AI 개발자를 위한 일일 뉴스 자동 집계. 제로 의존성. Claude Code 네이티브.</em>
</p>

<p align="center">
  <img src="https://img.shields.io/github/stars/DaiOwen/ai-pulse?style=flat&color=yellow" alt="GitHub Stars">
  <img src="https://img.shields.io/badge/license-MIT-blue" alt="라이선스">
  <img src="https://img.shields.io/badge/dependencies-zero-brightgreen" alt="제로 의존성">
  <img src="https://img.shields.io/github/contributors/DaiOwen/ai-pulse?color=orange" alt="기여자">
  <img src="https://img.shields.io/badge/PRs-welcome-orange" alt="PR 환영">
  <a href="https://daiowen.github.io/ai-pulse/"><img src="https://img.shields.io/badge/demo-live%20preview-6366f1?style=flat" alt="Live Demo"></a>
  <img src="https://img.shields.io/badge/edition-3x%20daily-22c55e" alt="매일 3회">
</p>

---

**AI Pulse**는 [Claude Code](https://claude.ai)로 구동되는 AI 개발자용 일일 뉴스 집계 HTML 페이지입니다. 30개 이상의 플랫폼과 11명의 저명한 AI 블로거로부터 7개 차원 — 애그리게이터, 미디어, 커뮤니티, 연구, 공식 블로그, 뉴스레터, KOL — 에서 하루 3회 자동으로 뉴스를 수집, 정리하여 아름다운 HTML 페이지를 생성합니다. npm, Python, 외부 서비스가 전혀 필요 없습니다. Claude Code와 터미널만 있으면 됩니다.

## 🔗 라이브 데모

**[https://daiowen.github.io/ai-pulse/](https://daiowen.github.io/ai-pulse/)**

설치가 필요 없습니다 — 브라우저에서 열면 최신 AI 뉴스 다이제스트를 바로 확인할 수 있습니다.

> 💡 **뉴스만 읽으러 오셨나요?** 위의 라이브 데모 링크를 열기만 하면 됩니다 — 매일 3회 자동 업데이트, 설정 불필요. [RSS](https://daiowen.github.io/ai-pulse/feed.xml)로 구독도 가능합니다.

## ✨ 기능

| 기능 | 설명 |
|------|------|
| 🤖 **7개 큐레이션 섹션** | 모델 업데이트, 도구 및 배포, 정책 및 규정 준수, 논문 스포트라이트, 실제 AI 사례, 오픈소스 동향, 글로벌 브리프 |
| ⚡ **4단계 정보 깊이** | TL;DR(3초) → 헤드라인(10초) → 요약(30초) → 전문 |
| 🎨 **Apple 영감 디자인** | 다크/라이트 테마 + 동적 애니메이션 광구 + 글라스모피즘 카드 + 그리드 애니메이션 |
| 📱 **반응형 레이아웃** | 데스크톱, 태블릿, 모바일에서 완벽하게 표시 |
| 📅 **아카이브 캘린더** | 대화형 캘린더로 과거 호 열람, 에디션 전환 지원 |
| 🔍 **제로 의존성** | 순수 HTML/CSS/JS, 빌드 도구나 패키지 매니저 불필요 |
| 🇨🇳 **중국 AI 생태계 집중** | 중국 국내 모델 및 규정 준수 정보 우선 coverage |
| ⏰ **자동 스케줄링** | 매일 08:00, 12:00, 20:00에 자동 생성 |
| 📡 **RSS 피드** | RSS 리더 구독으로 매일 자동 업데이트 |
| 📲 **PWA 지원** | 홈 화면에 추가 가능, 오프라인 캐시 콘텐츠 |
| 🔗 **소셜 공유** | OG/Twitter 메타 태그로 소셜 미디어 미리보기 지원 |
| 🗺️ **사이트맵** | 자동 생성된 sitemap.xml로 SEO 최적화 |
| 🩺 **헬스 체크** | `/ai-digest status`로 Cron, 권한, 최종 생성 시간 진단 |

## 🚀 빠른 시작

> **사전 조건:** [Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview) CLI를 설치하고 첫 로그인(`claude login`)을 완료하세요.

### 1. 리포지토리 클론

```bash
git clone https://github.com/DaiOwen/ai-pulse.git
cd ai-pulse
```

### 2. Claude Code를 실행하고 첫 호를 생성

프로젝트 디렉토리에서 Claude Code 대화형 인터페이스를 시작합니다:

```bash
claude
```

Claude Code가 프로젝트 설정(`CLAUDE.md`)을 자동으로 로드합니다. 채팅에서 슬래시 명령어를 입력하세요:

```
/ai-digest morning
```

AI가 전체 파이프라인을 자동으로 완료합니다:
- 6개 이상의 소스에서 최신 AI 뉴스 검색 (WebSearch)
- 상위 기사 상세 가져오기 (WebFetch)
- 중복 제거, 점수 산정, 번역, 분류
- 완전한 HTML을 생성하여 `archive/`와 `index.html`에 저장
- `feed.xml` RSS 피드 업데이트
- `sitemap.xml` 업데이트

### 3. 생성된 페이지 열기

```bash
open index.html    # macOS
start index.html   # Windows
```

또는 `index.html`을 더블클릭하여 브라우저에서 엽니다.

첫 실행 후 Cron 작업이 자동 등록됩니다 (매일 08:00 / 12:00 / 20:00). 이후 추가 작업은 필요하지 않습니다.

> 💡 **`/ai-digest` 란?** 이것은 터미널 명령어가 아니라 **Claude Code 슬래시 명령어**로, Claude Code 대화창에서만 작동합니다. 비유하자면: `git clone`은 터미널에서 실행하고, `/ai-digest morning`은 Claude Code 채팅에 입력합니다. 프로젝트 루트의 `CLAUDE.md` 파일이 "AI 사용 설명서" 역할을 하며, Claude Code가 이를 읽고 자동으로 지침을 따릅니다. 코드를 한 줄도 작성할 필요가 없습니다.

## ⏰ 예약 작업

첫 수동 실행 후 세 개의 Cron 작업이 자동으로 등록됩니다:

| 작업 | 시간 | 대상 범위 |
|------|------|-----------|
| 🌅 아침 | 08:00 | 전날 해외 + 국내 아침 뉴스 + arXiv 논문 |
| ☀️ 점심 | 12:00 | 오전 업데이트 증분 반영 |
| 🌙 저녁 | 20:00 | 종일 요약 + 오픈소스 전체 데이터 |

> ⚠️ **중요: Cron은 Claude Code 실행 중에만 작동합니다.** 터미널을 닫거나 Claude Code를 종료하면 예약 작업이 실행되지 않습니다. 터미널 창을 열어두거나 `tmux` / `screen`을 사용하세요. `/ai-digest status`로 언제든지 상태를 확인할 수 있습니다.

## 🎮 수동 명령어

| 명령어 | 설명 |
|--------|------|
| `/ai-digest now` | **즉시 업데이트** — 자동으로 에디션 선택, Cron 기다리기 싫을 때 사용 |
| `/ai-digest morning` | 아침 호 생성 (논문 스포트라이트 포함) |
| `/ai-digest noon` | 점심 호 생성 (증분 업데이트) |
| `/ai-digest evening` | 저녁 호 생성 (종일 요약 + 오픈소스 Top 10) |
| `/ai-digest update` | 업스트림 최신 코드를 가져와 프로젝트 업데이트 동기화 |
| `/ai-digest status` | 프로젝트 상태 진단 — Cron, 권한, 최종 생성 시간 |

## 🔄 업데이트 메커니즘

### 라이브 데모 (GitHub Pages)

완전 자동화, 사람 개입 불필요:

```
Cron 실행 (08:00 / 12:00 / 20:00)
  → Claude Code가 뉴스 검색 & HTML + RSS + Sitemap 생성
  → git add & commit & push
  → GitHub Pages 자동 배포 (약 1~2분 후 업데이트)
```

### 셀프 호스팅 사용자

최신 콘텐츠를 얻는 세 가지 방법:

| 방법 | 설명 |
|------|------|
| `/ai-digest update` | **추천.** 원클릭으로 업스트림 최신 코드 가져오기 |
| `git pull` | 수동 터미널 풀 — Claude Code 불필요 |
| `/ai-digest morning` | 생성 명령을 직접 실행하여 실시간 뉴스 수집 |

리포지토리를 포크하고 자신의 GitHub Pages를 자동 업데이트하려면 Claude Code를 로컬에서 실행 상태로 유지하기만 하면 됩니다 (Cron 작업 + git push가 모든 것을 처리). 자세한 내용은 [CLAUDE.md](CLAUDE.md)를 참조하세요.

## 📰 콘텐츠 섹션

| 섹션 | 아침 | 점심 | 저녁 | 설명 |
|------|:----:|:----:|:----:|------|
| 🤖 모델 업데이트 | 4-5 | 1-2 | 5 | 중국 국내 모델 우선 + 글로벌 주요 릴리스 |
| 🛠️ 도구 및 배포 | 3-4 | 1-2 | 4 | 프레임워크 업데이트, 하드웨어 적응, 추론 배포 |
| 📋 정책 및 규정 준수 | 1-2 | 1 | 2 | CAC 신고, AI 안전 검토, 산업 표준 |
| 💡 실제 AI 사례 | 2 | 1 | 2 | 기업 AI 통합 사례 및 모범 사례 |
| ⭐ 오픈소스 동향 | Top5 | Top5 | Top10 | GitHub/Gitee Stars 상승 랭킹 |
| 🌍 글로벌 브리프 | 3 | — | 3 | 중국에 영향을 미치는 해외 동향 3건 선정 |
| 📄 논문 스포트라이트 | 1 | — | — | 실용 가치가 있는 arXiv 논문 매일 선정 |

### 소스 매트릭스

7개 차원, 30개 이상의 플랫폼과 11명의 AI 사상가로부터 콘텐츠 수집:

| 차원 | 대표 소스 |
|------|-----------|
| 🎯 애그리게이터 | RadarAI, AIHOT, AIbase, Digg AI |
| 📰 미디어 | 36Kr, TMTPost, Synced, QbitAI, GeekPark, VentureBeat, The Verge, MIT Technology Review |
| 💬 커뮤니티 | Reddit r/ML, Hacker News, Zhihu AI, ModelScope |
| 🔬 연구 | arXiv, Papers with Code, Hugging Face |
| 🏢 공식 블로그 | OpenAI, DeepMind, Anthropic, Microsoft, Meta, 알리바바 통의, 바이트댄스 더우바오, 바이두 원신, 즈푸 GLM |
| 📧 뉴스레터 | The Decoder, Import AI |
| 👤 KOL | Karpathy, Lilian Weng, Jim Fan, Simon Willison, Chip Huyen, Andrew Ng + 중국인 블로거 5명 |

> 핵심 규칙: 뉴스는 2개 이상의 독립적인 소스에서 확인된 것만 게재됩니다.

### 점수 산정 알고리즘

```
총점 = 인기도×0.4 + 시의성×0.3 + 소스 품질×0.3

인기도: 교차 검증됨(+5) / 최초 보도(+3) / 높은 커뮤니티 참여(+1)
시의성: 6시간 이내(+5) / 12시간 이내(+3) / 24시간 이내(+1) / 48시간 초과(+0)
소스 품질: 36Kr/VentureBeat/TheVerge(+3) / MIT Tech Review/인민망/cnblogs(+2) / 기타(+1)
```

## 🏗️ 아키텍처

```
Cron 스케줄 (08:00 / 12:00 / 20:00)
       │
       ▼
Claude Code 실행
       │
       ├─ WebSearch (15-20회 다중 키워드 검색)
       ├─ WebFetch (상위 5-8개 결과 심층 가져오기)
       └─ GitHub/Gitee API (오픈소스 트렌드 데이터)
       │
       ▼
처리 파이프라인
  ① 중복 제거 (제목 유사도 > 80% + URL 정규화)
  ② 점수 산정 (인기도×0.4 + 시의성×0.3 + 소스 품질×0.3)
  ③ 번역 (해외 뉴스 → 요약 번역, 숫자는 원문 유지)
  ④ 분류 (7개 섹션)
  ⑤ 요약 생성 (각 2-3문장 + 개발자 영향도 표기)
       │
       ▼
HTML 생성 및 아카이브
  • 완전 자체 포함 HTML 생성 (다크/라이트 테마)
  • archive/YYYY-MM-DD-{edition}.html에 저장
  • index.html을 최신 호로 업데이트
  • feed.xml RSS 피드 업데이트 (최근 10개 유지)
  • sitemap.xml 업데이트
  • git commit & push → GitHub Pages 자동 배포
```

## 📁 프로젝트 구조

```
ai-pulse/
├── index.html              # 메인 페이지 (최신 호 + 캘린더 네비게이션)
├── feed.xml                # RSS 피드
├── sitemap.xml             # SEO 사이트맵
├── manifest.json           # PWA 설정
├── subscribe.html          # RSS 구독 가이드
├── archive/                # 역사 아카이브
│   └── YYYY-MM-DD-{edition}.html
├── assets/
│   ├── favicon.svg         # 사이트 아이콘
│   └── og-image.svg        # 소셜 공유 미리보기 이미지
├── design/                 # 디자인 참고 자료
├── screenshots/            # 스크린샷
├── .github/                # GitHub 설정
│   ├── workflows/          # GitHub Actions 자동화
│   ├── ISSUE_TEMPLATE/
│   └── PULL_REQUEST_TEMPLATE.md
├── .claude/                # Claude Code 설정
│   ├── commands/           # 슬래시 명령어 정의
│   │   └── ai-digest.md
│   ├── settings.json
│   └── scheduled_tasks.json
├── CLAUDE.md               # 프로젝트 지침 + Skill 정의
├── CONTRIBUTING.md         # 기여 가이드
├── CODE_OF_CONDUCT.md      # 행동 강령
├── ROADMAP.md              # 로드맵
├── SECURITY.md             # 보안 정책
├── CHANGELOG.md            # 변경 로그
├── LICENSE                 # MIT 라이선스
├── .gitignore
└ README.{md,en.md,ja.md,de.md,ko.md}  # 다국어 문서
```

## 📸 스크린샷

### 🌙 다크 모드 (기본)

![AI Pulse Dark Mode](screenshots/dark-mode.png)

### ☀️ 라이트 모드

![AI Pulse Light Mode](screenshots/light-mode.png)

### 📅 아카이브 캘린더

![AI Pulse Calendar](screenshots/calendar.png)

## 🔒 보안

**데이터 프라이버시와 보안은 기본 설계 원칙입니다.** AI Pulse는 100% 로컬에서 실행되며 — 데이터가 기기를 떠나지 않습니다.

| 특징 | 설명 |
|------|------|
| 🏠 순수 로컬 실행 | 제3자 서버로 데이터 업로드 없음 |
| 🔌 제로 외부 요청 | 생성된 HTML은 추적, 텔레메트리, 광고 없음 |
| 🔑 API 키 불필요 | 제3자 API 토큰이 필요 없음 |
| 👁️ MIT 오픈소스 | 완전히 감사 가능한 코드 |

전체 보안 정책은 [SECURITY.md](SECURITY.md)를 참조하세요.

## ❓ 자주 묻는 질문 (FAQ)

**Q: 라이브 데모가 항상 오래된 콘텐츠를 표시하고 수동 새로고침이 필요합니다.**
A: 이전 버전의 Service Worker가 페이지를 캐시했습니다. **한 번만 수정:** 페이지 열기 → F12 → Application → Service Workers → "Unregister" 클릭 → 새로고침. 새 SW(v2)가 이미 이 문제를 수정했으며, 이후에는 항상 최신 콘텐츠가 표시됩니다.

**Q: index.html이 비어 있습니다.**
A: 첫 실행 시 `/ai-digest morning`을 먼저 실행하여 콘텐츠를 생성해야 합니다.

**Q: 과거 호를 어떻게 볼 수 있나요?**
A: 오른쪽 상단의 "아카이브" 버튼을 클릭하여 모든 날짜와 호(아침/점심/저녁)를 보여주는 캘린더 모달을 엽니다.

**Q: 예약 작업이 실행되지 않습니다.**
A: Claude Code 채팅에서 `CronList`를 실행하여 작업 상태를 확인하세요. Claude Code가 실행 중인지 확인하십시오.

**Q: 생성이 누락된 날이 있습니다.**
A: 해당 `/ai-digest` 명령어를 수동으로 실행하여 백필할 수 있습니다.

**Q: 콘텐츠 섹션을 사용자 정의할 수 있나요?**
A: 네 — `CLAUDE.md`의 분류 규칙을 편집하여 섹션 우선순위와 소스를 조정할 수 있습니다.

**Q: Claude Code는 비용이 드나요?**
A: Claude Code는 무료 티어(약 50-100회/일 도구 호출)를 제공합니다. 1회 `/ai-digest` 실행은 약 20-30회(검색 + 가져오기)를 소비하므로 일일 사용에 무료 티어로 충분합니다. 더 많은 사용량을 위해 [Claude Pro](https://claude.ai/pricing)($20/월) 또는 Max($100-200/월)를 이용할 수 있습니다.

**Q: Claude Code를 설치하지 않고 뉴스만 읽을 수 있나요?**
A: 물론입니다. 두 가지 방법이 있습니다:
- 라이브 데모 방문: **[https://daiowen.github.io/ai-pulse/](https://daiowen.github.io/ai-pulse/)** — 설치 불필요
- 리포지토리를 클론하고 `git pull`로 최신 `index.html`을 가져와 브라우저에서 열기

**Q: 1회 생성에 얼마나 걸리나요? 왜 멈춘 것 같나요?**
A: 전체 `/ai-digest` 실행은 3-5분이 걸립니다 (15-20회 웹 검색 + 8-10회 심층 가져오기). 멈춘 것이 아닙니다 — 기다려 주세요. 먼저 `/ai-digest status`를 실행하여 설정이 올바른지 확인하세요.

**Q: RSS 구독은 어떻게 사용하나요?**
A: 원하는 RSS 리더(Feedly, Inoreader, NetNewsWire 등)로 `https://daiowen.github.io/ai-pulse/feed.xml`을 구독하세요. 각 에디션 업데이트 후 자동으로 푸시됩니다.

## 🤝 기여

버그 신고, 기능 요청, 코드 제출, 문서 개선 등 모든 형태의 기여를 환영합니다.

자세한 가이드라인은 [CONTRIBUTING.md](CONTRIBUTING.md)를 참조하세요.

## 🗺️ 로드맵

프로젝트의 향후 개발 계획은 [ROADMAP.md](ROADMAP.md)를 참조하세요.

## 📄 라이선스

이 프로젝트는 MIT 라이선스에 따라 오픈소스로 제공됩니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하세요.

---

<p align="center">
  <a href="https://claude.ai">Claude Code</a>로 구축 ·
  <a href="https://github.com/DaiOwen/ai-pulse">GitHub</a> ·
  <a href="https://daiowen.github.io/ai-pulse/">라이브 데모</a> ·
  <a href="feed.xml">RSS 피드</a> ·
  <a href="CHANGELOG.md">변경 로그</a>
</p>