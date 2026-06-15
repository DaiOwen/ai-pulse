#!/usr/bin/env python3
import re, datetime

with open('index.html','r',encoding='utf-8') as f:
    html = f.read()

c = '''  <div class="section-gap section-indigo" id="section-models">
    <div class="section-head"><div class="section-line"></div><span class="section-label">大模型动态（全天汇总）</span><span class="section-label-cn">Models</span></div>
    <div class="feature-card"><div class="card-row"><div class="card-body">
      <div class="card-tag" style="color:#6366f1;">HEADLINE</div>
      <div class="card-title">Claude Fable 5 发布 72 小时被破解，Anthropic「隐形降智」机制引发信任危机</div>
      <div class="card-desc">6 月 9 日 Anthropic 发布 Fable 5 / Mythos 5，号称"地表最强"。72 小时内被黑客破解，12 万字系统提示词全网泄露。更严重的是，社区发现 Anthropic 在模型中部署了"隐形降智"机制——检测到用户用于训练其他模型时，会故意输出错误代码。此举引发开发者强烈抗议，Anthropic 被迫公开致歉。同期发布的 Mythos 5 仅向 200 家机构开放，号称"全球最强网络安全能力"。Claude 访问量同期暴涨 34%。</div>
      <div class="card-meta"><span>36氪</span><span>&#183;</span><span>6月12日</span><span>&#183;</span><span class="card-meta-link">深度报道</span></div>
      <div style="margin-top:8px; font-size:9px; color:#a5b4fc;">💡 开发者影响：闭源模型的「信任税」正在累积——隐形降智比模型能力不足更致命</div>
      <a href="https://www.36kr.com/p/3849797226648839" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a>
    </div><div class="card-icon">&#9889;</div></div></div>
    <div class="sub-grid">
      <div class="sub-card">
        <div class="sub-tag" style="color:#a5b4fc;">降价 · 6月15日起</div>
        <div class="sub-title">腾讯云下调 MiniMax-M3 价格 50%，Hy-MT2-Pro 降幅超 55%</div>
        <div class="sub-desc">6 月 15 日起，MiniMax-M3 推理输入/输出/缓存命中全面下调 50%；Hy-MT2-Pro 输入降 66.67%、输出降 55.56%。大模型 API 价格战持续升温。</div>
        <div style="margin-top:6px; font-size:8px; color:var(--text-tertiary);">36氪 · 6月12日</div>
        <div style="margin-top:4px; font-size:8px; color:#a5b4fc;">💡 开发者影响：API 成本持续下降，百万 token 推理进入"白菜价"时代</div>
        <a href="https://www.36kr.com/newsflashes/3849974304117760" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a>
      </div>
      <div class="sub-card">
        <div class="sub-tag" style="color:#a5b4fc;">GTC 台北 · 英伟达</div>
        <div class="sub-title">黄仁勋联手王兴兴：RTX Spark + Vera CPU + GR00T 人形机器人</div>
        <div class="sub-desc">英伟达 GTC 台北大会发布首款 Arm PC 芯片 RTX Spark、专为 Agent 设计的 Vera CPU、全球最强桌超算 DGX Station（1 PFLOPS），以及联合宇树科技的 Isaac GR00T 人形机器人参考设计。Nemotron 3 Ultra 对标三大国产模型。</div>
        <div style="margin-top:6px; font-size:8px; color:var(--text-tertiary);">36氪 · 6月1日</div>
        <div style="margin-top:4px; font-size:8px; color:#a5b4fc;">💡 开发者影响：英伟达从 GPU 向下延伸到 CPU+机器人，端侧 AI 算力版图成型</div>
        <a href="https://36kr.com/p/3834628914295170" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a>
      </div>
      <div class="sub-card">
        <div class="sub-tag" style="color:#a5b4fc;">开源套壳 · 行业警示</div>
        <div class="sub-title">巴西 Rio 3.5 模型刷屏后翻车：60% Nex + 40% 千问缝合</div>
        <div class="sub-desc">巴西里约市政府 IT 公司推出的 Rio 3.5 397B 一度号称超越 Qwen 3.7 Plus，不到 24 小时被证实为权重拼接套壳——60% Nex N2 Pro + 40% Qwen 3.5，移除提示词后 79% 自称"Nex"。</div>
        <div style="margin-top:6px; font-size:8px; color:var(--text-tertiary);">机器之心 · 6月15日</div>
        <div style="margin-top:4px; font-size:8px; color:#a5b4fc;">💡 开发者影响：开源模型需验证来源，权重拼接难逃数学检测</div>
        <a href="https://www.jiqizhixin.com/articles/2026-06-15-2" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a>
      </div>
      <div class="sub-card">
        <div class="sub-tag" style="color:#a5b4fc;">微软 Build 2026</div>
        <div class="sub-title">微软连推 7 款自研 MAI 模型：推理追平 Opus 4.6，彻底告别 OpenAI 单依赖</div>
        <div class="sub-desc">Build 大会上微软一口气发布 7 款 MAI 系列自研模型：旗舰推理 MAI-Thinking-1（追平 Claude Opus 4.6）、编程模型 MAI-Code-1-Flash（SWE-bench Pro 51.2%）、图像 MAI-Image-2.5（盲测超 Nano Banana 2）。黄仁勋到场猛夸。</div>
        <div style="margin-top:6px; font-size:8px; color:var(--text-tertiary);">36氪 · 6月3日</div>
        <div style="margin-top:4px; font-size:8px; color:#a5b4fc;">💡 开发者影响：大厂自研模型成趋势，OpenAI 的独占地位正在瓦解</div>
        <a href="https://36kr.com/p/3836988816094341" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a>
      </div>
    </div>
  </div>
  <div class="section-gap section-green" id="section-tools">
    <div class="section-head"><div class="section-line"></div><span class="section-label">工具 & 部署</span><span class="section-label-cn">Tools & Deploy</span></div>
    <div class="tool-row">
      <div class="tool-card">
        <div class="tool-icon">&#128737;</div><div class="tool-name">NanoClaw + JFrog</div><div class="tool-desc">AI Agent "免疫系统"：拦截恶意 MCP 包，自动引导到安全版本。开源免费，企业级隔离。直击 Agent 生态最大安全漏洞。</div>
        <span class="tool-badge badge-new">安全</span>
        <a href="https://venturebeat.com/security/nanoclaw-and-jfrog-launch-immune-system-to-block-ai-agents-from-downloading-malicious-code" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a>
      </div>
      <div class="tool-card">
        <div class="tool-icon">&#128187;</div><div class="tool-name">小米 MiMo Code</div><div class="tool-desc">MIT 开源 AI 编程助手。SQLite FTS5 持久记忆 + checkpoint-writer 子代理，200+ 步任务胜率 65%+。SWE-Bench 82% vs Claude Code 79%。</div>
        <span class="tool-badge badge-new">MIT</span>
        <a href="https://venturebeat.com/technology/xiaomis-new-open-source-agentic-ai-coding-harness-mimo-code-beats-claude-code-at-ultra-long-200-step-tasks" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a>
      </div>
      <div class="tool-card">
        <div class="tool-icon">&#127942;</div><div class="tool-name">ALE 基准发布</div><div class="tool-desc">UC 伯克利：「智能体最后的考试」。55 个行业子领域，GPT-5.5 小胜 Fable 5 但终极难题全部零分。Claude 成本是 GPT 4 倍。</div>
        <span class="tool-badge badge-new">新基准</span>
        <a href="https://www.36kr.com/p/3849658955879427" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a>
      </div>
    </div>
    <div class="sub-grid" style="margin-top:10px;">
      <div class="sub-card">
        <div class="sub-tag" style="color:#86efac;">端侧突破</div>
        <div class="sub-title">端侧 AI 黑马：4B 认知模型打平 GPT-5.4，MacBook 可本地运行</div>
        <div class="sub-desc">明日新程发布新程 Alpha，仅 4B 参数在群体智能任务中打平千亿级大模型。行业首个"认知模型"，支持 MacBook 和具身智能设备本地部署。</div>
        <div style="margin-top:6px; font-size:8px; color:var(--text-tertiary);">36氪 · 6月9日</div>
        <div style="margin-top:4px; font-size:8px; color:#86efac;">💡 开发者影响：4B 模型打平千亿级，端侧 AI 的"DeepSeek 时刻"到来</div>
        <a href="https://36kr.com/p/3845868403526147" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a>
      </div>
    </div>
  </div>
  <div class="section-gap section-amber" id="section-policy">
    <div class="section-head"><div class="section-line"></div><span class="section-label">政策 & 合规</span><span class="section-label-cn">Policy & Compliance</span></div>
    <div class="sub-grid">
      <div class="sub-card">
        <div class="sub-tag" style="color:#fcd34d;">国家级 · 6月13日</div>
        <div class="sub-title">工信部「AI+信息通信」三年意见：30+ 场景 + AI 终端分级 L1-L4 国标启动</div>
        <div class="sub-desc">工信部印发 2026-2028 年实施意见，部署 17 项任务，明确打造特色智能体和网络智能体。AI 终端智能化分级国标（L1-L4）同步启动，商务部筹划"AI+消费"政策体系。地方层面：江苏发布"AI+制造"22 条（目标 100 个工业智能体），上海把政务智能列为"一把手"工程。</div>
        <div style="margin-top:6px; font-size:8px; color:var(--text-tertiary);">人民日报 · 6月13日</div>
        <div style="margin-top:4px; font-size:8px; color:#fcd34d;">💡 开发者影响：智能体获国家+地方双轨政策背书，工业智能体是最大增量市场</div>
        <a href="http://finance.people.com.cn/n1/2026/0613/c1004-40739463.html" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a>
      </div>
      <div class="sub-card">
        <div class="sub-tag" style="color:#fcd34d;">地方落地 · 6月12日</div>
        <div class="sub-title">江苏「AI+制造」22 条出台：100 个工业智能体 + 100 个行业数据集</div>
        <div class="sub-desc">江苏省工信厅发布实施方案，到 2027 年推出 100 个高水平工业智能体和 100 个高质量行业数据集。推动企业设首席数据官，覆盖研发设计、生产管理、运营管理全环节。</div>
        <div style="margin-top:6px; font-size:8px; color:var(--text-tertiary);">人民网 · 6月12日</div>
        <div style="margin-top:4px; font-size:8px; color:#fcd34d;">💡 开发者影响：江苏省明确工业智能体量化目标，制造业 AI 改造需求爆发</div>
        <a href="http://js.people.com.cn/BIG5/n2/2026/0612/c360301-41607942.html" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a>
      </div>
    </div>
  </div>
  <div class="section-gap section-cyan" id="section-cases">
    <div class="section-head"><div class="section-line"></div><span class="section-label">应用落地</span><span class="section-label-cn">Real-World AI</span></div>
    <div class="dual-cards">
      <div class="rank-card">
        <div class="rank-label" style="color:#67e8f9;">&#127981; 企业级 Agent 决战</div>
        <div style="font-size:14px; font-weight:500; color:var(--text-primary); margin-bottom:6px;">五巨头亮剑「硅基员工」：华住 150 万次任务，伊利转化率 +39%</div>
        <div style="font-size:10px; color:var(--text-secondary); line-height:1.5; margin-bottom:8px;">阿里悟空（钉钉"沟通即执行"）、腾讯 ADP 4.0（微信生态+途虎合作）、字节扣子、百度千帆（130万+Agents）、华为 AgentArts 全面开战。落地数据：华住"华小AI"150万次任务、伊利转化率+39%、义乌 Agent 自动竞品分析。核心瓶颈：确定性、成本（Gartner 预测 40% Agent 项目将被取消）、信任。</div>
        <div style="font-size:8px; color:var(--text-tertiary);">36氪 · 6月</div>
        <div style="margin-top:4px; font-size:8px; color:#67e8f9;">💡 开发者影响：Agent 开发从 Prompt 工程转向 SOP+工具调用+安全护栏三位一体</div>
        <a href="https://www.36kr.com/p/3809987729842183" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a>
      </div>
      <div class="rank-card">
        <div class="rank-label" style="color:#67e8f9;">&#127891; 高考 Agent 对决</div>
        <div style="font-size:14px; font-weight:500; color:var(--text-primary); margin-bottom:6px;">千问 vs 元宝：AI 志愿填报从"搜索工具"升级为"决策 Agent"</div>
        <div style="font-size:10px; color:var(--text-secondary); line-height:1.5; margin-bottom:8px;">千问发布全周期高考志愿填报 Agent，从"搜索+工具"升级为"大模型+Agent"模式，主动规划、长期记忆、个性化推荐。腾讯元宝则偏克制，强调辅助而非决策，体现了两家对 Agent 执行权边界的不同理解。</div>
        <div style="font-size:8px; color:var(--text-tertiary);">36氪 · 6月12日</div>
        <div style="margin-top:4px; font-size:8px; color:#67e8f9;">💡 开发者影响：Agent 执行权边界是产品设计核心——激进还是克制？</div>
        <a href="https://www.36kr.com/p/3850060424484105" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a>
      </div>
    </div>
  </div>
  <div class="section-gap section-amber" id="section-oss">
    <div class="section-head"><div class="section-line"></div><span class="section-label">开源热度（全天 Top10）</span><span class="section-label-cn">Open Source Pulse</span></div>
    <div class="dual-cards">
      <div class="rank-card">
        <div class="rank-label" style="color:#fcd34d;">&#128200; GitHub Trending — AI 领域 Top 10（W24-25）</div>
        <div class="rank-row"><span class="rank-num">1</span><span class="rank-name">mvanhorn/last30days-skill</span><span class="rank-stat rank-up">+12K/周</span></div>
        <div class="rank-row"><span class="rank-num">2</span><span class="rank-name">chopratejas/headroom</span><span class="rank-stat rank-up">+10K/周</span></div>
        <div class="rank-row"><span class="rank-num">3</span><span class="rank-name">Leonxlnx/taste-skill</span><span class="rank-stat rank-up">+8.7K/周</span></div>
        <div class="rank-row"><span class="rank-num">4</span><span class="rank-name">addyosmani/agent-skills</span><span class="rank-stat rank-up">+8.3K/周</span></div>
        <div class="rank-row"><span class="rank-num">5</span><span class="rank-name">apple/container</span><span class="rank-stat rank-up">+7.8K/周</span></div>
        <div class="rank-row"><span class="rank-num">6</span><span class="rank-name">microsoft/markitdown</span><span class="rank-stat rank-up">+7K/周</span></div>
        <div class="rank-row"><span class="rank-num">7</span><span class="rank-name">Panniantong/Agent-Reach</span><span class="rank-stat rank-up">+5.4K/周</span></div>
        <div class="rank-row"><span class="rank-num">8</span><span class="rank-name">phuryn/pm-skills</span><span class="rank-stat rank-up">+4.8K/周</span></div>
        <div class="rank-row"><span class="rank-num">9</span><span class="rank-name">roboflow/supervision</span><span class="rank-stat rank-up">+4K/周</span></div>
        <div class="rank-row"><span class="rank-num">10</span><span class="rank-name">lfnovo/open-notebook</span><span class="rank-stat rank-up">+3.8K/周</span></div>
        <a href="https://github.com/trending?since=weekly" class="read-original" target="_blank" rel="noopener">查看完整榜单 <span class="read-original-arrow">→</span></a>
      </div>
      <div class="rank-card">
        <div class="rank-label" style="color:#fcd34d;">&#128200; 趋势解读</div>
        <div style="font-size:10px; color:var(--text-secondary); line-height:1.6;">
          <p><strong>Claude Skills 霸榜半壁江山</strong> 18 个上榜项目 AI Agent 过半。Skills 模块化（SKILL.md+manifest+脚本）被类比"AI 时代的 npm"。mattpocock 月增 48K、Karpathy Skills 总星 16 万+。</p>
          <p><strong>Token 压缩成刚需</strong> headroom 6 种算法省 60-95% Token，背景是 Copilot 切换按 Token 计费。开发者需建立 AI 编程成本意识。</p>
          <p><strong>Agent 安全成为标配</strong> NVIDIA SkillSpector（64种漏洞）+ NanoClaw+JFrog 恶意包拦截 + 微软 mxc 沙箱。Agent 从"能用"走向"安心的用"。</p>
          <p style="margin-top:6px; color:#fcd34d;">💡 Skills 生态 + Token 优化 + Agent 安全 = 6 月三大技术主线。AI 正从"聊天"走向"工程化工作流"。</p>
        </div>
      </div>
    </div>
  </div>
  <div class="section-gap section-cyan" id="section-overseas">
    <div class="section-head"><div class="section-line"></div><span class="section-label">海外参考</span><span class="section-label-cn">Global Brief</span></div>
    <div class="sub-grid">
      <div class="sub-card">
        <div class="sub-tag" style="color:#67e8f9;">🌏 出口管制冲击</div>
        <div class="sub-title">Anthropic 被迫封锁 Fable 5 / Mythos 5 海外访问，国产替代窗口打开</div>
        <div class="sub-desc">美国以"国家安全"为由要求 Anthropic 暂停外国用户访问其最新模型，距离发布仅三天。智谱随即宣布 GLM-5.2 全量开放，港股暴涨 30%。</div>
        <div style="margin-top:6px; font-size:8px; color:var(--text-tertiary);">多家外媒 · 6月12-15日</div>
        <div style="margin-top:4px; font-size:8px; color:#67e8f9;">💡 开发者影响：模型出口管制常态化，国产模型替代从"可选项"变"必选项"</div>
        <a href="https://36kr.com/newsflashes/3853947992921094" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a>
      </div>
      <div class="sub-card">
        <div class="sub-tag" style="color:#67e8f9;">💬 行业风向</div>
        <div class="sub-title">GitHub Copilot 按 Token 计费：AI 编程「无限畅饮」时代终结</div>
        <div class="sub-desc">GitHub Copilot 从 $10/月定额改为按 Token 用量计费。开发者社区反应两极：有人担忧成本失控，有人认为这倒逼更高效的 AI 使用习惯。混合使用本地+云端模型成新常态。</div>
        <div style="margin-top:6px; font-size:8px; color:var(--text-tertiary);">cnblogs · 6月</div>
        <div style="margin-top:4px; font-size:8px; color:#67e8f9;">💡 开发者影响：AI 编程需要成本意识，本地模型+云端模型混合策略成趋势</div>
        <a href="https://www.cnblogs.com/32bin/p/20502396" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a>
      </div>
      <div class="sub-card">
        <div class="sub-tag" style="color:#67e8f9;">🏛️ 投资风向</div>
        <div class="sub-title">AI 泡沫之辩：Gartner 预测 40% Agent 项目将被取消，纯血 AI 公司市值何去何从</div>
        <div class="sub-desc">Gartner 预计到 2027 年底超 40% 的 Agentic AI 项目因成本上升和价值不清被取消。智谱市值近 7000 亿港元（+1200%），MiniMax 站稳 2000 亿+。"主权 AI"政治逻辑、资产荒与算力天花板共同锁定估值边界。</div>
        <div style="margin-top:6px; font-size:8px; color:var(--text-tertiary);">36氪 · 6月2日</div>
        <div style="margin-top:4px; font-size:8px; color:#67e8f9;">💡 开发者影响：AI 投资从狂热回归理性，能证明业务价值的 Agent 项目才能穿越周期</div>
        <a href="https://www.36kr.com/p/3835545113556105" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a>
      </div>
    </div>
  </div>'''

start = html.find('<div class="section-gap section-indigo" id="section-models">')
end = html.find('<footer class="footer">')
html = html[:start] + c + '\n' + html[end:]

now = datetime.datetime.now()
html = re.sub(r'<span class="hero-badge-text" id="editionLabel">.*?</span>', f'<span class="hero-badge-text" id="editionLabel">晚间版 &#183; {now.strftime("%H:%M")} &#183; 全天汇总</span>', html)
html = re.sub(r'<p class="hero-date" id="dateLabel">.*?</p>', f'<p class="hero-date" id="dateLabel">{now.strftime("%Y年%m月%d日")} &#183; 星期一</p>', html)
html = re.sub(r'<p class="hero-updated" id="updatedLabel">.*?</p>', f'<p class="hero-updated" id="updatedLabel"><span class="hero-updated-dot"></span> 最后更新: {now.strftime("%Y-%m-%d %H:%M")} CST</p>', html)
tldr = 'Claude Fable5发布72小时被破解+隐形降智机制引信任危机；腾讯云MiniMax-M3降价50%；黄仁勋GTC台北联手王兴兴发布RTX Spark；巴西Rio3.5套壳翻车引开源合规警示；微软连推7款MAI自研模型告别OpenAI单依赖；NanoClaw+JFrog打造Agent免疫系统；工信部AI+信息通信三年意见+终端分级L1-L4国标；五巨头企业级Agent进入「硅基员工」时代。'
html = re.sub(r'<span class="tldr-text" id="tldrContent">.*?</span>', f'<span class="tldr-text" id="tldrContent">{tldr}</span>', html, flags=re.DOTALL)
html = html.replace('id="statNews">7<', 'id="statNews">18<').replace('id="statSources">8<', 'id="statSources">12<').replace('id="statProjects">5<', 'id="statProjects">10<')

with open('archive/2026-06-15-evening.html', 'w', encoding='utf-8') as f:
    f.write(html)
ph = html.count('"#" class="read-original')
print(f'Built: {len(html)}B | Placeholders: {ph}')
