import os
import re

# 新版日历代码（用于 archive 目录，无 archive/ 前缀）
new_calendar_block = '''  // Calendar
  const archiveMap = {
    "2026-06-14": ["morning"],
    "2026-06-15": ["noon", "evening"],
    "2026-06-16": "full",
    "2026-06-17": ["morning"],
    "2026-06-18": ["morning", "noon"],
    "2026-06-22": ["morning"],
    "2026-06-23": ["morning"],
    "2026-06-24": ["morning"]
  };
  (function(){for(var d in archiveMap){if(Array.isArray(archiveMap[d])&&archiveMap[d].length>=3)archiveMap[d]='full';}})();

  const monthLabel = document.getElementById('calMonth');
  const calGrid = document.getElementById('calGrid');
  const overlay = document.getElementById('archiveOverlay');
  let calYear = new Date().getFullYear();
  let calMonth = new Date().getMonth() + 1;

  function renderCalendar() {
    const daysInMonth = new Date(calYear, calMonth, 0).getDate();
    const firstDay = new Date(calYear, calMonth - 1, 1).getDay();
    const adjustedFirst = firstDay === 0 ? 6 : firstDay - 1;
    const today = new Date();
    const todayStr = today.getFullYear() + '-' + String(today.getMonth()+1).padStart(2,'0') + '-' + String(today.getDate()).padStart(2,'0');

    monthLabel.textContent = calYear + '年' + calMonth + '月';

    let html2 = '';
    const dows = ['一','二','三','四','五','六','日'];
    dows.forEach(d => html2 += '<div class="cal-dow">' + d + '</div>');

    for (let i = 0; i < adjustedFirst; i++) html2 += '<div class="cal-day"></div>';

    for (let d = 1; d <= daysInMonth; d++) {
      const ds = calYear + '-' + String(calMonth).padStart(2,'0') + '-' + String(d).padStart(2,'0');
      const entry = archiveMap[ds];
      let cls = 'cal-day';
      if (entry) {
        cls += entry === 'full' ? ' full has-archive' : ' has-archive';
      }
      if (ds === todayStr) cls += ' today';

      html2 += '<div class="' + cls + '"';
      if (entry) {
        html2 += ' data-date="' + ds + '"';
        html2 += ' style="cursor:pointer"';
      }
      html2 += '>' + d;
      if (entry && entry !== 'full' && Array.isArray(entry)) {
        html2 += '<div class="cal-day-editions">';
        entry.forEach(function(ed) {
          html2 += '<span class="cal-edition-dot ' + ed + '"></span>';
        });
        html2 += '</div>';
      }
      html2 += '</div>';
    }

    calGrid.innerHTML = html2;

    calGrid.querySelectorAll('.has-archive').forEach(function(el) {
      el.addEventListener('click', function() {
        const date = el.getAttribute('data-date');
        const entry = archiveMap[date];
        if (entry === 'full') {
          window.open(date + '-morning.html', '_blank');
        } else if (Array.isArray(entry) && entry.length > 0) {
          window.open(date + '-' + entry[0] + '.html', '_blank');
        }
      });
    });
  }

  document.getElementById('btnArchive').addEventListener('click', function() {
    overlay.classList.add('open');
    calYear = new Date().getFullYear();
    calMonth = new Date().getMonth() + 1;
    renderCalendar();
  });
  document.getElementById('calPrev').addEventListener('click', function() {
    calMonth--; if (calMonth < 1) { calMonth = 12; calYear--; }
    renderCalendar();
  });
  document.getElementById('calNext').addEventListener('click', function() {
    calMonth++; if (calMonth > 12) { calMonth = 1; calYear++; }
    renderCalendar();
  });
  document.getElementById('calClose').addEventListener('click', function() {
    overlay.classList.remove('open');
  });
  overlay.addEventListener('click', function(e) {
    if (e.target === overlay) overlay.classList.remove('open');
  });'''

# 新版日历 CSS
new_calendar_css = '''  .cal-dow { font-size:11px; color:var(--text-tertiary); padding:4px 0; }
  .cal-day { font-size:13px; padding:8px 4px; border-radius:8px; cursor:default; position:relative; color:var(--text-tertiary); }
  .cal-day.has-archive { color:var(--text-primary); background:rgba(99,102,241,0.08); cursor:pointer; transition:background 0.2s; }
  .cal-day.has-archive:hover { background:rgba(99,102,241,0.2); }
  .cal-day.full { background:rgba(34,197,94,0.12); color:#4ade80; font-weight:600; }
  .cal-day.full:hover { background:rgba(34,197,94,0.25); }
  .cal-day.today { border:1px solid var(--accent-indigo); }
  .cal-day-editions { display:flex; gap:2px; justify-content:center; margin-top:2px; }
  .cal-edition-dot { width:6px; height:6px; border-radius:50%; }
  .cal-edition-dot.morning { background:#f59e0b; }
  .cal-edition-dot.noon { background:#06b6d4; }
  .cal-edition-dot.evening { background:#8b5cf6; }'''

files_to_fix = [
    'archive/2026-06-14-morning.html',
    'archive/2026-06-15-evening.html',
    'archive/2026-06-15-noon.html',
    'archive/2026-06-16-evening.html',
    'archive/2026-06-16-morning.html',
    'archive/2026-06-16-noon.html',
    'archive/2026-06-17-morning.html',
    'archive/2026-06-18-morning.html',
    'archive/2026-06-18-noon.html',
    'archive/2026-06-22-morning.html',
]

for filepath in files_to_fix:
    print(f"Processing {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 替换旧版日历 CSS
    content = re.sub(
        r'  \.calendar-day-header \{[^}]+\}\s*\n'
        r'  \.calendar-day \{[^}]+\}\s*\n'
        r'  \.calendar-day:hover \{[^}]+\}\s*\n'
        r'  \.calendar-day\.today \{[^}]+\}\s*\n'
        r'  \.calendar-day\.has-content \{[^}]+\}\s*\n'
        r'  \.calendar-day\.full \{[^}]+\}\s*\n'
        r'  \.calendar-day\.partial \{[^}]+\}\s*\n'
        r'  \.calendar-day\.other-month \{[^}]+\}',
        new_calendar_css,
        content
    )

    # 替换旧版日历 JS：找到整个 (function() { ... })(); 块
    # 模式：从 "(function() {" 开始，包含 "archiveMap"，到 "})();" 结束
    pattern = r'\(function\(\)\s*\{[\s\S]*?const archiveMap[\s\S]*?\}\)\(\);'
    content = re.sub(pattern, new_calendar_block, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  Fixed {filepath}")

print("Done!")
