#!/usr/bin/env python3
import re, datetime
with open('index.html','r',encoding='utf-8') as f: html = f.read()

c = r'''  <div class="section-gap section-indigo" id="section-models">
    <div class="section-head"><div class="section-line"></div><span class="section-label">大模型动态</span><span class="section-label-cn">Models</span></div>
    <div class="feature-card"><div class="card-row"><div class="card-body">
      <div class="card-tag" style="color:#6366f1;">HEADLINE</div>
      <div class="card-title">阿里发布首个具身大模型系列 Qwen-Robot：VLA 操作 + VLN 移动 + 世界模型，AI 走进物理世界</div>
      <div class="card-desc">6 月 16 日，阿里正式发布 Qwen-Robot 系列——国内首个具身大模型家族。包含三大模块：VLA（视觉-语言-动作）操作模型、VLN（视觉-语言-导航）移动模型、以及世界模型。这意味着千问从"理解世界"进入"操作世界"阶段。此前发布的 Qwen3.7-Plus 已接入淘宝、支付宝等 400+ 办事场景，Qwen3-Max-Thinking 万亿参数旗舰推理模型也在持续迭代。阿里 AI 正从"数字助手"走向"物理执行者"。</div>
      <div class="card-meta"><span>证券时报</span><span>&#183;</span><span>6月16日</span><span>&#183;</span><span class="card-meta-link">今日重磅</span></div>
      <div style="margin-top:8px; font-size:9px; color:#a5b4fc;">💡 开发者影响：具身大模型开放 API 后，机器人开发将从 ROS 编程转向自然语言交互</div>
      <a href="https://www.stcn.com/article/detail/3963742.html" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a>
    </div><div class="card-icon">&#9889;</div></div></div>
    <div class="sub-grid">
      <div class="sub-card"><div class="sub-tag" style="color:#a5b4fc;">人才变革 · 36氪</div><div class="sub-title">AI 原生组织人才标准重塑：Prompt 不再是壁垒，判断力与任务拆解成新稀缺</div><div class="sub-desc">36氪深度洞察：AI 原生组织正在重塑人才标准。Prompt 工程已不是核心竞争力——自主性、品味判断力（Taste）、复杂任务拆解能力成为新的稀缺资源。"昨日人才，今日废柴"正在部分 AI 公司真实上演。</div><div style="margin-top:6px; font-size:8px; color:var(--text-tertiary);">36氪 · 近日</div><div style="margin-top:4px; font-size:8px; color:#a5b4fc;">💡 开发者影响：职业护城河从"会写代码"变成"会拆问题+会编排Agent"</div><a href="https://36kr.com/p/3855123438376196" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
      <div class="sub-card"><div class="sub-tag" style="color:#a5b4fc;">医疗AI · 证券时报</div><div class="sub-title">讯飞星火医疗大模型 V3.5 发布：全国产算力训练，聚焦临床诊疗</div><div class="sub-desc">6 月 9 日，科大讯飞发布星火医疗大模型 V3.5，100% 基于国产算力训练。聚焦临床诊疗与健康管理两大场景，在多学科问诊、病历质控等任务上接近资深医师水平。医疗 AI 正从"辅助建议"走向"独立诊断"。</div><div style="margin-top:6px; font-size:8px; color:var(--text-tertiary);">证券时报 · 6月9日</div><div style="margin-top:4px; font-size:8px; color:#a5b4fc;">💡 开发者影响：医疗 AI 是监管最严格的垂直赛道，合规能力 > 模型能力</div><a href="https://stcn.com/article/detail/3952107.html" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
      <div class="sub-card"><div class="sub-tag" style="color:#a5b4fc;">政策治理 · 人民网</div><div class="sub-title">信通院院长余晓晖：AI 治理需覆盖数据、模型、应用、全球四层</div><div class="sub-desc">中国信通院院长余晓晖在人民日报撰文提出 AI 治理四层框架：夯实数据治理、提升模型治理、优化应用治理（分级分类+沙盒监管+触发式监管）、强化全球治理协同。中国已发布 30 项 AI 国标、84 项制定中，主导国际标准制定。</div><div style="margin-top:6px; font-size:8px; color:var(--text-tertiary);">人民网 · 4月9日</div><div style="margin-top:4px; font-size:8px; color:#a5b4fc;">💡 开发者影响：沙盒监管和分级分类管理是 AI 产品上市的前置条件</div><a href="http://theory.people.com.cn/n1/2026/0409/c40531-40697780.html" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
    </div>
  </div>
  <div class="section-gap section-green" id="section-tools">
    <div class="section-head"><div class="section-line"></div><span class="section-label">工具 & 部署</span><span class="section-label-cn">Tools & Deploy</span></div>
    <div class="tool-row">
      <div class="tool-card"><div class="tool-icon">&#129302;</div><div class="tool-name">阿里 Qwen-Robot</div><div class="tool-desc">国内首个具身大模型系列。VLA操作模型+VLN移动模型+世界模型三件套。AI 从"理解世界"到"操作世界"的关键一步。</div><span class="tool-badge badge-new">具身智能</span><a href="https://www.stcn.com/article/detail/3963742.html" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
      <div class="tool-card"><div class="tool-icon">&#128737;</div><div class="tool-name">网络安全 AI 重构</div><div class="tool-desc">业界告别"补丁式"防御，进入"低-中-高"三位一体 AI 安全架构：低位产品执行+中位智能体调度+高位大模型决策。</div><span class="tool-badge badge-update">安全</span><a href="http://finance.people.com.cn/BIG5/n1/2026/0604/c1004-40734073.html" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
      <div class="tool-card"><div class="tool-icon">&#128200;</div><div class="tool-name">AI 人才市场变革</div><div class="tool-desc">Prompt 工程不再是核心壁垒。自主性+Taste+任务拆解能力成为新稀缺。AI 原生组织加速淘汰传统技能人才。</div><span class="tool-badge badge-new">趋势</span><a href="https://36kr.com/p/3855123438376196" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
    </div>
  </div>
  <div class="section-gap section-amber" id="section-policy">
    <div class="section-head"><div class="section-line"></div><span class="section-label">政策 & 合规</span><span class="section-label-cn">Policy & Compliance</span></div>
    <div class="sub-grid">
      <div class="sub-card"><div class="sub-tag" style="color:#fcd34d;">国家标准 · 人民网</div><div class="sub-title">中国已发布 30 项 AI 国家标准，84 项制定中——主导国际标准</div><div class="sub-desc">中国已发布 30 项 AI 国标，84 项正在制定中，覆盖基础软硬件、关键技术、行业应用与安全治理全链条。中国还在主导制定《生成式人工智能风险处理指南》国际标准。信通院院长提出数据、模型、应用、全球四层治理框架。</div><div style="margin-top:6px; font-size:8px; color:var(--text-tertiary);">人民网 · 4-5月</div><div style="margin-top:4px; font-size:8px; color:#fcd34d;">💡 开发者影响：84 项在制国标意味着 AI 产品合规要求将密集出台</div><a href="http://theory.people.com.cn/n1/2026/0409/c40531-40697780.html" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
      <div class="sub-card"><div class="sub-tag" style="color:#fcd34d;">安全架构 · 人民网</div><div class="sub-title">网络安全迈入"智能重构"阶段：AI 安全三位一体防御体系</div><div class="sub-desc">6 月 4 日业界提出"低-中-高"AI 安全协同防御架构：低位产品执行+中位智能体运营调度+高位大模型底座决策。告别被动"补丁式"防御，进入主动智能防御时代。</div><div style="margin-top:6px; font-size:8px; color:var(--text-tertiary);">人民网 · 6月4日</div><div style="margin-top:4px; font-size:8px; color:#fcd34d;">💡 开发者影响：AI 安全从"附加功能"升级为"架构设计"，Agent 权限管理是核心</div><a href="http://finance.people.com.cn/BIG5/n1/2026/0604/c1004-40734073.html" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
    </div>
  </div>
  <div class="section-gap section-purple" id="section-paper">
    <div class="section-head"><div class="section-line"></div><span class="section-label">论文速递</span><span class="section-label-cn">Paper Spotlight</span></div>
    <div class="paper-spotlight"><div class="paper-header"><span class="paper-label">&#128218; 今日精选 · 阿里 Qwen-Robot</span></div>
      <div class="paper-title">Qwen-Robot：从语言理解到物理操作的跨模态迁移</div>
      <div class="paper-abstract">阿里发布首个具身大模型系列，核心突破在于将大语言模型的推理能力迁移到物理操作领域。VLA（视觉-语言-动作）模型实现了从自然语言指令到机器人动作轨迹的端到端映射；VLN（视觉-语言-导航）模型让机器人能在未知环境中基于语言指令自主导航；世界模型为机器人提供物理常识和动作规划的基础。</div>
      <div class="paper-meta">阿里巴巴 · 6月16日 · 国内首个具身大模型系列</div>
      <div style="margin-top:6px; font-size:8px; color:#c4b5fd;">💡 开发者影响：具身大模型将机器人编程从"写控制代码"变成"描述任务目标"</div>
    </div>
  </div>
  <div class="section-gap section-cyan" id="section-cases">
    <div class="section-head"><div class="section-line"></div><span class="section-label">应用落地</span><span class="section-label-cn">Real-World AI</span></div>
    <div class="dual-cards">
      <div class="rank-card"><div class="rank-label" style="color:#67e8f9;">&#127981; 产业落地 · 36氪</div><div style="font-size:14px; font-weight:500; color:var(--text-primary); margin-bottom:6px;">千问 APP 已接入淘宝、支付宝等 400+ 办事场景：AI 从"聊天"走向"办事"</div><div style="font-size:10px; color:var(--text-secondary); line-height:1.5; margin-bottom:8px;">阿里 Qwen3.7-Plus 发布后，千问 APP 已接入淘宝、支付宝、高德、饿了么等阿里系生态，实现 AI 购物、订票、叫车、点外卖等超 400 项办事功能。这是国内首个实现"AI 直接办事"而非"AI 建议你做"的超级应用。</div><div style="font-size:8px; color:var(--text-tertiary);">证券时报 · 6月</div><div style="margin-top:4px; font-size:8px; color:#67e8f9;">💡 开发者影响：AI 办事能力需要打通支付+物流+客服全链路，生态壁垒是核心竞争力</div><a href="https://stcn.com/article/detail/3938527.html" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
      <div class="rank-card"><div class="rank-label" style="color:#67e8f9;">&#127891; 人才市场 · 36氪</div><div style="font-size:14px; font-weight:500; color:var(--text-primary); margin-bottom:6px;">AI 原生组织人才革命：Prompt 不再是壁垒，判断力成新货币</div><div style="font-size:10px; color:var(--text-secondary); line-height:1.5; margin-bottom:8px;">36氪深度洞察：AI 公司正在重塑人才标准。纯 Prompt 工程师岗位需求锐减——AI 已经能自己写 Prompt。新的稀缺人才是：能拆解复杂问题、有"品味"（Taste）判断 AI 输出质量、能编排多 Agent 协作系统的人。这正在对计算机教育体系产生倒逼压力。</div><div style="font-size:8px; color:var(--text-tertiary);">36氪 · 近日</div><a href="https://36kr.com/p/3855123438376196" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
    </div>
  </div>
  <div class="section-gap section-amber" id="section-oss">
    <div class="section-head"><div class="section-line"></div><span class="section-label">开源热度</span><span class="section-label-cn">Open Source Pulse</span></div>
    <div class="dual-cards">
      <div class="rank-card"><div class="rank-label" style="color:#fcd34d;">&#128200; GitHub Trending — AI Top 5（5月月榜）</div>
        <div class="rank-row"><span class="rank-num">1</span><span class="rank-name">mattpocock/skills</span><span class="rank-stat rank-up">+71K/月</span></div><div class="rank-row"><span class="rank-num">2</span><span class="rank-name">andrej-karpathy-skills</span><span class="rank-stat rank-up">+65K/月</span></div><div class="rank-row"><span class="rank-num">3</span><span class="rank-name">Understand-Anything</span><span class="rank-stat rank-up">+36K/月</span></div><div class="rank-row"><span class="rank-num">4</span><span class="rank-name">codegraph</span><span class="rank-stat rank-up">+33K/月</span></div><div class="rank-row"><span class="rank-num">5</span><span class="rank-name">TradingAgents</span><span class="rank-stat rank-up">+27K/月</span></div>
        <a href="https://github.com/trending?since=monthly" class="read-original" target="_blank" rel="noopener">查看完整榜单 <span class="read-original-arrow">→</span></a></div>
      <div class="rank-card"><div class="rank-label" style="color:#fcd34d;">&#128200; 趋势解读</div><div style="font-size:10px; color:var(--text-secondary); line-height:1.6;"><p><strong>Skills 范式统治</strong> 月榜 Top2 都是 Skills，合计 136K★/月。Skills 模块化是上半年最大开源趋势。</p><p><strong>代码知识图谱</strong> codegraph 33K★/月，本地代码图数据库成 AI 编程标配。</p><p><strong>金融 Agent 崛起</strong> TradingAgents 27K★/月，多 Agent 协作进入量化交易。</p><p style="margin-top:6px; color:#fcd34d;">💡 Skills 生态+代码图谱+金融 Agent=三大增长极</p></div></div>
    </div>
  </div>
  <div class="section-gap section-cyan" id="section-overseas">
    <div class="section-head"><div class="section-line"></div><span class="section-label">海外参考</span><span class="section-label-cn">Global Brief</span></div>
    <div class="sub-grid">
      <div class="sub-card"><div class="sub-tag" style="color:#67e8f9;">🌏 Chrome Agent · The Verge</div><div class="sub-title">Gemini 嵌入 Chrome 免费开放：Google 用浏览器撬动 Agent 入口</div><div class="sub-desc">Gemini 直接嵌入 Chrome 浏览器并免费开放。即将上线 Agent 能力：帮你买菜、比价、预订。The Verge 评论：浏览器正成为 Agent 时代最重要的操作系统。</div><div style="margin-top:4px; font-size:8px; color:#67e8f9;">💡 Chrome 插件生态面临 Agent 化重构</div><a href="https://www.theverge.com/ai-artificial-intelligence/781192/chrome-gemini-ai-agentic-update-google-mac-windows" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
      <div class="sub-card"><div class="sub-tag" style="color:#67e8f9;">💬 人才变革 · 36氪</div><div class="sub-title">AI 原生组织人才革命：Prompt 工程师需求锐减，判断力成新货币</div><div class="sub-desc">全球 AI 公司人才标准统一变化：纯 Prompt 工程师需求下降，能拆解问题+判断AI输出+编排多Agent的人才成为核心资产。计算机教育面临倒逼压力。</div><div style="margin-top:4px; font-size:8px; color:#67e8f9;">💡 职业护城河从"会写代码"变成"会拆问题+会编排Agent"</div><a href="https://36kr.com/p/3855123438376196" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
      <div class="sub-card"><div class="sub-tag" style="color:#67e8f9;">🏛️ AI 治理 · 人民网</div><div class="sub-title">中国主导制定《生成式AI风险处理指南》国际标准，30项国标已发布</div><div class="sub-desc">中国已发布 30 项 AI 国标，84 项制定中，主导国际标准制定。信通院提出四层治理框架——数据、模型、应用、全球协同。</div><div style="margin-top:4px; font-size:8px; color:#67e8f9;">💡 84 项在制国标意味着 AI 合规要求将密集出台</div><a href="http://theory.people.com.cn/n1/2026/0409/c40531-40697780.html" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
    </div>
  </div>'''

start = html.find('<div class="section-gap section-indigo" id="section-models">')
end = html.find('<footer class="footer">')
html = html[:start] + c + '\n' + html[end:]

now = datetime.datetime.now()
html = re.sub(r'<span class="hero-badge-text" id="editionLabel">.*?</span>', f'<span class="hero-badge-text" id="editionLabel">早间版 · {now.strftime("%H:%M")} · 清晨速递</span>', html)
html = re.sub(r'<p class="hero-date" id="dateLabel">.*?</p>', f'<p class="hero-date" id="dateLabel">{now.strftime("%Y年%m月%d日")} · 星期三</p>', html)
html = re.sub(r'<p class="hero-updated" id="updatedLabel">.*?</p>', f'<p class="hero-updated" id="updatedLabel"><span class="hero-updated-dot"></span> 最后更新: {now.strftime("%Y-%m-%d %H:%M")} CST</p>', html)
tl = '阿里发布首个具身大模型系列Qwen-Robot：VLA操作+VLN移动+世界模型AI走进物理世界；AI原生组织人才标准重塑：Prompt不再是壁垒判断力成新货币；讯飞星火医疗大模型V3.5发布全国产算力训练；中国已发布30项AI国标84项制定中主导国际标准；千问APP已接入400+办事场景；网络安全迈入AI智能重构三位一体防御时代。'
html = re.sub(r'<span class="tldr-text" id="tldrContent">.*?</span>', f'<span class="tldr-text" id="tldrContent">{tl}</span>', html, flags=re.DOTALL)

with open('archive/2026-06-17-morning.html', 'w', encoding='utf-8') as f: f.write(html)
print(f'OK {len(html)}B | #: {html.count(chr(34)+"#" + chr(34) + " class=" + chr(34) + "read-original")}')
