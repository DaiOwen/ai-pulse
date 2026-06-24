import os
import re

# 统一的 archiveMap（基于实际存在的文件）
CORRECT_ARCHIVE_MAP = '''  const archiveMap = {
    "2026-06-14": ["morning"],
    "2026-06-15": ["noon", "evening"],
    "2026-06-16": "full",
    "2026-06-17": ["morning"],
    "2026-06-18": ["morning", "noon"],
    "2026-06-22": ["morning"],
    "2026-06-23": ["morning", "noon"],
    "2026-06-24": ["morning"]
  };
  (function(){for(var d in archiveMap){if(Array.isArray(archiveMap[d])&&archiveMap[d].length>=3)archiveMap[d]='full';}})();'''

# 所有需要更新的文件
files_to_fix = [
    'index.html',
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

def fix_archive_map(filepath):
    print(f"Processing {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 匹配旧 archiveMap 块
    # 格式: const archiveMap = { ... }; 后面可能有 normalizer 函数
    pattern = r'const archiveMap\s*=\s*\{[^}]+\}\s*;[^}]*\(function\(\)\{for\(var d in archiveMap\).*?\}\)\(\);?'

    # 替换为正确的 archiveMap
    content = re.sub(pattern, CORRECT_ARCHIVE_MAP, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  Fixed {filepath}")

for filepath in files_to_fix:
    fix_archive_map(filepath)

print("\nDone! All archiveMap synchronized.")