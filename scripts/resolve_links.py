import re, html, sys, subprocess

with open(sys.argv[1], 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

results = re.findall(r'<h3[^>]*>.*?</h3>', content, re.DOTALL)
for i, r in enumerate(results):
    m = re.search(r'<a[^>]*href="([^"]+)"[^>]*>(.*?)</a>', r, re.DOTALL)
    if m:
        url = html.unescape(m.group(1))
        t = re.sub(r'<[^>]+>', '', m.group(2))
        print(f'RESULT_{i}: {html.unescape(t)}')
        print(f'URL: {url}')
        print()
