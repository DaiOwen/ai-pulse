#!/usr/bin/env python3
"""Build noon edition HTML by replacing content sections in the template."""
import re, datetime

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ===== NEW CONTENT =====

models_section = '''  <div class="section-gap section-indigo" id="section-models">
    <div class="section-head">
      <div class="section-line"></div>
      <span class="section-label">大模型动态</span>
      <span class="section-label-cn">Models</span>
    </div>

    <div class="feature-card">
      <div class="card-row">
        <div class="card-body">
          <div class="card-tag" style="color:#6366f1;">HEADLINE</div>
          <div class="card-title">智谱 GLM-5.2 正式发布：百万上下文全量开放，港股暴涨超 30%</div>
          <div class="card-desc">6 月 15 日，智谱华章通过港交所公告正式推出旗舰大模型 GLM-5.2。1M 超长上下文窗口，MIT 协议开源，API 和开源权重将于下周正式上线。此前因美国出口管制 Anthropic Fable 5 / Mythos 5 被禁，GLM-5.2 成为最直接的国产替代选项——智谱港股当日暴涨超 30%，带动联想、英诺赛科等 AI 产业链集体走高。东方证券指出智谱正沿"代码增强→Agent化→长时任务→自主操作系统"路径演进。</div>
          <div class="card-meta"><span>36氪 / 证券时报</span><span>&#183;</span><span>6月15日</span><span>&#183;</span><span class="card-meta-link">多源报道</span><span>&#183;</span><a href="https://36kr.com/newsflashes/3853947992921094" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
          <div style="margin-top:8px; font-size:9px; color:#a5b4fc;">💡 开发者影响：MIT 开源百万上下文模型即将可用，国产替代窗口已打开</div>
        </div>
        <div class="card-icon">&#9889;</div>
      </div>
    </div>

    <div class="sub-grid">
      <div class="sub-card">
        <div class="sub-tag" style="color:#a5b4fc;">行业警示 · 开源合规</div>
        <div class="sub-title">巴西 "黑马模型" Rio 3.5 一夜翻车：套壳缝合国产模型</div>
        <div class="sub-desc">巴西里约热内卢市政府旗下 IT 公司推出的 Rio 3.5 397B 一度刷屏，号称超越 Qwen 3.7 Plus。不到 24 小时即被 Nex-AGI 团队数学分析揭穿：Rio 3.5 ≈ 0.6×Nex N2 Pro + 0.4×Qwen 3.5，实为权重拼接缝合模型。事件暴露了开源社区在署名和致谢方面的规范缺失，也验证了国产模型（千问系列）的真实实力。</div>
        <div style="margin-top:6px; font-size:8px; color:var(--text-tertiary);">PConline · 6月15日</div>
        <div style="margin-top:4px; font-size:8px; color:#a5b4fc;">💡 开发者影响：选择开源模型需验证来源，权重拼接难逃数学检测</div>
        <a href="https://g.pconline.com.cn/x/2172/21729944.html" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a>
      </div>
    </div>
  </div>'''

tools_section = '''  <div class="section-gap section-green" id="section-tools">
    <div class="section-head">
      <div class="section-line"></div>
      <span class="section-label">工具 & 部署</span>
      <span class="section-label-cn">Tools & Deploy</span>
    </div>

    <div class="tool-row">
      <div class="tool-card">
        <div class="tool-icon">&#128187;</div>
        <div class="tool-name">小米 MiMo Code</div>
        <div class="tool-desc">6 月 11 日开源，MIT 协议终端 AI 编程助手。持久记忆系统（SQLite+多层文件结构）解决长会话失忆，Compose 编排模式支持 200+ 步骤任务。SWE-bench Verified 82% vs Claude Code 79%。一键安装：curl -fsSL https://mimo.xiaomi.com/install | bash。GitHub 已获 6.4K+ Stars。</div>
        <span class="tool-badge badge-new">开源 MIT</span>
        <a href="https://venturebeat.com/technology/xiaomis-new-open-source-agentic-ai-coding-harness-mimo-code-beats-claude-code-at-ultra-long-200-step-tasks" class="read-original" target="_blank" rel="noopener" style="display:block;">阅读原文 <span class="read-original-arrow">→</span></a>
      </div>
      <div class="tool-card">
        <div class="tool-icon">&#127942;</div>
        <div class="tool-name">Kimi K2.7 Code</div>
        <div class="tool-desc">Moonshot AI 6 月 12 日开源编码 Agent 模型。1 万亿参数 MoE（32B 激活），Modified MIT 许可。MCP 多服务器协同评分 81.1% 超 Claude Opus 4.8（76.4%）。推理 Token 消耗比 K2.6 降 30%，输入 $0.95/百万 token。</div>
        <span class="tool-badge badge-new">开源</span>
        <a href="https://pc.watch.impress.co.jp/docs/news/2116913.html" class="read-original" target="_blank" rel="noopener" style="display:block;">阅读原文 <span class="read-original-arrow">→</span></a>
      </div>
    </div>
  </div>'''

policy_section = '''  <div class="section-gap section-amber" id="section-policy">
    <div class="section-head">
      <div class="section-line"></div>
      <span class="section-label">政策 & 合规</span>
      <span class="section-label-cn">Policy & Compliance</span>
    </div>

    <div class="sub-grid">
      <div class="sub-card">
        <div class="sub-tag" style="color:#fcd34d;">国家战略 · 6月10日</div>
        <div class="sub-title">工信部发布「人工智能+信息通信」三年实施意见，正式确立智能体战略地位</div>
        <div class="sub-desc">6 月 10 日，工信部发布《"人工智能+信息通信"创新发展实施意见（2026-2028 年）》。核心要点：建设 400G/800G 骨干传输网络、构建城域算力 1 毫秒时延圈、突破光电芯片与 CPO 技术破解"内存墙"。首次在国家级政策中明确"智能体"定位——到 2028 年形成 30+ 高价值典型场景。同期，长安汽车天枢大模型通过国家生成式 AI 备案（重庆首家）。</div>
        <div style="margin-top:6px; font-size:8px; color:var(--text-tertiary);">工信部 / 人民网 · 6月10日</div>
        <div style="margin-top:4px; font-size:8px; color:#fcd34d;">💡 开发者影响：智能体获国家级政策背书，算力基建提速利好推理部署</div>
        <a href="http://cq.people.com.cn/n2/2026/0606/c365402-41603081.html" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a>
      </div>
    </div>
  </div>'''

cases_section = '''  <div class="section-gap section-cyan" id="section-cases">
    <div class="section-head">
      <div class="section-line"></div>
      <span class="section-label">应用落地</span>
      <span class="section-label-cn">Real-World AI</span>
    </div>

    <div class="dual-cards">
      <div class="rank-card">
        <div class="rank-label" style="color:#67e8f9;">&#127981; 智能汽车 · 全行业上车</div>
        <div style="font-size:14px; font-weight:500; color:var(--text-primary); margin-bottom:6px;">"大模型上车"进入深水区：理想小鹏蔚来已全量推送，长安获批备案</div>
        <div style="font-size:10px; color:var(--text-secondary); line-height:1.5; margin-bottom:8px;">国内主流车企已完成大模型初步布局：理想 MindGPT、小鹏灵犀大模型、蔚来 NOMI GPT 已全量推送上车；长安天枢大模型成为重庆首家获国家生成式 AI 备案的车企；吉利星睿、广汽 AI 大模型已接入量产车型；华为盘古大模型全面赋能问界/智界。大模型正从"有"走向"好用"，智能座舱交互和自动驾驶辅助成为两大核心落地场景。</div>
        <div style="font-size:8px; color:var(--text-tertiary);">证券时报 / 人民网 · 6月上旬</div>
        <div style="margin-top:4px; font-size:8px; color:#67e8f9;">💡 开发者影响：车载 AI 赛道正式开放，多模态交互+备案合规成入场门槛</div>
        <a href="https://stcn.com/article/detail/3948517.html" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a>
      </div>
    </div>
  </div>'''

oss_section = '''  <div class="section-gap section-amber" id="section-oss">
    <div class="section-head">
      <div class="section-line"></div>
      <span class="section-label">开源热度</span>
      <span class="section-label-cn">Open Source Pulse</span>
    </div>

    <div class="dual-cards">
      <div class="rank-card">
        <div class="rank-label" style="color:#fcd34d;">&#128200; GitHub Trending — AI 领域 Top 5（W24-25）</div>
        <div class="rank-row"><span class="rank-num">1</span><span class="rank-name">mvanhorn/last30days-skill</span><span class="rank-stat rank-up">+12K stars/周</span></div>
        <div class="rank-row"><span class="rank-num">2</span><span class="rank-name">chopratejas/headroom</span><span class="rank-stat rank-up">+10K stars/周</span></div>
        <div class="rank-row"><span class="rank-num">3</span><span class="rank-name">addyosmani/agent-skills</span><span class="rank-stat rank-up">+9.3K stars/周</span></div>
        <div class="rank-row"><span class="rank-num">4</span><span class="rank-name">Leonxlnx/taste-skill</span><span class="rank-stat rank-up">+8.7K stars/周</span></div>
        <div class="rank-row"><span class="rank-num">5</span><span class="rank-name">apple/container</span><span class="rank-stat rank-up">+7.8K stars/周</span></div>
        <a href="https://github.com/trending?since=weekly" class="read-original" target="_blank" rel="noopener">查看完整榜单 <span class="read-original-arrow">→</span></a>
      </div>
      <div class="rank-card">
        <div class="rank-label" style="color:#fcd34d;">&#128200; 趋势解读</div>
        <div style="font-size:10px; color:var(--text-secondary); line-height:1.6;">
          <p><strong>Claude Skills 成新包管理范式</strong> 至少 8 个 .claude/skills 项目同时登榜，SKILL.md + manifest + 脚本被类比为"AI 时代的 npm 包"。</p>
          <p><strong>Agent 安全从可选变标配</strong> NVIDIA SkillSpector 覆盖 16 类 64 种漏洞模式，微软 MXC 沙箱提供策略驱动隔离。</p>
          <p><strong>Token 压缩赛道火热</strong> headroom 6 种压缩算法减少 60-95% Token，背景是 GitHub Copilot 刚切换按 Token 计费。</p>
          <p><strong>大厂密集入局开源</strong> Apple 开源容器工具，NVIDIA 开源物理 AI 技能，小米 MiMo Code MIT 开源。</p>
          <p style="margin-top:6px; color:#fcd34d;">💡 Skills 生态 + Token 优化 + Agent 安全 = 6 月三大技术主线</p>
        </div>
      </div>
    </div>
  </div>'''

# Replace content between first section and footer
start = html.find('<div class="section-gap section-indigo" id="section-models">')
end = html.find('<footer class="footer">')

if start > 0 and end > start:
    new_body = models_section + '\n' + tools_section + '\n' + policy_section + '\n' + cases_section + '\n' + oss_section + '\n'
    html = html[:start] + new_body + html[end:]

# Update hero
now = datetime.datetime.now()
html = html.replace(
    '<span class="hero-badge-text" id="editionLabel">午间版 &#183; 12:00 &#183; 增量更新</span>',
    f'<span class="hero-badge-text" id="editionLabel">午间版 &#183; {now.strftime("%H:%M")} &#183; 增量更新</span>'
)
html = html.replace(
    '<p class="hero-date" id="dateLabel">2026年6月15日 &#183; 星期一</p>',
    f'<p class="hero-date" id="dateLabel">{now.strftime("%Y年%m月%d日")} &#183; 星期一</p>'
)
html = html.replace(
    '<span class="hero-updated-dot"></span> 最后更新: 2026-06-15 12:00 CST',
    f'<span class="hero-updated-dot"></span> 最后更新: {now.strftime("%Y-%m-%d %H:%M")} CST'
)

# Update TL;DR
old_tldr = r'<span class="tldr-text" id="tldrContent">.*?</span>'
new_tldr = '<span class="tldr-text" id="tldrContent">智谱GLM-5.2全量开放百万上下文+MIT开源，港股暴涨30%国产替代窗口打开；巴西Rio 3.5套壳国产模型一夜翻车引开源合规警示；小米MiMo Code开源(MIT)SWE-bench超Claude Code；Kimi K2.7 Code万亿MoE开源MCP评分超Opus 4.8；工信部确立智能体国家战略地位；车企大模型全行业上车。</span>'
html = re.sub(old_tldr, new_tldr, html, flags=re.DOTALL)

# Update stats
html = html.replace('id="statNews">7<', 'id="statNews">7<')
html = html.replace('id="statSources">8<', 'id="statSources">8<')
html = html.replace('id="statPapers">0<', 'id="statPapers">0<')

# Update footer quote
html = html.replace('"The best way to predict the future is to invent it."', '"AI 不会取代人类，但会用 AI 的人类会取代不会用 AI 的人类。"')
html = html.replace('Alan Kay', '李开复')

with open('archive/2026-06-15-noon.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Noon edition built successfully')
print(f'Filesize: {len(html)} bytes')

# Verify no placeholders
if 'href="#" class="read-original' in html:
    print('WARNING: placeholder href="#" still present!')
else:
    print('All read-original links have real URLs')
