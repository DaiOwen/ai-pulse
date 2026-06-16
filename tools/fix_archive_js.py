#!/usr/bin/env python3
"""Inject fixed calendar JS into all archive files."""
import re, glob

with open('index.html', 'r', encoding='utf-8') as f:
    index = f.read()

# Extract the calendar JS function from index.html
# Find the function that starts with "const overlay = document.getElementById('calendarOverlay')"
start_marker = "(function() {\n  const overlay = document.getElementById('calendarOverlay');"
start_idx = index.find(start_marker)
if start_idx == -1:
    print("ERROR: calendar JS not found")
    exit(1)

# Find the matching closing "})();"
depth = 0
end_idx = start_idx
i = start_idx
while i < len(index):
    if index[i:i+8] == 'function':
        depth += 1
        i += 8
        continue
    if index[i:i+3] == '})()':
        if depth == 1:
            end_idx = i + 4
            break
        depth -= 1
    i += 1

fixed_js = index[start_idx:end_idx]
print(f"Extracted {len(fixed_js)} chars of calendar JS")

# Now find and replace in each archive file
# The old JS starts with similar marker
old_start = "(function() {\n  const overlay = document.getElementById('calendarOverlay');"

for f in sorted(glob.glob('archive/2026-06-*.html')):
    with open(f, 'r', encoding='utf-8') as fh:
        content = fh.read()

    old_s = content.find(old_start)
    if old_s == -1:
        print(f'{f}: no calendar JS found')
        continue

    # Find end of old JS
    depth = 0
    i = old_s
    while i < len(content):
        if content[i:i+8] == 'function':
            depth += 1
            i += 8
            continue
        if content[i:i+3] == '})()':
            if depth == 1:
                old_e = i + 4
                break
            depth -= 1
        i += 1

    new_content = content[:old_s] + fixed_js + content[old_e:]
    with open(f, 'w', encoding='utf-8') as fh:
        fh.write(new_content)
    print(f'{f}: updated ({old_e - old_s}B old → {len(fixed_js)}B new)')
