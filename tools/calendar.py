"""Generate archiveMap JS from actual archive files on disk."""
import glob, re, json

def build_archive_map(archive_dir='archive'):
    """Scan archive dir and return archiveMap as a JS object string."""
    amap = {}
    for f in sorted(glob.glob(f'{archive_dir}/????-??-??-*.html')):
        m = re.match(r'.*/(\d{4}-\d{2}-\d{2})-(morning|noon|evening)\.html$', f)
        if not m:
            continue
        date, edition = m.group(1), m.group(2)
        if date not in amap:
            amap[date] = []
        if edition not in amap[date]:
            amap[date].append(edition)
    # Sort editions: morning, noon, evening
    order = {'morning': 0, 'noon': 1, 'evening': 2}
    for date in amap:
        amap[date].sort(key=lambda e: order.get(e, 99))
        if len(amap[date]) >= 3:
            amap[date] = 'full'
    return json.dumps(amap, indent=4, ensure_ascii=False)

def inject_archive_map(html, archive_dir='archive'):
    """Replace archiveMap in HTML with freshly-built version."""
    new_map = build_archive_map(archive_dir)
    # Match: const archiveMap = {... old data ...};
    pattern = r'const archiveMap = \{[\s\S]*?\n  \};'
    replacement = f'const archiveMap = {new_map};'
    return re.sub(pattern, replacement, html)
