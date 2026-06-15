#!/usr/bin/env python3
"""Build noon edition from curate source-pool search results."""
import re, datetime

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

models = '''  <div class="section-gap section-indigo" id="section-models">
    <div class="section-head">
      <div class="section-line"></div>
      <span class="section-label">大模型动态</span>
      <span class="section-label-cn">Models</span>
    </div>
    <div class="feature-card">
      <div class="card-row">
        <div class="card-body">
          <div class="card-tag" style="color:#6366f1;">HEADLINE</div>
          <div class="card-title">智谱 GLM-5.2 正式发布：百万上下文 + MIT 开源，港股暴涨超 30%</div>
          <div class="card-desc">6 月 15 日，智谱华章通过港交所公告正式推出旗舰大模型 GLM-5.2。1M 超长上下文窗口，MIT 协议开源，API 和权重将于下周上线。受 Anthropic Fable 5/Mythos 5 被美国出口管制强制下线的替代需求刺激，智谱港股当日暴涨超 30%，带动联想、英诺赛科等 AI 产业链集体走高。东方证券指出 GLM 系列正沿"代码增强→Agent 化→长时任务→自主操作系统"路径演进。此前 GLM-5.1 已在 SWE-Bench Pro 上以 58.4 分超越 GPT-5.4(57.7) 和 Claude Opus 4.6(57.3)。</div>
          <div class="card-meta"><span>36氪</span><span>&#183;</span><span>6月15日</span><span>&#183;</span><span class="card-meta-link">多源报道</span><span>&#183;</span><a href="https://36kr.com/newsflashes/3853947992921094" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
          <div style="margin-top:8px; font-size:9px; color:#a5b4fc;">💡 开发者影响：MIT 开源百万上下文模型即将可用，国产替代窗口正式打开，港股市场已用真金白银投票</div>
        </div>
        <div class="card-icon">&#9889;</div>
      </div>
    </div>
    <div class="sub-grid">
      <div class="sub-card">
        <div class="sub-tag" style="color:#a5b4fc;">深度调查 · 机器之心</div>
        <div class="sub-title">巴西「黑马模型」Rio 3.5 一夜翻车：60% Nex + 40% 千问缝合，移除提示词后 79% 概率自称 Nex</div>
        <div class="sub-desc">巴西里约热内卢市政府旗下 IT 公司推出的 Rio 3.5 397B 一度刷屏，号称超越 Qwen 3.7 Plus 斩获多项 SOTA。不到 24 小时，上海创智学院 Nex-AGI 团队通过数学分析揭穿——Rio 3.5 ≈ 0.6×Nex N2 Pro + 0.4×Qwen 3.5，属于典型的模型合并（Model Merge）套壳，且未署名校准。移除系统提示词后 79% 概率自称 Nex 而非 Rio。机器之心评论：开源社区署名和致谢规范亟待建立。</div>
        <div style="margin-top:6px; font-size:8px; color:var(--text-tertiary);">机器之心 · 6月15日</div>
        <div style="margin-top:4px; font-size:8px; color:#a5b4fc;">💡 开发者影响：使用开源模型需验证来源，权重拼接难逃数学检测，模型溯源工具将成为必备</div>
        <a href="https://www.jiqizhixin.com/articles/2026-06-15-2" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a>
      </div>
    </div>
  </div>'''

tools = '''  <div class="section-gap section-green" id="section-tools">
    <div class="section-head">
      <div class="section-line"></div>
      <span class="section-label">工具 & 部署</span>
      <span class="section-label-cn">Tools & Deploy</span>
    </div>
    <div class="tool-row">
      <div class="tool-card">
        <div class="tool-icon">&#128187;</div>
        <div class="tool-name">小米 MiMo Code</div>
        <div class="tool-desc">MIT 协议开源的终端原生 AI 编程助手。持久记忆系统（SQLite + 多层文件）解决长会话"失忆"痛点，Compose 编排模式支持 200+ 步骤任务。SWE-Bench Verified 82% vs Claude Code 79%。一键安装：curl -fsSL https://mimo.xiaomi.com/install | bash。内置限时免费 MiMo-V2.5（310B MoE）。</div>
        <span class="tool-badge badge-new">MIT 开源</span>
        <a href="https://venturebeat.com/technology/xiaomis-new-open-source-agentic-ai-coding-harness-mimo-code-beats-claude-code-at-ultra-long-200-step-tasks" class="read-original" target="_blank" rel="noopener" style="display:block;">阅读原文 <span class="read-original-arrow">→</span></a>
      </div>
      <div class="tool-card">
        <div class="tool-icon">&#127942;</div>
        <div class="tool-name">Cohere Command A+</div>
        <div class="tool-desc">Cohere 首个完全 Apache 2.0 许可的开源模型。218B 参数 Sparse MoE（25B 激活），128K 上下文。核心突破：无损 4-bit 量化 + 原生引文生成 + 多模态文档处理。可在单张 NVIDIA B200 或双 H100 上运行，专为"主权 AI"场景设计——企业可完全审计和定制。</div>
        <span class="tool-badge badge-new">Apache 2.0</span>
        <a href="https://venturebeat.com/technology/cohere-cracks-lossless-quantization-and-native-citations-with-first-full-apache-2-0-licensed-open-model-command-a" class="read-original" target="_blank" rel="noopener" style="display:block;">阅读原文 <span class="read-original-arrow">→</span></a>
      </div>
    </div>
  </div>'''

policy = '''  <div class="section-gap section-amber" id="section-policy">
    <div class="section-head">
      <div class="section-line"></div>
      <span class="section-label">政策 & 合规</span>
      <span class="section-label-cn">Policy & Compliance</span>
    </div>
    <div class="sub-grid">
      <div class="sub-card">
        <div class="sub-tag" style="color:#fcd34d;">重磅法规 · 7月15日施行</div>
        <div class="sub-title">五部门联合发布《人工智能拟人化互动服务管理暂行办法》，算法备案 + 安全评估制度化</div>
        <div class="sub-desc">国家网信办、发改委、工信部、公安部、市场监管总局五部门联合公布该办法，将于 2026 年 7 月 15 日正式施行。核心制度设计：对 AI 拟人化互动服务实行包容审慎和分类分级监管，明确安全评估、算法备案、AI 沙箱安全服务平台建设三大制度支柱。覆盖国家安全、未成年人保护、老年人权益保护及个人信息保护四大领域。同期，中央网信办 6 月 12 日上线「涉 AI 应用乱象举报专区」，将"未按规定履行大模型备案登记义务"列为首要举报受理项。</div>
        <div style="margin-top:6px; font-size:8px; color:var(--text-tertiary);">人民日报 · 4月13日 / 人民网 · 6月12日</div>
        <div style="margin-top:4px; font-size:8px; color:#fcd34d;">💡 开发者影响：7月15日前须完成算法备案和安全评估，拟人化 AI 产品合规成本将显著上升</div>
        <a href="http://society.people.com.cn/n1/2026/0612/c1008-40739344.html" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a>
      </div>
    </div>
  </div>'''

cases = '''  <div class="section-gap section-cyan" id="section-cases">
    <div class="section-head">
      <div class="section-line"></div>
      <span class="section-label">应用落地</span>
      <span class="section-label-cn">Real-World AI</span>
    </div>
    <div class="dual-cards">
      <div class="rank-card">
        <div class="rank-label" style="color:#67e8f9;">&#127981; 超级入口之战 · 36氪深度</div>
        <div style="font-size:14px; font-weight:500; color:var(--text-primary); margin-bottom:6px;">微信 AI Agent 生态七天密集接入：刘炽平定调「AgentOS」，14 亿用户入口重构</div>
        <div style="font-size:10px; color:var(--text-secondary); line-height:1.5; margin-bottom:8px;">6 月官宣后一周内，美团、京东、得物、五大手机厂商密集接入微信 AI Agent。腾讯总裁刘炽平内部定调"AgentOS"——用 AI 重构 14 亿用户入口，用户一句话即可完成叫车、点外卖、订酒店。但 36氪深度分析指出仍需迈过三道坎：算力成本由谁承担（日均千万级 Agent 调用）、平台利益如何分配（京东小程序同比+18.3% 但佣金模式待定）、推荐中立性与商业变现的根本矛盾。同期腾讯云发布 ADP 4.0 智能体开发平台，伊利导购智能体点击率提升 15.7%，华住"华小AI"落地上万家门店。</div>
        <div style="font-size:8px; color:var(--text-tertiary);">36氪 · 6月</div>
        <div style="margin-top:4px; font-size:8px; color:#67e8f9;">💡 开发者影响：微信 AI 生态催生大量小程序 Agent 开发机会，但需关注成本分摊和平台规则</div>
        <a href="https://36kr.com/p/3845619279870597" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a>
      </div>
    </div>
  </div>'''

oss = '''  <div class="section-gap section-amber" id="section-oss">
    <div class="section-head">
      <div class="section-line"></div>
      <span class="section-label">开源热度</span>
      <span class="section-label-cn">Open Source Pulse</span>
    </div>
    <div class="dual-cards">
      <div class="rank-card">
        <div class="rank-label" style="color:#fcd34d;">&#128200; GitHub Trending — AI 领域 Top 5（2026 W24-25）</div>
        <div class="rank-row"><span class="rank-num">1</span><span class="rank-name">mattpocock/skills</span><span class="rank-stat rank-up">+71K stars/月</span></div>
        <div class="rank-row"><span class="rank-num">2</span><span class="rank-name">mvanhorn/last30days-skill</span><span class="rank-stat rank-up">+12K stars/周</span></div>
        <div class="rank-row"><span class="rank-num">3</span><span class="rank-name">chopratejas/headroom</span><span class="rank-stat rank-up">+10K stars/周</span></div>
        <div class="rank-row"><span class="rank-num">4</span><span class="rank-name">addyosmani/agent-skills</span><span class="rank-stat rank-up">+9.3K stars/周</span></div>
        <div class="rank-row"><span class="rank-num">5</span><span class="rank-name">NVIDIA/SkillSpector</span><span class="rank-stat rank-up">+3.6K stars/周</span></div>
        <a href="https://github.com/trending?since=weekly" class="read-original" target="_blank" rel="noopener">查看完整榜单 <span class="read-original-arrow">→</span></a>
      </div>
      <div class="rank-card">
        <div class="rank-label" style="color:#fcd34d;">&#128200; 趋势解读</div>
        <div style="font-size:10px; color:var(--text-secondary); line-height:1.6;">
          <p><strong>Claude Skills 霸榜半壁江山</strong> mattpocock/skills 月增 7.1 万星，Karpathy Skills 总星超 16 万。Skills 模块化被类比为"AI 时代的 npm 包"——不再是堆 Prompt，而是构建可组合、可复用的技能模块。</p>
          <p><strong>Token 压缩成刚需</strong> headroom 6 种算法节省 60-95% Token，背景是 GitHub Copilot 刚切换为按 Token 计费，成本意识空前。</p>
          <p><strong>Agent 安全从可选变为标配</strong> NVIDIA SkillSpector 覆盖 16 类 64 种漏洞模式，微软 MXC 提供策略驱动沙箱隔离。6 月发生的 Agent 误删用户邮件事故加速了这一趋势。</p>
          <p style="margin-top:6px; color:#fcd34d;">💡 Skills 生态 + Token 优化 + Agent 安全 = 2026 年 6 月三大技术主线</p>
        </div>
      </div>
    </div>
  </div>'''

# Splice
start = html.find('<div class="section-gap section-indigo" id="section-models">')
end = html.find('<footer class="footer">')
html = html[:start] + models + '\n' + tools + '\n' + policy + '\n' + cases + '\n' + oss + '\n' + html[end:]

# Update hero
now = datetime.datetime.now()
html = re.sub(
    r'<span class="hero-badge-text" id="editionLabel">.*?</span>',
    f'<span class="hero-badge-text" id="editionLabel">午间版 &#183; {now.strftime("%H:%M")} &#183; 增量更新</span>',
    html
)
html = re.sub(
    r'<p class="hero-date" id="dateLabel">.*?</p>',
    f'<p class="hero-date" id="dateLabel">{now.strftime("%Y年%m月%d日")} &#183; 星期一</p>',
    html
)
html = re.sub(
    r'<p class="hero-updated" id="updatedLabel">.*?</p>',
    f'<p class="hero-updated" id="updatedLabel"><span class="hero-updated-dot"></span> 最后更新: {now.strftime("%Y-%m-%d %H:%M")} CST</p>',
    html
)
html = re.sub(
    r'<span class="tldr-text" id="tldrContent">.*?</span>',
    f'<span class="tldr-text" id="tldrContent">智谱GLM-5.2正式发布百万上下文+MIT开源，港股暴涨30%国产替代窗口打开；巴西Rio 3.5套壳翻车，机器之心深挖：60%Nex+40%千问缝合；小米MiMo Code开源MIT协议SWE-Bench 82%超Claude Code；Cohere Command A+首个Apache2.0全开源无损量化+引文生成；五部门AI拟人化管理办法7月施行；微信AgentOS重构14亿用户入口。</span>',
    html, flags=re.DOTALL
)

# Footer
html = html.replace('"The best way to predict the future is to invent it."', '"AI 不会取代人类，但会用 AI 的人类会取代不会用 AI 的人类。"')
html = html.replace('Alan Kay', '李开复')

with open('archive/2026-06-15-noon.html', 'w', encoding='utf-8') as f:
    f.write(html)
print(f'Built: {len(html)} bytes')
print('Placeholders:', html.count('href="#" class="read-original'))
