# Show HN 帖子

## 标题

```
Show HN: AI Pulse — Daily AI news digest powered entirely by Claude Code, zero deps
```

## URL

```
https://daiowen.github.io/ai-pulse/
```

## 正文（第一条评论）

```
I built a daily AI news aggregator that runs entirely on Claude Code CLI — no Python scripts, no npm packages, no backend server. Just a CLAUDE.md file that tells Claude Code what to search, how to score, and how to generate the HTML.

How it works:
- 3x daily cron (08:00/12:00/20:00 CST), Claude Code auto-searches 30+ verified sources across 7 dimensions
- Cross-source verification: a story needs 2+ independent sources to be considered "confirmed"
- Claude Code handles everything: WebSearch → dedup → scoring → translation → HTML generation → git push
- Output is a single self-contained HTML file with cosmic nebula UI, dark/light themes, PWA, RSS

Tech choices I'm curious for feedback on:
- Using Claude Code CLI as the entire backend — is this a pattern or a dead end?
- The CLAUDE.md file IS the codebase. Anyone can fork and customize the search strategy by editing a markdown file
- Source quality vs quantity: I cut the source pool from 30+ aspirational to 8 verified-reliable after discovering most platforms don't index well in WebSearch

Live demo: https://daiowen.github.io/ai-pulse/
GitHub: https://github.com/DaiOwen/ai-pulse

Built this for Chinese AI developers who want a quick morning scan of what's happening. Would love feedback on the source selection, UI, and whether the "CLAUDE.md as codebase" approach resonates.
```

## 发布步骤

1. 打开 https://news.ycombinator.com/
2. 点击右上角 **Submit**
3. **Title** 填入上面的标题
4. **URL** 填入 `https://daiowen.github.io/ai-pulse/`
5. 点击 Submit
6. **等帖子出现后**，找到自己的帖子，点击 **comments**
7. 在评论区粘贴上面的正文，作为第一条评论

## 发帖时机

- 最佳：北京时间周二至周四 21:00-23:00（美东早 9-11 点）
- 现在：08:07 UTC，可以发但流量低一些

## 如果上首页

- HN 首页流量 5000-20000+ 访问
- 准备好回复技术问题的英文回答
- 不要刷票（HN 有反作弊），自然讨论就好
