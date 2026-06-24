# 产品优化计划 / Product Optimization Roadmap

> 基于产品经理评审建议，逐步提升用户体验和系统健壮性。

---

## 📊 总览

| 阶段 | 功能 | 状态 | 预计工作量 | 优先级 |
|------|------|:----:|:----------:|:------:|
| Phase 1 | 返回顶部按钮 | ✅ 已完成 | 10分钟 | P0 |
| Phase 2 | 收藏功能 | ✅ 已完成 | 1小时 | P0 |
| Phase 3 | 分享功能 | ✅ 已完成 | 1小时 | P0 |
| Phase 4 | 快捷键支持 | ✅ 已完成 | 30分钟 | P1 |
| Phase 3 | 分享功能 | ⏳ 待开始 | 1小时 | P0 |
| Phase 4 | 快捷键支持 | ⏳ 待开始 | 30分钟 | P1 |
| Phase 5 | 网络容错机制 | ⏳ 待开始 | 2小时 | P0 |
| Phase 6 | 搜索功能 | ⏳ 待开始 | 3小时 | P1 |
| Phase 7 | 个性化标签 | ⏳ 待开始 | 2小时 | P2 |

**总预计工作量：约 9-10 小时**

---

## Phase 1: 返回顶部按钮 ⏳

### 背景
长页面浏览时，用户需要快速返回顶部查看导航或 TL;DR。

### 需求
- 滚动超过一屏后显示「返回顶部」按钮
- 点击后平滑滚动到页面顶部
- 支持暗/亮双主题

### 技术方案
```html
<!-- 在 footer 前添加 -->
<button id="backToTop" class="back-to-top" title="返回顶部">↑</button>

<style>
.back-to-top {
  position: fixed;
  bottom: 24px;
  right: 24px;
  width: 44px;
  height: 44px;
  border-radius: 50%;
  background: linear-gradient(135deg, #6366f1, #8b5cf6);
  color: #fff;
  border: none;
  font-size: 18px;
  cursor: pointer;
  opacity: 0;
  visibility: hidden;
  transition: all 0.3s ease;
  box-shadow: 0 4px 16px rgba(99,102,241,0.3);
  z-index: 99;
}
.back-to-top.visible {
  opacity: 1;
  visibility: visible;
}
.back-to-top:hover {
  transform: translateY(-3px);
  box-shadow: 0 6px 24px rgba(99,102,241,0.4);
}
</style>

<script>
const backToTop = document.getElementById('backToTop');
window.addEventListener('scroll', () => {
  backToTop.classList.toggle('visible', window.scrollY > 500);
});
backToTop.addEventListener('click', () => {
  window.scrollTo({ top: 0, behavior: 'smooth' });
});
</script>
```

### 验收标准
- [ ] 滚动超过 500px 时按钮出现
- [ ] 点击后平滑滚动到顶部
- [ ] 暗色/亮色模式下均可见

---

## Phase 2: 收藏功能 ⏳

### 背景
用户希望保存感兴趣的条目，方便后续查阅。

### 需求
- 每条新闻旁显示收藏按钮（空心星 → 实心星）
- 收藏数据存储在 LocalStorage
- 新增「我的收藏」页面展示已收藏内容
- 导航栏增加收藏入口

### 技术方案

#### 2.1 数据结构
```javascript
// LocalStorage key: ai-pulse-favorites
// 数据结构
{
  "news-glasswing-20260624": {
    title: "Anthropic 发布 Project Glasswing...",
    url: "https://venturebeat.com/...",
    source: "VentureBeat",
    date: "2026-06-24",
    savedAt: "2026-06-24T20:30:00Z"
  }
}
```

#### 2.2 收藏按钮组件
```html
<button class="favorite-btn" data-id="news-glasswing-20260624" onclick="toggleFavorite(this)">
  <span class="favorite-icon">☆</span>
</button>

<style>
.favorite-btn {
  background: none;
  border: none;
  cursor: pointer;
  font-size: 18px;
  padding: 4px;
  transition: transform 0.2s;
}
.favorite-btn:hover { transform: scale(1.2); }
.favorite-btn.active .favorite-icon { color: #f59e0b; }
.favorite-btn.active .favorite-icon::before { content: '★'; }
</style>
```

#### 2.3 JavaScript 逻辑
```javascript
// 收藏/取消收藏
function toggleFavorite(btn) {
  const id = btn.dataset.id;
  const favorites = JSON.parse(localStorage.getItem('ai-pulse-favorites') || '{}');
  
  if (favorites[id]) {
    delete favorites[id];
    btn.classList.remove('active');
  } else {
    favorites[id] = {
      title: btn.closest('.feature-card, .sub-card').querySelector('.card-title, .sub-title').textContent,
      url: btn.closest('.feature-card, .sub-card').querySelector('.read-original')?.href || '#',
      source: btn.closest('.feature-card, .sub-card').querySelector('.card-meta span')?.textContent || '',
      date: document.querySelector('.hero-date')?.textContent || '',
      savedAt: new Date().toISOString()
    };
    btn.classList.add('active');
  }
  
  localStorage.setItem('ai-pulse-favorites', JSON.stringify(favorites));
  updateFavoriteCount();
}

// 页面加载时恢复收藏状态
function restoreFavorites() {
  const favorites = JSON.parse(localStorage.getItem('ai-pulse-favorites') || '{}');
  document.querySelectorAll('.favorite-btn').forEach(btn => {
    if (favorites[btn.dataset.id]) {
      btn.classList.add('active');
    }
  });
  updateFavoriteCount();
}
```

#### 2.4 收藏页面 favorites.html
```html
<!-- 展示所有收藏的新闻列表 -->
<!-- 支持删除、按日期排序 -->
```

### 验收标准
- [ ] 点击收藏按钮可切换收藏状态
- [ ] 刷新页面后收藏状态保留
- [ ] 导航栏显示收藏数量
- [ ] 收藏页面可查看和管理收藏

---

## Phase 3: 分享功能 ⏳

### 背景
用户希望分享单条新闻给同事或朋友。

### 需求
- 每条新闻增加「复制链接」按钮
- 链接格式：`https://daiowen.github.io/ai-pulse/#news-{id}`
- 复制成功后显示提示
- 支持分享到微信（生成二维码）

### 技术方案

#### 3.1 锚点 ID
```html
<div id="news-glasswing-20260624" class="feature-card">
  ...
</div>
```

#### 3.2 分享按钮
```html
<button class="share-btn" onclick="shareNews('news-glasswing-20260624')">
  🔗 复制链接
</button>

<style>
.share-btn {
  font-size: 11px;
  color: var(--text-tertiary);
  background: none;
  border: none;
  cursor: pointer;
  padding: 4px 8px;
  border-radius: 4px;
  transition: all 0.2s;
}
.share-btn:hover {
  color: var(--accent-indigo);
  background: rgba(99,102,241,0.1);
}
</style>
```

#### 3.3 JavaScript 逻辑
```javascript
function shareNews(newsId) {
  const url = `${window.location.origin}${window.location.pathname}#${newsId}`;
  
  navigator.clipboard.writeText(url).then(() => {
    showToast('链接已复制到剪贴板');
  }).catch(() => {
    // 降级方案
    const input = document.createElement('input');
    input.value = url;
    document.body.appendChild(input);
    input.select();
    document.execCommand('copy');
    document.body.removeChild(input);
    showToast('链接已复制到剪贴板');
  });
}

function showToast(message) {
  const toast = document.createElement('div');
  toast.className = 'toast';
  toast.textContent = message;
  toast.style.cssText = `
    position: fixed; bottom: 80px; left: 50%; transform: translateX(-50%);
    background: rgba(34,197,94,0.9); color: #fff; padding: 8px 16px;
    border-radius: 8px; font-size: 13px; z-index: 1000;
    animation: fadeInOut 2s ease forwards;
  `;
  document.body.appendChild(toast);
  setTimeout(() => toast.remove(), 2000);
}
```

#### 3.4 页面加载时跳转到锚点
```javascript
// 页面加载时如果有 hash，滚动到对应新闻
window.addEventListener('load', () => {
  if (window.location.hash) {
    const target = document.querySelector(window.location.hash);
    if (target) {
      setTimeout(() => {
        target.scrollIntoView({ behavior: 'smooth', block: 'center' });
        target.style.boxShadow = '0 0 0 2px var(--accent-indigo)';
        setTimeout(() => target.style.boxShadow = '', 3000);
      }, 500);
    }
  }
});
```

### 验收标准
- [ ] 点击复制链接后显示成功提示
- [ ] 分享链接可直接跳转到对应新闻
- [ ] 跳转后高亮显示目标新闻

---

## Phase 4: 快捷键支持 ⏳

### 背景
效率用户希望使用键盘快速导航。

### 需求
- `J` / `↓`：滚动到下一条新闻
- `K` / `↑`：滚动到上一条新闻
- `/`：聚焦搜索框（如果有）
- `T`：切换主题
- `Esc`：关闭弹窗

### 技术方案
```javascript
document.addEventListener('keydown', (e) => {
  // 忽略输入框内的按键
  if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') {
    if (e.key === 'Escape') e.target.blur();
    return;
  }
  
  const newsItems = document.querySelectorAll('.feature-card, .sub-card');
  const currentPosition = Array.from(newsItems).findIndex(item => {
    const rect = item.getBoundingClientRect();
    return rect.top >= 0 && rect.top < window.innerHeight / 2;
  });
  
  switch(e.key.toLowerCase()) {
    case 'j':
    case 'arrowdown':
      e.preventDefault();
      if (currentPosition < newsItems.length - 1) {
        newsItems[currentPosition + 1].scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
      break;
    case 'k':
    case 'arrowup':
      e.preventDefault();
      if (currentPosition > 0) {
        newsItems[currentPosition - 1].scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
      break;
    case 't':
      document.getElementById('themeToggle').click();
      break;
    case '/':
      e.preventDefault();
      // 如果有搜索框则聚焦
      const searchInput = document.getElementById('searchInput');
      if (searchInput) searchInput.focus();
      break;
  }
});
```

### 快捷键提示
```html
<!-- 在页面底部添加快捷键提示 -->
<div class="shortcuts-hint">
  <span><kbd>J</kbd>/<kbd>K</kbd> 导航</span>
  <span><kbd>T</kbd> 切换主题</span>
  <span><kbd>/</kbd> 搜索</span>
</div>
```

### 验收标准
- [ ] J/K 可上下导航新闻
- [ ] T 可切换主题
- [ ] 输入框内按键不触发快捷键
- [ ] 页面显示快捷键提示

---

## Phase 5: 网络容错机制 ⏳

### 背景
WebSearch/WebFetch 可能因网络限制而失败，导致无法生成新内容。

### 需求
- 搜索失败时显示友好提示
- 提供降级方案（如 GitHub Trending API）
- 生成「回顾版」而非空页面

### 技术方案

#### 5.1 修改 CLAUDE.md 流程
```markdown
### 第1步：搜索（带容错）

**主搜索**：WebSearch → 如果失败 → **降级搜索**
**降级搜索**：
1. GitHub Trending API（更稳定）
2. 本地历史数据抽取

**如果所有搜索失败**：
- 生成「回顾版」页面
- 展示最近 3 天归档中的热门内容
- 标注「网络受限模式」
```

#### 5.2 容错 HTML 模板
```html
<div class="error-notice">
  <div class="error-icon">⚠️</div>
  <div class="error-title">网络受限模式</div>
  <div class="error-desc">
    由于网络原因，无法获取最新内容。以下为近期热门回顾。
  </div>
</div>

<style>
.error-notice {
  background: rgba(245,158,11,0.1);
  border: 1px solid rgba(245,158,11,0.3);
  border-radius: 12px;
  padding: 16px 20px;
  margin-bottom: 24px;
  display: flex;
  align-items: center;
  gap: 16px;
}
.error-icon { font-size: 24px; }
.error-title { font-size: 15px; font-weight: 600; color: #fbbf24; }
.error-desc { font-size: 13px; color: var(--text-secondary); }
</style>
```

### 验收标准
- [ ] WebSearch 失败时尝试降级方案
- [ ] 所有方案失败时生成「回顾版」
- [ ] 页面明确标注「网络受限模式」

---

## Phase 6: 搜索功能 ⏳

### 背景
用户希望搜索历史各期内容，追踪特定话题。

### 需求
- 全文搜索所有归档内容
- 支持关键词高亮
- 显示搜索结果来源日期
- 使用 lunr.js 实现纯前端搜索

### 技术方案

#### 6.1 生成搜索索引
```javascript
// 在生成 HTML 时，同时生成 search-index.json
{
  "documents": [
    {
      "id": "2026-06-24-glasswing",
      "title": "Anthropic 发布 Project Glasswing",
      "content": "首个因过于危险被限制发布的AI模型...",
      "date": "2026-06-24",
      "edition": "evening",
      "url": "archive/2026-06-24-evening.html#news-glasswing"
    }
  ]
}
```

#### 6.2 搜索页面 search.html
```html
<div class="search-container">
  <input type="text" id="searchInput" placeholder="搜索历史内容..." />
  <div id="searchResults"></div>
</div>

<script src="https://unpkg.com/lunr/lunr.min.js"></script>
<script>
// 加载索引并初始化 lunr
let idx;
fetch('search-index.json')
  .then(res => res.json())
  .then(data => {
    idx = lunr(function() {
      this.ref('id');
      this.field('title');
      this.field('content');
      data.documents.forEach(doc => this.add(doc));
    });
    window.searchData = data.documents;
  });

function performSearch(query) {
  const results = idx.search(query);
  const resultsHtml = results.map(r => {
    const doc = searchData.find(d => d.id === r.ref);
    return `
      <div class="search-result">
        <div class="result-date">${doc.date} ${doc.edition}</div>
        <a href="${doc.url}" class="result-title">${doc.title}</a>
      </div>
    `;
  }).join('');
  document.getElementById('searchResults').innerHTML = resultsHtml;
}
</script>
```

### 验收标准
- [ ] 可输入关键词搜索
- [ ] 搜索结果显示标题、日期、来源
- [ ] 点击结果跳转到对应页面锚点

---

## Phase 7: 个性化标签 ⏳

### 背景
用户希望只看自己关注的内容类别。

### 需求
- 首次访问时显示标签选择弹窗
- 用户可选择关注的板块
- LocalStorage 存储用户偏好
- 页面加载时优先显示关注的内容

### 技术方案

#### 7.1 标签选择弹窗
```html
<div id="tagModal" class="tag-modal">
  <div class="tag-modal-content">
    <h3>选择你感兴趣的内容</h3>
    <div class="tag-options">
      <label class="tag-option">
        <input type="checkbox" value="模型" checked />
        <span>🤖 大模型动态</span>
      </label>
      <label class="tag-option">
        <input type="checkbox" value="工具" checked />
        <span>🛠️ 工具 & 部署</span>
      </label>
      <!-- ... 其他标签 -->
    </div>
    <button onclick="saveTagPreferences()">保存偏好</button>
  </div>
</div>
```

#### 7.2 JavaScript 逻辑
```javascript
// 检查是否首次访问
if (!localStorage.getItem('ai-pulse-tags')) {
  document.getElementById('tagModal').classList.add('open');
}

function saveTagPreferences() {
  const tags = Array.from(document.querySelectorAll('.tag-option input:checked'))
    .map(input => input.value);
  localStorage.setItem('ai-pulse-tags', JSON.stringify(tags));
  document.getElementById('tagModal').classList.remove('open');
  highlightUserTags();
}

function highlightUserTags() {
  const userTags = JSON.parse(localStorage.getItem('ai-pulse-tags') || '[]');
  document.querySelectorAll('.section-gap').forEach(section => {
    const sectionName = section.querySelector('.section-label')?.textContent;
    if (userTags.some(tag => sectionName?.includes(tag))) {
      section.classList.add('highlighted');
    }
  });
}
```

### 验收标准
- [ ] 首次访问显示标签选择弹窗
- [ ] 用户偏好保存到 LocalStorage
- [ ] 关注的内容高亮或置顶显示

---

## 📈 进度追踪

| 日期 | 完成内容 | 备注 |
|------|----------|------|
| 2026-06-24 | Phase 1: 返回顶部按钮 | 已上线 |
| 2026-06-24 | Phase 2: 收藏功能 | 已上线，支持收藏/取消/管理 |
| 2026-06-24 | Phase 3: 分享功能 | 已上线，支持复制链接+锚点跳转 |
| 2026-06-24 | Phase 4: 快捷键支持 | 已上线，J/K导航 + T切换主题 |

---

## 🔄 变更日志

| 日期 | 变更内容 |
|------|----------|
| 2026-06-24 | 创建产品优化计划文档 |