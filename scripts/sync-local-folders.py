#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sync-local-folders.py — 本地编号目录 <-> 发布镜像同步

本地 vault 用编号命名（03.Skills/ 06.Concepts/），GitHub 用无编号（skills/ concepts/）。
修改本地编号目录后，运行本脚本同步发布镜像并提示提交。

用法：
  python scripts/sync-local-folders.py          # 同步（本地 -> 发布镜像）
  python scripts/sync-local-folders.py --dry    # 预览差异
"""
import os, sys, filecmp

PAIRS = [('03.Skills', 'skills'), ('06.Concepts', 'concepts')]

def collect(root):
    result = {}
    for dirpath, dirnames, filenames in os.walk(root):
        for fn in filenames:
            full = os.path.join(dirpath, fn)
            rel = os.path.relpath(full, root)
            result[rel] = full
    return result

def main():
    dry = '--dry' in sys.argv
    changed = []
    for local, pub in PAIRS:
        if not os.path.isdir(local):
            continue
        os.makedirs(pub, exist_ok=True)
        lf = collect(local)
        pf = collect(pub)
        # 本地新增/修改 -> 发布
        for rel, full in lf.items():
            dst = os.path.join(pub, rel)
            if rel not in pf or not filecmp.cmp(full, dst, shallow=False):
                os.makedirs(os.path.dirname(dst), exist_ok=True)
                if not dry:
                    import shutil
                    shutil.copy2(full, dst)
                changed.append(('+', os.path.join(pub, rel)))
        # 发布多余 -> 提示（不自动删）
        for rel in pf:
            if rel not in lf:
                changed.append(('?', os.path.join(pub, rel) + ' (发布端多余，检查后手动删)'))
    for tag, p in changed:
        print(f'  {tag} {p}')
    if not dry and changed:
        print('同步完成。请执行: git add -A && git commit -m "sync" && git push')
    elif not changed:
        print('无差异，已是最新。')

if __name__ == '__main__':
    main()
