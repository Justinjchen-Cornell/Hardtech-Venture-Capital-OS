import re, html, sys, io

def parse(fname):
    with open(fname, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    results = re.findall(r'<li class="b_algo".*?</li>', content, re.DOTALL)
    out = []
    out.append(f'Number of results: {len(results)}')
    for i, r in enumerate(results[:12]):
        title = re.search(r'<h2>.*?<a[^>]*href="([^"]+)"[^>]*>(.*?)</a>', r, re.DOTALL)
        snippet = re.search(r'<p[^>]*>(.*?)</p>', r, re.DOTALL)
        t = title.group(2) if title else 'N/A'
        s = snippet.group(1) if snippet else 'N/A'
        t = re.sub(r'<[^>]+>', '', t)
        s = re.sub(r'<[^>]+>', '', s)
        out.append(f'--- Result {i+1} ---')
        out.append(f'URL: {title.group(1) if title else "N/A"}')
        out.append(f'Title: {html.unescape(t)}')
        out.append(f'Snippet: {html.unescape(s)[:600]}')
        out.append('')
    return '\n'.join(out)

if __name__ == '__main__':
    result = parse(sys.argv[1])
    with open('parse_out.txt', 'w', encoding='utf-8') as f:
        f.write(result)
    print('done')
