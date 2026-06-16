#!/usr/bin/env python3
import re, datetime

with open('index.html','r',encoding='utf-8') as f: html = f.read()

c = r'''  <div class="section-gap section-indigo" id="section-models">
    <div class="section-head"><div class="section-line"></div><span class="section-label">大模型动态</span><span class="section-label-cn">Models</span></div>
    <div class="feature-card"><div class="card-row"><div class="card-body">
      <div class="card-tag" style="color:#6366f1;">HEADLINE</div>
      <div class="card-title">Perplexity 发布企业级 AI Agent「Computer」：编排 20+ 模型，叫板微软 Salesforce</div>
      <div class="card-desc">Ask 2026 大会上 Perplexity 推出企业级多模型 AI Agent "Computer"。它编排约 20 个模型（Claude Opus 4.6、Gemini、GPT-5.2、Grok 等），将任务拆解后分派给专用子代理，运行在 Firecracker microVM 隔离环境中。集成 Slack、Snowflake、Datadog、Salesforce、SharePoint、HubSpot。定价采用用量制（credit pool）而非按人头收费，直接挑战微软 Copilot 和 Salesforce Agentforce。</div>
      <div class="card-meta"><span>VentureBeat</span><span>&#183;</span><span>近日</span><span>&#183;</span><span class="card-meta-link">独家报道</span></div>
      <div style="margin-top:8px; font-size:9px; color:#a5b4fc;">💡 开发者影响：多模型编排+微VM隔离成为企业Agent标配架构，单一模型依赖走向终结</div>
      <a href="https://venturebeat.com/ai/perplexity-takes-its-computer-ai-agent-into-the-enterprise-taking-aim-at" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a>
    </div><div class="card-icon">&#9889;</div></div></div>
    <div class="sub-grid">
      <div class="sub-card"><div class="sub-tag" style="color:#a5b4fc;">深度学习 · VentureBeat</div><div class="sub-title">Sakana AI 发布「Sakana Marlin」：8 小时自主推理，生成 100+ 页战略报告</div><div class="sub-desc">东京 Sakana AI（Transformer 作者 Llion Jones + 前 Google Brain David Ha 联合创立，估值 $26 亿）发布企业级深度研究 Agent。采用自适应分支蒙特卡洛树搜索（AB-MCTS），在探索新假设和深入细化之间动态平衡。可连续推理 8 小时，产出 100+ 页带引文和执行摘要的战略报告，定位为"虚拟首席战略官"。</div><div style="margin-top:6px; font-size:8px; color:var(--text-tertiary);">VentureBeat · 近日</div><div style="margin-top:4px; font-size:8px; color:#a5b4fc;">💡 开发者影响：8小时深度推理 Agent 为企业战略场景打开新可能，AB-MCTS 值得关注</div><a href="https://venturebeat.com/technology/when-deep-research-isnt-enough-for-your-business-sakana-ai-launches-ultra-deep-research-agent-for-100-page-reports-in-8-hours" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
    </div>
  </div>
  <div class="section-gap section-green" id="section-tools">
    <div class="section-head"><div class="section-line"></div><span class="section-label">工具 & 部署</span><span class="section-label-cn">Tools & Deploy</span></div>
    <div class="tool-row">
      <div class="tool-card"><div class="tool-icon">&#129302;</div><div class="tool-name">Kimi K2 Thinking</div><div class="tool-desc">月之暗面推出 1 万亿 MoE 推理模型，训练成本仅 $460 万——在 Agent 能力上对标 GPT-5。开源权重，重新定义"高性价比大模型"的边界。</div><span class="tool-badge badge-new">开源</span><a href="https://eu.36kr.com/zh/p/3543851834322816" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
      <div class="tool-card"><div class="tool-icon">&#127981;</div><div class="tool-name">ClickUp Brain Max</div><div class="tool-desc">企业级跨应用 AI 平台：查询 Google Drive/OneDrive/SharePoint，管理工单/邮件，自研 Brain 模型智能路由到最佳 AI。统一数据模型保留权限，Agent 尊重访问控制。</div><span class="tool-badge badge-new">企业级</span><a href="https://venturebeat.com/ai/as-ai-use-expands-platforms-like-brainmax-seek-to-simplify-cross-app-integration" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
    </div>
  </div>
  <div class="section-gap section-amber" id="section-policy">
    <div class="section-head"><div class="section-line"></div><span class="section-label">政策 & 合规</span><span class="section-label-cn">Policy & Compliance</span></div>
    <div class="sub-grid">
      <div class="sub-card"><div class="sub-tag" style="color:#fcd34d;">工信部 · 4月</div><div class="sub-title">工信部将发布"AI+"高价值场景，AI 核心产业规模超 1.2 万亿元</div><div class="sub-desc">工信部宣布将发布一批"人工智能+"高价值场景，建设特色智能体。我国 AI 核心产业规模已超 1.2 万亿元，相关企业超 6200 家，规上制造业企业 AI 应用普及率超 30%。广东 AI 核心产业规模突破 3000 亿元，推理芯片、Token 工厂、智能体成为 2026 年三大关键词。</div><div style="margin-top:6px; font-size:8px; color:var(--text-tertiary);">人民网 · 4月</div><div style="margin-top:4px; font-size:8px; color:#fcd34d;">💡 开发者影响：1.2 万亿产业规模意味着巨大的 B 端 AI 应用市场</div><a href="http://finance.people.com.cn/n1/2026/0412/c1004-40699571.html" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
    </div>
  </div>
  <div class="section-gap section-cyan" id="section-cases">
    <div class="section-head"><div class="section-line"></div><span class="section-label">应用落地</span><span class="section-label-cn">Real-World AI</span></div>
    <div class="dual-cards">
      <div class="rank-card"><div class="rank-label" style="color:#67e8f9;">&#127981; 产品创新 · 36氪</div><div style="font-size:14px; font-weight:500; color:var(--text-primary); margin-bottom:6px;">WPS 灵犀：一个完全不同的 Agent 样本——「Agentic Software」概念诞生</div><div style="font-size:10px; color:var(--text-secondary); line-height:1.5; margin-bottom:8px;">金山办公发布原生 Office 智能体 WPS 灵犀，提出"Agentic Software"概念——AI 不只是辅助工具，而是能与 Office 软件深度协同的智能主体。这不同于 ChatGPT 式聊天 Agent 或 Copilot 式侧边栏助手，而是在文档、表格、演示中直接"做事"。</div><div style="font-size:8px; color:var(--text-tertiary);">36氪 · 近期</div><div style="margin-top:4px; font-size:8px; color:#67e8f9;">💡 开发者影响：Agentic Software 是新的产品范式——AI 从 UI 层嵌入到业务逻辑层</div><a href="https://m.36kr.com/p/3399797612644740" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
    </div>
  </div>
  <div class="section-gap section-amber" id="section-oss">
    <div class="section-head"><div class="section-line"></div><span class="section-label">开源热度</span><span class="section-label-cn">Open Source Pulse</span></div>
    <div class="dual-cards">
      <div class="rank-card"><div class="rank-label" style="color:#fcd34d;">&#128200; GitHub Trending — AI Top 5（W24-25）</div>
        <div class="rank-row"><span class="rank-num">1</span><span class="rank-name">mvanhorn/last30days-skill</span><span class="rank-stat rank-up">+12K/周</span></div><div class="rank-row"><span class="rank-num">2</span><span class="rank-name">chopratejas/headroom</span><span class="rank-stat rank-up">+10K/周</span></div><div class="rank-row"><span class="rank-num">3</span><span class="rank-name">Leonxlnx/taste-skill</span><span class="rank-stat rank-up">+8.7K/周</span></div><div class="rank-row"><span class="rank-num">4</span><span class="rank-name">addyosmani/agent-skills</span><span class="rank-stat rank-up">+8.3K/周</span></div><div class="rank-row"><span class="rank-num">5</span><span class="rank-name">apple/container</span><span class="rank-stat rank-up">+7.8K/周</span></div>
        <a href="https://github.com/trending?since=weekly" class="read-original" target="_blank" rel="noopener">查看完整榜单 <span class="read-original-arrow">→</span></a></div>
      <div class="rank-card"><div class="rank-label" style="color:#fcd34d;">&#128200; 趋势（cnblogs W24）</div><div style="font-size:10px; color:var(--text-secondary); line-height:1.6;"><p><strong>Skills 生态</strong> 8+ 项目登榜，模块化成为新范式。</p><p><strong>Token 压缩</strong> headroom 6 种算法省 60-95%，Agent 上下文需求驱动。</p><p><strong>安全标配</strong> SkillSpector+MXC+NanoClaw 三位一体。</p><p style="margin-top:6px; color:#fcd34d;">💡 重心从"做模型"彻底转向"做 Agent 基础设施"</p></div></div>
    </div>
  </div>'''

start = html.find('<div class="section-gap section-indigo" id="section-models">')
end = html.find('<footer class="footer">')
html = html[:start] + c + '\n' + html[end:]

now = datetime.datetime.now()
html = re.sub(r'<span class="hero-badge-text" id="editionLabel">.*?</span>', f'<span class="hero-badge-text" id="editionLabel">午间版 · {now.strftime("%H:%M")} · 增量更新</span>', html)
html = re.sub(r'<p class="hero-date" id="dateLabel">.*?</p>', f'<p class="hero-date" id="dateLabel">{now.strftime("%Y年%m月%d日")} · 星期二</p>', html)
html = re.sub(r'<p class="hero-updated" id="updatedLabel">.*?</p>', f'<p class="hero-updated" id="updatedLabel"><span class="hero-updated-dot"></span> 最后更新: {now.strftime("%Y-%m-%d %H:%M")} CST</p>', html)
tl = 'Perplexity发布企业级AI Agent「Computer」编排20+模型叫板微软Salesforce；Sakana AI发布Marlin 8小时自主推理生成100+页战略报告；Kimi K2 Thinking万亿MoE训练成本仅460万美元；ClickUp Brain Max跨应用企业Agent平台；工信部AI核心产业规模超1.2万亿元将发布高价值场景；WPS灵犀提出Agentic Software新概念。'
html = re.sub(r'<span class="tldr-text" id="tldrContent">.*?</span>', f'<span class="tldr-text" id="tldrContent">{tl}</span>', html, flags=re.DOTALL)

with open('archive/2026-06-16-noon.html', 'w', encoding='utf-8') as f: f.write(html)
ph = html.count('"#" class="read-original')
print(f'Built: {len(html)}B | Placeholders: {ph}')
