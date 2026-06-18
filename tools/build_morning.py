#!/usr/bin/env python3
import re, datetime
with open('index.html','r',encoding='utf-8') as f: html = f.read()

c = r'''  <div class="section-gap section-indigo" id="section-models">
    <div class="section-head"><div class="section-line"></div><span class="section-label">大模型动态</span><span class="section-label-cn">Models</span></div>
    <div class="feature-card"><div class="card-row"><div class="card-body">
      <div class="card-tag" style="color:#6366f1;">HEADLINE</div>
      <div class="card-title">OpenAI 发布 Codex 桌面版：多 Agent 并行编程平台，macOS 首发</div>
      <div class="card-desc">OpenAI 推出 Codex macOS 桌面应用——定位为"Agent 指挥中心"。核心能力：将多个编程任务并行分派给 AI Agent，每个 Agent 可自主运行 30 分钟。引入"Skills"（工具集成脚本包）和"Automations"（后台定时任务）。Sam Altman 称其为"我们内部最受喜爱的产品"。面向 ChatGPT Plus/Pro/Business/Enterprise/Edu 用户，Windows 版和云端连续 Agent 在路线图中。</div>
      <div class="card-meta"><span>VentureBeat</span><span>&#183;</span><span>近日</span><span>&#183;</span><span class="card-meta-link">产品发布</span></div>
      <div style="margin-top:8px; font-size:9px; color:#a5b4fc;">💡 开发者影响：Codex Desktop 标志着 AI 编程从"助手"进入"Agent 指挥中心"时代</div>
      <a href="https://venturebeat.com/orchestration/openai-launches-a-codex-desktop-app-for-macos-to-run-multiple-ai-coding" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a>
    </div><div class="card-icon">&#9889;</div></div></div>
    <div class="sub-grid">
      <div class="sub-card"><div class="sub-tag" style="color:#a5b4fc;">开源称王 · VentureBeat</div><div class="sub-title">MiniMax-M2 登顶开源 LLM 榜首：230B MoE 仅 10B 激活，MIT 协议</div><div class="sub-desc">MiniMax-M2 在 Artificial Analysis 智能指数上排名开源模型第一。230B MoE 仅 10B 激活参数，4 张 H100 即可运行。Agent 工具调用基准 τ²-Bench 77.2 超越 GPT-5。MIT 许可证，API 仅 $0.30/$1.20 每百万 Token。阿里和腾讯联合投资背景。</div><div style="margin-top:6px; font-size:8px; color:var(--text-tertiary);">VentureBeat · 近日</div><div style="margin-top:4px; font-size:8px; color:#a5b4fc;">💡 开发者影响：MIT 开源+4 张 H100 可跑+极致性价比=值得立即评估</div><a href="https://venturebeat.com/ai/minimax-m2-is-the-new-king-of-open-source-llms-especially-for-agentic-tool" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
      <div class="sub-card"><div class="sub-tag" style="color:#a5b4fc;">编程新范式 · 36氪</div><div class="sub-title">Loop Engineering 崛起：Claude Code 之父+龙虾之父共推"循环工程"</div><div class="sub-desc">Claude Code 创始人 Boris Cherny 和 OpenClaw 之父 Peter Steinberger 共同推崇"循环工程"——从 Prompt 工程迈向设计 Agent 循环系统。核心是让 AI 在"执行→验证→修正→再执行"的闭环中自主迭代，而非人类持续干预。36氪评论：这可能是自 DevOps 以来最大的软件工程范式变迁。</div><div style="margin-top:6px; font-size:8px; color:var(--text-tertiary);">36氪 · 6月8日</div><div style="margin-top:4px; font-size:8px; color:#a5b4fc;">💡 开发者影响：设计 Agent Loop 正在取代编写 Prompt 成为 AI 时代的核心技能</div><a href="https://eu.36kr.com/zh/p/3844224911346184" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
      <div class="sub-card"><div class="sub-tag" style="color:#a5b4fc;">腾讯换船 · 36氪</div><div class="sub-title">腾讯 AI 秘密"换船"：元宝失宠，WorkBuddy 月访问 885 万接棒</div><div class="sub-desc">36氪独家：腾讯 WorkBuddy 办公 Agent 月访问量达 885 万（环比+831%），已取代元宝成为腾讯最高优先级 AI 产品。标志着腾讯 AI 战略从"聊天助手"转向"办公 Agent"。WorkBuddy 深度整合企业微信、腾讯文档、腾讯会议，覆盖日程管理、会议纪要、文档协作等场景。</div><div style="margin-top:6px; font-size:8px; color:var(--text-tertiary);">36氪 · 6月12日</div><div style="margin-top:4px; font-size:8px; color:#a5b4fc;">💡 开发者影响：WorkBuddy 生态开放度将决定腾讯 Agent 平台的开发者吸引力</div><a href="https://www.36kr.com/p/3848757418251523" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
    </div>
  </div>
  <div class="section-gap section-green" id="section-tools">
    <div class="section-head"><div class="section-line"></div><span class="section-label">工具 & 部署</span><span class="section-label-cn">Tools & Deploy</span></div>
    <div class="tool-row">
      <div class="tool-card"><div class="tool-icon">&#128187;</div><div class="tool-name">Codex Desktop macOS</div><div class="tool-desc">多 Agent 并行编程+Skills 集成+30分钟自主运行。Altman称"最受喜爱内部产品"。Windows版开发中。</div><span class="tool-badge badge-new">macOS</span><a href="https://venturebeat.com/orchestration/openai-launches-a-codex-desktop-app-for-macos-to-run-multiple-ai-coding" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
      <div class="tool-card"><div class="tool-icon">&#127942;</div><div class="tool-name">MiniMax-M2 MIT 开源</div><div class="tool-desc">230B MoE/10B active，4×H100 可跑。Agent 工具调用超 GPT-5。API $0.30/M input。</div><span class="tool-badge badge-new">MIT</span><a href="https://venturebeat.com/ai/minimax-m2-is-the-new-king-of-open-source-llms-especially-for-agentic-tool" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
      <div class="tool-card"><div class="tool-icon">&#129302;</div><div class="tool-name">Loop Engineering</div><div class="tool-desc">Claude Code之父+龙虾之父共推新范式。AI在"执行→验证→修正"闭环中自主迭代。</div><span class="tool-badge badge-new">新范式</span><a href="https://eu.36kr.com/zh/p/3844224911346184" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
    </div>
  </div>
  <div class="section-gap section-amber" id="section-policy">
    <div class="section-head"><div class="section-line"></div><span class="section-label">政策 & 合规</span><span class="section-label-cn">Policy & Compliance</span></div>
    <div class="sub-grid">
      <div class="sub-card"><div class="sub-tag" style="color:#fcd34d;">工信部八部门 · 1月</div><div class="sub-title">"AI+制造"21项措施：1000 个工业智能体 + 500 个典型场景</div><div class="sub-desc">工信部等八部门联合印发《"人工智能+制造"专项行动实施意见》，21 项措施覆盖算力、模型、数据、应用、安全全链条。量化目标：3-5 个通用大模型在制造业深度应用、1000 个工业智能体、500 个典型场景、培育 2-3 家全球生态型企业。</div><div style="margin-top:6px; font-size:8px; color:var(--text-tertiary);">人民网 · 1月9日</div><div style="margin-top:4px; font-size:8px; color:#fcd34d;">💡 开发者影响：1000 个工业智能体是明确的市场信号，制造业 AI 需求即将爆发</div><a href="http://finance.people.com.cn/n1/2026/0109/c1004-40641726.html" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
      <div class="sub-card"><div class="sub-tag" style="color:#fcd34d;">地方落地 · 人民网</div><div class="sub-title">上海：10万台人形机器人进工厂 + 算力券模型券发放</div><div class="sub-desc">上海"模塑申城"工程目标：十五五末推动 10 万台人形机器人进工厂。同期发放算力券、模型券、语料券降低企业AI使用成本。北京最高 3000 万元算力补贴+具身智能工厂 3000 万元奖励。杭州 2026 年培育 50 家"AI 工厂"。厦门最高 3000 万元 AI 产业奖励。</div><div style="margin-top:6px; font-size:8px; color:var(--text-tertiary);">人民网 · 5-7月</div><div style="margin-top:4px; font-size:8px; color:#fcd34d;">💡 开发者影响：算力券+模型券降低创业成本，北京/上海/杭州/厦门四城竞争态势</div><a href="http://sh.people.com.cn/n2/2026/0611/c134768-41607234.html" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
    </div>
  </div>
  <div class="section-gap section-purple" id="section-paper">
    <div class="section-head"><div class="section-line"></div><span class="section-label">论文速递</span><span class="section-label-cn">Paper Spotlight</span></div>
    <div class="paper-spotlight"><div class="paper-header"><span class="paper-label">&#128218; 本周精选 · MIT License</span></div>
      <div class="paper-title">MiniMax-M2：MoE 架构在 Agent 工具调用中的极致效率</div>
      <div class="paper-abstract">MiniMax-M2 证明了稀疏 MoE 架构（230B/10B）在 Agent 工具调用场景可以同时实现 SOTA 性能和极致性价比。τ²-Bench 77.2 超越 GPT-5，API 成本仅为 GPT-5 的约 5%。MIT 开源许可证使企业可自由商用和定制，4 张 H100 的运行门槛大幅降低了 Agent 部署的硬件门槛。</div>
      <div class="paper-meta">MiniMax · VentureBeat 报道 · 开源模型榜第一</div><div style="margin-top:6px; font-size:8px; color:#c4b5fd;">💡 开发者影响：MIT 协议+4 卡部署+超 GPT-5 Agent 能力=值得立即评估的亮点模型</div></div>
  </div>
  <div class="section-gap section-cyan" id="section-cases">
    <div class="section-head"><div class="section-line"></div><span class="section-label">应用落地</span><span class="section-label-cn">Real-World AI</span></div>
    <div class="dual-cards">
      <div class="rank-card"><div class="rank-label" style="color:#67e8f9;">&#127981; 产业落地 · 36氪</div><div style="font-size:14px; font-weight:500; color:var(--text-primary); margin-bottom:6px;">腾讯 WorkBuddy 月访问 885 万：从聊天助手到办公 Agent 的战略换船</div><div style="font-size:10px; color:var(--text-secondary); line-height:1.5; margin-bottom:8px;">36氪独家披露腾讯 AI 战略转向：WorkBuddy 办公 Agent 月访问量 885 万（环比暴增 831%），取代元宝成为最高优先级产品。深度整合企业微信、腾讯文档、腾讯会议，从"聊天"走向"办事"。</div><div style="font-size:8px; color:var(--text-tertiary);">36氪 · 6月12日</div><a href="https://www.36kr.com/p/3848757418251523" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
      <div class="rank-card"><div class="rank-label" style="color:#67e8f9;">&#127891; 新范式 · 36氪</div><div style="font-size:14px; font-weight:500; color:var(--text-primary); margin-bottom:6px;">Loop Engineering：自 DevOps 以来最大的软件工程范式变迁</div><div style="font-size:10px; color:var(--text-secondary); line-height:1.5; margin-bottom:8px;">Claude Code 和 Codex 都在推动"循环工程"——AI 在"执行→验证→修正→再执行"闭环中自主迭代。编写 Prompt 正在被设计 Agent Loop 取代。这不仅是技术变迁，更是开发者思维方式的根本转变。</div><div style="font-size:8px; color:var(--text-tertiary);">36氪 · 6月8日</div><a href="https://eu.36kr.com/zh/p/3844224911346184" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
    </div>
  </div>
  <div class="section-gap section-amber" id="section-oss">
    <div class="section-head"><div class="section-line"></div><span class="section-label">开源热度</span><span class="section-label-cn">Open Source Pulse</span></div>
    <div class="dual-cards">
      <div class="rank-card"><div class="rank-label" style="color:#fcd34d;">&#128200; GitHub Trending — AI Top 5（6月上半旬）</div>
        <div class="rank-row"><span class="rank-num">1</span><span class="rank-name">mvanhorn/last30days-skill</span><span class="rank-stat rank-up">+12K/周</span></div><div class="rank-row"><span class="rank-num">2</span><span class="rank-name">chopratejas/headroom</span><span class="rank-stat rank-up">+10K/周</span></div><div class="rank-row"><span class="rank-num">3</span><span class="rank-name">harry0703/MoneyPrinterTurbo</span><span class="rank-stat rank-up">+6.9K/周</span></div><div class="rank-row"><span class="rank-num">4</span><span class="rank-name">microsoft/markitdown</span><span class="rank-stat rank-up">+6.3K/周</span></div><div class="rank-row"><span class="rank-num">5</span><span class="rank-name">NVIDIA/SkillSpector</span><span class="rank-stat rank-up">+3.6K/周</span></div>
        <a href="https://github.com/trending?since=weekly" class="read-original" target="_blank" rel="noopener">查看完整榜单 <span class="read-original-arrow">→</span></a></div>
      <div class="rank-card"><div class="rank-label" style="color:#fcd34d;">&#128200; 趋势解读（cnblogs）</div><div style="font-size:10px; color:var(--text-secondary); line-height:1.6;"><p><strong>Skills 成为 2026 最重要的技术原语</strong> 类似 npm 的 Agent 技能市场生态已初步形成。开发者注意力从"哪个模型最强"转向"哪个框架最工程化"。</p><p><strong>Loop Engineering 范式兴起</strong> AI 编程从"写 Prompt"进化为"设计 Agent 循环系统"。</p><p><strong>TypeScript+Python 统治</strong> 占 AI 工具链绝对主力。</p><p style="margin-top:6px; color:#fcd34d;">💡 Skills 生态+Loop Engineering+多 Agent 协作=2026 开源三大方向</p></div></div>
    </div>
  </div>
  <div class="section-gap section-cyan" id="section-overseas">
    <div class="section-head"><div class="section-line"></div><span class="section-label">海外参考</span><span class="section-label-cn">Global Brief</span></div>
    <div class="sub-grid">
      <div class="sub-card"><div class="sub-tag" style="color:#67e8f9;">🌏 Codex · VentureBeat</div><div class="sub-title">OpenAI Codex Desktop 发布：多 Agent 并行编程 macOS 首发</div><div class="sub-desc">Codex 桌面版定位"Agent 指挥中心"，多 Agent 并行+30 分钟自主运行+Skills 集成。Altman 称"最受喜爱内部产品"。Windows 版开发中。</div><div style="margin-top:4px; font-size:8px; color:#67e8f9;">💡 AI 编程从"助手"升级为"Agent 指挥中心"</div><a href="https://venturebeat.com/orchestration/openai-launches-a-codex-desktop-app-for-macos-to-run-multiple-ai-coding" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
      <div class="sub-card"><div class="sub-tag" style="color:#67e8f9;">💬 MiniMax · VentureBeat</div><div class="sub-title">MiniMax-M2 登顶开源榜首：MIT 协议+Agent 工具调用超 GPT-5</div><div class="sub-desc">230B MoE/10B active，4×H100 可跑，API 仅 GPT-5 的 5%。中国开源模型在 Agent 赛道上全面追平甚至超越美国前沿闭源模型。</div><div style="margin-top:4px; font-size:8px; color:#67e8f9;">💡 中国开源模型在 Agent 基准上首次超越 GPT-5</div><a href="https://venturebeat.com/ai/minimax-m2-is-the-new-king-of-open-source-llms-especially-for-agentic-tool" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
      <div class="sub-card"><div class="sub-tag" style="color:#67e8f9;">🏛️ 中国制造 · 人民网</div><div class="sub-title">工信部"AI+制造"21项措施 + 四城 AI 补贴政策全面铺开</div><div class="sub-desc">1000 个工业智能体+500 个典型场景+北京/上海/杭州/厦门四城最高 3000 万元补贴。中国 AI 产业政策从"鼓励"进入"量化目标+现金激励"阶段。</div><div style="margin-top:4px; font-size:8px; color:#67e8f9;">💡 四城 AI 产业补贴政策竞争态势明确</div><a href="http://finance.people.com.cn/n1/2026/0109/c1004-40641726.html" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
    </div>
  </div>'''

start = html.find('<div class="section-gap section-indigo" id="section-models">')
end = html.find('<footer class="footer">')
html = html[:start] + c + '\n' + html[end:]

now = datetime.datetime.now()
html = re.sub(r'<span class="hero-badge-text" id="editionLabel">.*?</span>', f'<span class="hero-badge-text" id="editionLabel">早间版 · {now.strftime("%H:%M")} · 清晨速递</span>', html)
html = re.sub(r'<p class="hero-date" id="dateLabel">.*?</p>', f'<p class="hero-date" id="dateLabel">{now.strftime("%Y年%m月%d日")} · 星期四</p>', html)
html = re.sub(r'<p class="hero-updated" id="updatedLabel">.*?</p>', f'<p class="hero-updated" id="updatedLabel"><span class="hero-updated-dot"></span> 最后更新: {now.strftime("%Y-%m-%d %H:%M")} CST</p>', html)
tl = 'OpenAI发布Codex桌面版macOS多Agent并行编程平台；MiniMax-M2登顶开源LLM榜首230B MoE仅10B激活MIT协议Agent工具调用超GPT-5；Loop Engineering新范式崛起Claude Code之父+龙虾之父共推；腾讯AI秘密换船WorkBuddy月访问885万接棒元宝；工信部八部门AI+制造21项措施目标1000个工业智能体；上海10万台人形机器人进工厂四城AI补贴全面铺开。'
html = re.sub(r'<span class="tldr-text" id="tldrContent">.*?</span>', f'<span class="tldr-text" id="tldrContent">{tl}</span>', html, flags=re.DOTALL)

with open('archive/2026-06-18-morning.html', 'w', encoding='utf-8') as f: f.write(html)
print(f'OK {len(html)}B | #: {html.count(chr(34)+"#" + chr(34) + " class=" + chr(34) + "read-original")}')
