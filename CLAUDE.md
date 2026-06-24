# AI 脉搏 · AI热点速览

面向中国 AI 开发者每日 AI 新闻聚合。Claude Code CLI 驱动，零外部依赖。

## 快速执行（每次 /ai-digest 的标准流程）

**不要读模板文件，不要读旧 index.html，不要 CronList 自检。直接开始。**

### 第1步：搜索

**关键原则：优先搜 ✅ 信源，每条新闻必须标注来源。URL 必须真实，禁止 `#` 占位。**

用以下搜索覆盖所有板块（共约 10-12 次）。同一搜索可跨板块复用结果。

#### 核心搜索（必搜，每次 4 次）

```
1. site:venturebeat.com AI model OR release          → 大模型+应用
2. site:36kr.com 大模型 OR AI OR 发布                  → 大模型+工具+应用
3. site:theverge.com AI OR model OR agent            → 大模型+海外
4. site:people.com.cn 人工智能 OR AI OR 智能体        → 政策
```

#### 补充搜索（按版次，4-6 次）

```
5. site:36kr.com AI 开源 OR 工具 OR Agent              → 工具+应用（morning/evening）
6. site:venturebeat.com AI agent OR enterprise       → 应用落地（morning/evening）
7. GitHub trending AI 周榜 site:cnblogs.com            → 开源热度（必搜）
8. site:arxiv.org cs.AI OR cs.CL 2026                → 论文（仅 morning）
9. site:technologyreview.com AI OR regulation        → 政策国际+海外（仅 morning/evening）
```

**noon 版搜索 5-6 次**（skip arxiv + technologyreview）

**空返不重试。** 同一信源结果可覆盖多个板块。

### 第2步：去重 + 评分

**去重：** 标题相似度 > 80% 视为重复 → 保留评分高者。同一事件不同角度报道 → 合并为一条，标注多来源。

**评分（每条新闻打分，入选板块按分数排序）：**
```
总分 = 热度信号×0.4 + 时效信号×0.3 + 来源质量×0.3

热度信号：多源交叉验证(+5) / 优先信源首发(+3) / 社区讨论热度高(+1)
时效信号：6h内(+5) / 12h内(+3) / 24h内(+1) / 48h内(+0)
来源质量：36氪/VentureBeat/TheVerge(+3) / MIT Tech Review/人民网/cnblogs(+2) / 其他(+1)
```

**翻译规范（海外内容）：** 原文标题 + 中文翻译。摘要全中文 2-3 句。关键数据（金额、百分比、版本号）原文照搬。

### 第3步：生成 HTML

直接拼接字符串生成完整 HTML，**不要读取任何模板文件**。复用以下固化结构：

- CSS/JS 框架完全固化：4 个模糊光球 + 40 微粒 + 网格线动画 + theme toggle + PWA + 日历弹窗（代码见下方模板）
- 搜索到的新闻填入对应板块
- archiveMap 在现有值基础上追加当前日期

### 第4步：写入文件（3 个文件）

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

