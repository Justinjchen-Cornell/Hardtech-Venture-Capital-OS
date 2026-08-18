#!/bin/bash
# usage: fetch_so.sh <outfile> <so-link-or-url>
OUT=$1
URL=$2
"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" --headless=new --disable-gpu --dump-dom "$URL" > "$OUT" 2>/dev/null
python - "$OUT" << 'PYEOF'
import re, sys
with open(sys.argv[1],'r',encoding='utf-8',errors='ignore') as f:
    c=f.read()
t = re.search(r'<title>(.*?)</title>', c, re.DOTALL)
print('TITLE:', t.group(1).strip() if t else 'N/A')
text = re.sub(r'<script.*?</script>', '', c, flags=re.DOTALL)
text = re.sub(r'<style.*?</style>', '', text, flags=re.DOTALL)
text = re.sub(r'<[^>]+>', ' ', text)
text = re.sub(r'\s+', ' ', text)
print('TEXT:', text[:3000])
PYEOF
