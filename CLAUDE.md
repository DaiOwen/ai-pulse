# AI 脉搏 · AI热点速览

面向中国 AI 开发者每日 AI 新闻聚合。Claude Code CLI 驱动，零外部依赖。

## 快速执行（每次 /ai-digest 的标准流程）

**不要读旧 index.html，不要 CronList 自检。直接开始。**

**⚠️ 重要：必须读取 template.html 获取完整样式框架！**

### 第1步：抓取新闻（本地 Python 脚本）

**关键原则：优先本地抓取，每条新闻必须标注来源。URL 必须真实，禁止 `#` 占位。**

**抓取方式：**
```bash
# 主抓取（优先）
python3 fetch_news.py > news.json

# 如果脚本失败，生成「回顾版」
```

**支持的信源（10个）：**

| 信源 | 类型 | 状态 | 备注 |
|------|------|------|------|
| 量子位 | 国内AI快讯 | ✅ | 直接HTML抓取 |
| 36氪 | 国内科技商业 | ✅ | RSS抓取（修复JS渲染问题） |
| Solidot | 开源科技新闻 | ✅ | 替代机器之心 |
| 雷锋网 | AI/硬件新闻 | ✅ | 替代澎湃新闻 |
| 钛媒体 | 国内科技商业 | ✅ | 新增 |
| IT之家 | 科技资讯 | ✅ | 新增 |
| TechCrunch | 海外科技 | ✅ | 直接HTML抓取 |
| The Verge | 海外科技 | ⚠️ 偶发超时 | 直接HTML抓取 |
| Ars Technica | 海外深度 | ✅ | 直接HTML抓取 |
| Hacker News | 开发者社区 | ✅ | Algolia API（修复超时问题） |

**抓取容错机制：**
1. 主抓取：`python3 fetch_news.py` → 输出 JSON
2. 如果失败或结果为空：生成「回顾版」页面
3. 回顾版从最近 3 天归档中抽取热门内容
4. 页面顶部显示「网络受限模式」提示

### 第2步：去重 + 评分

**去重：** 标题相似度 > 80% 视为重复 → 保留评分高者。同一事件不同角度报道 → 合并为一条，标注多来源。

**评分（每条新闻打分，入选板块按分数排序）：**
```
总分 = 热度信号×0.4 + 时效信号×0.3 + 来源质量×0.3

热度信号：多源交叉验证(+5) / 优先信源首发(+3) / 社区讨论热度高(+1)
时效信号：6h内(+5) / 12h内(+3) / 24h内(+1) / 48h内(+0)
来源质量：量子位/36氪/TechCrunch(+3) / 机器之心/澎湃新闻/Ars Technica(+2) / 其他(+1)
```

**翻译规范（海外内容）：** 原文标题 + 中文翻译。摘要全中文 2-3 句。关键数据（金额、百分比、版本号）原文照搬。

### 第3步：生成 HTML

**⚠️ 必须先读取 template.html 获取完整 CSS/JS 框架！**

1. 读取 `template.html` 获取样式框架
2. 替换模板变量：
   - `{{DATE}}` → 完整日期（如 "2026年6月25日"）
   - `{{EDITION}}` → 版次（morning/noon/evening）
   - `{{TLDR_CONTENT}}` → TL;DR 摘要
   - `{{NEWS_CONTENT}}` → 新闻内容 HTML
   - `{{ARCHIVE_MAP}}` → 归档映射 JSON
3. 保持所有样式完整：日历弹窗、收藏功能、返回顶部、亮暗主题等

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
