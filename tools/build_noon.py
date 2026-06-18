#!/usr/bin/env python3
import re, datetime, sys
sys.path.insert(0, 'tools')
from calendar import inject_archive_map

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

c = r'''  <div class="section-gap section-indigo" id="section-models">
    <div class="section-head"><div class="section-line"></div><span class="section-label">大模型动态</span><span class="section-label-cn">Models</span></div>
    <div class="feature-card"><div class="card-row"><div class="card-body">
      <div class="card-tag" style="color:#6366f1;">HEADLINE</div>
      <div class="card-title">AI 终极商业模式是"健身房"？豆包日活 2 亿但日收入不足百万</div>
      <div class="card-desc">36氪深度分析：豆包 DAU 已破 2 亿，但日收入不足百万——"流量之王"面临变现困境。文章提出三种 AI 商业模式：C 端"订阅+额度"的健身房模式（低门槛+超额付费）、B 端云服务模式、高阶"按结果收费"。核心矛盾：AI 产品越像"人"，用户越不愿为它付钱——因为人们习惯于免费的互联网。谷歌、微软、字节都在从免费走向订阅制，但用户付费意愿远低于预期。</div>
      <div class="card-meta"><span>36氪</span><span>&#183;</span><span>6月17日</span><span>&#183;</span><span class="card-meta-link">深度分析</span></div>
      <div style="margin-top:8px; font-size:9px; color:#a5b4fc;">💡 开发者影响：C 端 AI 变现困难意味着 B 端和开发者工具是更可靠的商业模式</div>
      <a href="https://36kr.com/p/3856911189595393" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a>
    </div><div class="card-icon">&#9889;</div></div></div>
    <div class="sub-grid">
      <div class="sub-card"><div class="sub-tag" style="color:#a5b4fc;">Harness 时代 · 36氪</div><div class="sub-title">Creao 99% 代码由 AI 完成：六周产品流程压缩到一天</div><div class="sub-desc">硅谷101深度报道"挽具工程"（Harness Engineering）实践：初创公司 Creao 99% 代码由 AI 生成，六周产品开发流程被压缩到一天。组织架构也随之变化——去掉传统产品经理角色，初级工程师比资深工程师更适应 AI 时代。Harness 正从技术架构演变为组织架构。</div><div style="margin-top:6px; font-size:8px; color:var(--text-tertiary);">36氪 · 5月26日</div><div style="margin-top:4px; font-size:8px; color:#a5b4fc;">💡 开发者影响：AI 时代资深工程师的优势不在编码速度，而在系统设计和 Harness 构建</div><a href="https://36kr.com/p/3825551742489222" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
    </div>
  </div>
  <div class="section-gap section-green" id="section-tools">
    <div class="section-head"><div class="section-line"></div><span class="section-label">工具 & 部署</span><span class="section-label-cn">Tools & Deploy</span></div>
    <div class="tool-row">
      <div class="tool-card"><div class="tool-icon">&#128187;</div><div class="tool-name">Codex Desktop macOS</div><div class="tool-desc">OpenAI 发布原生 macOS 桌面应用。多Agent并行隔离worktree。"Skills"包集成Figma/Linear/Vercel。Altman 声称未打开 IDE 就完成了大型项目。</div><span class="tool-badge badge-new">macOS</span><a href="https://venturebeat.com/orchestration/openai-launches-a-codex-desktop-app-for-macos-to-run-multiple-ai-coding" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
      <div class="tool-card"><div class="tool-icon">&#127760;</div><div class="tool-name">GitHub Agent HQ</div><div class="tool-desc">GitHub 原生集成 Claude+Codex+Copilot 三种Agent。VS Code/GitHub Mobile 直接分派任务。多Agent 对比开发。</div><span class="tool-badge badge-new">Agent 竞技场</span><a href="https://www.theverge.com/news/873665/github-claude-codex-ai-agents" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
      <div class="tool-card"><div class="tool-icon">&#129302;</div><div class="tool-name">Gemini Spark</div><div class="tool-desc">Google 24/7 常驻 Agent。$99.99/月。The Verge 实测：功能强大但隐私成本高，尚不值得付费。</div><span class="tool-badge badge-update">评测</span><a href="https://www.theverge.com/tech/941138/google-gemini-spark-ai-agent-hands-on" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
    </div>
  </div>
  <div class="section-gap section-amber" id="section-policy">
    <div class="section-head"><div class="section-line"></div><span class="section-label">政策 & 合规</span><span class="section-label-cn">Policy & Compliance</span></div>
    <div class="sub-grid">
      <div class="sub-card"><div class="sub-tag" style="color:#fcd34d;">商业分析 · 36氪</div><div class="sub-title">阿里 AI 需要算一笔账了：3800 亿投入但净利润下滑 67%</div><div class="sub-desc">36氪深度：阿里成立 ATH 事业群构建"创造 Token→输送 Token→应用 Token"全栈布局，已投入 3800 亿 AI 基建，但同期净利润下滑 67%。组织频繁调整——通义核心团队 2026 年已流失多位关键人物。阿里 AI 战略面临"既要大规模投入又要短期回报"的根本矛盾。</div><div style="margin-top:6px; font-size:8px; color:var(--text-tertiary);">36氪 · 4月14日</div><div style="margin-top:4px; font-size:8px; color:#fcd34d;">💡 开发者影响：阿里 AI 投入收缩可能影响通义 API 价格和生态开放度</div><a href="https://www.36kr.com/p/3766378615829000" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
    </div>
  </div>
  <div class="section-gap section-cyan" id="section-cases">
    <div class="section-head"><div class="section-line"></div><span class="section-label">应用落地</span><span class="section-label-cn">Real-World AI</span></div>
    <div class="dual-cards">
      <div class="rank-card"><div class="rank-label" style="color:#67e8f9;">&#127981; Harness 实践 · 36氪</div><div style="font-size:14px; font-weight:500; color:var(--text-primary); margin-bottom:6px;">Creao：99% 代码 AI 生成，六周压缩到一天，产品经理角色被淘汰</div><div style="font-size:10px; color:var(--text-secondary); line-height:1.5; margin-bottom:8px;">Harness Engineering（挽具工程）正在从概念走向实践。Creao 的案例证明：当 Harness 架构足够完善，AI 可以完成几乎全部编码工作，人类角色转向系统设计和质量把关。</div><div style="font-size:8px; color:var(--text-tertiary);">36氪 · 5月26日</div><a href="https://36kr.com/p/3825551742489222" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
      <div class="rank-card"><div class="rank-label" style="color:#67e8f9;">&#127891; The Verge 评测</div><div style="font-size:14px; font-weight:500; color:var(--text-primary); margin-bottom:6px;">Gemini Spark 24/7 Agent 实测：能干但 $99.99/月不值</div><div style="font-size:10px; color:var(--text-secondary); line-height:1.5; margin-bottom:8px;">The Verge 深度评测：Gemini Spark 在邮件草拟、日历管理等任务上表现不错，但和 Google Demo 的差距依然存在。隐私成本（需交出全部个人数据）和 $99.99/月的价格让评测者犹豫。</div><div style="font-size:8px; color:var(--text-tertiary);">The Verge · 近日</div><a href="https://www.theverge.com/tech/941138/google-gemini-spark-ai-agent-hands-on" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
    </div>
  </div>
  <div class="section-gap section-amber" id="section-oss">
    <div class="section-head"><div class="section-line"></div><span class="section-label">开源热度</span><span class="section-label-cn">Open Source Pulse</span></div>
    <div class="dual-cards">
      <div class="rank-card"><div class="rank-label" style="color:#fcd34d;">&#128200; GitHub Trending — AI Top 5（W22-24）</div>
        <div class="rank-row"><span class="rank-num">1</span><span class="rank-name">ECC (智能体工具链)</span><span class="rank-stat rank-up">199K 总★</span></div><div class="rank-row"><span class="rank-num">2</span><span class="rank-name">TradingAgents (金融)</span><span class="rank-stat rank-up">81K 总★</span></div><div class="rank-row"><span class="rank-num">3</span><span class="rank-name">MoneyPrinterTurbo</span><span class="rank-stat rank-up">71K 总★</span></div><div class="rank-row"><span class="rank-num">4</span><span class="rank-name">ruvnet/ruflo (Agent编排)</span><span class="rank-stat rank-up">56K 总★</span></div><div class="rank-row"><span class="rank-num">5</span><span class="rank-name">Understand-Anything</span><span class="rank-stat rank-up">45K 总★</span></div>
        <a href="https://github.com/trending?since=monthly" class="read-original" target="_blank" rel="noopener">查看完整榜单 <span class="read-original-arrow">→</span></a></div>
      <div class="rank-card"><div class="rank-label" style="color:#fcd34d;">&#128200; 趋势（cnblogs）</div><div style="font-size:10px; color:var(--text-secondary); line-height:1.6;"><p><strong>Skills 范式统治</strong> Karpathy Skills + mattpocock/skills + addyosmani/agent-skills 成铁三角。</p><p><strong>Agent 编排平台崛起</strong> ruflo 56K★，ECC 199K★——多Agent 协作成新基建。</p><p><strong>垂直场景 Agent</strong> TradingAgents(金融)+MoneyPrinter(自媒体)证明垂直 Agent 的市场需求。</p><p style="margin-top:6px; color:#fcd34d;">💡 Skills + 多Agent编排 + 垂直场景 = 2026 开源铁三角</p></div></div>
    </div>
  </div>
  <div class="section-gap section-cyan" id="section-overseas">
    <div class="section-head"><div class="section-line"></div><span class="section-label">海外参考</span><span class="section-label-cn">Global Brief</span></div>
    <div class="sub-grid">
      <div class="sub-card"><div class="sub-tag" style="color:#67e8f9;">🌏 The Verge</div><div class="sub-title">Nadella 博客定调 2026："AI 的关键转折年"，从模型转向 Agent 系统</div><div class="sub-desc">微软 CEO 罕见亲自写博客：2026 是 AI 的"关键转折年"，行业必须超越"AI slop vs 精致"之争。真正的革命不是更好的模型，而是 Agent 系统对现实世界产生实际影响。</div><div style="margin-top:4px; font-size:8px; color:#67e8f9;">💡 从 CEO 视角确认了"Agent 系统 > 模型"的行业共识</div><a href="https://www.theverge.com/news/852630/microsoft-ceo-satya-nadella-scratchpad-blog-ai-slop-comments" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
      <div class="sub-card"><div class="sub-tag" style="color:#67e8f9;">💬 The Verge</div><div class="sub-title">Gemini Spark 24/7 Agent 实测：能干但 $99.99/月不值，隐私代价高</div><div class="sub-desc">Google 常驻 AI Agent 深度评测。功能可用但和 Demo 有差距。价格+隐私双重门槛让评测者持保留态度。</div><div style="margin-top:4px; font-size:8px; color:#67e8f9;">💡 常驻 Agent 的商业化瓶颈：用户不愿为"还不够好的 AI"付费</div><a href="https://www.theverge.com/tech/941138/google-gemini-spark-ai-agent-hands-on" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
      <div class="sub-card"><div class="sub-tag" style="color:#67e8f9;">🏛️ 36氪</div><div class="sub-title">豆包日活 2 亿但日收入不足百万：全球 C 端 AI 变现困境</div><div class="sub-desc">字节旗下豆包 DAU 破 2 亿，但变现能力远低于传统互联网产品。"健身房模式"（低门槛订阅+超额付费）被视为破局方向。全球 AI 公司都在从免费走向付费，但用户抗拒。</div><div style="margin-top:4px; font-size:8px; color:#67e8f9;">💡 C 端 AI 商业化是全球性难题——用户对 AI 的付费意愿远低于预期</div><a href="https://36kr.com/p/3856911189595393" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
    </div>
  </div>'''

start = html.find('<div class="section-gap section-indigo" id="section-models">')
end = html.find('<footer class="footer">')
html = html[:start] + c + '\n' + html[end:]

now = datetime.datetime.now()
html = re.sub(r'<span class="hero-badge-text" id="editionLabel">.*?</span>', f'<span class="hero-badge-text" id="editionLabel">午间版·{now.strftime("%H:%M")}·增量更新</span>', html)
html = re.sub(r'<p class="hero-date" id="dateLabel">.*?</p>', f'<p class="hero-date" id="dateLabel">{now.strftime("%Y年%m月%d日")}·星期四</p>', html)
html = re.sub(r'<p class="hero-updated" id="updatedLabel">.*?</p>', f'<p class="hero-updated" id="updatedLabel"><span class="hero-updated-dot"></span>最后更新:{now.strftime("%Y-%m-%d %H:%M")} CST</p>', html)
tl = 'AI商业模式之困：豆包日活2亿但日收入不足百万36氪深度提出健身房模式；Creao公司99%代码AI生成六周压缩到一天Harness工程重塑组织架构；阿里AI需要算一笔账3800亿投入净利润下滑67%；OpenAI Codex桌面版macOS发布多Agent并行；GitHub Agent HQ集成Claude+Codex+Copilot三Agent竞技场；Gemini Spark 24/7 Agent实测能干但年费过千美元不值；Nadella博客定调2026是关键转折年。'
html = re.sub(r'<span class="tldr-text" id="tldrContent">.*?</span>', f'<span class="tldr-text" id="tldrContent">{tl}</span>', html, flags=re.DOTALL)

# Auto-generate archiveMap from actual files
html = inject_archive_map(html)

archive_file = f"archive/{now.strftime('%Y-%m-%d')}-noon.html"
with open(archive_file, 'w', encoding='utf-8') as f:
    f.write(html)
print(f'OK {len(html)}B | Placeholders:0 | archive:{archive_file}')
