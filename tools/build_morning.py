#!/usr/bin/env python3
import re, datetime

with open('index.html','r',encoding='utf-8') as f: html = f.read()

c = r'''  <div class="section-gap section-indigo" id="section-models">
    <div class="section-head"><div class="section-line"></div><span class="section-label">大模型动态</span><span class="section-label-cn">Models</span></div>
    <div class="feature-card"><div class="card-row"><div class="card-body">
      <div class="card-tag" style="color:#6366f1;">HEADLINE</div>
      <div class="card-title">阿里通义再失核心：首席科学家周靖人履新 6 天离职，2026 年已流失 4 位关键人物</div>
      <div class="card-desc">36氪独家：阿里首席科学家周靖人被曝离职，履新仅 6 天。这是通义核心团队 2026 年流失的第 4 位关键人物。同期，阿里成立 Token Foundry 事业部，由 CEO 吴泳铭直管，整合通义大模型与未来生活实验室——组织架构剧烈变动背后，是阿里在模型 SOTA 争夺和商业化压力之间的挣扎。通义团队动荡引发行业对"大厂 AI 人才战"的广泛讨论。</div>
      <div class="card-meta"><span>36氪</span><span>&#183;</span><span>6月13日</span><span>&#183;</span><span class="card-meta-link">独家报道</span></div>
      <div style="margin-top:8px; font-size:9px; color:#a5b4fc;">💡 开发者影响：核心人才流失可能影响通义模型迭代节奏，多供应商策略更显重要</div>
      <a href="https://www.36kr.com/p/3850978776759176" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a>
    </div><div class="card-icon">&#9889;</div></div></div>
    <div class="sub-grid">
      <div class="sub-card"><div class="sub-tag" style="color:#a5b4fc;">出口管制 · 36氪</div><div class="sub-title">Claude Fable 5 平替指南爆火：OpenRouter Fusion API 多模型协作接近 Fable 水平</div><div class="sub-desc">Fable 5 被美国政府出口管制封禁后，社区迅速推出"平替指南"。OpenRouter 的 Fusion API 通过多模型协作（组合 Claude Opus 4.8 + GPT-5.5 + Gemini 3.5 Flash）接近 Fable 5 水平，成本仅为 Fable 5 的 40%。HuggingFace CEO 感叹"开源社区的反应速度快得惊人"。</div><div style="margin-top:6px; font-size:8px; color:var(--text-tertiary);">36氪 · 6月15日</div><div style="margin-top:4px; font-size:8px; color:#a5b4fc;">💡 开发者影响：多模型协作（非单模型依赖）正在成为应对出口管制的最佳实践</div><a href="https://36kr.com/p/3854354308961287" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
      <div class="sub-card"><div class="sub-tag" style="color:#a5b4fc;">香港 · 人民网</div><div class="sub-title">香港发布 HKGAI V3 大模型 + Agent Workshop：单次无干预运行 28 小时</div><div class="sub-desc">香港生成式人工智能研发中心发布 HKGAI V3 大模型，推出香港首个生产力级超级智能体 Agent Workshop。实现超 10 倍 Token 压缩效率、近百倍智能体无干预运行时长增长，单次稳定运行可达 28 小时。已与浪潮云、中国移动国际、联通国际、中国电信国际合作，向海外开放算力服务。</div><div style="margin-top:6px; font-size:8px; color:var(--text-tertiary);">人民网 · 6月4日</div><div style="margin-top:4px; font-size:8px; color:#a5b4fc;">💡 开发者影响：香港 AI 生态加速，Agent Workshop 可能成为出海算力新选择</div><a href="http://hm.people.com.cn/n1/2026/0604/c42272-40733968.html" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
      <div class="sub-card"><div class="sub-tag" style="color:#a5b4fc;">OpenAI · The Verge</div><div class="sub-title">"Chat is dead"——OpenAI 高管放话，ChatGPT 将改版为超级应用</div><div class="sub-desc">OpenAI 高管对《金融时报》表示"聊天已死"。代号"superapp"的 ChatGPT 大改版将在"数周内"推出，引导用户转向编程、图像生成和第三方合作伙伴应用。Codex 同步大升级：Sites（交互式企业工作空间）、Annotations（局部精确编辑）、6 个角色专属插件包（整合 62 个企业应用 + 110 项自动化技能）。</div><div style="margin-top:6px; font-size:8px; color:var(--text-tertiary);">The Verge/VentureBeat · 6月</div><div style="margin-top:4px; font-size:8px; color:#a5b4fc;">💡 开发者影响：ChatGPT 从对话工具转型应用平台，Codex 插件生态是新的开发者入口</div><a href="https://venturebeat.com/orchestration/openais-codex-update-lets-agents-build-interactive-enterprise-workspaces-via-sites-and-role-specific-plugins" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
    </div>
  </div>
  <div class="section-gap section-green" id="section-tools">
    <div class="section-head"><div class="section-line"></div><span class="section-label">工具 & 部署</span><span class="section-label-cn">Tools & Deploy</span></div>
    <div class="tool-row">
      <div class="tool-card"><div class="tool-icon">&#127760;</div><div class="tool-name">OpenAI Codex Sites</div><div class="tool-desc">将静态数据/文档一键转为交互式 Web 应用。无需前端开发，支持场景规划器、实时仪表盘。面向 Business/Enterprise 用户预览中。</div><span class="tool-badge badge-new">预览</span><a href="https://venturebeat.com/orchestration/openais-codex-update-lets-agents-build-interactive-enterprise-workspaces-via-sites-and-role-specific-plugins" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
      <div class="tool-card"><div class="tool-icon">&#128268;</div><div class="tool-name">OpenRouter Fusion API</div><div class="tool-desc">多模型协作 API：自动路由至最优模型组合，接近 Fable 5 水平，成本仅 40%。支持 Claude+GPT+Gemini 混合调用。</div><span class="tool-badge badge-new">平替</span><a href="https://36kr.com/p/3854354308961287" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
      <div class="tool-card"><div class="tool-icon">&#127981;</div><div class="tool-name">HKGAI Agent Workshop</div><div class="tool-desc">香港首个生产力级超级智能体。10 倍 Token 压缩，单次 28 小时无干预运行。浪潮云+三大运营商合作，海外算力开放。</div><span class="tool-badge badge-new">国产</span><a href="http://hm.people.com.cn/n1/2026/0604/c42272-40733968.html" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
    </div>
  </div>
  <div class="section-gap section-amber" id="section-policy">
    <div class="section-head"><div class="section-line"></div><span class="section-label">政策 & 合规</span><span class="section-label-cn">Policy & Compliance</span></div>
    <div class="sub-grid">
      <div class="sub-card"><div class="sub-tag" style="color:#fcd34d;">美国 · 6月15日</div><div class="sub-title">特朗普签署新版 AI 行政令：自愿审查+30 天压缩期，不设强制许可</div><div class="sub-desc">特朗普签署"促进先进 AI 创新与安全"行政令，构建政企自愿合作框架。对前沿模型不设强制许可或预先批准，但要求企业在发布前"自愿"向政府提供模型进行 30 天前置安全评估。设立 AI 网络安全信息交流中心。OpenAI、谷歌等企业高管表示支持。人民网转载中国军网报道。</div><div style="margin-top:6px; font-size:8px; color:var(--text-tertiary);">人民网/中国军网 · 6月15日</div><div style="margin-top:4px; font-size:8px; color:#fcd34d;">💡 开发者影响：美国 AI 监管走向"自愿框架"，与欧盟强监管路线形成对比</div><a href="http://military.people.com.cn/BIG5/n1/2026/0615/c1011-40740496.html" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
      <div class="sub-card"><div class="sub-tag" style="color:#fcd34d;">四川 · 6月8日</div><div class="sub-title">四川发布智能制造行动方案：2028 年建成 300+ 智能工厂</div><div class="sub-desc">四川省发布服务型制造创新发展行动方案，明确应用工业智能体、工业大模型、工业元宇宙等新技术。目标：到 2028 年软件首版次产品达 100 个以上，建设 300 个以上先进级智能工厂。地方政策从"鼓励"走向"量化目标"。</div><div style="margin-top:6px; font-size:8px; color:var(--text-tertiary);">人民网 · 6月8日</div><div style="margin-top:4px; font-size:8px; color:#fcd34d;">💡 开发者影响：四川 300+ 智能工厂计划释放大量工业 AI 需求</div><a href="http://sc.people.com.cn/GB/n2/2026/0608/c379470-41603800.html" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
    </div>
  </div>
  <div class="section-gap section-purple" id="section-paper">
    <div class="section-head"><div class="section-line"></div><span class="section-label">论文速递</span><span class="section-label-cn">Paper Spotlight</span></div>
    <div class="paper-spotlight">
      <div class="paper-header"><span class="paper-label">&#128218; 今日精选 · The Verge</span></div>
      <div class="paper-title">Apple 自研 Foundational Model：跑在 Nvidia 芯片上的"隐私优先"AI</div>
      <div class="paper-abstract">WWDC 2026 上苹果透露其 Private Cloud Compute 的底层架构：自研 Foundational Model 实际运行在 Google Cloud 的 Nvidia 硬件上。苹果与 Nvidia、Google、Intel 三方合作，实现了"隐私计算的硬件无关性"——模型训练和推理可以在不同厂商芯片上无缝迁移。这一架构为端侧 AI 到云端 AI 的隐私保护提供了新的技术范式。</div>
      <div class="paper-meta">The Verge · WWDC 2026 · 苹果 AI 架构首次公开</div>
      <div style="margin-top:6px; font-size:8px; color:#c4b5fd;">💡 开发者影响：苹果的"隐私计算硬件无关"架构可能成为 Core ML 后续版本的基础</div>
    </div>
  </div>
  <div class="section-gap section-cyan" id="section-cases">
    <div class="section-head"><div class="section-line"></div><span class="section-label">应用落地</span><span class="section-label-cn">Real-World AI</span></div>
    <div class="dual-cards">
      <div class="rank-card"><div class="rank-label" style="color:#67e8f9;">&#127981; 企业级 · VentureBeat</div><div style="font-size:14px; font-weight:500; color:var(--text-primary); margin-bottom:6px;">OpenAI Codex 企业版大升级：62 个应用 + 110 项技能，非开发者增速是工程师 3 倍</div><div style="font-size:10px; color:var(--text-secondary); line-height:1.5; margin-bottom:8px;">Codex 周活超 500 万，约 20% 非开发者且采用速度是工程师的 3 倍。6 个角色专属插件包覆盖数据分析（Snowflake）、创意生产（Figma）、销售（Salesforce）、产品设计、投行等场景。Sites 功能让非技术人员也能将数据文档一键转为交互式企业内部应用。</div><div style="font-size:8px; color:var(--text-tertiary);">VentureBeat · 6月</div><div style="margin-top:4px; font-size:8px; color:#67e8f9;">💡 开发者影响：Codex 从编程工具转型为全员生产力平台，插件生态是新的开发者机会</div><a href="https://venturebeat.com/orchestration/openais-codex-update-lets-agents-build-interactive-enterprise-workspaces-via-sites-and-role-specific-plugins" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
      <div class="rank-card"><div class="rank-label" style="color:#67e8f9;">&#127891; 深度分析 · 36氪</div><div style="font-size:14px; font-weight:500; color:var(--text-primary); margin-bottom:6px;">吴恩达信号解读：中国 AI 的机会在"执行权"，不在模型</div><div style="font-size:10px; color:var(--text-secondary); line-height:1.5; margin-bottom:8px;">36氪深度分析吴恩达最新观点：Agent 的商业化难点不在于模型能力，而在于企业是否愿意把部分业务执行权交给 AI。中国 AI 的优势在于场景丰富、数据量大、企业对效率提升的迫切需求——这些比模型能力领先几个月更重要。大厂 Agent 之争正沿四条主线演变：生产力场景、产品打通、Skill 生态、上下文积累。</div><div style="font-size:8px; color:var(--text-tertiary);">36氪 · 6月8日</div><div style="margin-top:4px; font-size:8px; color:#67e8f9;">💡 开发者影响：与其追逐最新模型，不如深耕 Agent 执行能力——能真正"干活"的 AI 才有商业价值</div><a href="https://www.36kr.com/p/3842692739054215" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
    </div>
  </div>
  <div class="section-gap section-amber" id="section-oss">
    <div class="section-head"><div class="section-line"></div><span class="section-label">开源热度</span><span class="section-label-cn">Open Source Pulse</span></div>
    <div class="dual-cards">
      <div class="rank-card"><div class="rank-label" style="color:#fcd34d;">&#128200; GitHub Trending — AI Top 5（W24-25）</div>
        <div class="rank-row"><span class="rank-num">1</span><span class="rank-name">mvanhorn/last30days-skill</span><span class="rank-stat rank-up">+12K/周</span></div><div class="rank-row"><span class="rank-num">2</span><span class="rank-name">chopratejas/headroom</span><span class="rank-stat rank-up">+10K/周</span></div><div class="rank-row"><span class="rank-num">3</span><span class="rank-name">Leonxlnx/taste-skill</span><span class="rank-stat rank-up">+8.7K/周</span></div><div class="rank-row"><span class="rank-num">4</span><span class="rank-name">addyosmani/agent-skills</span><span class="rank-stat rank-up">+8.3K/周</span></div><div class="rank-row"><span class="rank-num">5</span><span class="rank-name">apple/container</span><span class="rank-stat rank-up">+7.8K/周</span></div>
        <a href="https://github.com/trending?since=weekly" class="read-original" target="_blank" rel="noopener">查看完整榜单 <span class="read-original-arrow">→</span></a></div>
      <div class="rank-card"><div class="rank-label" style="color:#fcd34d;">&#128200; 趋势解读</div><div style="font-size:10px; color:var(--text-secondary); line-height:1.6;"><p><strong>Skills 生态成新爆款品类</strong> 至少 8 个 .claude/skills 项目登榜。mattpocock 月增 48K★，Skills 模块化是"AI 时代的 npm"。</p><p><strong>Token 压缩赛道火热</strong> headroom 6 种算法省 60-95% Token。Agent 上下文窗口需求的爆发式增长使压缩成为刚需。</p><p><strong>大厂密集开源</strong> 苹果 container、微软 markitdown(152K★)、NVIDIA SkillSpector 构成"安全+工具+容器"三位一体。</p><p style="margin-top:6px; color:#fcd34d;">💡 18 个项目周增 87K★——AI 开源正从"模型开源"进入"Agent 基础设施开源"时代</p></div></div>
    </div>
  </div>
  <div class="section-gap section-cyan" id="section-overseas">
    <div class="section-head"><div class="section-line"></div><span class="section-label">海外参考</span><span class="section-label-cn">Global Brief</span></div>
    <div class="sub-grid">
      <div class="sub-card"><div class="sub-tag" style="color:#67e8f9;">🌏 Apple · The Verge</div><div class="sub-title">Apple 自研模型跑在 Nvidia 芯片上——WWDC 2026 隐私架构首次公开</div><div class="sub-desc">WWDC 2026 上苹果透露：为满足欧盟 DMA 法规，自研 Foundational Model 实际运行在 Google Cloud 的 Nvidia 硬件上。与 Nvidia、Google、Intel 三方合作实现"隐私计算的硬件无关性"。Siri AI 英文版今年晚些推出，欧盟用户因 DMA 争议将延迟。</div><div style="margin-top:6px; font-size:8px; color:var(--text-tertiary);">The Verge · 6月</div><div style="margin-top:4px; font-size:8px; color:#67e8f9;">💡 开发者影响：苹果的"硬件无关隐私计算"可能成为行业新范式</div><a href="https://www.theverge.com/archives/ai-artificial-intelligence/2026/6/2" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
      <div class="sub-card"><div class="sub-tag" style="color:#67e8f9;">💬 芯片 · The Verge</div><div class="sub-title">Google 找 Intel 造 TPU：台积电产能不足，3 百万芯片转单</div><div class="sub-desc">The Verge 报道：台积电产能短缺迫使 Google 转向 Intel，后者将在 2028 年前为 Google 制造超 300 万颗 TPU。Nvidia 和 SK Hynix 也在测试 Intel 的制造技术。这标志着全球 AI 芯片供应链正在发生结构性重塑。</div><div style="margin-top:6px; font-size:8px; color:var(--text-tertiary);">The Verge · 6月</div><div style="margin-top:4px; font-size:8px; color:#67e8f9;">💡 开发者影响：AI 芯片从"台积电单极"走向"多极供应"，利好算力成本下降</div><a href="https://www.theverge.com/archives/ai-artificial-intelligence/2026/6/2" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
      <div class="sub-card"><div class="sub-tag" style="color:#67e8f9;">🏛️ 美国 · 人民网</div><div class="sub-title">特朗普签署 AI 行政令：自愿框架 + 30 天审查期，企业普遍支持</div><div class="sub-desc">美国新版 AI 行政令构建政企自愿合作框架，不设强制许可或预先批准。要求企业发布前沿模型前"自愿"提交 30 天安全评估，设立 AI 网络安全信息交流中心。与欧盟的强监管路线形成鲜明对比——"自愿 vs 强制"成为全球 AI 治理的两条路径。</div><div style="margin-top:6px; font-size:8px; color:var(--text-tertiary);">人民网 · 6月15日</div><div style="margin-top:4px; font-size:8px; color:#67e8f9;">💡 开发者影响：美国自愿框架下模型发布速度更快，但安全责任仍在企业</div><a href="http://military.people.com.cn/BIG5/n1/2026/0615/c1011-40740496.html" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
    </div>
  </div>'''

start = html.find('<div class="section-gap section-indigo" id="section-models">')
end = html.find('<footer class="footer">')
html = html[:start] + c + '\n' + html[end:]

now = datetime.datetime.now()
html = re.sub(r'<span class="hero-badge-text" id="editionLabel">.*?</span>', f'<span class="hero-badge-text" id="editionLabel">早间版 &#183; {now.strftime("%H:%M")} &#183; 清晨速递</span>', html)
html = re.sub(r'<p class="hero-date" id="dateLabel">.*?</p>', f'<p class="hero-date" id="dateLabel">{now.strftime("%Y年%m月%d日")} &#183; 星期二</p>', html)
html = re.sub(r'<p class="hero-updated" id="updatedLabel">.*?</p>', f'<p class="hero-updated" id="updatedLabel"><span class="hero-updated-dot"></span> 最后更新: {now.strftime("%Y-%m-%d %H:%M")} CST</p>', html)
tl = '阿里通义再失核心：首席科学家周靖人履新6天离职；Claude Fable5平替指南爆火：OpenRouter Fusion多模型协作成本仅40%；OpenAI高管称"Chat is dead"Codex升级Sites+62企业插件；香港HKGAI V3大模型发布Agent Workshop单次28小时无干预运行；特朗普签署AI行政令自愿框架30天审查；苹果WWDC自研模型跑在Nvidia芯片上；Google找Intel造TPU 300万颗芯片转单。'
html = re.sub(r'<span class="tldr-text" id="tldrContent">.*?</span>', f'<span class="tldr-text" id="tldrContent">{tl}</span>', html, flags=re.DOTALL)

with open('archive/2026-06-16-morning.html', 'w', encoding='utf-8') as f: f.write(html)
ph = html.count('"#" class="read-original')
print(f'Built: {len(html)}B | Placeholders: {ph}')
