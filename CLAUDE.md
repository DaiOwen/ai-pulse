# AI 脉搏 · AI热点速览

面向中国 AI 开发工程师的每日 AI 新闻智能聚合。每天早中晚三次自动生成精美 HTML 页面。

## 项目身份

- 名称：AI 脉搏 (AI Pulse)
- 目标用户：中国 AI/大模型开发工程师
- 运行方式：Claude Code CLI 驱动，零外部依赖

## 项目架构

```
用户输入 /ai-digest morning
        │
        ▼
.claude/commands/ai-digest.md    ← 命令注册（YAML frontmatter + 路由逻辑）
        │
        ▼
CLAUDE.md                        ← 完整执行规范（本文件）
        │
        ▼
Claude Code 按规范执行            ← WebSearch → 去重评分 → 生成 HTML → git push
```

**关键：** `/ai-digest` 能工作的前提是 `.claude/commands/ai-digest.md` 存在（命令注册）且 CLAUDE.md 被加载（执行规范）。两者缺一不可。

## 命令

### `/ai-digest [edition]`

生成一期 AI 热点速览。**预计耗时 3-5 分钟**（15-20 次网络搜索 + 8-10 次原文抓取 + HTML 生成），请耐心等待，勿中途取消。

**参数：**
- `edition`：`morning`（早间版·默认）| `noon`（午间版）| `evening`（晚间版）

**示例：**
```
/ai-digest morning    # 生成早间版
/ai-digest evening    # 生成晚间版
```

### `/ai-digest now`

即时生成——不想等 Cron 定时触发时使用。自动根据当前时间选择最合适的版次：

| 当前时间 | 自动选择 | 说明 |
|---------|:--:|------|
| 00:00 – 10:59 | `morning` | 早间版，覆盖昨夜到现在 |
| 11:00 – 16:59 | `noon` | 午间版，增量更新 |
| 17:00 – 23:59 | `evening` | 晚间版，全天汇总 |

**示例：**
```
/ai-digest now        # 随时运行，自动选版次即时更新
```

### `/ai-digest update`

拉取上游仓库最新代码，一键同步项目更新（新功能、设计改进、Bug 修复等）。

**执行流程：**
1. 检查是否有本地未提交的修改（`git status --porcelain`）
2. 如有本地修改，自动 `git stash` 暂存
3. 执行 `git pull origin master` 拉取最新代码
4. 展示最近 5 条 commit 变更摘要
5. 如果 CLAUDE.md 有更新，提示「新配置将在下次启动 Claude Code 时生效」
6. 如果之前 stash 了，自动执行 `git stash pop` 恢复本地修改

**示例：**
```
/ai-digest update      # 同步项目最新版本
```

### `/ai-digest status`

诊断当前项目状态，一键排查所有配置问题。

**检查项：**
1. **权限配置**：`.claude/settings.json` 是否存在、必要权限是否完整
2. **Cron 任务**：三个定时任务是否已注册、下次过期时间
3. **上次生成**：最近一次成功的 archive 文件及时间
4. **Git 状态**：是否有未提交的更改、是否与上游同步

**输出示例：**
```
🔍 AI脉搏 状态诊断
━━━━━━━━━━━━━━━━━━━━━━━━━
✅ 权限配置：完整
✅ Cron 早间版：已注册 (下次过期: 2026-06-22)
✅ Cron 午间版：已注册 (下次过期: 2026-06-22)
✅ Cron 晚间版：已注册 (下次过期: 2026-06-22)
✅ 上次生成：archive/2026-06-15-evening.html (2小时前，18条新闻)
✅ Git：工作区干净，与 origin/master 同步
━━━━━━━━━━━━━━━━━━━━━━━━━
⚠️  重要提醒：Cron 仅在 Claude Code 运行时触发。
   如果终端关闭，定时任务不会执行。建议保持 claude 进程运行。
```

## 新闻采集策略

### 核心信源（已验证可用）

以下信源均经过 WebSearch 实测验证。标记 ⚠️ 的偶尔空返，标记 ❌ 的基本搜不到，标记 🔒 的为封闭平台需间接搜索。

| 信源 | 状态 | 搜索方式 |
|------|:--:|---------|
| **36氪** (36kr.com) | ✅ | `site:36kr.com 关键词` |
| **人民网** (people.com.cn) | ✅ | `site:people.com.cn 关键词` |
| **The Verge** (theverge.com) | ✅ | `site:theverge.com 关键词` |
| **VentureBeat** (venturebeat.com) | ✅ | `site:venturebeat.com 关键词` |
| **cnblogs** (cnblogs.com) | ✅ | `GitHub trending site:cnblogs.com` |
| **TechCrunch** (techcrunch.com) | ✅ | `site:techcrunch.com 关键词` |
| **MIT Tech Review** (technologyreview.com) | ✅ | `site:technologyreview.com 关键词` |
| **Ars Technica** (arstechnica.com) | ✅ | `site:arstechnica.com AI` |
| **Hacker News** (news.ycombinator.com) | ⚠️ | `site:news.ycombinator.com AI OR LLM` |
| **GitHub Blog** (github.blog) | ⚠️ | `site:github.blog AI OR LLM` |
| **机器之心** (jiqizhixin.com) | ⚠️ | `site:jiqizhixin.com 关键词` |
| **量子位** (qbitai.com) | ⚠️ | `site:qbitai.com 关键词` |
| **Reddit** (reddit.com/r/MachineLearning) | ⚠️ | `site:reddit.com/r/MachineLearning` |
| **arXiv** (arxiv.org) | ⚠️ | `site:arxiv.org cs.AI OR cs.CL` |
| **公众号/微博/小红书** | 🔒 | 搜索"关键词 解读 OR 分析"获取第三方转载 |
| **知乎** (zhihu.com) | 🔒 | `site:zhihu.com AI OR 大模型`（登录墙限制） |
| **HuggingFace/PapersWithCode** | ❌ | 技术站点，新闻性内容少，不建议作为新闻源 |

> **关键原则：优先搜 ✅ 信源，每个板块必须覆盖至少 2 个不同 ✅ 信源。⚠️ 信源作为补充，🔒 信源通过第三方转载间接获取。**

### 各板块搜索计划

执行时严格按以下顺序搜索，不得跳过。括号内为每版最低搜索次数。

**🤖 大模型动态**（morning 5 次 / noon 3 次 / evening 4 次）：
```
1. site:36kr.com 大模型 OR AI OR 发布                    ← 必搜
2. site:venturebeat.com AI model OR release              ← 必搜
3. site:theverge.com AI OR model OR agent                ← 必搜
4. site:technologyreview.com AI OR model                 ← morning/evening
5. site:jiqizhixin.com AI 模型 OR 发布                    ← 补充（可能空返）
6. AI 大模型 最新 发布 OR 开源 2026 site:stcn.com        ← 补充（资本视角）
```
时效：24h | 每次至少搜 3 个不同信源

**🛠️ 工具 & 部署**（morning 4 次 / noon 2 次 / evening 3 次）：
```
1. site:36kr.com AI 开发 OR 开源 OR 工具                  ← 必搜
2. site:venturebeat.com AI tool OR open source           ← 必搜
3. site:github.blog AI OR LLM OR release                ← 补充
4. "vllm" OR "langchain" OR "ollama" OR "MCP" 更新      ← 补充（工具关键词）
```
时效：48h | 每次至少搜 2 个不同信源

**📋 政策 & 合规**（morning 2 次 / noon 1 次 / evening 2 次）：
```
1. site:people.com.cn 人工智能 OR AI OR 智能体 监管       ← 必搜
2. site:technologyreview.com AI policy OR regulation    ← 补充（国际视角）
3. site:theverge.com AI regulation OR policy            ← 补充
```
时效：7天 | 每次至少搜 2 个不同信源

**📄 论文速递**（仅 morning 2-3 次）：
```
1. site:arxiv.org cs.AI OR cs.CL 2026                  ← 必搜
2. site:jiqizhixin.com 论文 解读 OR 速递                  ← 补充
3. "LLM" OR "large language model" breakthrough         ← 补充
```

**💡 应用落地**（morning 3 次 / noon 1 次 / evening 2 次）：
```
1. site:36kr.com AI 落地 OR 应用 OR Agent 案例           ← 必搜
2. site:venturebeat.com AI agent OR enterprise          ← 必搜
3. site:theverge.com AI product OR app OR launch        ← 补充
```

**⭐ 开源热度**（morning/evening 2 次 / noon 1 次）：
```
1. GitHub trending AI 周榜 site:cnblogs.com              ← 必搜（最可靠）
2. site:github.com/trending AI OR LLM                   ← 补充
```

**🌍 海外参考**（仅 morning 3 次 / evening 3 次）：
```
1. site:theverge.com AI                                 ← 必搜
2. site:venturebeat.com AI                              ← 必搜
3. site:technologyreview.com AI                         ← 补充
4. site:arstechnica.com AI OR LLM                       ← 补充
```

### 搜索执行规范

1. **必须搜够次数**：按上表最低搜索次数执行，不得因"36氪已经够了"而跳过 The Verge 或 VentureBeat
2. **信源分散原则**：每板块至少覆盖 2 个不同 ✅ 信源。禁只搜 36氪+人民网就交差
3. **空返处理**：⚠️ 信源空返时换一个搜索词重试一次；仍空返则跳过，不消耗额外搜索配额
4. **封闭平台策略**：公众号/微博/小红书内容通过搜索"事件关键词+解读/分析"获取第三方转载，不直接搜索平台
5. **原文 URL 必须收集**：从搜索结果中提取真实 URL——**严禁使用 `#` 占位符**
6. **信源标注**：每条新闻必须标注来源媒体名
7. 总搜索次数：morning 15-20 次，noon 6-10 次，evening 12-18 次

## 内容处理规范

### 去重
- 标题相似度 > 80% 视为重复，保留评分高者
- 同一事件不同角度报道，合并为一条（标注多来源）

### 评分公式
```
总分 = 热度信号×0.4 + 时效信号×0.3 + 来源质量×0.3
热度信号：多源交叉验证(+5) / 优先信源(+3) / 社区讨论度(+1)
时效信号：6h内(+5) / 12h内(+3) / 24h内(+1)
来源质量：36氪/量子位/机器之心(+3) / 其他(+1)
```

### 翻译规范（海外内容）
- 保留原始标题，后面附中文翻译
- 摘要全中文，2-3 句
- 关键数据（金额、百分比、版本号）原文照搬

### 内容量按版次

| 板块 | morning | noon | evening |
|------|:-------:|:----:|:-------:|
| 大模型动态 | Lead×1 + Sub×3 | 增量1-2条 | 全天汇总×5 |
| 工具&部署 | 3-4条 | 增量1-2条 | 汇总×4 |
| 政策&合规 | 1-2条 | 1条 | 汇总×2 |
| 论文速递 | 1篇 | — | — |
| 应用落地 | 2条 | 1条 | 2条 |
| 开源热度 | 快照Top5 | 快照Top5 | 全天Top10 |
| 海外参考 | 3条 | — | 3条 |

## HTML 生成规范

### 生成流程

1. **读取参考模板**：Read `design/fusion-preview.html` 理解视觉结构和 CSS 规范
2. **生成完整 HTML**：按照融合设计（参考 fusion-preview.html）的视觉规格，生成完整的独立 HTML 文件
3. **保存文件（原子写入）**：
   - 先将完整 HTML 写入临时文件 `index.tmp.html`
   - 使用 `mv index.tmp.html index.html` 原子替换（同一文件系统内 rename 是原子操作）
   - 同时保存到 `archive/YYYY-MM-DD-{edition}.html`（如 `archive/2026-06-14-morning.html`）
   - **重要**：先写 archive 文件（不影响主页），确认成功后再原子替换 index.html。如果生成中途失败，index.html 不受影响
   - **⚠️ 严禁覆盖其他 archive 文件**：只写入当前期次的 archive 文件。**绝不**使用 `cp index.html archive/*.html` 或任何批量覆盖操作——这会导致历史各期内容永久丢失。每期 archive 是独立的历史记录
4. **生成 RSS 订阅文件**：更新 `feed.xml`——
   - 在 `<channel>` 最顶部插入新 `<item>`（最新一期排最前）
   - 每期 `<item>` 必须包含：标题（含版次+日期）、链接（指向 archive 文件）、发布时间（RFC 822 格式）、描述（含各板块新闻标题列表 + 阅读原文链接）
   - 保留最近 10 条 `<item>`，旧条目自动清理
   - 更新 `<lastBuildDate>` 为当前时间
5. **自动发布（Git Push）**：文件保存成功后，自动提交并推送到 GitHub：
   ```bash
   git add index.html archive/ feed.xml
   git commit -m "auto: {edition} edition — $(date +%Y-%m-%d)"
   git push origin master
   ```
   - 推送后 GitHub Pages 自动部署，在线演示约 1-2 分钟后更新
   - 此步骤由 Cron 定时任务和手动 `/ai-digest` 命令共享
   - 如果 git push 失败（网络问题等），内容已保存到本地，下次运行时会一并推送

### HTML 文件要求

1. **完全自包含**：所有 CSS 内嵌于 `<style>` 标签，所有 JS 内嵌于 `<script>` 标签
2. **字体从 CDN**：Inter + Noto Sans SC 从 Google Fonts CDN 加载（`@import url(...)`）
3. **动态背景**：必须包含 4 个模糊光球 + 40 个微粒 + 网格线动画（纯 CSS + JS，无外部依赖）
4. **主题切换**：右上角滑块 Toggle，默认暗色，localStorage 记住偏好
5. **内容标记**：每条新闻包含分类标签、来源链接、时间、"💡 开发者影响"标注
6. **阅读原文链接**：每条新闻必须包含"阅读原文 →"链接（`class="read-original"`），**必须填入 WebSearch 返回的真实原始 URL**，新窗口打开（`target="_blank" rel="noopener"`）。严禁使用 `#` 占位符。论文速递指向 arXiv 原文，开源热度指向 GitHub Trending 页面
7. **每日一语**：页脚包含行业名言（优先 Alan Kay、Andrej Karpathy、李开复等 AI 领域人物）
8. **PWA 支持**：包含 `<link rel="manifest">` 和 Service Worker 注册代码。SW 使用 network-first 策略处理 HTML（不缓存页面本身，确保用户始终看到最新内容），cache-first 处理静态资源。`<head>` 中必须包含 `Cache-Control: no-cache` meta 标签防止浏览器缓存
9. **RSS 订阅**：`<head>` 中包含 `<link rel="alternate" type="application/rss+xml">`，页脚包含 RSS 订阅链接

### index.html 额外要求

除上述内容外，index.html 还需包含：
- 日历月导航入口（「往期回顾」按钮 → 下拉/弹窗展示当月日历 + 各日期版次链接）
- 日历数据使用 JS 硬编码 `archiveMap` 对象（不再依赖 GitHub API），每次 `/ai-digest` 生成 HTML 时更新该对象：在 `const archiveMap = {` 后追加新日期的条目，格式 `'YYYY-MM-DD': ['morning']`，若该日期已有条目则追加 edition 到数组。**同步更新所有 archive/*.html 文件中的 archiveMap。**

### 错误处理

- 某信源无结果 → 静默跳过，不影响其他板块
- 全部信源无结果 → 生成页面展示"暂无可获取新闻"，标注最后成功时间
- 开源 API 限流 → 使用本地缓存的昨日数据，标注"数据来自昨日"

### 生成失败通知

当 `/ai-digest` 在 Cron 定时任务中执行失败时（全部信源无结果、网络错误等），应采取以下措施：

1. **静默失败**：不要中断 Cron 任务链，错误不应导致后续 Cron 任务被跳过
2. **记录失败**：在 `archive/.last-failure` 文件中记录失败时间和原因
3. **页面降级**：index.html 保留上次成功生成的内容不变（原子写入保证了这一点）
4. **下次自愈**：下一次 Cron 触发时自动重试，无需人工介入
5. **连续失败检测**：如果连续 3 次 Cron 均失败，下次手动运行 `/ai-digest status` 时应显示 ⚠️ 警告

连续失败原因可能是 API 限流、网络中断或 Claude Code 版本更新导致的不兼容，应提示用户检查网络连接或运行 `/ai-digest update` 更新项目代码。

## 自动配置

以下检查在**每次** `/ai-digest` 运行时执行。创建操作仅当对应文件/任务不存在时触发（幂等，可安全重复执行）。

### 1. 权限配置自动创建

检查 `.claude/settings.json` 是否存在。如果不存在，创建：

```json
{
  "permissions": {
    "allow": [
      "WebSearch",
      "WebFetch",
      "Bash(git:*)",
      "Bash(ls:*)",
      "Bash(mkdir:*)",
      "Bash(cat:*)",
      "Bash(date:*)",
      "Bash(curl:*)"
    ]
  }
}
```

### 2. Cron 定时任务自动创建

检查是否存在定时任务（通过 CronList 工具）。如果不存在，创建 3 个：

| 任务 | Cron 表达式 | 说明 |
|------|------------|------|
| 早间版 | `0 8 * * *` | 08:00 触发，采集昨夜到今晨 |
| 午间版 | `0 12 * * *` | 12:00 触发，增量更新 |
| 晚间版 | `0 20 * * *` | 20:00 触发，全天汇总 |

> Cron 时间选在整点（8:00 / 12:00 / 20:00），容易记忆。整点触发在实际使用中延迟可忽略（生成本身需要 3-5 分钟）。

**⚠️ 重要前提——Cron 仅在 Claude Code 运行时触发：** Cron 定时任务不是操作系统级的 crontab，而是 Claude Code 会话内的调度器。这意味着：
- **必须保持 `claude` 进程运行**（终端不能关闭）
- 如果关闭终端或退出 Claude Code，定时任务不会触发
- 建议使用 `tmux` / `screen` 或保持一个终端窗口常开
- 如果错过了某次定时生成，手动运行对应版次的 `/ai-digest` 即可补生成

**⚠️ Cron 7天过期提醒：** CronCreate 的 `durable` 任务默认 7 天后自动过期。每次运行 `/ai-digest` 时检查 CronList，如任务已过期或不存在，自动重新注册。同时注册一个每周提醒任务：

- 每周日 09:00 执行 Cron 健康检查：`检查 CronList，如 AI脉搏任务缺失或即将过期则重新注册`

### 3. 自检清单

每次运行 `/ai-digest` 前输出一行自检：
```
🔍 AI脉搏自检：权限配置 ✓ | Cron早间 ✓ 午间 ✓ 晚间 ✓ (下次过期: YYYY-MM-DD) | 上次生成：archive/YYYY-MM-DD-evening.html
```

如果 Cron 任务将在 24 小时内过期，自检信息中标注 ⚠️ 警告。
