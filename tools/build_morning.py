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
      <div class="card-title">Fable 5 系统提示词泄露 12 万字：不是纯 LLM，而是完整 Agent 系统</div>
      <div class="card-desc">36氪独家：Claude Fable 5 的 12 万字系统提示词被泄露，揭示了一个颠覆性事实——Fable 5 并非传统意义上的大语言模型，而是一个完整的 Agent 操作系统。内置 Linux 沙箱、子 Agent 分发能力、动态工作流编排，甚至包含反蒸馏"隐形降智"机制来检测是否被用于训练其他模型。此前 Anthropic 刚以 H 轮 650 亿美元融资、估值 9650 亿美元超越 OpenAI。Stripe 测试中 Fable 5 一天完成了一个团队两个月的 5000 万行 Ruby 代码迁移。</div>
      <div class="card-meta"><span>36氪</span><span>&#183;</span><span>6月17日</span><span>&#183;</span><span class="card-meta-link">独家爆料</span></div>
      <div style="margin-top:8px; font-size:9px; color:#a5b4fc;">💡 开发者影响：前沿模型正从"语言引擎"进化为"Agent 操作系统"——这比模型能力提升更值得关注</div>
      <a href="https://36kr.com/p/3857125518972165" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a>
    </div><div class="card-icon">&#9889;</div></div></div>
    <div class="sub-grid">
      <div class="sub-card"><div class="sub-tag" style="color:#a5b4fc;">小米 · VentureBeat</div><div class="sub-title">小米 MiMo-V2-Pro 发布：1T 参数仅 42B 激活，性能接近 GPT-5.2，成本 1/7</div><div class="sub-desc">VentureBeat 报道：小米发布 MiMo-V2-Pro，1 万亿参数 MoE 仅 42B 激活，1M 上下文，混合注意力 7:1。性能接近 GPT-5.2/Opus 4.6，API 仅 $1/$3 每百万 Token。中国开源模型持续证明"少激活+多专家"架构的效率优势。</div><div style="margin-top:6px; font-size:8px; color:var(--text-tertiary);">VentureBeat · 近日</div><div style="margin-top:4px; font-size:8px; color:#a5b4fc;">💡 开发者影响：42B 激活即可接近 GPT-5.2——MoE 架构效率继续碾压密集模型</div><a href="https://venturebeat.com/technology/xiaomi-stuns-with-new-mimo-v2-pro-llm-nearing-gpt-5-2-opus-4-6-performance" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
      <div class="sub-card"><div class="sub-tag" style="color:#a5b4fc;">Anthropic · VentureBeat</div><div class="sub-title">Claude Opus 4.6 支持百万上下文+Agent Teams，Claude Code 年收入破 $10 亿</div><div class="sub-desc">Opus 4.6 首次将 1M Token 上下文带入 Opus 级别，新增 Agent Teams 功能——多 Agent 并行自主协作。Terminal-Bench 2.0 和 Humanity's Last Exam 双料冠军。Claude Code 年化收入突破 $10 亿。</div><div style="margin-top:6px; font-size:8px; color:var(--text-tertiary);">VentureBeat · 近日</div><a href="https://venturebeat.com/technology/anthropics-claude-opus-4-6-brings-1m-token-context-and-agent-teams-to-take" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
      <div class="sub-card"><div class="sub-tag" style="color:#a5b4fc;">泡沫破裂 · 36氪</div><div class="sub-title">AI 应用层出清：Sora 关停、Yupp.ai 倒闭，底层模型能力下沉淘汰包装者</div><div class="sub-desc">36氪报道 AI 应用层泡沫破裂：OpenAI Sora 关停、Yupp.ai 倒闭、Pixel Studio 下架。仅靠"包装 GPT API"的应用正在批量死亡。真正活下来的产品是嵌入高频场景、进入真实工作流的。</div><div style="margin-top:6px; font-size:8px; color:var(--text-tertiary);">36氪 · 6月16日</div><a href="https://36kr.com/p/3854657422119941" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
    </div>
  </div>
  <div class="section-gap section-green" id="section-tools">
    <div class="section-head"><div class="section-line"></div><span class="section-label">工具 & 部署</span><span class="section-label-cn">Tools & Deploy</span></div>
    <div class="tool-row">
      <div class="tool-card"><div class="tool-icon">&#129302;</div><div class="tool-name">Claude Agent Teams</div><div class="tool-desc">Opus 4.6 新增多 Agent 并行协作。百万上下文+自主分工。Claude Code $1B ARR。</div><span class="tool-badge badge-new">Agent Teams</span><a href="https://venturebeat.com/technology/anthropics-claude-opus-4-6-brings-1m-token-context-and-agent-teams-to-take" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
      <div class="tool-card"><div class="tool-icon">&#128241;</div><div class="tool-name">Google FunctionGemma</div><div class="tool-desc">270M 参数端侧模型。手机/浏览器/IoT 本地运行。自然语言→结构化代码。85% 准确率。</div><span class="tool-badge badge-new">端侧</span><a href="https://venturebeat.com/technology/google-releases-functiongemma-a-tiny-edge-model-that-can-control-mobile" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
      <div class="tool-card"><div class="tool-icon">&#128200;</div><div class="tool-name">AI 成本失控</div><div class="tool-desc">Uber 烧光年预算、米哈游一夜 200 万。Meta 员工月烧 31.2 万亿 Token。Token 经济成核心命题。</div><span class="tool-badge badge-update">警示</span><a href="https://36kr.com/p/3841823029447170" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
    </div>
  </div>
  <div class="section-gap section-amber" id="section-policy">
    <div class="section-head"><div class="section-line"></div><span class="section-label">政策 & 合规</span><span class="section-label-cn">Policy & Compliance</span></div>
    <div class="sub-grid">
      <div class="sub-card"><div class="sub-tag" style="color:#fcd34d;">七部门 · 6月19日</div><div class="sub-title">七部门发布平台经济行动方案：引导平台加强智能体创新布局，2028 年 60+ 场景</div><div class="sub-desc">七部门联合发布《促进平台经济大中小企业协同发展行动方案》，明确引导平台企业加强通用大模型、行业大模型和智能体等 AI 领域创新布局。面向中小企业优化智能体服务，到 2028 年打造不少于 60 个智能服务应用场景。此前国-务院已提出 2027 年智能体普及率超 70%。</div><div style="margin-top:6px; font-size:8px; color:var(--text-tertiary);">新华社/人民网 · 6月19日</div><a href="http://finance.people.com.cn/n1/2026/0619/c1004-40743599.html" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
      <div class="sub-card"><div class="sub-tag" style="color:#fcd34d;">上海 · 人民网</div><div class="sub-title">上海目标：10 万台人形机器人进工厂，规上企业智能体普及率超 80%</div><div class="sub-desc">上海"十五五"末推动 10 万台人形机器人进工厂，规上工业企业智能体应用普及率超 80%。杭州 2026 年培育 50 家"AI 工厂"。地方 AI 竞争进入量化目标阶段。</div><div style="margin-top:6px; font-size:8px; color:var(--text-tertiary);">人民网 · 5-6月</div><a href="http://sh.people.com.cn/n2/2026/0611/c134768-41607234.html" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
    </div>
  </div>
  <div class="section-gap section-cyan" id="section-cases">
    <div class="section-head"><div class="section-line"></div><span class="section-label">应用落地</span><span class="section-label-cn">Real-World AI</span></div>
    <div class="dual-cards">
      <div class="rank-card"><div class="rank-label" style="color:#67e8f9;">&#127981; Claude Code · VentureBeat</div><div style="font-size:14px; font-weight:500; color:var(--text-primary); margin-bottom:6px;">Claude Code 年收入破 $10 亿：Uber/Salesforce/Accenture/Spotify 采用</div><div style="font-size:10px; color:var(--text-secondary); line-height:1.5; margin-bottom:8px;">Anthropic 的 AI 编码工具年化收入突破 $10 亿。Agent Teams 实现多 Agent 并行自主协作。Stripe 测试 Fable 5 一天完成 5000 万行代码迁移。</div><div style="font-size:8px; color:var(--text-tertiary);">VentureBeat · 近日</div><a href="https://venturebeat.com/technology/anthropics-claude-opus-4-6-brings-1m-token-context-and-agent-teams-to-take" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
      <div class="rank-card"><div class="rank-label" style="color:#67e8f9;">&#127891; 行业洗牌 · 36氪</div><div style="font-size:14px; font-weight:500; color:var(--text-primary); margin-bottom:6px;">AI 应用层出清加速：Sora 关停、Yupp 倒闭，模型能力下沉淘汰简单包装</div><div style="font-size:10px; color:var(--text-secondary); line-height:1.5; margin-bottom:8px;">仅靠包装 GPT API 的应用正批量死亡。底层模型能力下沉使"薄包装"产品价值归零。活下来的都具备深度场景嵌入。</div><div style="font-size:8px; color:var(--text-tertiary);">36氪 · 6月16日</div><a href="https://36kr.com/p/3854657422119941" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
    </div>
  </div>
  <div class="section-gap section-amber" id="section-oss">
    <div class="section-head"><div class="section-line"></div><span class="section-label">开源热度</span><span class="section-label-cn">Open Source Pulse</span></div>
    <div class="dual-cards">
      <div class="rank-card"><div class="rank-label" style="color:#fcd34d;">&#128200; GitHub Trending — AI Top 5（6月上半旬）</div>
        <div class="rank-row"><span class="rank-num">1</span><span class="rank-name">mvanhorn/last30days-skill</span><span class="rank-stat rank-up">+12K/周</span></div><div class="rank-row"><span class="rank-num">2</span><span class="rank-name">chopratejas/headroom</span><span class="rank-stat rank-up">+10K/周</span></div><div class="rank-row"><span class="rank-num">3</span><span class="rank-name">mattpocock/skills</span><span class="rank-stat rank-up">+71K/月</span></div><div class="rank-row"><span class="rank-num">4</span><span class="rank-name">Karpathy Skills</span><span class="rank-stat rank-up">+65K/月</span></div><div class="rank-row"><span class="rank-num">5</span><span class="rank-name">MoneyPrinterTurbo</span><span class="rank-stat rank-up">+6.9K/周</span></div>
        <a href="https://github.com/trending?since=weekly" class="read-original" target="_blank" rel="noopener">查看完整榜单 <span class="read-original-arrow">→</span></a></div>
      <div class="rank-card"><div class="rank-label" style="color:#fcd34d;">&#128200; 趋势（cnblogs）</div><div style="font-size:10px; color:var(--text-secondary); line-height:1.6;"><p><strong>Skills > 模型本身</strong> 最热的不是大模型而是周边配置和工程化工具。</p><p><strong>Agent 安全诉求上升</strong> 6月误删邮件事故后安全沙箱被放大。</p><p><strong>Rust 在 AI 基建层崛起</strong> OpenClaw/Goose 等使用 Rust。</p><p style="margin-top:6px; color:#fcd34d;">💡 2026 开源风向：Skills 生态 + Agent 安全 + Rust 基建</p></div></div>
    </div>
  </div>
  <div class="section-gap section-cyan" id="section-overseas">
    <div class="section-head"><div class="section-line"></div><span class="section-label">海外参考</span><span class="section-label-cn">Global Brief</span></div>
    <div class="sub-grid">
      <div class="sub-card"><div class="sub-tag" style="color:#67e8f9;">🌏 Anthropic · VentureBeat</div><div class="sub-title">Anthropic H 轮 $650 亿估值 $9650 亿超越 OpenAI，已秘密提交 IPO</div><div class="sub-desc">Claude Code 年收入破 $10 亿。Stripe 测试一天完成 5000 万行代码迁移。从"模型公司"转型为"Agent 平台公司"。</div><div style="margin-top:4px; font-size:8px; color:#67e8f9;">💡 估值超越 OpenAI 标志着 Agent 能力 > 模型能力的市场共识</div><a href="https://venturebeat.com/technology/anthropics-claude-opus-4-6-brings-1m-token-context-and-agent-teams-to-take" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
      <div class="sub-card"><div class="sub-tag" style="color:#67e8f9;">💬 端侧 · VentureBeat</div><div class="sub-title">Google FunctionGemma：270M 参数端侧模型，手机本地运行控制应用</div><div class="sub-desc">仅 270M 参数，手机/浏览器/IoT 本地运行。自然语言→结构化可执行代码，无需云端。</div><div style="margin-top:4px; font-size:8px; color:#67e8f9;">💡 端侧 AI 从"可能"走向"可用"——270M 即可移动设备控制</div><a href="https://venturebeat.com/technology/google-releases-functiongemma-a-tiny-edge-model-that-can-control-mobile" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
      <div class="sub-card"><div class="sub-tag" style="color:#67e8f9;">🏛️ 政策 · 人民网</div><div class="sub-title">中国七部门引导平台加强智能体布局，2028 年 60+ 场景落地</div><div class="sub-desc">国-务院目标 2027 年普及率超 70%，七部门最新方案加码到 2028 年 60+ 场景。全球最激进的 AI 产业政策。</div><div style="margin-top:4px; font-size:8px; color:#67e8f9;">💡 中国 AI 政策从"鼓励"走向"量化考核"</div><a href="http://finance.people.com.cn/n1/2026/0619/c1004-40743599.html" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
    </div>
  </div>'''

start = html.find('<div class="section-gap section-indigo" id="section-models">')
end = html.find('<footer class="footer">')
html = html[:start] + c + '\n' + html[end:]

now = datetime.datetime.now()
html = re.sub(r'<span class="hero-badge-text" id="editionLabel">.*?</span>', f'<span class="hero-badge-text" id="editionLabel">早间版 · {now.strftime("%H:%M")} · 清晨速递</span>', html)
html = re.sub(r'<p class="hero-date" id="dateLabel">.*?</p>', f'<p class="hero-date" id="dateLabel">{now.strftime("%Y年%m月%d日")} · 星期日</p>', html)
html = re.sub(r'<p class="hero-updated" id="updatedLabel">.*?</p>', f'<p class="hero-updated" id="updatedLabel"><span class="hero-updated-dot"></span> 最后更新: {now.strftime("%Y-%m-%d %H:%M")} CST</p>', html)
html = re.sub(r'<span class="tldr-text" id="tldrContent">.*?</span>', f'<span class="tldr-text" id="tldrContent">Fable5系统提示词泄露12万字不是纯LLM而是完整Agent操作系统；小米MiMo-V2-Pro 1T参数仅42B激活成本1/7；Claude Opus4.6百万上下文+Agent Teams年收入破10亿美元；AI应用层泡沫Sora关停Yupp倒闭；七部门平台经济方案2028年60+智能体场景；Google FunctionGemma 270M端侧模型；上海10万台人形机器人进工厂。</span>', html, flags=re.DOTALL)

html = inject_archive_map(html)
archive_file = f"archive/{now.strftime('%Y-%m-%d')}-morning.html"
with open(archive_file, 'w', encoding='utf-8') as f: f.write(html)
print(f'OK {len(html)}B')
