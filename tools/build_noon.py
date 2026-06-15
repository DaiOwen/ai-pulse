#!/usr/bin/env python3
import re

with open('archive/2026-06-15-noon.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ===== NEW CONTENT FOR NOON EDITION =====

# 大模型动态: Lead (智谱 GLM-5.2) + 1 sub (星火 X2-VL)
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
          <div class="card-title">智谱 AI 开源 GLM-5.2：100 万 Token 上下文，MIT 许可证直击出口管制</div>
          <div class="card-desc">6 月 13 日，智谱 AI 宣布将于 6 月 20 日正式开源 GLM-5.2，采用 MIT 许可证。最大亮点是 100 万 token 超长上下文窗口——目前开源模型中最大。此举被广泛视为对美国 AI 出口管制（迫使 Anthropic 封锁 Fable 5 / Mythos 5 海外访问）的直接战略回应。现场演示了生成复杂 SVG 图形、Three.js + Cannon.js 3D 游戏、浏览器内迷你电子表格等编程能力。定价方面，API 调用仅为国际同类产品的约 2%。</div>
          <div class="card-meta"><span>Pandaily</span><span>&#183;</span><span>2天前</span><span>&#183;</span><span class="card-meta-link">多源报道</span><span>&#183;</span><a href="#" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a></div>
          <div style="margin-top:8px; font-size:9px; color:#a5b4fc;">💡 开发者影响：MIT 许可证百万上下文开源模型，可在国产硬件上自由商用部署</div>
        </div>
        <div class="card-icon">&#9889;</div>
      </div>
    </div>

    <div class="sub-grid">
      <div class="sub-card">
        <div class="sub-tag" style="color:#a5b4fc;">国产算力 · 全国产训练</div>
        <div class="sub-title">科大讯飞星火 X2-VL：纯国产算力训练，高考数学 148/150</div>
        <div class="sub-desc">6 月 11-13 日在无锡 2026 长三角机器人博览会上发布。采用自研 MoE 架构，100% 基于无锡「太湖星跃」国产算力平台训练，是当前唯一完全基于全国产算力训练的主流大模型。2026 高考数学全国 I 卷实测 148/150 分（由两位国家级数学名师阅卷），多学科图文题准确率接近 95%。</div>
        <div style="margin-top:6px; font-size:8px; color:var(--text-tertiary);">证券时报 · 6月13日</div>
        <div style="margin-top:4px; font-size:8px; color:#a5b4fc;">💡 开发者影响：国产算力训练路线验证可行，Inspire 生态开发者可优先适配</div>
        <a href="#" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a>
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
        <div class="tool-icon">&#128640;</div>
        <div class="tool-name">vLLM v0.20.0</div>
        <div class="tool-desc">正式升级至 CUDA 13.0 + PyTorch 2.11，PagedAttention 持续优化。RTX 4090 实测 50 并发用户下吞吐量达 Ollama 5.9 倍，p99 延迟仅 2.8 秒。支持 AWQ/GPTQ/FP8 量化，OpenAI 兼容 API 服务。每两周一个小版本，已成为 LLM 推理的事实标准引擎。</div>
        <span class="tool-badge badge-update">更新</span>
        <a href="#" class="read-original" target="_blank" rel="noopener" style="display:block;">阅读原文 <span class="read-original-arrow">→</span></a>
      </div>
      <div class="tool-card">
        <div class="tool-icon">&#127942;</div>
        <div class="tool-name">Claude Skills 生态爆发</div>
        <div class="tool-desc">6 月第 24 周 GitHub Trending 榜上至少 8 个 .claude/skills 相关项目同时上榜：mattpocock/skills（月+48K stars）、addyosmani/agent-skills（周+9.3K stars）、Leonxlnx/taste-skill（月+26K stars）。Skills 模块化正成为 AI 编码新范式——不再比模型大小，比谁能编排更多 Skills。</div>
        <span class="tool-badge badge-new">新范式</span>
        <a href="#" class="read-original" target="_blank" rel="noopener" style="display:block;">阅读原文 <span class="read-original-arrow">→</span></a>
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
        <div class="sub-tag" style="color:#fcd34d;">监管升级 · 6月12日</div>
        <div class="sub-title">中央网信办上线「涉 AI 应用乱象举报专区」，14 类问题可举报</div>
        <div class="sub-desc">6 月 12 日，中央网信办举报中心正式开设「涉 AI 应用乱象举报专区」，配合「清朗·整治 AI 应用乱象」专项行动。受理范围涵盖 14 类问题：未备案登记、语料安全、数据投毒、生成标识不到位、AI「魔改」经典、虚假信息、AI 水军等。举报渠道包括 12377 热线、www.12377.cn 网站及微信公众号「全国网络举报」。此举标志着 AI 监管从政策制定进入公众参与监督阶段。</div>
        <div style="margin-top:6px; font-size:8px; color:var(--text-tertiary);">新华网 / 人民网 · 6月12日</div>
        <div style="margin-top:4px; font-size:8px; color:#fcd34d;">💡 开发者影响：上线前务必完成备案登记，公众举报渠道已全面开启</div>
        <a href="#" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a>
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
        <div class="rank-label" style="color:#67e8f9;">&#127981; 企业级 Agent 平台</div>
        <div style="font-size:14px; font-weight:500; color:var(--text-primary); margin-bottom:6px;">腾讯 WorkBuddy 企业版发布：三一重工、中联重科、茶颜悦色已落地</div>
        <div style="font-size:10px; color:var(--text-secondary); line-height:1.5; margin-bottom:8px;">腾讯云发布 WorkBuddy 企业版，提出「专家→助理→团队」三层架构，让 AI 从 8 小时工具进化为 7×24 数字员工。三一重工用于无人矿卡远程操控与 AI 编程提效，中联重科用于工程图纸识别与文档检索，茶颜悦色打造 AI 面试与门店运营决策平台。SkillHub 生态已收录 7.7 万+ Skills，两月下载量超 3000 万。同期，销售易 NeoAgent 2.0 面向湖南千亿级制造业集群提供智能 CRM。</div>
        <div style="font-size:8px; color:var(--text-tertiary);">IT之家 · 6月12日</div>
        <div style="margin-top:4px; font-size:8px; color:#67e8f9;">💡 开发者影响：企业 Agent 从 Copilot 走向数字员工，Skill 模块化是入场券</div>
        <a href="#" class="read-original" target="_blank" rel="noopener">阅读原文 <span class="read-original-arrow">→</span></a>
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
        <div class="rank-label" style="color:#fcd34d;">&#128200; GitHub Trending — AI 领域 Top 5（2026 W24）</div>
        <div class="rank-row"><span class="rank-num">1</span><span class="rank-name">mvanhorn/last30days-skill</span><span class="rank-stat rank-up">+12K stars/周</span></div>
        <div class="rank-row"><span class="rank-num">2</span><span class="rank-name">chopratejas/headroom</span><span class="rank-stat rank-up">+10.6K stars/周</span></div>
        <div class="rank-row"><span class="rank-num">3</span><span class="rank-name">addyosmani/agent-skills</span><span class="rank-stat rank-up">+9.3K stars/周</span></div>
        <div class="rank-row"><span class="rank-num">4</span><span class="rank-name">apple/container</span><span class="rank-stat rank-up">+9.1K stars/周</span></div>
        <div class="rank-row"><span class="rank-num">5</span><span class="rank-name">Leonxlnx/taste-skill</span><span class="rank-stat rank-up">+8K stars/周</span></div>
        <a href="https://github.com/trending?since=weekly" class="read-original" target="_blank" rel="noopener">查看完整榜单 <span class="read-original-arrow">→</span></a>
      </div>
      <div class="rank-card">
        <div class="rank-label" style="color:#fcd34d;">&#128200; 趋势解读</div>
        <div style="font-size:10px; color:var(--text-secondary); line-height:1.6;">
          <p><strong>Claude Skills 生态爆发</strong> 6 月至少 8 个 .claude/skills 项目同时登榜，Skills 模块化正成为 AI 编码新范式。</p>
          <p><strong>Token 压缩赛道</strong> headroom 宣称可节省 60-95% Token 消耗，反映 Agent 工作流对成本优化的刚性需求。</p>
          <p><strong>Agent 安全标配</strong> NVIDIA SkillSpector（+3.6K stars）、微软 MXC 沙箱相继开源，Agent 安全从可选变为标配。</p>
          <p><strong>Mac 本地化</strong> apple/container 首次开源 Mac 端轻量 Linux 容器，本地 AI 开发工具链持续完善。</p>
          <p style="margin-top:6px; color:#fcd34d;">💡 Skills 模块化 + Token 压缩 + Agent 安全构成 6 月三大技术主线</p>
        </div>
      </div>
    </div>
  </div>'''

# Replace sections
def replace_section(html, section_id, new_content):
    pattern = r'<div class="section-gap[^"]*" id="' + section_id + r'">.*?</div>\s*</div>\s*</div>\s*(?:</div>\s*)?(?:</div>\s*)?'
    return re.sub(pattern, new_content, html, flags=re.DOTALL)

# Try a different approach - find and replace by markers
# Find start of first section
start_marker = '<div class="section-gap section-indigo" id="section-models">'
end_marker = '<footer class="footer">'

start_idx = html.find(start_marker)
end_idx = html.find(end_marker)

if start_idx > 0 and end_idx > start_idx:
    new_body = models_section + '\n' + tools_section + '\n' + policy_section + '\n' + cases_section + '\n' + oss_section + '\n'
    html = html[:start_idx] + new_body + html[end_idx:]

with open('archive/2026-06-15-noon.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Content sections replaced successfully')
print(f'File size: {len(html)} bytes')
