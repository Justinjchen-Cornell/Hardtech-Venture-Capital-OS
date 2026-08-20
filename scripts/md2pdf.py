#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""md2pdf.py — Markdown → 排版精良 PDF（中文支持）

用法：
  python scripts/md2pdf.py <input.md> [output.pdf]
  python scripts/md2pdf.py 04.Projects/郑宗良天线/16-Rogers基材与壁垒层级分析-20260820.md

原理：markdown lib → 带 CSS 的 HTML → Edge headless --print-to-pdf（走 ASCII 临时路径，规避中文路径写入问题）
依赖：python-markdown + Edge（Windows 自带）
"""
import io, os, re, sys, subprocess, tempfile, shutil, markdown

def build_html(md_text: str, title: str) -> str:
    body = markdown.markdown(md_text, extensions=['tables', 'fenced_code'])
    css = """
@page { size: A4; margin: 2cm 1.8cm;
  @bottom-center { content: "Hardtech-VC-OS · 第 " counter(page) " 页 / " counter(pages) " 页"; font-size: 8pt; color: #888; } }
body { font-family: "Microsoft YaHei", "PingFang SC", sans-serif; font-size: 10.5pt; line-height: 1.7; color: #222; }
h1 { font-size: 20pt; color: #1a3a5c; border-bottom: 3px solid #1a3a5c; padding-bottom: 8px; margin-top: 28px; page-break-after: avoid; }
h2 { font-size: 14pt; color: #1a3a5c; border-left: 4px solid #1a3a5c; padding-left: 8px; margin-top: 22px; page-break-after: avoid; }
h3 { font-size: 11.5pt; color: #2d5a88; margin-top: 16px; page-break-after: avoid; }
blockquote { background: #f4f7fa; border-left: 4px solid #1a3a5c; margin: 10px 0; padding: 8px 14px; color: #444; }
table { border-collapse: collapse; width: 100%; margin: 10px 0; font-size: 9.5pt; }
th { background: #1a3a5c; color: #fff; padding: 6px 8px; text-align: left; }
td { border: 1px solid #ccd5de; padding: 5px 8px; vertical-align: top; }
tr:nth-child(even) td { background: #f4f7fa; }
code { background: #eef1f4; padding: 1px 4px; border-radius: 3px; font-size: 9pt; }
hr { border: none; border-top: 1px solid #ccd5de; margin: 18px 0; }
strong { color: #1a3a5c; }
"""
    header = f"""
<div style="background:#1a3a5c; color:#fff; padding:12px 16px; border-radius:6px; margin-bottom:12px;">
  <div style="font-size:14pt; font-weight:bold;">{title}</div>
  <div style="font-size:9pt; margin-top:3px; opacity:0.8;">Hardtech-Venture-Capital-OS · 文档 PDF 版</div>
</div>
"""
    return f"<!DOCTYPE html><html><head><meta charset='utf-8'><style>{css}</style></head><body>{header}{body}</body></html>"

def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(1)
    src = sys.argv[1]
    dst = sys.argv[2] if len(sys.argv) > 2 else os.path.splitext(src)[0] + '.pdf'
    md_text = io.open(src, encoding='utf-8').read()
    title = os.path.basename(src).replace('.md', '')
    html = build_html(md_text, title)

    tmpdir = tempfile.mkdtemp(prefix='md2pdf_')
    try:
        html_tmp = os.path.join(tmpdir, 'doc.html')
        pdf_tmp = os.path.join(tmpdir, 'doc.pdf')
        io.open(html_tmp, 'w', encoding='utf-8').write(html)
        edge = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
        url = 'file:///' + html_tmp.replace(chr(92), '/')
        r = subprocess.run([edge, '--headless', '--disable-gpu', '--no-pdf-header-footer',
                            '--user-data-dir=' + os.path.join(tmpdir, 'profile'),
                            '--print-to-pdf=' + pdf_tmp, url],
                           capture_output=True, timeout=90)
        if not os.path.exists(pdf_tmp):
            print('ERROR: PDF 未生成'); print(r.stderr.decode('utf-8', 'replace')[:500]); sys.exit(1)
        os.makedirs(os.path.dirname(os.path.abspath(dst)), exist_ok=True)
        shutil.copy2(pdf_tmp, dst)
        print(f'OK {dst} ({os.path.getsize(dst):,} bytes)')
    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)

if __name__ == '__main__':
    main()
