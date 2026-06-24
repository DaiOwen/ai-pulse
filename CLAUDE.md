# AI 脉搏 · AI热点速览

面向中国 AI 开发者每日 AI 新闻聚合。Claude Code CLI 驱动，零外部依赖。

## 快速执行（每次 /ai-digest 的标准流程）

**不要读模板文件，不要读旧 index.html，不要 CronList 自检。直接开始。**

### 第1步：搜索（精简版）

用 6-8 次 WebSearch 覆盖所有板块。以下搜索一次返回可覆盖多个板块：

```
1. site:venturebeat.com AI model OR release OR agent          → 大模型+工具+应用
2. site:36kr.com 大模型 OR AI OR 开源 OR 工具 OR 发布          → 大模型+工具+应用
3. site:theverge.com AI                                       → 海外参考+大模型
4. site:people.com.cn 人工智能 OR AI OR 智能体                  → 政策合规
5. GitHub trending AI 周榜 site:cnblogs.com                     → 开源热度
6. site:arxiv.org cs.AI OR cs.CL 2026                         → 论文速递(morning only)
```

**停止搜更多。** 如果某次搜索空返，跳过，不重试。noon 版只需 3-4 次搜索（skip arxiv + theverge）。

### 第2步：生成 HTML

直接拼接字符串生成完整 HTML，**不要读取任何模板文件**。复用以下固化结构：

- CSS/JS 框架完全固化：4 个模糊光球 + 40 微粒 + 网格线动画 + theme toggle + PWA + 日历弹窗（代码见下方模板）
- 搜索到的新闻填入对应板块
- archiveMap 在现有值基础上追加当前日期

### 第3步：写入文件（3 个文件）

```bash
# 写入 HTML（直接写，不用 tmp 文件）
Write: index.html（完整 HTML）
cp     archive/YYYY-MM-DD-{edition}.html（同内容）

# 更新 feed.xml：在 <lastBuildDate> 后插入新 <item>，保留最近 10 条
# 无需更新其他 archive 文件的 archiveMap

# 提交推送
git add index.html archive/ feed.xml
git commit -m "auto: {edition} — {date} ({top3-news-keywords})"
git push origin master
```

### 板块内容量

| 板块 | morning | noon | evening |
|------|:--:|:--:|:--:|
| 大模型动态 | 4-5条 | 1-2条 | 5条 |
| 工具&部署 | 3-4条 | 1-2条 | 4条 |
| 政策&合规 | 1-2条 | 1条 | 2条 |
| 应用落地 | 2条 | 1条 | 2条 |
| 开源热度 | Top5 | Top5 | Top10 |
| 海外参考 | 3条 | — | 3条 |
| 论文速递 | 1篇 | — | — |

### 每条新闻格式

```html
标题（加粗）+ 2-3句中文摘要 + 来源(信源名) + 阅读原文链接(真实URL, target="_blank")
```

**严禁使用 `#` 作为 URL。**

