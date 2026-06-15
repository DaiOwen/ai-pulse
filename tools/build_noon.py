#!/usr/bin/env python3
import re, datetime

with open('index.html','r',encoding='utf-8') as f:
    html = f.read()

c = '''  <div class="section-gap section-indigo" id="section-models">
    <div class="section-head"><div class="section-line"></div><span class="section-label">大模型动态</span><span class="section-label-cn">Models</span></div>
    <div class="feature-card"><div class="card-row"><div class="card-body">
      <div class="card-tag" style="color:#6366f1;">HEADLINE</div>
      <div class="card-title">腾讯云下调 MiniMax-M3 价格 50%，黄仁勋 GTC 台北联手王兴兴发布 RTX Spark</div>
      <div class="card-desc">6 月 15 日起，腾讯云将 MiniMax-M3 推理输入/输出/缓存命中费用全面下调 50%，Hy-MT2-Pro 输入降 66.67%、输出降 55.56%。同一周，英伟达 GTC 台北大会上黄仁勋联手宇树科技王兴兴，发布首款 Arm PC 芯片 RTX Spark、专为 Agent 设计的 Vera CPU、全球最强桌超算 DGX Station，以及 Isaac GR00T 人形机器人参考设计。Nemotron 3 Ultra 模型对标三大国产模型。</div>
      <div class="card-meta"><span>36氪</span><span>&#183;</span><span>6月15日</span><span>&#183;</span><span class="card-meta-link">多源报道</span></div>
      <div style="margin-top:8px; font-size:9px; color:#a5b4fc;">💡 开发者影响：MiniMax-M3 API 成本砍半，英伟达端侧芯片布局利好本地 Agent 部署</div>
      <a href="https://www.36kr.com/newsflashes/3849974304117760" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a>
    </div><div class="card-icon">&#9889;</div></div></div>
    <div class="sub-grid">
      <div class="sub-card">
        <div class="sub-tag" style="color:#a5b4fc;">人形机器人 · 上交会首秀</div>
        <div class="sub-title">魔法原子发布 Magic-VLA K02 大模型 + Magic-Mix 世界模型</div>
        <div class="sub-desc">人形机器人公司魔法原子在中国（上海）国际技术进出口交易会上首次公开发布 Magic-VLA K02 视觉语言动作大模型和 Magic-Mix 世界模型。VLA K02 实现视觉-语言-动作端到端推理，世界模型可模拟物理交互场景训练。标志着国内人形机器人"大脑"研发从实验室走向公开展示阶段。</div>
        <div style="margin-top:6px; font-size:8px; color:var(--text-tertiary);">36氪 · 6月13日</div>
        <div style="margin-top:4px; font-size:8px; color:#a5b4fc;">💡 开发者影响：VLA+世界模型成具身智能标配，机器人"大脑"赛道加速</div>
        <a href="https://www.36kr.com/newsflashes/3850998799373319" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a>
      </div>
    </div>
  </div>
  <div class="section-gap section-green" id="section-tools">
    <div class="section-head"><div class="section-line"></div><span class="section-label">工具 & 部署</span><span class="section-label-cn">Tools & Deploy</span></div>
    <div class="tool-row">
      <div class="tool-card">
        <div class="tool-icon">&#128737;</div><div class="tool-name">NanoClaw + JFrog</div>
        <div class="tool-desc">AI Agent "免疫系统"：NanoClaw（OpenClaw 企业分支）联手 JFrog，在 Agent 下载 MCP 服务器/包时实时拦截恶意代码。检测到投毒包返回 403 并自动引导 Agent 到安全版本。开源社区完全免费。</div>
        <span class="tool-badge badge-new">安全</span>
        <a href="https://venturebeat.com/security/nanoclaw-and-jfrog-launch-immune-system-to-block-ai-agents-from-downloading-malicious-code" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a>
      </div>
      <div class="tool-card">
        <div class="tool-icon">&#128187;</div><div class="tool-name">小米 MiMo Code V0.1.0</div>
        <div class="tool-desc">MIT 开源终端 AI 编程助手。持久记忆系统（SQLite FTS5 + checkpoint-writer 子代理）解决 200+ 步任务"失忆"痛点。SWE-Bench Verified 82% vs Claude Code 79%，576 人内测 65%+ 胜率。免费搭载 MiMo-V2.5 模型。</div>
        <span class="tool-badge badge-new">MIT 开源</span>
        <a href="https://venturebeat.com/technology/xiaomis-new-open-source-agentic-ai-coding-harness-mimo-code-beats-claude-code-at-ultra-long-200-step-tasks" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a>
      </div>
    </div>
  </div>
  <div class="section-gap section-amber" id="section-policy">
    <div class="section-head"><div class="section-line"></div><span class="section-label">政策 & 合规</span><span class="section-label-cn">Policy & Compliance</span></div>
    <div class="sub-grid">
      <div class="sub-card">
        <div class="sub-tag" style="color:#fcd34d;">密集政策 · 6月中旬</div>
        <div class="sub-title">工信部 AI+信息通信三年意见 + AI 终端分级国标 L1-L4 + 江苏 100 个工业智能体</div>
        <div class="sub-desc">6 月 13 日，工信部印发「人工智能+信息通信」创新发展实施意见（2026-2028），部署 17 项任务，目标 30+ 高价值场景和特色智能体。同日，AI 终端智能化分级国家标准启动实施（L1-L4 级）。6 月 12 日，江苏发布「AI+制造」22 条方案，目标 2027 年推出 100 个工业智能体。上海同日召开政务智能推进会，陈吉宁强调把政务智能作为"一把手"工程。</div>
        <div style="margin-top:6px; font-size:8px; color:var(--text-tertiary);">人民日报 · 6月13日</div>
        <div style="margin-top:4px; font-size:8px; color:#fcd34d;">💡 开发者影响：智能体从概念进入国家+地方双轨政策落地，工业智能体是最大增量市场</div>
        <a href="http://finance.people.com.cn/n1/2026/0613/c1004-40739463.html" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a>
      </div>
    </div>
  </div>
  <div class="section-gap section-cyan" id="section-cases">
    <div class="section-head"><div class="section-line"></div><span class="section-label">应用落地</span><span class="section-label-cn">Real-World AI</span></div>
    <div class="dual-cards">
      <div class="rank-card">
        <div class="rank-label" style="color:#67e8f9;">&#127981; 落地决战 · 五巨头亮剑</div>
        <div style="font-size:14px; font-weight:500; color:var(--text-primary); margin-bottom:6px;">企业级 AI Agent 进入「硅基员工」时代：华住 150 万次任务、伊利转化率 +39%</div>
        <div style="font-size:10px; color:var(--text-secondary); line-height:1.5; margin-bottom:8px;">阿里悟空（钉钉 CLI 化"沟通即执行"）、腾讯 ADP 4.0（途虎养车合作）、字节扣子、百度千帆（130 万+ Agents）、华为 AgentArts 五巨头全面开战。落地数据：华住"华小AI"落地万家门店累计执行近 150 万次任务、自动处理 70%+ 高频问询；伊利导购 Agent 点击率 +15.7%、下单转化率 +39%；义乌企业用 Agent 自动抓取竞品数据生成策略。核心瓶颈：确定性（B 端零容错）、成本（Gartner 预计 40% 项目将因成本被取消）、信任（敢不敢把执行权交给 AI）。</div>
        <div style="font-size:8px; color:var(--text-tertiary);">36氪 · 6月</div>
        <div style="margin-top:4px; font-size:8px; color:#67e8f9;">💡 开发者影响：Agent 岗位从"写 Prompt"升级为"设计 SOP + 工具调用 + 安全护栏"三位一体</div>
        <a href="https://www.36kr.com/p/3809987729842183" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a>
      </div>
    </div>
  </div>
  <div class="section-gap section-amber" id="section-oss">
    <div class="section-head"><div class="section-line"></div><span class="section-label">开源热度</span><span class="section-label-cn">Open Source Pulse</span></div>
    <div class="dual-cards">
      <div class="rank-card">
        <div class="rank-label" style="color:#fcd34d;">&#128200; GitHub Trending — AI Top 5（W24-25）</div>
        <div class="rank-row"><span class="rank-num">1</span><span class="rank-name">mvanhorn/last30days-skill</span><span class="rank-stat rank-up">+12K stars/周</span></div>
        <div class="rank-row"><span class="rank-num">2</span><span class="rank-name">chopratejas/headroom</span><span class="rank-stat rank-up">+10K stars/周</span></div>
        <div class="rank-row"><span class="rank-num">3</span><span class="rank-name">mattpocock/skills</span><span class="rank-stat rank-up">+48K stars/月</span></div>
        <div class="rank-row"><span class="rank-num">4</span><span class="rank-name">harry0703/MoneyPrinterTurbo</span><span class="rank-stat rank-up">+6.9K stars/周</span></div>
        <div class="rank-row"><span class="rank-num">5</span><span class="rank-name">NVIDIA/SkillSpector</span><span class="rank-stat rank-up">+3.6K stars/周</span></div>
        <a href="https://github.com/trending?since=weekly" class="read-original" target="_blank" rel="noopener">查看完整榜单 <span class="read-original-arrow">→</span></a>
      </div>
      <div class="rank-card">
        <div class="rank-label" style="color:#fcd34d;">&#128200; 趋势解读</div>
        <div style="font-size:10px; color:var(--text-secondary); line-height:1.6;">
          <p><strong>Claude Skills 横扫半壁江山</strong> mattpocock/skills 月增 48K、last30days-skill 周增 12K。Skills 模块化成为"AI 时代的 npm 包"。</p>
          <p><strong>Token 压缩 + Agent 安全双主线</strong> headroom 省 60-95% Token；NVIDIA SkillSpector 检测 64 种漏洞，NanoClaw+JFrog 拦截恶意包。</p>
          <p><strong>GitHub Copilot 按 Token 计费</strong> 开发者需建立 AI 编程成本意识，本地+云端混合模型成新常态。</p>
          <p style="margin-top:6px; color:#fcd34d;">💡 Skills 生态 + Token 优化 + Agent 安全 = 6 月三大技术主线</p>
        </div>
      </div>
    </div>
  </div>'''

start = html.find('<div class="section-gap section-indigo" id="section-models">')
end = html.find('<footer class="footer">')
html = html[:start] + c + '\n' + html[end:]

now = datetime.datetime.now()
html = re.sub(r'<span class="hero-badge-text" id="editionLabel">.*?</span>', f'<span class="hero-badge-text" id="editionLabel">午间版 &#183; {now.strftime("%H:%M")} &#183; 增量更新</span>', html)
html = re.sub(r'<p class="hero-date" id="dateLabel">.*?</p>', f'<p class="hero-date" id="dateLabel">{now.strftime("%Y年%m月%d日")} &#183; 星期一</p>', html)
html = re.sub(r'<p class="hero-updated" id="updatedLabel">.*?</p>', f'<p class="hero-updated" id="updatedLabel"><span class="hero-updated-dot"></span> 最后更新: {now.strftime("%Y-%m-%d %H:%M")} CST</p>', html)
tldr = '腾讯云MiniMax-M3降价50%+黄仁勋GTC台北联手王兴兴发布RTX Spark；魔法原子VLA K02人形机器人世界模型首秀；NanoClaw+JFrog打造AI Agent免疫系统；小米MiMo Code开源MIT协议SWE-Bench 82%；工信部AI+信息通信三年意见+AI终端分级L1-L4国标启动；五巨头企业级Agent落地决战华住150万次任务。'
html = re.sub(r'<span class="tldr-text" id="tldrContent">.*?</span>', f'<span class="tldr-text" id="tldrContent">{tldr}</span>', html, flags=re.DOTALL)

with open('archive/2026-06-15-noon.html', 'w', encoding='utf-8') as f:
    f.write(html)
print(f'Built: {len(html)}B | # links: {html.count(chr(34)+"#" + chr(34) + " class=" + chr(34) + "read-original")}')
