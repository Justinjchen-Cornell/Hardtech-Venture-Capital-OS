import re, html, sys

def decode(fname):
    with open(fname, 'rb') as f:
        raw = f.read()
    for enc in ('utf-8', 'gb18030'):
        try:
            return raw.decode(enc)
        except UnicodeDecodeError:
            continue
    return raw.decode('utf-8', errors='ignore')

content = decode(sys.argv[1])
out = []
results = re.findall(r'<h3[^>]*>.*?</h3>', content, re.DOTALL)
out.append(f'Number of h3 titles: {len(results)}')
for i, r in enumerate(results):
    m = re.search(r'<a[^>]*href="([^"]+)"[^>]*>(.*?)</a>', r, re.DOTALL)
    if m:
        url = html.unescape(m.group(1))
        t = re.sub(r'<[^>]+>', '', m.group(2))
        t = html.unescape(t).strip()
        if t:
            out.append(f'--- Result {i} ---')
            out.append(f'TITLE: {t}')
            out.append(f'URL: {url}')

# Also snippets
snippets = re.findall(r'<div class="res-desc[^"]*"[^>]*>(.*?)</div>', content, re.DOTALL)
out.append('')
out.append(f'=== {len(snippets)} snippets ===')
for i, s in enumerate(snippets[:12]):
    s = re.sub(r'<[^>]+>', ' ', s)
    s = html.unescape(re.sub(r'\s+', ' ', s)).strip()
    if s:
        out.append(f'SNIPPET_{i}: {s[:300]}')

with open(sys.argv[1] + '.parsed.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(out))
print('done')
