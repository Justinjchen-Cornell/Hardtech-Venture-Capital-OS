#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""book_pipeline.py — 读书 -> Skill 生成管线（Hardtech-VC-OS）

将一本（或一份）书的 MD 文本转化为可加载的 Claude Code skill：
  预处理(清洗/重建标题) -> 章节定位 -> 精选提取 -> 组装 skill

用法：
  python book_pipeline.py --md <书.md> --slug <skill名> [--mode auto|clean|headings|chapters]
示例：
  python book_pipeline.py --md 守正.md --slug shou-zheng --mode headings
  python book_pipeline.py --md IV.md --slug damodaran --mode chapters --select 13,22,23,24
"""
import os, re, sys, argparse

def clean_nul(md_path, out_path):
    """去除 PDF 提取残留的 NUL 字节"""
    data = open(md_path, 'rb').read()
    n = data.count(b'\x00')
    clean = data.replace(b'\x00', b'')
    text = clean.decode('utf-8', errors='replace')
    open(out_path, 'w', encoding='utf-8').write(text)
    return n

def rebuild_headings(md_path, out_path):
    """中文书标题重建：无 Markdown 标题 -> 规范 # 标题"""
    lines = open(md_path, encoding='utf-8', errors='replace').read().split('\n')
    part_pat = re.compile(r'^第[一二三四五六七八九十百]+篇')
    chap_pat = re.compile(r'^#{0,3}\s*第[一二三四五六七八九十百]+章')
    sec_pat = re.compile(r'^第[一二三四五六七八九十百]+节\s')
    out = []
    cnt = {'part': 0, 'chapter': 0, 'section': 0}
    for l in lines:
        t = l.strip()
        if part_pat.match(t):
            out.append('## ' + t); cnt['part'] += 1
        elif chap_pat.match(t):
            out.append('### ' + t.lstrip('#').strip()); cnt['chapter'] += 1
        elif sec_pat.match(t):
            out.append('#### ' + t); cnt['section'] += 1
        else:
            out.append(l)
    open(out_path, 'w', encoding='utf-8').write('\n'.join(out))
    return cnt

def locate_chapters(md_path, body_start=0):
    """英文书正文 CHAPTER N 标记 -> 行号映射（升序去重）"""
    lines = open(md_path, encoding='utf-8', errors='replace').read().split('\n')
    raw = []
    for i, l in enumerate(lines):
        t2 = l.strip().lstrip('#').strip()
        m = re.match(r'^CHAPTER\s+(\d+)', t2, re.I)
        if m and i >= body_start:
            raw.append((int(m.group(1)), i))
    result = {}
    for c, i in raw:
        if c not in result:
            result[c] = i
    return result

def extract_chapters(md_path, out_path, selected, body_start=0):
    """按章号提取精选章节"""
    raw = locate_chapters(md_path, body_start)
    lines = open(md_path, encoding='utf-8', errors='replace').read().split('\n')
    total_lines = len(lines)
    out, total = [], 0
    keys = sorted(raw.keys())
    for idx, c in enumerate(keys):
        if c in selected:
            s = raw[c]
            nxt = keys[idx+1] if idx+1 < len(keys) else total_lines
            e = raw.get(nxt, nxt)
            total += e - s
            out.append('\n\n===== CHAPTER %d =====\n' % c)
            out.extend(lines[s:e])
    open(out_path, 'w', encoding='utf-8').write('\n'.join(out))
    return total

def assemble_skill(slug, skill_md, chapters_map, patterns, glossary, cheatsheet, out_dir):
    """组装 skill 目录：SKILL.md + chapters/ + patterns + glossary + cheatsheet"""
    base = os.path.join(out_dir, slug)
    os.makedirs(os.path.join(base, 'chapters'), exist_ok=True)
    open(os.path.join(base, 'SKILL.md'), 'w', encoding='utf-8').write(skill_md)
    for name, content in chapters_map.items():
        open(os.path.join(base, 'chapters', name), 'w', encoding='utf-8').write(content)
    if patterns:
        open(os.path.join(base, 'patterns.md'), 'w', encoding='utf-8').write(patterns)
    if glossary:
        open(os.path.join(base, 'glossary.md'), 'w', encoding='utf-8').write(glossary)
    if cheatsheet:
        open(os.path.join(base, 'cheatsheet.md'), 'w', encoding='utf-8').write(cheatsheet)
    return base

def main():
    ap = argparse.ArgumentParser(description='Book-to-Skill 管线')
    ap.add_argument('--md', required=True, help='书/文档的 MD 路径')
    ap.add_argument('--slug', required=True, help='skill 名称')
    ap.add_argument('--mode', default='auto',
                    choices=['auto', 'clean', 'headings', 'chapters'])
    ap.add_argument('--select', default='', help='chapters 模式：逗号分隔章号')
    ap.add_argument('--out', default=os.path.expanduser('~/.claude/skills'))
    args = ap.parse_args()

    work = os.path.join(os.path.dirname(args.md), 'structured')
    os.makedirs(work, exist_ok=True)
    cleaned = os.path.join(work, os.path.basename(args.md).replace('.md', '-clean.md'))

    n = clean_nul(args.md, cleaned)
    print('清洗: %d NUL 字节' % n)

    if args.mode == 'clean':
        print('完成（仅清洗）:', cleaned)
        return

    if args.mode == 'headings':
        cnt = rebuild_headings(cleaned, os.path.join(work, os.path.basename(args.md).replace('.md', '-structured.md')))
        print('标题重建: 篇%d 章%d 节%d' % (cnt['part'], cnt['chapter'], cnt['section']))
        return

    if args.mode == 'chapters':
        selected = [int(x) for x in args.select.split(',') if x.strip()]
        out = os.path.join(work, os.path.basename(args.md).replace('.md', '-selected.md'))
        total = extract_chapters(cleaned, out, selected)
        print('精选提取: %d 章 / %d 行 -> %s' % (len(selected), total, out))
        return

    raw = locate_chapters(cleaned)
    if raw:
        print('检测到 %d 章（英文书模式）' % len(raw))
        print('  chapters 模式可用：--mode chapters --select 13,22,23,24')
    else:
        print('未检测到 CHAPTER N（中文书模式）')
        print('  headings 模式可用：--mode headings')

if __name__ == '__main__':
    main()
