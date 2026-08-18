import re, html, sys

with open(sys.argv[1], 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

out = []
# Baidu result containers
results = re.findall(r'<h3[^>]*>.*?</h3>', content, re.DOTALL)
out.append(f'Number of h3 titles: {len(results)}')
for i, r in enumerate(results[:15]):
    m = re.search(r'<a[^>]*href="([^"]+)"[^>]*>(.*?)</a>', r, re.DOTALL)
    if m:
        url = m.group(1)
        t = re.sub(r'<[^>]+>', '', m.group(2))
        out.append(f'--- Result {i+1} ---')
        out.append(f'URL: {html.unescape(url)}')
        out.append(f'Title: {html.unescape(t)}')

# Also extract any text snippets
text = re.sub(r'<script.*?</script>', '', content, flags=re.DOTALL)
text = re.sub(r'<style.*?</style>', '', text, flags=re.DOTALL)
text = re.sub(r'<[^>]+>', ' ', text)
text = re.sub(r'\s+', ' ', text)
out.append('')
out.append('=== PAGE TEXT SNIPPET ===')
out.append(text[:3000])

with open('parse_out.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(out))
print('done')
