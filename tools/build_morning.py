#!/usr/bin/env python3
import re, datetime

with open('index.html','r',encoding='utf-8') as f: html = f.read()

c = r'''  <div class="section-gap section-indigo" id="section-models">
    <div class="section-head"><div class="section-line"></div><span class="section-label">大模型动态</span><span class="section-label-cn">Models</span></div>
    <div class="feature-card"><div class="card-row"><div class="card-body">
      <div class="card-tag" style="color:#6366f1;">HEADLINE</div>
      <div class="card-title">智源发布全球首个通用世界基座模型「悟界·Physis」：从"预测下一个词"到"预测下一个物理状态"</div>
      <div class="card-desc">6 月 12 日，北京智源研究院发布全球首个通用世界基座模型 悟界·Physis-v0.1，标志着 AI 从语言预测迈向物理状态预测的范式革命。该模型可模拟真实物理世界的状态演变，为具身智能、自动驾驶、工业仿真等场景提供底层能力。证券时报评论：这是中国在"世界模型"赛道上的一次重要抢跑。</div>
      <div class="card-meta"><span>证券时报</span><span>&#183;</span><span>6月12日</span><span>&#183;</span><span class="card-meta-link">独家报道</span></div>
      <div style="margin-top:8px; font-size:9px; color:#a5b4fc;">💡 开发者影响：世界模型是具身智能的基础设施，Physis 开源后可加速机器人/自动驾驶仿真训练</div>
      <a href="https://stcn.com/article/detail/3959545.html" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a>
    </div><div class="card-icon">&#9889;</div></div></div>
    <div class="sub-grid">
      <div class="sub-card"><div class="sub-tag" style="color:#a5b4fc;">推理突破 · 证券时报</div><div class="sub-title">小米 MiMo-V2.5-Pro 全球首个通用 GPU 突破 1000 Tokens/s</div><div class="sub-desc">6 月 8 日，小米 AI 上线 UltraSpeed 模式，成为全球首个在通用 GPU 上推理速度突破 1000 Tokens/s 的万亿参数模型。这刷新了旗舰模型的推理速度纪录，让实时 AI 交互体验向前迈进一大步。</div><div style="margin-top:6px; font-size:8px; color:var(--text-tertiary);">证券时报 · 6月8日</div><div style="margin-top:4px; font-size:8px; color:#a5b4fc;">💡 开发者影响：1000 Tokens/s 意味着实时语音+视频 Agent 交互成为现实</div><a href="https://www.stcn.com/article/detail/3950835.html" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
      <div class="sub-card"><div class="sub-tag" style="color:#a5b4fc;">万亿参数 · 证券时报</div><div class="sub-title">阿里千问 Qwen3-Max-Thinking 发布：万亿参数，预训练 36T Tokens</div><div class="sub-desc">1 月 27 日发布旗舰推理模型，总参数超 1T，预训练数据量高达 36T Tokens，整体性能媲美 GPT-5.2、Claude Opus 4.5 和 Gemini 3 Pro。从"预测下一个词"到"深度思考"，千问旗舰补齐了推理能力短板。</div><div style="margin-top:6px; font-size:8px; color:var(--text-tertiary);">证券时报 · 1月27日</div><div style="margin-top:4px; font-size:8px; color:#a5b4fc;">💡 开发者影响：国产万亿参数推理模型可用，API 接入成本低于国际同类</div><a href="https://stcn.com/article/detail/3938527.html" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
      <div class="sub-card"><div class="sub-tag" style="color:#a5b4fc;">开源生态 · 证券时报</div><div class="sub-title">智谱 GLM-5.2 宣布 MIT 协议开源，MiniMax M3 启动 A 股 IPO</div><div class="sub-desc">6 月 15 日智谱推出旗舰 GLM-5.2（1M 上下文，MIT 开源）。6 月 1 日 MiniMax 发布 M3（自研稀疏注意力 MSA，100 万词元上下文，推理效率提升约 20 倍），同步启动科创板 IPO。国产大模型从"拼参数"进入"拼落地+拼商业化"阶段。</div><div style="margin-top:6px; font-size:8px; color:var(--text-tertiary);">证券时报 · 6月</div><div style="margin-top:4px; font-size:8px; color:#a5b4fc;">💡 开发者影响：GLM-5.2 MIT 开源可直接商用，MiniMax M3 IPO 意味着更透明的 API 定价</div><a href="https://stcn.com/article/detail/3961497.html" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
    </div>
  </div>
  <div class="section-gap section-green" id="section-tools">
    <div class="section-head"><div class="section-line"></div><span class="section-label">工具 & 部署</span><span class="section-label-cn">Tools & Deploy</span></div>
    <div class="tool-row">
      <div class="tool-card"><div class="tool-icon">&#128268;</div><div class="tool-name">华为版 CUDA 全面开源</div><div class="tool-desc">华为昇腾 CANN 神经网络计算架构全面开源，对标英伟达 CUDA。配套开源 MindSpore 框架，已支持 PyTorch/TensorFlow/飞桨。传奇 GPU 架构师 Raja Koduri 同日创立 Oxmiq Labs 挑战 CUDA 生态。</div><span class="tool-badge badge-new">国产替代</span><a href="https://m.36kr.com/p/3411091131567747" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
      <div class="tool-card"><div class="tool-icon">&#129302;</div><div class="tool-name">EvoAgentX 自进化框架</div><div class="tool-desc">英国格拉斯哥大学发布全球首个 AI 智能体自进化开源框架。支持提示词、工作流结构、记忆机制多维度自进化，多任务场景性能提升 8%-13%。一键部署，终生可用。</div><span class="tool-badge badge-new">开源</span><a href="https://36kr.com/p/3314754737285121" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
      <div class="tool-card"><div class="tool-icon">&#9888;</div><div class="tool-name">Vibe Coding 争议</div><div class="tool-desc">36氪深度：AI 编程工具（Cursor/Claude/Copilot）正在"杀死"开源——AI 作为中介层截走用户关注和反馈，开源维护者失去社区动力。学者论文警告：短期提效，长期破坏生态。</div><span class="tool-badge badge-update">警示</span><a href="https://36kr.com/p/3667072467690370" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
    </div>
  </div>
  <div class="section-gap section-amber" id="section-policy">
    <div class="section-head"><div class="section-line"></div><span class="section-label">政策 & 合规</span><span class="section-label-cn">Policy & Compliance</span></div>
    <div class="sub-grid">
      <div class="sub-card"><div class="sub-tag" style="color:#fcd34d;">国家目标 · 人民网</div><div class="sub-title">智能体普及率目标：2027 年超 70%，2030 年超 90%</div><div class="sub-desc">两会特别节目透露：国务院明确提出智能体普及率目标——2027 年超 70%，2030 年超 90%。从"人找服务"到"服务找人"。同期八部门联合发文推动"AI+制造"，工业企业应用大模型/智能体比例从 2024 年 9.6% 跃升至 2025 年 47.5%。</div><div style="margin-top:6px; font-size:8px; color:var(--text-tertiary);">人民网 · 2026年3-4月</div><div style="margin-top:4px; font-size:8px; color:#fcd34d;">💡 开发者影响：智能体产业有明确的政策时间表，2027 年前是窗口期</div><a href="http://finance.people.com.cn/n1/2026/0115/c1004-40645854.html" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
      <div class="sub-card"><div class="sub-tag" style="color:#fcd34d;">企业实践 · 人民网</div><div class="sub-title">杨元庆：联想全球供应链智能体已实现多智能体协同，决策时间缩短 50%</div><div class="sub-desc">联想 CEO 杨元庆在人民网撰文主张"混合式 AI"路径（云+端协同），透露联想全球供应链智能体已实现多智能体协同运作，决策时间缩短 50% 以上。这是中国制造业龙头企业首次公开披露智能体的量化业务成效。</div><div style="margin-top:6px; font-size:8px; color:var(--text-tertiary);">人民网 · 4月14日</div><div style="margin-top:4px; font-size:8px; color:#fcd34d;">💡 开发者影响：联想供应链智能体证明了多 Agent 协同的 ROI 可量化</div><a href="http://hb.people.com.cn/BIG5/n2/2026/0414/c192237-41551304.html" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
    </div>
  </div>
  <div class="section-gap section-purple" id="section-paper">
    <div class="section-head"><div class="section-line"></div><span class="section-label">论文速递</span><span class="section-label-cn">Paper Spotlight</span></div>
    <div class="paper-spotlight"><div class="paper-header"><span class="paper-label">&#128218; 今日精选 · 智源研究院</span></div>
      <div class="paper-title">悟界·Physis：从语言预测到物理状态预测的范式跃迁</div>
      <div class="paper-abstract">智源研究院发布全球首个通用世界基座模型。传统 LLM 学习"预测下一个词"，Physis 学习"预测下一个物理状态"——物体运动、流体变化、碰撞反应。这一范式跃迁使得 AI 可以内化物理常识，而不仅仅是从文本中统计规律。对具身智能、自动驾驶仿真、工业数字孪生等领域具有基础性意义。</div>
      <div class="paper-meta">智源研究院 · 6月12日 · 全球首个通用世界基座模型</div>
      <div style="margin-top:6px; font-size:8px; color:#c4b5fd;">💡 开发者影响：世界模型将取代传统物理引擎成为机器人仿真训练的核心基础设施</div>
    </div>
  </div>
  <div class="section-gap section-cyan" id="section-cases">
    <div class="section-head"><div class="section-line"></div><span class="section-label">应用落地</span><span class="section-label-cn">Real-World AI</span></div>
    <div class="dual-cards">
      <div class="rank-card"><div class="rank-label" style="color:#67e8f9;">&#127981; 产业智能体 · 人民网</div><div style="font-size:14px; font-weight:500; color:var(--text-primary); margin-bottom:6px;">从"人找服务"到"服务找人"：智能体走进日常生活</div><div style="font-size:10px; color:var(--text-secondary); line-height:1.5; margin-bottom:8px;">人民网两会特别报道：智能体能代下单、填信息、支付。应用已覆盖客服（百度文心平台 15 万+企业）、教育（AI 助教）、医疗（AI 医生）、文旅（"杭小忆""刘三姐"数字人）、编程（Copilot/Codex）、气象等多个领域。IDC 预测 2025 年为智能体规模化落地元年。</div><div style="font-size:8px; color:var(--text-tertiary);">人民网 · 3月</div><div style="margin-top:4px; font-size:8px; color:#67e8f9;">💡 开发者影响：智能体从"能聊天"走向"能办事"，执行能力是差异化关键</div><a href="http://yn.people.com.cn/n2/2026/0311/c378440-41520309.html" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
      <div class="rank-card"><div class="rank-label" style="color:#67e8f9;">&#127891; 开源争议 · 36氪</div><div style="font-size:14px; font-weight:500; color:var(--text-primary); margin-bottom:6px;">三年开源，阿里换来了什么？Qwen 衍生模型超 20 万，下载量破 10 亿</div><div style="font-size:10px; color:var(--text-secondary); line-height:1.5; margin-bottom:8px;">36氪深度复盘阿里开源战略：通义千问衍生模型超 20 万个，下载量突破 10 亿次。但核心人才林俊旸离职引发对阿里开源路线的深层追问——"开源信仰"还是"开源作为竞争工具"？文章指出中国 AI 开源正处于十字路口。</div><div style="font-size:8px; color:var(--text-tertiary);">36氪 · 近期</div><div style="margin-top:4px; font-size:8px; color:#67e8f9;">💡 开发者影响：Qwen 生态规模已形成网络效应，但核心人才稳定性是持续发展的关键</div><a href="https://m.36kr.com/p/3709760632402696" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
    </div>
  </div>
  <div class="section-gap section-amber" id="section-oss">
    <div class="section-head"><div class="section-line"></div><span class="section-label">开源热度</span><span class="section-label-cn">Open Source Pulse</span></div>
    <div class="dual-cards">
      <div class="rank-card"><div class="rank-label" style="color:#fcd34d;">&#128200; GitHub Trending — AI Top 5（W24-25）</div>
        <div class="rank-row"><span class="rank-num">1</span><span class="rank-name">mvanhorn/last30days-skill</span><span class="rank-stat rank-up">+12K/周</span></div><div class="rank-row"><span class="rank-num">2</span><span class="rank-name">chopratejas/headroom</span><span class="rank-stat rank-up">+10K/周</span></div><div class="rank-row"><span class="rank-num">3</span><span class="rank-name">Leonxlnx/taste-skill</span><span class="rank-stat rank-up">+8.7K/周</span></div><div class="rank-row"><span class="rank-num">4</span><span class="rank-name">addyosmani/agent-skills</span><span class="rank-stat rank-up">+8.3K/周</span></div><div class="rank-row"><span class="rank-num">5</span><span class="rank-name">apple/container</span><span class="rank-stat rank-up">+7.8K/周</span></div>
        <a href="https://github.com/trending?since=weekly" class="read-original" target="_blank" rel="noopener">查看完整榜单 <span class="read-original-arrow">→</span></a></div>
      <div class="rank-card"><div class="rank-label" style="color:#fcd34d;">&#128200; 趋势解读（cnblogs W24）</div><div style="font-size:10px; color:var(--text-secondary); line-height:1.6;"><p><strong>Skills 生态成新范式</strong> 至少 8 个 .claude/skills 项目登榜，形成"AI 时代的 npm 包"生态。</p><p><strong>Token 压缩刚需爆发</strong> headroom 6 种算法省 60-95% Token，Agent 上下文需求驱动。</p><p><strong>Agent 安全标配</strong> NVIDIA SkillSpector（64种漏洞）+ 微软 mxc 沙箱 + NanoClaw+JFrog 供应链防护。</p><p style="margin-top:6px; color:#fcd34d;">💡 AI 开源重心已从"做模型"彻底转向"做 Agent 基础设施"</p></div></div>
    </div>
  </div>
  <div class="section-gap section-cyan" id="section-overseas">
    <div class="section-head"><div class="section-line"></div><span class="section-label">海外参考</span><span class="section-label-cn">Global Brief</span></div>
    <div class="sub-grid">
      <div class="sub-card"><div class="sub-tag" style="color:#67e8f9;">🌏 MIT Tech Review</div><div class="sub-title">MIT Tech Review 预测 2026 AI 五大趋势：硅谷产品将跑在中国模型上</div><div class="sub-desc">年初重磅预测：①更多硅谷产品将构建在中国 LLM 之上 ②美国 AI 监管陷入拉锯战 ③AI 聊天机器人将改变购物方式（Agentic Commerce）④LLM 将做出重要科学发现 ⑤AI 监管从自愿走向强制。三个月后看，第①条正在应验——微软已在内部广泛采用 Claude Code 的同时评估中国模型。</div><div style="margin-top:6px; font-size:8px; color:var(--text-tertiary);">MIT Technology Review · 1月5日</div><div style="margin-top:4px; font-size:8px; color:#67e8f9;">💡 开发者影响：中国模型出海不只是价格优势——硅谷产品已经开始认真评估技术能力</div><a href="https://www.technologyreview.com/2026/01/05/1130662/whats-next-for-ai-in-2026/" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
      <div class="sub-card"><div class="sub-tag" style="color:#67e8f9;">💬 36氪国际</div><div class="sub-title">微软 Build 2026：7 款自研 MAI 模型 + Surface RTX Spark + Project Solara</div><div class="sub-desc">微软史上最大规模 AI 发布：MAI-Thinking-1（35B 活跃/1T 总参数，从零训练不蒸馏）、Surface RTX Spark Dev Box（1 PFLOPS 本地算力）、Project Solara（专为 AI Agent 设计的安卓系统）。从 OpenAI 分销商变成全栈竞争者。</div><div style="margin-top:6px; font-size:8px; color:var(--text-tertiary);">36氪/爱范儿 · 6月3日</div><div style="margin-top:4px; font-size:8px; color:#67e8f9;">💡 开发者影响：微软自研 MAI 模型 + 自研芯片 + AgentOS = 全栈 AI 平台</div><a href="https://www.36kr.com/p/3836668626891910" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
      <div class="sub-card"><div class="sub-tag" style="color:#67e8f9;">🏛️ MIT Tech Review</div><div class="sub-title">OpenAI 终于发布开源权重模型：Apache 2.0 协议，性能对标 o3-mini/o4-mini</div><div class="sub-desc">MIT Tech Review 报道：OpenAI 发布 GPT-OSS 系列开源权重模型（Apache 2.0），这是自 2019 年 GPT-2 以来首次。背景是中国开源模型（DeepSeek/Qwen/Kimi）的全球主导地位给美国带来的战略压力。标志着 OpenAI 从"完全闭源"路线开始松动。</div><div style="margin-top:6px; font-size:8px; color:var(--text-tertiary);">MIT Technology Review · 8月5日</div><div style="margin-top:4px; font-size:8px; color:#67e8f9;">💡 开发者影响：OpenAI 开源标志着闭源阵营松动，Apache 2.0 可直接商用</div><a href="https://www.technologyreview.com/2025/08/05/1121092/openai-has-finally-released-open-weight-language-models/" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
    </div>
  </div>'''

start = html.find('<div class="section-gap section-indigo" id="section-models">')
end = html.find('<footer class="footer">')
html = html[:start] + c + '\n' + html[end:]

now = datetime.datetime.now()
html = re.sub(r'<span class="hero-badge-text" id="editionLabel">.*?</span>', f'<span class="hero-badge-text" id="editionLabel">早间版 · {now.strftime("%H:%M")} · 清晨速递</span>', html)
html = re.sub(r'<p class="hero-date" id="dateLabel">.*?</p>', f'<p class="hero-date" id="dateLabel">{now.strftime("%Y年%m月%d日")} · 星期二</p>', html)
html = re.sub(r'<p class="hero-updated" id="updatedLabel">.*?</p>', f'<p class="hero-updated" id="updatedLabel"><span class="hero-updated-dot"></span> 最后更新: {now.strftime("%Y-%m-%d %H:%M")} CST</p>', html)
tl = '智源发布全球首个通用世界基座模型悟界·Physis从语言预测迈向物理状态预测；小米MiMo突破1000Tokens/s推理速度纪录；阿里Qwen3-Max-Thinking万亿参数发布；智谱GLM-5.2宣布MIT开源MiniMax启动科创板IPO；华为版CUDA全面开源对标英伟达；国务院智能体普及率目标2027年超70%；微软Build发布7款MAI自研模型+Surface RTX Spark。'
html = re.sub(r'<span class="tldr-text" id="tldrContent">.*?</span>', f'<span class="tldr-text" id="tldrContent">{tl}</span>', html, flags=re.DOTALL)

with open('archive/2026-06-16-morning.html', 'w', encoding='utf-8') as f: f.write(html)
ph = html.count('"#" class="read-original')
print(f'Built: {len(html)}B | Placeholders: {ph}')
