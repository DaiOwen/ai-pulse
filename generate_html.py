#!/usr/bin/env python3
"""
Generate AI Pulse HTML page from template + news JSON.
Usage: python3 fetch_news.py | python3 generate_html.py 2025-07-13 morning
Fallback: python3 generate_html.py 2025-07-13 morning --fallback
"""

import json
import sys
import os
import re
from datetime import datetime
from difflib import SequenceMatcher
from pathlib import Path

# ─── Edition config: section counts per edition ───────────────────────
EDITION_CONFIG = {
    "morning": {
        "models": 5, "tools": 4, "policy": 2, "applications": 2,
        "opensource": 5, "global": 3, "papers": 1, "industry": 2,
        "edition_cn": "早间", "time_label": "08:00 CST", "edition_upper": "MORNING",
    },
    "noon": {
        "models": 3, "tools": 2, "policy": 1, "applications": 1,
        "opensource": 5, "global": 0, "papers": 1, "industry": 2,
        "edition_cn": "午间", "time_label": "12:00 CST", "edition_upper": "NOON",
    },
    "evening": {
        "models": 5, "tools": 4, "policy": 2, "applications": 2,
        "opensource": 10, "global": 3, "papers": 1, "industry": 4,
        "edition_cn": "晚间", "time_label": "20:00 CST", "edition_upper": "EVENING",
    },
}

# ─── Source quality scores ────────────────────────────────────────────
SOURCE_QUALITY = {
    "量子位": 3, "36氪": 3, "TechCrunch": 3,
    "Solidot": 2, "雷锋网": 2, "Ars Technica": 2, "钛媒体": 2,
    "IT之家": 1, "Hacker News": 1, "The Verge": 1, "GitHub Trending": 1,
    "arXiv": 1,
}

# Category → HTML tag class mapping
CATEGORY_TAGS = {
    "model": ("tag-model", "模型"),
    "tool": ("tag-tool", "工具"),
    "industry": ("tag-industry", "产业"),
    "policy": ("tag-policy", "政策"),
    "paper": ("tag-paper", "论文"),
    "global": ("tag-global", "海外"),
    "application": ("tag-industry", "产业"),
    "opensource": ("tag-tool", "开源"),
}

# Section colors
SECTION_COLORS = {
    "models": "var(--accent-indigo)",
    "tools": "var(--accent-green)",
    "policy": "var(--accent-cyan)",
    "applications": "var(--accent-amber)",
    "opensource": "var(--accent-rose)",
    "global": "var(--accent-cyan)",
    "papers": "var(--accent-purple)",
    "industry": "var(--accent-amber)",
}

SECTION_ICONS = {
    "models": "🤖", "tools": "🛠️", "policy": "📜", "applications": "💼",
    "opensource": "🔥", "global": "🌍", "papers": "📄", "industry": "💰",
}

SECTION_CN = {
    "models": "大模型动态", "tools": "工具 & 部署", "policy": "政策 & 合规",
    "applications": "应用落地", "opensource": "开源热度", "global": "海外参考",
    "papers": "论文速递", "industry": "产业动态",
}

SECTION_EN = {
    "models": "MODEL UPDATES", "tools": "TOOLS & DEPLOY", "policy": "POLICY & COMPLIANCE",
    "applications": "APPLICATIONS", "opensource": "OPEN SOURCE TRENDING",
    "global": "GLOBAL PERSPECTIVE", "papers": "PAPER SPOTLIGHT", "industry": "INDUSTRY",
}


def calculate_score(item):
    """Score news item per CLAUDE.md formula"""
    # Heat signal
    heat = 1
    source = item.get("source", "")
    if item.get("score", 0) > 2:
        heat += 2  # multi-source or priority
    if source in ("量子位", "36氪", "TechCrunch"):
        heat += 2

    # Timeliness (assume current = +5)
    timeliness = 5

    # Source quality
    quality = SOURCE_QUALITY.get(source, 1)

    return heat * 0.4 + timeliness * 0.3 + quality * 0.3


def deduplicate(items, threshold=0.8):
    """Remove near-duplicate titles, keeping higher-scored one"""
    result = []
    for item in items:
        title = item["title"]
        is_dup = False
        for existing in result:
            ratio = SequenceMatcher(None, title, existing["title"]).ratio()
            if ratio > threshold:
                # Keep the one with higher score
                if calculate_score(item) > calculate_score(existing):
                    result.remove(existing)
                    result.append(item)
                is_dup = True
                break
        if not is_dup:
            result.append(item)
    return result


def map_category(raw_cat):
    """Map fetch_news.py categories to our section categories"""
    raw = (raw_cat or "general").lower()
    if raw in ("model",):
        return "models"
    elif raw in ("tool",):
        return "tools"
    elif raw in ("policy",):
        return "policy"
    elif raw in ("application",):
        return "applications"
    elif raw in ("opensource",):
        return "opensource"
    elif raw in ("global",):
        return "global"
    elif raw in ("paper",):
        return "papers"
    else:
        return "industry"


def categorize_news(news_data):
    """Organize news into sections, score and sort"""
    sections = {}
    for cat_key in ("models", "tools", "policy", "applications",
                     "opensource", "global", "papers", "industry"):
        sections[cat_key] = []

    cats = news_data.get("categories", {})
    for cat_key, items in cats.items():
        mapped = map_category(cat_key)
        for item in items:
            item["_score"] = calculate_score(item)
            item["_mapped_cat"] = mapped
            sections[mapped].append(item)

    # Also handle "general" category → industry
    for item in cats.get("general", []):
        item["_score"] = calculate_score(item)
        item["_mapped_cat"] = "industry"
        sections["industry"].append(item)

    # Deduplicate and sort each section
    for key in sections:
        sections[key] = deduplicate(sections[key])
        sections[key].sort(key=lambda x: x.get("_score", 0), reverse=True)

    return sections


def extract_summary(item, max_len=80):
    """Simple summary: use existing summary or truncate title"""
    summary = item.get("summary", "").strip()
    if summary:
        # Truncate to max_len
        if len(summary) > max_len:
            summary = summary[:max_len-3] + "..."
        return summary
    # Fallback: title as description
    return item.get("title", "")[:max_len]


def build_archive_map(archive_dir):
    """Build archive map from existing archive files"""
    amap = {}
    if not os.path.isdir(archive_dir):
        return amap
    for fname in os.listdir(archive_dir):
        if not fname.endswith(".html"):
            continue
        # Parse: YYYY-MM-DD-edition.html
        m = re.match(r"(\d{4}-\d{2}-\d{2})-(morning|noon|evening)\.html", fname)
        if m:
            date_str, edition = m.group(1), m.group(2)
            if date_str not in amap:
                amap[date_str] = []
            if edition not in amap[date_str]:
                amap[date_str].append(edition)
    # Sort editions
    order = {"morning": 0, "noon": 1, "evening": 2}
    for k in amap:
        amap[k].sort(key=lambda e: order.get(e, 99))
    return amap


def build_news_item_html(item, style="sub"):
    """Build HTML for a single news item"""
    source = item.get("source", "")
    url = item.get("url", "#")
    title = item.get("title", "")
    summary = extract_summary(item)
    raw_cat = item.get("category", item.get("_mapped_cat", "general"))
    tag_class, tag_text = CATEGORY_TAGS.get(raw_cat, ("tag-industry", "产业"))

    if style == "feature":
        icon_map = {"models": "🤖", "tools": "🛠️", "policy": "📜",
                     "global": "🌍", "industry": "💰", "papers": "📄"}
        icon = icon_map.get(item.get("_mapped_cat", ""), "📰")
        badge = ""
        if item.get("_score", 0) > 2.5:
            badge = '<span class="badge-hot">HOT</span>'
        else:
            badge = '<span class="badge-new">NEW</span>'

        return f'''
    <div class="feature-card">
      <div class="card-row">
        <div class="card-icon">{icon}</div>
        <div class="card-body">
          <div class="card-tag"><span class="news-item-tag {tag_class}">{tag_text}</span>{badge}</div>
          <div class="card-title">{title}</div>
          <div class="card-desc">{summary}</div>
          <div class="card-meta">
            <span>来源：{source}</span>
            <a class="read-original" href="{url}" target="_blank">阅读原文 <span class="read-original-arrow">→</span></a>
          </div>
        </div>
      </div>
    </div>'''

    else:  # sub card
        return f'''
      <div class="sub-card">
        <div class="sub-tag"><span class="news-item-tag {tag_class}">{tag_text}</span></div>
        <div class="sub-title">{title}</div>
        <div class="sub-desc">{summary}</div>
        <div class="sub-meta">
          <span>{source}</span>
          <a class="read-original" href="{url}" target="_blank">原文 <span class="read-original-arrow">→</span></a>
        </div>
      </div>'''


def build_section_html(section_key, items, limit, edition):
    """Build HTML for a section"""
    if not items or limit <= 0:
        return ""

    color = SECTION_COLORS.get(section_key, "var(--accent-indigo)")
    icon = SECTION_ICONS.get(section_key, "📰")
    cn_name = SECTION_CN.get(section_key, section_key)
    en_name = SECTION_EN.get(section_key, section_key.upper())
    selected = items[:limit]

    # Special handling for opensource = rank card
    if section_key == "opensource":
        rows = ""
        for i, item in enumerate(selected, 1):
            name = item.get("title", "")
            # Clean up GitHub Trending names
            if "GitHub Trending:" in name:
                name = name.split("GitHub Trending:")[1].strip().replace("\n", " ").strip()
            stat_class = "rank-up" if i <= 3 else "rank-neutral"
            prefix = "⭐" if i <= 3 else "🆕"
            rows += f'<div class="rank-row"><span class="rank-num">{i}</span><span class="rank-name">{name}</span><span class="rank-stat {stat_class}">{prefix}</span></div>'
        return f'''
  <section class="section-gap">
    <div class="section-head">
      <div class="section-line" style="background:{color};"></div>
      <span class="section-label" style="color:{color};">{icon} {cn_name}</span>
      <span class="section-label-cn">{en_name}</span>
    </div>
    <div class="rank-card">
      <div class="rank-label" style="color:{color};">🏆 GitHub Trending Top {limit}</div>
      {rows}
    </div>
  </section>'''

    # Special handling for papers = paper spotlight
    if section_key == "papers":
        item = selected[0] if selected else None
        if not item:
            return ""
        title = item.get("title", "")
        summary = item.get("summary", extract_summary(item, 150))
        url = item.get("url", "#")
        source = item.get("source", "arXiv")
        # Extract arXiv ID
        arxiv_id = ""
        m = re.search(r"(\d{4}\.\d{4,5})", url)
        if m:
            arxiv_id = m.group(1)
        meta_parts = [f"arXiv: {arxiv_id}"] if arxiv_id else []
        meta_parts.append(source)

        return f'''
  <section class="section-gap">
    <div class="section-head">
      <div class="section-line" style="background:{color};"></div>
      <span class="section-label" style="color:{color};">{icon} {cn_name}</span>
      <span class="section-label-cn">{en_name}</span>
    </div>
    <div class="paper-spotlight">
      <div class="paper-header"><span class="paper-label">📄 今日论文</span></div>
      <div class="paper-title">{title}</div>
      <div class="paper-abstract">{summary}</div>
      <div class="paper-meta">{" · ".join(meta_parts)}</div>
      <div style="margin-top:8px;"><a class="read-original" href="{url}" target="_blank">阅读论文 <span class="read-original-arrow">→</span></a></div>
    </div>
  </section>'''

    # Standard sections
    html = f'''
  <section class="section-gap">
    <div class="section-head">
      <div class="section-line" style="background:{color};"></div>
      <span class="section-label" style="color:{color};">{icon} {cn_name}</span>
      <span class="section-label-cn">{en_name}</span>
    </div>
'''

    # For models and global: first item as feature card, rest as sub grid
    if section_key in ("models", "global") and len(selected) >= 1:
        html += build_news_item_html(selected[0], "feature")
        rest = selected[1:]
        if rest:
            # Group into pairs for sub-grid
            for i in range(0, len(rest), 2):
                pair = rest[i:i+2]
                cards = "".join(build_news_item_html(it, "sub") for it in pair)
                html += f'<div class="sub-grid">{cards}</div>'
                if i + 2 < len(rest):
                    html += '<div style="height:10px;"></div>'
    elif section_key == "policy":
        # Policy grid
        cards = "".join(
            f'<div class="policy-card">{build_news_item_html(it, "sub")}</div>'
            for it in selected
        )
        html += f'<div class="policy-grid">{cards}</div>'
    else:
        # Sub grid pairs
        for i in range(0, len(selected), 2):
            pair = selected[i:i+2]
            cards = "".join(build_news_item_html(it, "sub") for it in pair)
            html += f'<div class="sub-grid">{cards}</div>'
            if i + 2 < len(selected):
                html += '<div style="height:10px;"></div>'

    html += '\n  </section>'
    return html


def build_tldr(sections, config):
    """Build TL;DR text from top items"""
    top_items = []
    # Pick top items from key sections
    for sec_key in ("models", "industry", "tools", "policy", "global"):
        items = sections.get(sec_key, [])
        if items:
            top_items.append(items[0]["title"])

    if not top_items:
        return "今日AI新闻汇总，暂无重大突破。"

    return "；".join(top_items[:5]) + "。"


def build_offline_notice():
    """Build offline notice HTML"""
    return '''
  <div class="offline-notice">
    <span class="offline-icon">📡</span>
    <div>
      <div class="offline-title">网络受限模式</div>
      <div class="offline-desc">当前网络不可用，内容精选自近期归档。部分新闻摘要为自动提取，详情请查看原文。</div>
    </div>
  </div>'''


def generate_html(date_str, edition, news_data, template_path, archive_dir, fallback=False):
    """Main generation function"""
    config = EDITION_CONFIG.get(edition, EDITION_CONFIG["morning"])

    # Read template
    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()

    # Categorize and score news
    sections = categorize_news(news_data)

    # Calculate stats
    total_headlines = sum(
        min(len(sections.get(k, [])), config.get(k, 0))
        for k in ("models", "tools", "policy", "applications", "global")
    )
    source_count = len(set(
        item.get("source", "") for items in sections.values() for item in items
    ))
    project_count = min(len(sections.get("opensource", [])), config.get("opensource", 5))
    paper_count = min(len(sections.get("papers", [])), config.get("papers", 1))

    # Format date
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    weekday_names = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
    date_cn = f"{dt.year}年{dt.month}月{dt.day}日 {weekday_names[dt.weekday()]}"

    # Build TL;DR
    tldr_text = build_tldr(sections, config) if not fallback else "网络受限模式：内容精选自近期归档，部分摘要为自动提取。"

    # Build news content HTML
    news_html = ""
    if fallback:
        news_html += build_offline_notice()

    section_order = ["models", "tools", "policy", "applications",
                      "opensource", "global", "papers", "industry"]
    for sec_key in section_order:
        limit = config.get(sec_key, 0)
        if limit <= 0:
            continue
        items = sections.get(sec_key, [])
        news_html += build_section_html(sec_key, items, limit, edition)

    # Build archive map
    archive_map = build_archive_map(archive_dir)
    # Add today's edition
    if date_str not in archive_map:
        archive_map[date_str] = []
    if edition not in archive_map[date_str]:
        archive_map[date_str].append(edition)

    archive_map_json = json.dumps(archive_map, ensure_ascii=False, separators=(',', ':'))

    # Source list
    all_sources = sorted(set(
        item.get("source", "") for items in sections.values() for item in items
    ))
    source_list = " · ".join(s for s in all_sources if s)

    # Replace template variables
    html = template
    html = html.replace("{{DATE}}", date_cn)
    html = html.replace("{{EDITION}}", edition)
    html = html.replace("{{EDITION_UPPER}}", config["edition_upper"])
    html = html.replace("{{EDITION_CN}}", config["edition_cn"])
    html = html.replace("{{TIME}}", config["time_label"])
    html = html.replace("{{DATE_CN}}", date_cn)
    html = html.replace("{{TLDR_CONTENT}}", tldr_text)
    html = html.replace("<!-- {{NEWS_CONTENT}} -->", news_html)
    html = html.replace("{{ARCHIVE_MAP}}", archive_map_json)
    html = html.replace("{{NEWS_COUNT}}", str(total_headlines))
    html = html.replace("{{SOURCE_COUNT}}", str(max(source_count, 1)))
    html = html.replace("{{PROJECT_COUNT}}", str(project_count))
    html = html.replace("{{PAPER_COUNT}}", str(paper_count))
    html = html.replace("{{SOURCE_LIST}}", source_list)

    # OG description from TLDR
    og_desc = tldr_text[:80] + ("..." if len(tldr_text) > 80 else "")
    html = html.replace("{{OG_DESCRIPTION}}", og_desc)

    # Fix title: replace the full title tag
    html = re.sub(
        r"<title>AI 脉搏 · 热点速览 — .*?</title>",
        f"<title>AI 脉搏 · 热点速览 — {date_cn} {config['edition_cn']}</title>",
        html
    )

    # Fix OG title
    html = re.sub(
        r'content="AI 脉搏 · AI 热点速览 — .*?"',
        f'content="AI 脉搏 · AI 热点速览 — {date_str} {config["edition_cn"]}"',
        html
    )

    # Fix hero badge text - ensure no double CST
    html = re.sub(
        r'<span class="hero-badge-text" id="heroBadge">.*?</span>',
        f'<span class="hero-badge-text" id="heroBadge">{config["edition_cn"]} · {config["time_label"]}</span>',
        html
    )

    # Fix nav sub
    html = re.sub(
        r'<div class="nav-sub" id="navSub">.*?</div>',
        f'<div class="nav-sub" id="navSub">AI PULSE · {config["edition_upper"]}</div>',
        html
    )

    # Fix hero date
    html = re.sub(
        r'<p class="hero-date" id="heroDate">.*?</p>',
        f'<p class="hero-date" id="heroDate">{date_cn}</p>',
        html
    )

    return html


def update_feed_xml(feed_path, date_str, edition, sections, config):
    """Add new item to feed.xml and trim to 10 items"""
    with open(feed_path, "r", encoding="utf-8", errors="replace") as f:
        content = f.read()

    # Build item description
    desc_parts = []
    for sec_key in ("models", "tools", "policy", "applications",
                     "opensource", "papers", "global", "industry"):
        items = sections.get(sec_key, [])
        if not items:
            continue
        cn_name = SECTION_CN.get(sec_key, sec_key)
        limit = config.get(sec_key, 0)
        if limit <= 0:
            continue
        desc_parts.append(f"<h3>{SECTION_ICONS.get(sec_key, '')} {cn_name}</h3><ul>")
        for item in items[:limit]:
            title = item.get("title", "")
            source = item.get("source", "")
            url = item.get("url", "#")
            desc_parts.append(f"<li>{title}（{source}）</li>")
        desc_parts.append("</ul>")

    desc_content = "\n        ".join(desc_parts)

    # Edition emoji
    emoji = {"morning": "🌅", "noon": "☀️", "evening": "🌙"}.get(edition, "📰")

    # Top keywords for title
    top_items = []
    for sec_key in ("models", "industry", "tools", "global"):
        for item in sections.get(sec_key, [])[:1]:
            top_items.append(item.get("title", "")[:20])
    keywords = " + ".join(top_items[:4])

    # Format pubDate
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    hours = {"morning": 8, "noon": 12, "evening": 20}.get(edition, 8)
    pub_date = dt.strftime(f"%a, %d %b %Y {hours:02d}:00:00 +0800")

    new_item = f"""    <item>
      <title>{emoji} {config['edition_cn']}版 — {date_str}（{keywords}）</title>
      <link>https://daiowen.github.io/ai-pulse/archive/{date_str}-{edition}.html</link>
      <guid isPermaLink="true">https://daiowen.github.io/ai-pulse/archive/{date_str}-{edition}.html</guid>
      <pubDate>{pub_date}</pubDate>
      <description><![CDATA[
        {desc_content}
      ]]></description>
    </item>

"""

    # Update lastBuildDate
    content = re.sub(
        r"<lastBuildDate>.*?</lastBuildDate>",
        f"<lastBuildDate>{pub_date}</lastBuildDate>",
        content
    )

    # Insert new item after the first <item> opening tag group
    # Find the first <item> and insert before it
    first_item_pos = content.find("<item>")
    if first_item_pos > 0:
        content = content[:first_item_pos] + new_item + content[first_item_pos:]

    # Trim to 10 items - count <item> tags and remove excess from end
    items = list(re.finditer(r"<item>.*?</item>", content, re.DOTALL))
    if len(items) > 10:
        # Remove excess items (keep first 10)
        for match in reversed(items[10:]):
            content = content[:match.start()] + content[match.end():]

    with open(feed_path, "w", encoding="utf-8", errors="replace") as f:
        f.write(content)


def do_fallback(date_str, edition, archive_dir, template_path, feed_path):
    """Fallback: copy most recent archive, update dates"""
    # Find most recent archive
    archives = sorted(Path(archive_dir).glob("*.html"), reverse=True)
    if not archives:
        print(f"ERROR: No archive files found in {archive_dir}", file=sys.stderr)
        sys.exit(1)

    # Read the most recent archive
    with open(archives[0], "r", encoding="utf-8") as f:
        html = f.read()

    config = EDITION_CONFIG.get(edition, EDITION_CONFIG["morning"])
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    weekday_names = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
    date_cn = f"{dt.year}年{dt.month}月{dt.day}日 {weekday_names[dt.weekday()]}"

    # Replace date references
    html = html.replace("AI PULSE · MORNING", f"AI PULSE · {config['edition_upper']}")
    html = html.replace("AI PULSE · NOON", f"AI PULSE · {config['edition_upper']}")
    html = html.replace("AI PULSE · EVENING", f"AI PULSE · {config['edition_upper']}")
    html = html.replace("早间 · 08:00 CST", f"{config['edition_cn']} · {config['time_label']}")
    html = html.replace("午间 · 12:00 CST", f"{config['edition_cn']} · {config['time_label']}")
    html = html.replace("晚间 · 20:00 CST", f"{config['edition_cn']} · {config['time_label']}")

    # Insert offline notice before first section
    notice = build_offline_notice()
    first_section = re.search(r'<section class="section-gap">', html)
    if first_section:
        pos = first_section.start()
        html = html[:pos] + notice + "\n" + html[pos:]

    # Update title
    html = re.sub(
        r"<title>AI 脉搏 · 热点速览 — .*?</title>",
        f"<title>AI 脉搏 · 热点速览 — {date_cn} {config['edition_cn']}</title>",
        html
    )

    return html


def main():
    if len(sys.argv) < 3:
        print("Usage: python3 generate_html.py YYYY-MM-DD morning|noon|evening [--fallback]",
              file=sys.stderr)
        sys.exit(1)

    date_str = sys.argv[1]
    edition = sys.argv[2]
    fallback = "--fallback" in sys.argv

    # Validate
    if edition not in EDITION_CONFIG:
        print(f"ERROR: Invalid edition '{edition}'. Use morning/noon/evening.", file=sys.stderr)
        sys.exit(1)

    try:
        datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        print(f"ERROR: Invalid date format '{date_str}'. Use YYYY-MM-DD.", file=sys.stderr)
        sys.exit(1)

    # Paths
    script_dir = Path(__file__).parent
    template_path = script_dir / "template.html"
    archive_dir = script_dir / "archive"
    feed_path = script_dir / "feed.xml"
    index_path = script_dir / "index.html"
    archive_path = archive_dir / f"{date_str}-{edition}.html"

    # Check if archive already exists for this date+edition
    if archive_path.exists():
        print(f"SKIP: Archive {archive_path} already exists. Not overwriting.", file=sys.stderr)
        sys.exit(0)

    if fallback:
        html = do_fallback(date_str, edition, str(archive_dir), str(template_path), str(feed_path))
    else:
        # Read news JSON from stdin
        try:
            news_data = json.load(sys.stdin)
        except json.JSONDecodeError as e:
            print(f"ERROR: Failed to parse news JSON from stdin: {e}", file=sys.stderr)
            print("Falling back to archive-based generation...", file=sys.stderr)
            html = do_fallback(date_str, edition, str(archive_dir), str(template_path), str(feed_path))
            fallback = True
            news_data = {}

        if not fallback:
            # Check if we got meaningful data
            total = news_data.get("total", 0)
            if total < 5:
                print(f"WARNING: Only {total} news items fetched. Falling back...", file=sys.stderr)
                html = do_fallback(date_str, edition, str(archive_dir), str(template_path), str(feed_path))
                fallback = True

            if not fallback:
                html = generate_html(date_str, edition, news_data, str(template_path), str(archive_dir))

                # Update feed.xml
                if feed_path.exists():
                    sections = categorize_news(news_data)
                    config = EDITION_CONFIG[edition]
                    update_feed_xml(str(feed_path), date_str, edition, sections, config)

    # Write files (handle encoding issues on Windows)
    with open(str(index_path), "w", encoding="utf-8", errors="replace") as f:
        f.write(html)
    print(f"Wrote {index_path}")

    # Ensure archive dir exists
    archive_dir.mkdir(parents=True, exist_ok=True)

    with open(str(archive_path), "w", encoding="utf-8", errors="replace") as f:
        f.write(html)
    print(f"Wrote {archive_path}")

    print(f"DONE: {date_str} {edition} edition generated{' (fallback)' if fallback else ''}")


if __name__ == "__main__":
    main()
