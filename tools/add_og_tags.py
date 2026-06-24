import os
import re

OG_TAGS = '''<meta property="og:image" content="https://daiowen.github.io/ai-pulse/assets/og-image.svg">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="AI 脉搏 · AI 热点速览">
<meta name="twitter:description" content="面向中国 AI 开发者的每日新闻智能聚合">
<meta name="twitter:image" content="https://daiowen.github.io/ai-pulse/assets/og-image.svg">'''

files_to_update = [
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
    'archive/2026-06-23-morning.html',
    'archive/2026-06-23-noon.html',
    'archive/2026-06-24-morning.html',
]

for filepath in files_to_update:
    print(f"Processing {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 检查是否已有 og:image
    if 'og:image' in content:
        print(f"  Already has og:image, skipping")
        continue

    # 在 <meta property="og:type" 后插入 OG 标签
    # 或者如果没有 og:type，在 </title> 后插入
    if '<meta property="og:type"' in content:
        content = re.sub(
            r'<meta property="og:type" content="website">',
            '<meta property="og:type" content="website">\n' + OG_TAGS,
            content
        )
    elif '<meta name="theme-color"' in content:
        content = re.sub(
            r'<meta name="theme-color" content="#0a0a0f">',
            '<meta name="theme-color" content="#0a0a0f">\n' + OG_TAGS,
            content
        )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  Updated {filepath}")

print("Done!")