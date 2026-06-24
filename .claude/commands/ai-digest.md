---
description: 生成 AI 热点速览、诊断状态或同步更新
argument-hint: morning | noon | evening | now | status | update
allowed-tools: WebSearch, WebFetch, Bash(git:*), Bash(ls:*), Bash(mkdir:*), Bash(cp:*), Bash(cat:*), Bash(date:*), Bash(head:*)
---

# /ai-digest

解析 `$ARGUMENTS`，按 CLAUDE.md 执行。

| $ARGUMENTS | 动作 |
|------------|------|
| `morning` | 搜索 6-8 次 → 生成 HTML → git push |
| `noon` | 搜索 3-4 次（增量，skip arxiv+theverge） → 生成 → git push |
| `evening` | 搜索 6-8 次 → 生成 → git push |
| `now` | 当前时间<11→morning / 11-17→noon / 17+→evening |
| `status` | CronList + ls archive/ + git status |
| `update` | git stash → git pull → 展示最近 3 commit → git stash pop |

**生成要求：不读模板文件，不读旧 index.html，不执行 CronList 自检。直接搜索→生成→推送。**
