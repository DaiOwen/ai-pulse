#!/usr/bin/env python3
import re, datetime

with open('index.html','r',encoding='utf-8') as f:
    html = f.read()

c = '''  <div class="section-gap section-indigo" id="section-models">
    <div class="section-head"><div class="section-line"></div><span class="section-label">大模型动态（全天汇总）</span><span class="section-label-cn">Models</span></div>
    <div class="feature-card"><div class="card-row"><div class="card-body">
      <div class="card-tag" style="color:#6366f1;">HEADLINE</div>
      <div class="card-title">Anthropic 全球停用 Claude Fable 5 / Mythos 5：AI 史上第一次商业模型被政府强制召回</div>
      <div class="card-desc">6 月 13 日，上线仅 72 小时的 Claude Fable 5 和 Mythos 5 遭美国政府引用国家安全权限发布出口管制指令，要求 Anthropic 全球禁用外籍人士对这两款模型的访问。被业界称为"AI 史上第一次商业大模型被政府强制召回"。此前 Anthropic 已在模型中秘密部署"反蒸馏护栏"——检测到用于训练其他模型时故意输出错误代码——引发开发者强烈抗议后被迫公开并回退。The Verge 评论：Anthropic 此举暴露了闭源模型"信任税"的结构性问题。</div>
      <div class="card-meta"><span>36氪</span><span>&#183;</span><span>6月13日</span><span>&#183;</span><span class="card-meta-link">多源报道</span></div>
      <div style="margin-top:8px; font-size:9px; color:#a5b4fc;">💡 开发者影响：模型出口管制从"可能性"变成"现实"，国产替代从可选项升级为必选项</div>
      <a href="https://www.36kr.com/p/3851015329027336" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a>
    </div><div class="card-icon">&#9889;</div></div></div>
    <div class="sub-grid">
      <div class="sub-card">
        <div class="sub-tag" style="color:#a5b4fc;">定价风暴 · VentureBeat</div>
        <div class="sub-title">Anthropic 恢复第三方 Agent 访问——但引入 Agent SDK 信用额度，被指"25 倍贬值"</div>
        <div class="sub-desc">Anthropic 4 月封禁 OpenClaw 等第三方 Agent 访问 Claude 订阅，6 月恢复但引入 Agent SDK 信用体系（$20-$200/月固定额度，按 API 费率计）。开发者社区反应激烈——对重度用户相当于"25 倍贬值"。VentureBeat 评论：这暴露了 AI 订阅模式在 Agent 时代的根本矛盾。</div>
        <div style="margin-top:6px; font-size:8px; color:var(--text-tertiary);">VentureBeat · 6月</div>
        <div style="margin-top:4px; font-size:8px; color:#a5b4fc;">💡 开发者影响：Agent 用量计费取代固定订阅成趋势，注意预算规划</div>
        <a href="https://venturebeat.com/technology/anthropic-reinstates-openclaw-and-third-party-agent-usage-on-claude-subscriptions-with-a-catch" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a>
      </div>
      <div class="sub-card">
        <div class="sub-tag" style="color:#a5b4fc;">安全争议 · 36氪</div>
        <div class="sub-title">Claude Fable 5「发疯」：高数被判网络攻击，问癌症直接封号</div>
        <div class="sub-desc">Fable 5 安全分类器被曝过度激进——免疫学家问"癌症"被标记为生物安全风险；纯数学概念 Selmer 群、同构被判定为"网络安全风险"直接拒答；高等数学问题被归为"网络攻击"，引发科学界强烈不满。暴露了安全护栏与模型可用性之间的根本矛盾。</div>
        <div style="margin-top:6px; font-size:8px; color:var(--text-tertiary);">36氪 · 6月12日</div>
        <div style="margin-top:4px; font-size:8px; color:#a5b4fc;">💡 开发者影响：安全护栏的粒度控制将成为模型选型的关键指标</div>
        <a href="https://www.36kr.com/p/3850107616678918" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a>
      </div>
      <div class="sub-card">
        <div class="sub-tag" style="color:#a5b4fc;">新模型 · VentureBeat</div>
        <div class="sub-title">智谱发布 GLM-5 Turbo：更快更便宜，专注 Agent ——但不开源</div>
        <div class="sub-desc">z.ai 推出 GLM-5 Turbo，专为 Agent 和"Claw"任务优化的非开源模型。速度更快、成本更低，但采取了闭源策略——与此前 GLM-5.1/5.2 的 MIT 开源路线形成对比。反映了国内模型公司在"开源获生态 vs 闭源保利润"之间的策略摇摆。</div>
        <div style="margin-top:6px; font-size:8px; color:var(--text-tertiary);">VentureBeat · 6月</div>
        <div style="margin-top:4px; font-size:8px; color:#a5b4fc;">💡 开发者影响：开源和闭源策略分化加速，选型时需考虑长期供应稳定性</div>
        <a href="https://venturebeat.com/technology/z-ai-debuts-faster-cheaper-glm-5-turbo-model-for-agents-and-claws-but-its" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a>
      </div>
      <div class="sub-card">
        <div class="sub-tag" style="color:#a5b4fc;">微软 Build · The Verge</div>
        <div class="sub-title">微软发布首个高级推理模型 MAI-Thinking-1：从零训练，无需蒸馏</div>
        <div class="sub-desc">微软在 Build 2026 发布 MAI-Thinking-1——首个从零训练（非蒸馏）的高级推理 AI，性能追平 Claude Opus 4.6。同步发布 MAI-Code-1-Flash、MAI-Image 2.5、MAI-Transcribe-1.5、MAI-Voice-2，共 7 款自研模型。The Verge 评论：微软已彻底告别"OpenAI 单依赖"时代。</div>
        <div style="margin-top:6px; font-size:8px; color:var(--text-tertiary);">The Verge · 6月3日</div>
        <div style="margin-top:4px; font-size:8px; color:#a5b4fc;">💡 开发者影响：微软从 OpenAI 分销商变成自研竞争者，MAI 系列值得关注</div>
        <a href="https://www.theverge.com/tech/941664/microsoft-ai-model-reasoning-mai-thinking-1-build-2026" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a>
      </div>
    </div>
  </div>
  <div class="section-gap section-green" id="section-tools">
    <div class="section-head"><div class="section-line"></div><span class="section-label">工具 & 部署</span><span class="section-label-cn">Tools & Deploy</span></div>
    <div class="tool-row">
      <div class="tool-card">
        <div class="tool-icon">&#127981;</div><div class="tool-name">NanoClaw → 企业"第二大脑"</div><div class="tool-desc">获 $12M 种子轮(Docker/Vercel/HuggingFace CEO参投)，250K+下载、29K★。Docker 沙箱+零信任网关，做每个员工的"专业助手"。</div>
        <span class="tool-badge badge-new">$12M 融资</span>
        <a href="https://venturebeat.com/orchestration/nanoclaws-creators-are-turning-the-secure-open-source-ai-agent-harness-into-an-enterprise-second-brain" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a>
      </div>
      <div class="tool-card">
        <div class="tool-icon">&#127942;</div><div class="tool-name">Nvidia Agent Toolkit</div><div class="tool-desc">GTC 2026 发布，Adobe/Salesforce/SAP/Siemens 等 17 家企业首批采用。Nemotron 模型 + AI-Q 混合推理 + OpenShell 策略沙箱。</div>
        <span class="tool-badge badge-new">17 家采用</span>
        <a href="https://venturebeat.com/ai/nvidia-launches-enterprise-ai-agent-platform-with-adobe-salesforce-sap-among" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a>
      </div>
      <div class="tool-card">
        <div class="tool-icon">&#9889;</div><div class="tool-name">Kimi K2.7-Code 开源</div><div class="tool-desc">万亿 MoE 参数编码模型，思考 Token 降 30%。独立评测："更诚实但没更强大"，部分 kernel 回退。Modified MIT 许可。</div>
        <span class="tool-badge badge-update">Mixed MIT</span>
        <a href="https://venturebeat.com/technology/kimi-k2-7-code-cuts-thinking-tokens-30-practitioners-say-benchmarks-dont-check-out" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a>
      </div>
    </div>
    <div class="sub-grid" style="margin-top:10px;">
      <div class="sub-card">
        <div class="sub-tag" style="color:#86efac;">开源争议 · 36氪</div>
        <div class="sub-title">小米 MiMo Code 开源获 5.1K★ 但 bug 不断，coding harness 该不该开源？</div>
        <div class="sub-desc">5 人 2 周"vibe coding"出品，内存泄漏、未经确认删用户全局 npm 包等问题引发社区大讨论。终端 AI 编程助手的质量底线在哪里？</div>
        <div style="margin-top:6px; font-size:8px; color:var(--text-tertiary);">36氪 · 6月12日</div>
        <div style="margin-top:4px; font-size:8px; color:#86efac;">💡 开发者影响：选开源工具时关注维护质量而非仅看 Star 数</div>
        <a href="https://36kr.com/p/3849833227572226" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a>
      </div>
    </div>
  </div>
  <div class="section-gap section-amber" id="section-policy">
    <div class="section-head"><div class="section-line"></div><span class="section-label">政策 & 合规</span><span class="section-label-cn">Policy & Compliance</span></div>
    <div class="sub-grid">
      <div class="sub-card">
        <div class="sub-tag" style="color:#fcd34d;">首部智能体专项 · 5月8日</div>
        <div class="sub-title">三部门联合印发《智能体规范应用与创新发展实施意见》：四层安全防护 + 19 个典型场景</div>
        <div class="sub-desc">国家网信办、发改委、工信部三部门联合印发，首次在国家层面定义"智能体"（自主感知、记忆、决策、交互、执行）。赛迪研究院专家钟新龙指出形成四层安全防护：外约束（规则内嵌+行为围栏）+ 内嵌入（数据安全+权限管理）+ 供应链（防数据投毒）+ 软法（区块链行为可追溯）。</div>
        <div style="margin-top:6px; font-size:8px; color:var(--text-tertiary);">人民网 · 5月8-16日</div>
        <div style="margin-top:4px; font-size:8px; color:#fcd34d;">💡 开发者影响：智能体从概念进入法律框架，安全评估和算法备案是上线前置条件</div>
        <a href="http://society.people.com.cn/n1/2026/0516/c1008-40720964.html" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a>
      </div>
      <div class="sub-card">
        <div class="sub-tag" style="color:#fcd34d;">标准化 · 6月15日</div>
        <div class="sub-title">AI 终端智能化分级国标 L1-L4 启动 + 商务部筹划"AI+消费"政策体系</div>
        <div class="sub-desc">工信部启动实施 AI 终端智能化分级系列国家标准（L1-L4 级）。商务部正筹划"AI+消费"政策体系，构建标准引领、权益保障与市场准入的立体化治理体系，严格规制大数据杀熟与诱导性消费。经济日报评论："AI+消费"需要打开想象空间的同时守住安全底线。</div>
        <div style="margin-top:6px; font-size:8px; color:var(--text-tertiary);">人民网 / 经济日报 · 6月15日</div>
        <div style="margin-top:4px; font-size:8px; color:#fcd34d;">💡 开发者影响：终端产品上市需通过 L1-L4 分级认证，合规流程前置</div>
        <a href="http://theory.people.com.cn/n1/2026/0615/c40531-40740229.html" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a>
      </div>
    </div>
  </div>
  <div class="section-gap section-cyan" id="section-cases">
    <div class="section-head"><div class="section-line"></div><span class="section-label">应用落地</span><span class="section-label-cn">Real-World AI</span></div>
    <div class="dual-cards">
      <div class="rank-card">
        <div class="rank-label" style="color:#67e8f9;">&#127981; 生态级 · 36氪</div>
        <div style="font-size:14px; font-weight:500; color:var(--text-primary); margin-bottom:6px;">字节火山引擎进军汽车：豆包大模型装车超 700 万辆，对标"鸿蒙智行"</div>
        <div style="font-size:10px; color:var(--text-secondary); line-height:1.5; margin-bottom:8px;">与赛力斯合作 AIVA 品牌、与上汽合作荣威家越 07，以豆包大模型为核心的 Agentic AI 座舱架构。同期，字节小云雀 Agent（基于 Seedance 2.0）与阿里万镜一刻（基于 Happy Horse）在内容 Agent 赛道正面交锋——字节闭环生态（生产→分发全自有体系）vs 阿里收费工具平台路线。</div>
        <div style="font-size:8px; color:var(--text-tertiary);">36氪 · 6月12日</div>
        <div style="margin-top:4px; font-size:8px; color:#67e8f9;">💡 开发者影响：车企 AI 座舱成为 Agent 新战场，豆包/鸿蒙两大生态对开发者开放接入</div>
        <a href="https://www.36kr.com/p/3849891803265667" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a>
      </div>
      <div class="rank-card">
        <div class="rank-label" style="color:#67e8f9;">&#127891; Agent 对决 · 36氪</div>
        <div style="font-size:14px; font-weight:500; color:var(--text-primary); margin-bottom:6px;">千问全周期高考志愿 Agent vs 腾讯元宝克制路线：执行权边界之争</div>
        <div style="font-size:10px; color:var(--text-secondary); line-height:1.5; margin-bottom:8px;">千问发布覆盖出分前后 20 多天全流程的志愿填报 Agent（主动规划+长期记忆+个性化推荐），腾讯元宝强调辅助而非决策。"搜索+工具"向"大模型+Agent"的格局汰换正在发生，核心分歧：Agent 该有多大的执行权？</div>
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
        <div class="rank-row"><span class="rank-num">6</span><span class="rank-name">microsoft/markitdown</span><span class="rank-stat rank-up">152K 总★</span></div>
        <div class="rank-row"><span class="rank-num">7</span><span class="rank-name">Panniantong/Agent-Reach</span><span class="rank-stat rank-up">+5.4K/周</span></div>
        <div class="rank-row"><span class="rank-num">8</span><span class="rank-name">phuryn/pm-skills</span><span class="rank-stat rank-up">+4.8K/周</span></div>
        <div class="rank-row"><span class="rank-num">9</span><span class="rank-name">roboflow/supervision</span><span class="rank-stat rank-up">+4K/周</span></div>
        <div class="rank-row"><span class="rank-num">10</span><span class="rank-name">NVIDIA/SkillSpector</span><span class="rank-stat rank-up">+3.6K/周</span></div>
        <a href="https://github.com/trending?since=weekly" class="read-original" target="_blank" rel="noopener">查看完整榜单 <span class="read-original-arrow">→</span></a>
      </div>
      <div class="rank-card">
        <div class="rank-label" style="color:#fcd34d;">&#128200; 趋势解读（W24-25）</div>
        <div style="font-size:10px; color:var(--text-secondary); line-height:1.6;">
          <p><strong>Claude Skills 占据半壁江山</strong> top 10 中 4 个是 Skills 项目。mattpocock/skills 月增 48K★，Skills 成为"AI 时代的 npm"。</p>
          <p><strong>Token 压缩 + Agent 安全双主线</strong> headroom 省 60-95% Token；NVIDIA SkillSpector 检测 64 种漏洞；NanoClaw+JFrog 成 Agent 供应链防火墙。</p>
          <p><strong>大厂入局开源</strong> 苹果开源容器、微软 markitdown 152K★、英伟达 Agent Toolkit。Linux 基金会接管 Goose 项目。</p>
          <p style="margin-top:6px; color:#fcd34d;">💡 Skills 模块化 + Token 优化 + Agent 安全 = 2026 年 6 月三大技术主线</p>
        </div>
      </div>
    </div>
  </div>
  <div class="section-gap section-cyan" id="section-overseas">
    <div class="section-head"><div class="section-line"></div><span class="section-label">海外参考</span><span class="section-label-cn">Global Brief</span></div>
    <div class="sub-grid">
      <div class="sub-card">
        <div class="sub-tag" style="color:#67e8f9;">🌏 出口管制 · 多源验证</div>
        <div class="sub-title">"AI 史上第一次商业模型被政府强制召回"——Claude Fable 5 禁售冲击波</div>
        <div class="sub-desc">美政府援引国家安全权限要求 Anthropic 全球封禁外籍用户访问 Fable 5/Mythos 5。36氪+The Verge+VentureBeat 三源交叉验证——海外媒体评论：这不仅是一次产品事件，更是 AI 进入地缘政治时代的标志性时刻。智谱随即宣布 GLM-5.2 全量开放，港股暴涨 30%。</div>
        <div style="margin-top:6px; font-size:8px; color:var(--text-tertiary);">36氪 / The Verge / VentureBeat · 6月13-15日</div>
        <div style="margin-top:4px; font-size:8px; color:#67e8f9;">💡 开发者影响：出口管制常态化，模型供应链安全应纳入技术选型考量</div>
        <a href="https://www.36kr.com/p/3851015329027336" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a>
      </div>
      <div class="sub-card">
        <div class="sub-tag" style="color:#67e8f9;">💬 Google I/O · The Verge</div>
        <div class="sub-title">Google I/O 2026 十三大发布：Gemini 3.5 Flash + Omni 任意模态 + Spark 常驻 Agent</div>
        <div class="sub-desc">Gemini 3.5 Flash 成为默认模型和 AI 搜索核心；Gemini Omni 实现任意输入到任意输出（文本/图像/视频/音频互转）；Gemini Spark 作为常驻 AI Agent 关掉电脑后仍可 24/7 后台执行任务。AI Ultra 新定价 $100/$200/月。The Verge 评论：Google 正在要求用户交出全部个人数据来换取 AI 能力。</div>
        <div style="margin-top:6px; font-size:8px; color:var(--text-tertiary);">The Verge · 5月</div>
        <div style="margin-top:4px; font-size:8px; color:#67e8f9;">💡 开发者影响：Gemini 生态从对话走向全模态+常驻 Agent，Android 开发需关注</div>
        <a href="https://www.theverge.com/tech/933415/google-io-2026-biggest-announcements-ai-gemini" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a>
      </div>
      <div class="sub-card">
        <div class="sub-tag" style="color:#67e8f9;">🏛️ 定价革命 · VentureBeat</div>
        <div class="sub-title">AI 订阅模式的 Agent 困境：Anthropic 信用额度制引发"25x 贬值"抗议</div>
        <div class="sub-desc">Anthropic 新 Agent SDK 策略将 API 用量从固定订阅中拆分并单独按 API 费率计费（$20-$200 月额度），重度用户实际成本暴涨 25 倍。这暴露了一个行业性矛盾：Agent 消耗 Token 远超聊天，固定订阅模式不可持续。GitHub Copilot 也已切换到按 Token 计费。</div>
        <div style="margin-top:6px; font-size:8px; color:var(--text-tertiary);">VentureBeat · 6月</div>
        <div style="margin-top:4px; font-size:8px; color:#67e8f9;">💡 开发者影响：AI 编程成本从"忽略不计"变成"需要预算规划"，混合本地+云端模型策略成趋势</div>
        <a href="https://venturebeat.com/technology/anthropic-reinstates-openclaw-and-third-party-agent-usage-on-claude-subscriptions-with-a-catch" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a>
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
tldr = 'Anthropic全球停用Claude Fable5——AI史上首次商业模型被政府强制召回；Agent SDK信用额度制被指25倍贬值；Fable5安全分类器过度激进问数学被封号；智谱GLM-5 Turbo发布(闭源)；NanoClaw获$12M种子轮进化为企业第二大脑；Nvidia Agent Toolkit获17家顶级企业采用；Kimi K2.7-Code开源思考Token降30%；三部门印发智能体实施意见四层安全防护；字节火山引擎进军汽车已装车超700万辆；Google I/O 2026十三大发布。'
html = re.sub(r'<span class="tldr-text" id="tldrContent">.*?</span>', f'<span class="tldr-text" id="tldrContent">{tldr}</span>', html, flags=re.DOTALL)

with open('archive/2026-06-15-evening.html', 'w', encoding='utf-8') as f:
    f.write(html)
ph = html.count('"#" class="read-original')
print(f'Built: {len(html)}B | Placeholders: {ph}')
