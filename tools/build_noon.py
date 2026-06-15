#!/usr/bin/env python3
import re, datetime

with open('index.html','r',encoding='utf-8') as f:
    html = f.read()

content = '''  <div class="section-gap section-indigo" id="section-models">
    <div class="section-head"><div class="section-line"></div><span class="section-label">大模型动态</span><span class="section-label-cn">Models</span></div>
    <div class="feature-card"><div class="card-row"><div class="card-body">
      <div class="card-tag" style="color:#6366f1;">HEADLINE</div>
      <div class="card-title">Anthropic 发布 Claude Fable 5 / Mythos 5，同时发出「递归自我改进」警告</div>
      <div class="card-desc">6 月 9 日，Anthropic 发布两款新模型：Fable 5 向公众开放，Mythos 5 仅向约 200 家关键基础设施机构开放（号称"全球最强网络安全能力"）。但更引人关注的是同步发布的反哺报告《当 AI 构建自身》——Anthropic 代码库中超过 80% 代码已由 Claude 撰写，公司警告"递归自我改进（RSI）"正在形成闭环，研发主体正从人转移到 AI，呼吁全球"放缓乃至暂停"前沿 AI 开发。Claude 访问量同期暴涨 34%。</div>
      <div class="card-meta"><span>36氪</span><span>&#183;</span><span>6月9日</span><span>&#183;</span><span class="card-meta-link">深度报道</span><span>&#183;</span><a href="https://www.36kr.com/p/3849931768281729" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
      <div style="margin-top:8px; font-size:9px; color:#a5b4fc;">💡 开发者影响：AI 自我研发闭环正在形成——这不仅是技术问题，更是开发者职业路径的结构性变化信号</div>
    </div><div class="card-icon">&#9889;</div></div></div>
    <div class="sub-grid">
      <div class="sub-card">
        <div class="sub-tag" style="color:#a5b4fc;">上市 + 新品</div>
        <div class="sub-title">MiniMax 启动 A 股上市：ARR 超 3 亿美元，M3 模型即将发布</div>
        <div class="sub-desc">5 月 29 日提交上市辅导备案（中信证券），港股股价较发行价已涨超 409%，市值约 2635 亿港元。全球用户约 3 亿，ARR 超 3 亿美元。即将发布的 M3 采用自研 Sparse Attention，百万 token 推理速度达到前代的 9.7 倍（预填充）和 15.6 倍（解码）。大模型"六小龙"进入集中上市/融资的分水岭阶段。</div>
        <div style="margin-top:6px; font-size:8px; color:var(--text-tertiary);">36氪 · 5月29日</div>
        <div style="margin-top:4px; font-size:8px; color:#a5b4fc;">💡 开发者影响：国产模型商业化加速，ARR 是评估模型公司健康状况的关键指标</div>
        <a href="https://eu.36kr.com/zh/p/3831159799834249" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a>
      </div>
    </div>
  </div>

  <div class="section-gap section-green" id="section-tools">
    <div class="section-head"><div class="section-line"></div><span class="section-label">工具 & 部署</span><span class="section-label-cn">Tools & Deploy</span></div>
    <div class="tool-row">
      <div class="tool-card">
        <div class="tool-icon">&#127942;</div><div class="tool-name">Arcee Trinity-Large-Thinking</div>
        <div class="tool-desc">30 人旧金山团队打造，Apache 2.0 开源。399B MoE（13B 激活），PinchBench 91.9 接近 Claude Opus 4.6（93.3），但输出成本仅 $0.90/百万 token vs Opus 的 $25——便宜 96%。定位为「美国主权 AI」替代方案。</div>
        <span class="tool-badge badge-new">Apache 2.0</span>
        <a href="https://venturebeat.com/ai/arcees-new-open-source-trinity-large-thinking-is-the-rare-powerful-u-s-made" class="read-original" target="_blank" rel="noopener" style="display:block;">阅读原文 <span class="read-original-arrow">→</span></a>
      </div>
      <div class="tool-card">
        <div class="tool-icon">&#128187;</div><div class="tool-name">Ai2 MolmoWeb</div>
        <div class="tool-desc">开源视觉 Web Agent（4B/8B），只靠浏览器截图操作网页（无需 HTML 解析）。附带最大公开人类 Web 任务数据集：30K 任务轨迹 + 590K 子任务 + 2.2M 截图 QA，覆盖 1,100+ 网站。</div>
        <span class="tool-badge badge-new">Open-Weight</span>
        <a href="https://venturebeat.com/data/ai2-releases-molmoweb-an-open-weight-visual-web-agent-with-30k-human-task" class="read-original" target="_blank" rel="noopener" style="display:block;">阅读原文 <span class="read-original-arrow">→</span></a>
      </div>
    </div>
  </div>

  <div class="section-gap section-amber" id="section-policy">
    <div class="section-head"><div class="section-line"></div><span class="section-label">政策 & 合规</span><span class="section-label-cn">Policy & Compliance</span></div>
    <div class="sub-grid">
      <div class="sub-card">
        <div class="sub-tag" style="color:#fcd34d;">重磅文件 · 5月9日印发</div>
        <div class="sub-title">三部门联合印发《智能体规范应用与创新发展实施意见》，定义 19 个典型场景</div>
        <div class="sub-desc">国家网信办、发改委、工信部联合发文，首次在国家层面明确「智能体」定义——具备自主感知、记忆、决策、交互、执行能力的智能系统。文件规定了智能体产品的安全可控原则，列出科研、产业、消费、民生、社会治理 5 大方向 19 个典型应用场景，并要求建立安全底线和治理体系。同期，政治局会议提出"完善人工智能治理"，工信部启动 AI 科技伦理审查先导计划，市场监管总局发布 AI 计量体系建设指引。</div>
        <div style="margin-top:6px; font-size:8px; color:var(--text-tertiary);">人民日报 / 人民网 · 5月</div>
        <div style="margin-top:4px; font-size:8px; color:#fcd34d;">💡 开发者影响：智能体产品从此有法可依——安全评估、伦理审查、计量标准三道关</div>
        <a href="https://cpc.people.com.cn/BIG5/n1/2026/0509/c64387-40716233.html" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a>
      </div>
    </div>
  </div>

  <div class="section-gap section-cyan" id="section-cases">
    <div class="section-head"><div class="section-line"></div><span class="section-label">应用落地</span><span class="section-label-cn">Real-World AI</span></div>
    <div class="dual-cards">
      <div class="rank-card">
        <div class="rank-label" style="color:#67e8f9;">&#127981; 巨头决战 · 36氪深度</div>
        <div style="font-size:14px; font-weight:500; color:var(--text-primary); margin-bottom:6px;">2026：企业级 AI Agent 落地决战年——五巨头亮剑，争夺「硅基员工」时代入口</div>
        <div style="font-size:10px; color:var(--text-secondary); line-height:1.5; margin-bottom:8px;">阿里悟空（钉钉组织入口，已规模化放量进电商/门店/制造）、腾讯 ADP 4.0（微信生态 AgentOS，途虎养车等已合作）、字节扣子（低门槛开发）、百度千帆（130 万+ Agents 基础设施）、华为 AgentArts（全栈自主可控、政企私有化）。核心转变：从"能聊天"到"能干活"——悟空对钉钉底层 CLI 化改造实现"沟通即执行"。最大挑战：B 端零容错要求（合同/财务/制造场景一个 bad case 就让客户否定整个 AI 模块）。</div>
        <div style="font-size:8px; color:var(--text-tertiary);">36氪 · 6月</div>
        <div style="margin-top:4px; font-size:8px; color:#67e8f9;">💡 开发者影响：Agent 开发从 Prompt 工程转向结构化 SOP + 长期记忆 + 工具调用，Skill 模块化是入场券</div>
        <a href="https://www.36kr.com/p/3809987729842183" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a>
      </div>
    </div>
  </div>

  <div class="section-gap section-amber" id="section-oss">
    <div class="section-head"><div class="section-line"></div><span class="section-label">开源热度</span><span class="section-label-cn">Open Source Pulse</span></div>
    <div class="dual-cards">
      <div class="rank-card">
        <div class="rank-label" style="color:#fcd34d;">&#128200; GitHub Trending — AI 领域 Top 5（W24-25）</div>
        <div class="rank-row"><span class="rank-num">1</span><span class="rank-name">mvanhorn/last30days-skill</span><span class="rank-stat rank-up">+12K stars/周</span></div>
        <div class="rank-row"><span class="rank-num">2</span><span class="rank-name">chopratejas/headroom</span><span class="rank-stat rank-up">+10K stars/周</span></div>
        <div class="rank-row"><span class="rank-num">3</span><span class="rank-name">microsoft/markitdown</span><span class="rank-stat rank-up">+6.3K stars/周</span></div>
        <div class="rank-row"><span class="rank-num">4</span><span class="rank-name">harry0703/MoneyPrinterTurbo</span><span class="rank-stat rank-up">+6.9K stars/周</span></div>
        <div class="rank-row"><span class="rank-num">5</span><span class="rank-name">NVIDIA/SkillSpector</span><span class="rank-stat rank-up">+3.6K stars/周</span></div>
        <a href="https://github.com/trending?since=weekly" class="read-original" target="_blank" rel="noopener">查看完整榜单 <span class="read-original-arrow">→</span></a>
      </div>
      <div class="rank-card">
        <div class="rank-label" style="color:#fcd34d;">&#128200; 趋势解读</div>
        <div style="font-size:10px; color:var(--text-secondary); line-height:1.6;">
          <p><strong>Claude Skills 横扫半壁江山</strong> 6 月上中旬至少 8 个 .claude/skills 项目登榜。mattpocock 月增 71K、addyosmani 9.3K/周、taste-skill 月增 26K。Skills 成为"AI 时代的 npm 包"。</p>
          <p><strong>Token 压缩 + Agent 安全双主线</strong> headroom 6 种算法省 60-95% Token，NVIDIA SkillSpector 检测 64 种漏洞。Agent 从"能用"走向"安心的用"。</p>
          <p><strong>开源模型价格战</strong> Arcee $0.90/M vs Opus $25/M（便宜 96%），小米 MiMo $0.40/M。性能追平的同时成本断崖式下降。</p>
          <p style="margin-top:6px; color:#fcd34d;">💡 Skills 生态 + Agent 安全 + 成本悬崖 = 2026 年 6 月三大技术主线</p>
        </div>
      </div>
    </div>
  </div>'''

start = html.find('<div class="section-gap section-indigo" id="section-models">')
end = html.find('<footer class="footer">')
html = html[:start] + content + '\n' + html[end:]

now = datetime.datetime.now()
html = re.sub(r'<span class="hero-badge-text" id="editionLabel">.*?</span>', f'<span class="hero-badge-text" id="editionLabel">午间版 &#183; {now.strftime("%H:%M")} &#183; 增量更新</span>', html)
html = re.sub(r'<p class="hero-date" id="dateLabel">.*?</p>', f'<p class="hero-date" id="dateLabel">{now.strftime("%Y年%m月%d日")} &#183; 星期一</p>', html)
html = re.sub(r'<p class="hero-updated" id="updatedLabel">.*?</p>', f'<p class="hero-updated" id="updatedLabel"><span class="hero-updated-dot"></span> 最后更新: {now.strftime("%Y-%m-%d %H:%M")} CST</p>', html)
tldr = 'Anthropic发布Fable5/Mythos5同时警告80%代码已由AI自写；MiniMax启动A股上市ARR超3亿美元M3即将发布；Arcee 30人团队打造399B开源模型成本仅Opus 4%；Ai2开源MolmoWeb视觉Web Agent；三部门印发智能体规范19个典型场景定义；五巨头决战企业级Agent「硅基员工」时代。'
html = re.sub(r'<span class="tldr-text" id="tldrContent">.*?</span>', f'<span class="tldr-text" id="tldrContent">{tldr}</span>', html, flags=re.DOTALL)

with open('archive/2026-06-15-noon.html', 'w', encoding='utf-8') as f:
    f.write(html)
print(f'Built: {len(html)} bytes | Placeholders: {html.count(chr(34)+"#" + chr(34) + " class=" + chr(34) + "read-original")}')
