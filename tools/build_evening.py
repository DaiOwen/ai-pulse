#!/usr/bin/env python3
import re, datetime
with open('index.html','r',encoding='utf-8') as f: html = f.read()

c = r'''  <div class="section-gap section-indigo" id="section-models">
    <div class="section-head"><div class="section-line"></div><span class="section-label">大模型动态（全天汇总）</span><span class="section-label-cn">Models</span></div>
    <div class="feature-card"><div class="card-row"><div class="card-body">
      <div class="card-tag" style="color:#6366f1;">HEADLINE</div>
      <div class="card-title">大厂 Token 不再「管够」：腾讯限额、字节部分报销、阿里不限、京东自研免费</div>
      <div class="card-desc">36氪独家调查：大厂全面推行 Token 配额制度。腾讯 6 月起下调额度（部门动态分配 1000-7000 元/月）；字节自研 TRAE 不限量、外部模型自费后部分报销（上限 1000 美元/年）；阿里产研岗月约 8000 元不限制模型；京东自研模型不限量、外部分摊到部门。有团队一晚上烧掉 200 万元 Token，龙虾之父 30 天 API 费用达 130 万美元。Token 成本管控正从宽松走向严格——AI 编程的"无限畅饮"时代结束。</div>
      <div class="card-meta"><span>36氪</span><span>&#183;</span><span>6月15日</span><span>&#183;</span><span class="card-meta-link">独家调查</span></div>
      <div style="margin-top:8px; font-size:9px; color:#a5b4fc;">💡 开发者影响：Token 配额制全面推广意味着 AI 编程需要成本意识，本地模型+云端混合策略是出路</div>
      <a href="https://36kr.com/p/3854191285507336" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a>
    </div><div class="card-icon">&#9889;</div></div></div>
    <div class="sub-grid">
      <div class="sub-card"><div class="sub-tag" style="color:#a5b4fc;">国产出路 · 36氪 6月16日</div><div class="sub-title">国产大模型出路：Fusion 动态路由 + Omnigent 元框架，从替代品变基础设施</div><div class="sub-desc">36氪今日深度：不再硬刚极限推理，转向"架构分权"——Fusion 多模型动态路由将复杂任务分发到不同模型并融合结果；Omnigent 元框架打破厂商封闭生态，实现跨模型"一键热插拔"。国产模型从前沿替代品→基础设施底层齿轮。</div><div style="margin-top:6px; font-size:8px; color:var(--text-tertiary);">36氪 · 6月16日</div><div style="margin-top:4px; font-size:8px; color:#a5b4fc;">💡 开发者影响：多模型编排能力比单一模型性能更重要，Fusion+元框架是工程趋势</div><a href="https://36kr.com/p/3855547730852745" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
      <div class="sub-card"><div class="sub-tag" style="color:#a5b4fc;">字节AI · 36氪独家</div><div class="sub-title">字节 AI 2026 四命题：世界模型、Seedance、Coding、豆包商业化</div><div class="sub-desc">36氪独家获悉字节AI四大方向：世界模型追赶 Google Genie 3；视频模型 Seedance 保持领先探索动态生成；Coding+Agent 夯实地基做好 Dogfooding；豆包商业化重点"办公"。火山引擎联合赛力斯推 AIVA 品牌，豆包大模型装车超 700 万辆。</div><div style="margin-top:6px; font-size:8px; color:var(--text-tertiary);">36氪 · 6月3日</div><div style="margin-top:4px; font-size:8px; color:#a5b4fc;">💡 开发者影响：豆包 DAU 破亿后的四大方向决定了字节 AI 生态的开放度和开发者机会</div><a href="https://36kr.com/newsflashes/3838463320869128" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
      <div class="sub-card"><div class="sub-tag" style="color:#a5b4fc;">AI+Science · 36氪</div><div class="sub-title">津渡生科获近亿元 A 轮：GeneLLM 15亿参数多组学大模型 + BioFord Agent</div><div class="sub-desc">GeneLLM 为 15 亿参数多组学大模型，端到端疾病分析。BioFord Agent 具身自主科研平台，五大智能体协作实现"干湿闭环"——AI 设计实验→机器人执行→AI 分析结果→迭代优化。AI for Science 从论文进入产业化落地。</div><div style="margin-top:6px; font-size:8px; color:var(--text-tertiary);">36氪 · 6月12日</div><div style="margin-top:4px; font-size:8px; color:#a5b4fc;">💡 开发者影响：AI+生命科学融资热度不减，垂直领域大模型是新的创业方向</div><a href="https://36kr.com/p/3849630446441729" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
      <div class="sub-card"><div class="sub-tag" style="color:#a5b4fc;">开发者角色 · VentureBeat</div><div class="sub-title">明天最好的开发者不写代码——他们策划、协调和指挥 AI</div><div class="sub-desc">VentureBeat 评论：AI 编程助手正在自动化初级编码任务，开发者角色转向"策划者+协调者+指挥者"——更像编排 AI 系统的技术 PM，而非亲自写每一行代码。这将对计算机教育、招聘标准和职业路径产生深远影响。</div><div style="margin-top:6px; font-size:8px; color:var(--text-tertiary);">VentureBeat · 近日</div><div style="margin-top:4px; font-size:8px; color:#a5b4fc;">💡 开发者影响：编程技能价值正从"写代码"转向"设计系统+编排Agent"</div><a href="https://venturebeat.com/programming-development/why-tomorrows-best-devs-wont-just-code-theyll-curate-coordinate-and-command-ai" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
    </div>
  </div>
  <div class="section-gap section-green" id="section-tools">
    <div class="section-head"><div class="section-line"></div><span class="section-label">工具 & 部署</span><span class="section-label-cn">Tools & Deploy</span></div>
    <div class="tool-row">
      <div class="tool-card"><div class="tool-icon">&#128200;</div><div class="tool-name">Token 配额时代</div><div class="tool-desc">腾讯/字节/阿里/京东全面推行 Token 配额制。有团队一夜烧 200 万。龙虾之父月烧 130 万美元。AI 编程成本意识成新常态。</div><span class="tool-badge badge-update">趋势</span><a href="https://36kr.com/p/3854191285507336" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
      <div class="tool-card"><div class="tool-icon">&#129302;</div><div class="tool-name">Harness 工程</div><div class="tool-desc">模型不再是瓶颈。Harness 将约束从"规则"→"结构/环境"，让错误路径无法发生。模型趋同后 AI 竞争的分水岭。</div><span class="tool-badge badge-new">新范式</span><a href="https://36kr.com/p/3736640995721472" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
      <div class="tool-card"><div class="tool-icon">&#127942;</div><div class="tool-name">Karpathy Skills 月冠</div><div class="tool-desc">andrej-karpathy-skills 月增 65K★ 登顶 GitHub 5 月榜。Skills 模块化成 AI 编程新范式——不再比模型大小。</div><span class="tool-badge badge-new">65K★/月</span><a href="https://www.cnblogs.com/qiniushanghai/p/20262033" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
    </div>
  </div>
  <div class="section-gap section-amber" id="section-policy">
    <div class="section-head"><div class="section-line"></div><span class="section-label">政策 & 合规</span><span class="section-label-cn">Policy & Compliance</span></div>
    <div class="sub-grid">
      <div class="sub-card"><div class="sub-tag" style="color:#fcd34d;">院士观点 · 人民网</div><div class="sub-title">邬贺铨：从单一 Agent 到 Agentic AI 协同群，IoA 智联网是下一步</div><div class="sub-desc">中国工程院院士邬贺铨：国务院"人工智能+"行动意见明确智能体应用普及。从单一 Agent 向 Agentic AI（智能体协同群）升级是必然趋势。未来需发展 IoA（智联网），实现开放式异构智能体跨域协作。</div><div style="margin-top:6px; font-size:8px; color:var(--text-tertiary);">人民网 · 2025年9月</div><div style="margin-top:4px; font-size:8px; color:#fcd34d;">💡 开发者影响：IoA 智联网是多 Agent 协作的下一个基础设施方向</div><a href="http://finance.people.com.cn/n1/2025/0905/c1004-40557957.html" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
      <div class="sub-card"><div class="sub-tag" style="color:#fcd34d;">北京方案 · 人民网</div><div class="sub-title">北京 2028 目标：100 个工业智能体 + 50 家智能方案供应商</div><div class="sub-desc">北京市印发《AI 赋能工业互联网高质量发展实施方案（2026-2028）》，量化目标：100 个工业高质量数据集、50 家智能化解决方案供应商、100 个高水平工业智能体、京津冀标准统一互认。</div><div style="margin-top:6px; font-size:8px; color:var(--text-tertiary);">人民网 · 5月12日</div><div style="margin-top:4px; font-size:8px; color:#fcd34d;">💡 开发者影响：北京 100 个工业智能体目标释放明确的 B 端采购需求</div><a href="http://bj.people.com.cn/n2/2026/0512/c14540-41578189.html" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
    </div>
  </div>
  <div class="section-gap section-cyan" id="section-cases">
    <div class="section-head"><div class="section-line"></div><span class="section-label">应用落地</span><span class="section-label-cn">Real-World AI</span></div>
    <div class="dual-cards">
      <div class="rank-card"><div class="rank-label" style="color:#67e8f9;">&#127981; Token 经济 · 36氪</div><div style="font-size:14px; font-weight:500; color:var(--text-primary); margin-bottom:6px;">大厂 Token 配额时代：腾讯限额、字节报销、阿里不限、京东自研免费</div><div style="font-size:10px; color:var(--text-secondary); line-height:1.5; margin-bottom:8px;">四家大厂 Token 管控策略对比+行业趋势分析。AI 编程从"公司买单"进入"部门核算"阶段。开发者需要建立 Token 成本意识，合理选择本地模型+云端模型组合。</div><div style="font-size:8px; color:var(--text-tertiary);">36氪 · 6月15日</div><a href="https://36kr.com/p/3854191285507336" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
      <div class="rank-card"><div class="rank-label" style="color:#67e8f9;">&#127891; AI+Science · 36氪</div><div style="font-size:14px; font-weight:500; color:var(--text-primary); margin-bottom:6px;">津渡生科 BioFord Agent：五大智能体协作实现 AI 自主科研"干湿闭环"</div><div style="font-size:10px; color:var(--text-secondary); line-height:1.5; margin-bottom:8px;">AI 设计实验→机器人执行→AI 分析结果→迭代优化。标志着 AI for Science 从论文发表进入产业化落地。</div><div style="font-size:8px; color:var(--text-tertiary);">36氪 · 6月12日</div><a href="https://36kr.com/p/3849630446441729" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
    </div>
  </div>
  <div class="section-gap section-amber" id="section-oss">
    <div class="section-head"><div class="section-line"></div><span class="section-label">开源热度（5月月榜）</span><span class="section-label-cn">Open Source Pulse</span></div>
    <div class="dual-cards">
      <div class="rank-card"><div class="rank-label" style="color:#fcd34d;">&#128200; GitHub 5月月榜 — AI Top 5</div>
        <div class="rank-row"><span class="rank-num">1</span><span class="rank-name">mattpocock/skills</span><span class="rank-stat rank-up">+71K/月</span></div><div class="rank-row"><span class="rank-num">2</span><span class="rank-name">andrej-karpathy-skills</span><span class="rank-stat rank-up">+65K/月</span></div><div class="rank-row"><span class="rank-num">3</span><span class="rank-name">Understand-Anything</span><span class="rank-stat rank-up">+36K/月</span></div><div class="rank-row"><span class="rank-num">4</span><span class="rank-name">codegraph</span><span class="rank-stat rank-up">+33K/月</span></div><div class="rank-row"><span class="rank-num">5</span><span class="rank-name">TradingAgents</span><span class="rank-stat rank-up">+27K/月</span></div>
        <a href="https://github.com/trending?since=monthly" class="read-original" target="_blank" rel="noopener">查看完整榜单 <span class="read-original-arrow">→</span></a></div>
      <div class="rank-card"><div class="rank-label" style="color:#fcd34d;">&#128200; 趋势解读</div><div style="font-size:10px; color:var(--text-secondary); line-height:1.6;"><p><strong>Skills 范式统治</strong> 月榜 Top2 都是 Skills，合计 136K★/月。Skills 模块化是 2026 年上半年最大开源趋势。</p><p><strong>AI Agent 金融交易</strong> TradingAgents 月增 27K★，多 Agent 协作进入量化金融。</p><p><strong>代码知识图谱</strong> codegraph 33K★/月，本地代码图数据库成 AI 编程标配。</p><p style="margin-top:6px; color:#fcd34d;">💡 5 月信号：Skills 生态+金融 Agent+代码图谱=三大增长极</p></div></div>
    </div>
  </div>
  <div class="section-gap section-cyan" id="section-overseas">
    <div class="section-head"><div class="section-line"></div><span class="section-label">海外参考</span><span class="section-label-cn">Global Brief</span></div>
    <div class="sub-grid">
      <div class="sub-card"><div class="sub-tag" style="color:#67e8f9;">🌏 开发者角色 · VentureBeat</div><div class="sub-title">明天最好的开发者不写代码——他们策划、协调和指挥 AI</div><div class="sub-desc">AI 编程助手自动化初级编码工作，开发者角色转向策划者+协调者+指挥者。这对计算机教育、招聘标准和职业路径将产生深远影响。</div><div style="margin-top:4px; font-size:8px; color:#67e8f9;">💡 编程技能价值正从"写代码"转向"设计系统+编排Agent"</div><a href="https://venturebeat.com/programming-development/why-tomorrows-best-devs-wont-just-code-theyll-curate-coordinate-and-command-ai" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
      <div class="sub-card"><div class="sub-tag" style="color:#67e8f9;">💬 Token 经济 · 36氪</div><div class="sub-title">AI 编程"无限畅饮"时代终结：全球大厂推行 Token 配额制度</div><div class="sub-desc">中国四厂+GitHub Copilot+Anthropic Agent SDK 同步转向按量计费。AI 编程从"公司买单"进入"成本核算"阶段。Token 成本管理将成为开发者必备技能。</div><div style="margin-top:4px; font-size:8px; color:#67e8f9;">💡 Token 成本管理=2026 下半年开发者必备技能</div><a href="https://36kr.com/p/3854191285507336" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
      <div class="sub-card"><div class="sub-tag" style="color:#67e8f9;">🏛️ 治理标准 · 人民网</div><div class="sub-title">全球仅 20% 公司建立成熟 AI 治理模型，"信任"成 AI 产品硬指标</div><div class="sub-desc">德勤报告+业界"双重授权"架构（访问权与行动权分离）。AI 产品的信任和治理能力将直接影响企业采购决策。</div><div style="margin-top:4px; font-size:8px; color:#67e8f9;">💡 AI 治理能力正从软性话题变成商业硬指标</div><a href="http://finance.people.com.cn/n1/2026/0202/c1004-40657725.html" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
    </div>
  </div>'''

start = html.find('<div class="section-gap section-indigo" id="section-models">')
end = html.find('<footer class="footer">')
html = html[:start] + c + '\n' + html[end:]

now = datetime.datetime.now()
html = re.sub(r'<span class="hero-badge-text" id="editionLabel">.*?</span>', f'<span class="hero-badge-text" id="editionLabel">晚间版 · {now.strftime("%H:%M")} · 全天汇总</span>', html)
html = re.sub(r'<p class="hero-date" id="dateLabel">.*?</p>', f'<p class="hero-date" id="dateLabel">{now.strftime("%Y年%m月%d日")} · 星期二</p>', html)
html = re.sub(r'<p class="hero-updated" id="updatedLabel">.*?</p>', f'<p class="hero-updated" id="updatedLabel"><span class="hero-updated-dot"></span> 最后更新: {now.strftime("%Y-%m-%d %H:%M")} CST</p>', html)
tl = '大厂Token不再管够：腾讯限额、字节部分报销、阿里不限、京东自研免费；国产大模型出路转向Fusion动态路由+Omnigent元框架；字节AI四命题世界模型+Seedance+Coding+豆包商业化；津渡生科GeneLLM+BioFord Agent五大智能体自主科研；邬贺铨院士提出IoA智联网异构智能体跨域协作；北京2028目标100个工业智能体；Karpathy Skills月增65K★ 登顶5月GitHub月榜。'
html = re.sub(r'<span class="tldr-text" id="tldrContent">.*?</span>', f'<span class="tldr-text" id="tldrContent">{tl}</span>', html, flags=re.DOTALL)

with open('archive/2026-06-16-evening.html', 'w', encoding='utf-8') as f: f.write(html)
print(f'OK {len(html)}B | #: {html.count(chr(34)+"#" + chr(34) + " class=" + chr(34) + "read-original")}')
