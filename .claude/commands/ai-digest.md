---
description: 生成 AI 热点速览、诊断状态或同步更新
argument-hint: morning | noon | evening | now | status | update
allowed-tools: WebSearch, WebFetch, Bash(git:*), Bash(ls:*), Bash(mkdir:*), Bash(cat:*), Bash(date:*), Bash(curl:*)
---

# /ai-digest — AI 脉搏命令入口

解析 `$ARGUMENTS` 确定子命令，然后严格按照项目根目录 `CLAUDE.md` 中的完整规范执行。

## 子命令路由

| $ARGUMENTS | 执行动作 |
|------------|---------|
| `morning` | 生成早间版（CLAUDE.md § 新闻采集策略 → § HTML 生成规范 → § 自动配置） |
| `noon` | 生成午间版（增量更新，同上流程） |
| `evening` | 生成晚间版（全天汇总，同上流程） |
| `now` | 根据当前时间自动选版次：00:00-10:59→morning / 11:00-16:59→noon / 17:00-23:59→evening，然后执行生成 |
| `status` | 执行诊断：CronList 检查任务状态 → 检查 .claude/settings.json 权限 → ls archive/ 最近文件 → git status |
| `update` | git stash → git pull origin master → 展示最近 5 条 commit → 如 CLAUDE.md 变更则提示重启 → git stash pop |
| 空或其他 | 默认执行 `morning`（早间版） |

## 执行要求

1. **每次生成前**输出自检行：`🔍 AI脉搏自检：权限配置 ✓ | Cron早间 ✓ 午间 ✓ 晚间 ✓ (下次过期: YYYY-MM-DD) | 上次生成：archive/YYYY-MM-DD-evening.html`
2. 严格按照 CLAUDE.md 中的搜索策略、评分公式、内容量表格执行
3. 生成的 HTML 必须满足 CLAUDE.md § HTML 文件要求 的全部 9 条规范
4. 流程结束自动执行 git add → commit → push

CLAUDE.md 的完整规范是执行的唯一权威来源，本文件仅做路由分发。
