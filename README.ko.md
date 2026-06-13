🌐 **언어 선택:** [English](README.md) · [中文](README.zh-CN.md) · [日本語](README.ja.md) · [Deutsch](README.de.md) · [한국어](README.ko.md)

<p align="center">
  <img src="assets/favicon.svg" width="64" alt="AI Pulse 로고" />
</p>

<h1 align="center">AI Pulse · 일일 AI 뉴스 다이제스트</h1>

<p align="center">
  <em>AI 개발자를 위한 일일 뉴스 자동 집계. 제로 의존성. Claude Code 네이티브.</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/license-MIT-blue" alt="라이선스">
  <img src="https://img.shields.io/badge/dependencies-zero-brightgreen" alt="제로 의존성">
  <img src="https://img.shields.io/badge/PRs-welcome-orange" alt="PR 환영">
</p>

---

**AI Pulse**는 [Claude Code](https://claude.ai)로 구동되는 AI 개발자용 일일 뉴스 집계 HTML 페이지입니다. 6개 이상의 소스에서 하루 3회 자동으로 뉴스를 수집, 정리하여 아름다운 HTML 페이지를 생성합니다. npm, Python, 외부 서비스가 전혀 필요 없습니다. Claude Code와 터미널만 있으면 됩니다.

## 기능

- 🤖 **7개 큐레이션 섹션** — 모델 업데이트, 도구 및 배포, 정책 및 규정 준수, 논문 스포트라이트, 실제 AI 사례, 오픈소스 동향, 글로벌 브리프
- ⚡ **4단계 정보 깊이** — TL;DR(3초) → 헤드라인(10초) → 요약(30초) → 전문
- 🎨 **Apple 영감 디자인** — 다크/라이트 테마, 동적 애니메이션 배경, 글라스모피즘 카드
- 📱 **반응형 레이아웃** — 데스크톱, 태블릿, 모바일에서 완벽하게 표시
- 📅 **아카이브 캘린더** — 대화형 캘린더로 과거 호 열람
- 🔍 **제로 의존성** — 순수 HTML/CSS/JS, 빌드 도구나 패키지 매니저 불필요
- 🇨🇳 **중국 AI 생태계 집중** — 중국 국내 모델 및 규정 준수 정보 우선 coverage
- ⏰ **자동 스케줄링** — 매일 07:49, 12:17, 20:13에 자동 생성

## 빠른 시작

```bash
# 1. 리포지토리 클론
git clone https://github.com/DaiOwen/ai-pulse.git
cd ai-pulse

# 2. 첫 호 생성
（Claude Code가 프로젝트 설정을 자동 로드합니다）
/ai-digest morning

# 3. 브라우저에서 index.html 열기
```

첫 실행 시 Claude Code가 자동으로 다음을 수행합니다:
- 6개 이상의 소스에서 최신 AI 뉴스 검색 (WebSearch)
- 상위 기사 상세 가져오기 (WebFetch)
- 중복 제거, 점수 산정, 번역, 분류
- 완전한 HTML을 생성하여 `archive/`와 `index.html`에 저장

### 예약 작업

첫 수동 실행 후 세 개의 Cron 작업이 자동으로 등록됩니다:

| 작업 | 시간 | 대상 범위 |
|------|------|-----------|
| 🌅 아침 | 07:49 | 전날 해외 + 국내 아침 뉴스 |
| ☀️ 점심 | 12:17 | 오전 업데이트 증분 반영 |
| 🌙 저녁 | 20:13 | 종일 요약 + 오픈소스 데이터 |

### 수동 명령어

| 명령어 | 설명 |
|--------|------|
| `/ai-digest morning` | 아침 호 생성 |
| `/ai-digest noon` | 점심 호 생성 (증분 업데이트) |
| `/ai-digest evening` | 저녁 호 생성 (종일 요약) |

## 콘텐츠 섹션

| 섹션 | 설명 |
|------|------|
| 🤖 모델 업데이트 | 중국 국내 모델 우선 + 글로벌 주요 릴리스 |
| 🛠️ 도구 및 배포 | 프레임워크 업데이트, 하드웨어 적응, 추론 배포 |
| 📋 정책 및 규정 준수 | CAC 신고, AI 안전 검토, 산업 표준 |
| 📄 논문 스포트라이트 | 실용 가치가 있는 arXiv 논문 매일 선정 |
| 💡 실제 AI 사례 | 기업 AI 통합 사례 및 모범 사례 |
| ⭐ 오픈소스 동향 | GitHub/Gitee Stars 상승 Top 10 + 주목도 Top 10 |
| 🌍 글로벌 브리프 | 중국에 영향을 미치는 해외 동향 3건 선정 |

## 아키텍처

```
Cron 스케줄 (07:49 / 12:17 / 20:13)
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
  ① 중복 제거 (제목 유사도 + URL 정규화)
  ② 점수 산정 (인기도×0.4 + 시의성×0.3 + 소스 품질×0.3)
  ③ 번역 (해외 뉴스 → 요약 번역)
  ④ 분류 (7개 섹션)
  ⑤ 요약 생성 (각 2-3문장 + 개발자 영향도 표기)
       │
       ▼
HTML 생성 및 아카이브
  • 완전 자체 포함 HTML 생성
  • archive/YYYY-MM-DD-{edition}.html에 저장
  • index.html을 최신 호로 업데이트
```

## 프로젝트 구조

```
ai-pulse/
├── index.html              # 메인 페이지 (최신 호 + 캘린더 네비게이션)
├── archive/                # 역사 아카이브
│   └── YYYY-MM-DD-{edition}.html
├── assets/
│   └── favicon.svg         # 사이트 아이콘
├── design/                 # 디자인 참고 자료
├── .claude/                # Claude Code 설정
│   ├── settings.json       # 권한 설정
│   └── scheduled_tasks.json # 예약 작업 (런타임)
├── CLAUDE.md               # 프로젝트 지침 + Skill 정의
├── .gitignore
└── README.md
```

## 스크린샷

> *스크린샷 준비 중 — `/ai-digest morning`을 실행하여 실제 페이지를 확인하세요.*

## 자주 묻는 질문 (FAQ)

**Q: index.html이 비어 있습니다.**
A: 첫 실행 시 `/ai-digest morning`을 먼저 실행하여 콘텐츠를 생성해야 합니다.

**Q: 과거 호를 어떻게 볼 수 있나요?**
A: "아카이브" 버튼을 클릭하여 모든 날짜와 호를 보여주는 캘린더 모달을 엽니다.

**Q: 예약 작업이 실행되지 않습니다.**
A: 터미널에서 `CronList`를 실행하여 작업 상태를 확인하세요. Claude Code가 실행 중인지 확인하십시오.

**Q: 생성이 누락된 날이 있습니다.**
A: 해당 `/ai-digest` 명령어를 수동으로 실행하여 백필할 수 있습니다.

**Q: 콘텐츠 섹션을 사용자 정의할 수 있나요?**
A: 네 — `CLAUDE.md`의 분류 규칙을 편집하여 섹션 우선순위를 조정할 수 있습니다.

---

<p align="center">
  <a href="https://claude.ai">Claude Code</a>로 구축 ·
  <a href="https://github.com/DaiOwen/ai-pulse">GitHub</a>
</p>
