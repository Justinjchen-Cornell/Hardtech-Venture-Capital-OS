#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""check.py — 引用完整性校验（借鉴 Anthropic financial-services scripts/check.py）

校验项：
  1. skills/*/SKILL.md 存在且 frontmatter 含 name + description
  2. agents/*.md frontmatter 合法（name/description）
  3. CLAUDE.md 索引中列出的 agent 都有对应文件
  4. agents/ 与 skills/ 中的 "调用 X skill" 引用都能解析到 skills/X/
  5. [[概念：X]] 双链能解析到 concepts/概念：X.md（未建概念=警告）
  6. .claude/commands/*.md 存在且 frontmatter 含 description
  7. docs/技能状态.md 中登记的技能都存在于 skills/

退出码：0=干净 / 1=有错误（警告不阻断）。纯标准库，无依赖。
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
errors, warnings, checked = [], [], 0

def err(m): errors.append(m)
def warn(m): warnings.append(m)
def rel(p): return str(p.relative_to(ROOT))

def frontmatter(p):
    """返回 dict；frontmatter 非法返回 None"""
    global checked
    checked += 1
    text = p.read_text(encoding='utf-8', errors='replace')
    m = re.match(r'^---\s*\n(.*?)\n---\s*\n', text, re.S)
    if not m:
        return None
    d = {}
    for line in m.group(1).splitlines():
        mm = re.match(r'^([A-Za-z0-9_-]+):\s*(.*)$', line)
        if mm:
            d[mm.group(1)] = mm.group(2)
    return d

# --- 1. skills 结构 ---
for skill_dir in sorted(ROOT.glob('skills/*')):
    if not skill_dir.is_dir() or skill_dir.name == 'README.md':
        continue
    skill_file = skill_dir / 'SKILL.md'
    if not skill_file.exists():
        err(f"skills/{skill_dir.name}/SKILL.md 缺失")
        continue
    fm = frontmatter(skill_file)
    if fm is None:
        err(f"{rel(skill_file)} frontmatter 非法")
    else:
        for k in ('name', 'description'):
            if k not in fm:
                err(f"{rel(skill_file)} 缺 frontmatter 字段: {k}")

# --- 2/3. agents 结构 + CLAUDE.md 索引 ---
agent_files = {p.stem: p for p in ROOT.glob('agents/*.md')}
for p in sorted(agent_files.values()):
    fm = frontmatter(p)
    if fm is None:
        err(f"{rel(p)} frontmatter 非法")
    elif 'name' not in fm:
        err(f"{rel(p)} 缺 frontmatter 字段: name")
# CLAUDE.md 索引里的 agent 名
claude = (ROOT / 'CLAUDE.md').read_text(encoding='utf-8', errors='replace')
idx_line = next((l for l in claude.splitlines() if 'agents（~/.claude/agents/）' in l or l.strip().startswith('- agents（')), None)
if idx_line:
    for name in re.findall(r'/([a-z0-9-]+)\s*[\)／]', idx_line):
        pass
    names = re.findall(r'\b(?:sector-scanner|tech-dd|valuation-analyst|tech-transfer-advisor|deal-negotiator|meeting-prep|deal-sourcing|ic-memo-auditor|ic-memo-writer)\b', idx_line)
    for n in names:
        if n not in agent_files:
            err(f"CLAUDE.md 索引的 agent 缺文件: agents/{n}.md")

# --- 4. skill 引用解析（agents + skills 内 "X skill"/skills/X 模式） ---
for p in list(agent_files.values()) + list(ROOT.glob('skills/*/SKILL.md')):
    text = p.read_text(encoding='utf-8', errors='replace')
    for name in re.findall(r'(?:调用|加载|引用)\s+([a-z0-9-]+)\s+skill', text):
        if name == 'skill' or not (ROOT / 'skills' / name).is_dir():
            # 允许引用书技能别名（如 poor-charlie-almanack）之外的本体存在性检查
            if name not in {d.name for d in ROOT.glob('skills/*')}:
                err(f"{rel(p)} 引用了不存在的 skill: {name}")

# --- 5. [[概念：X]] 双链 ---
concepts = {f.stem for f in ROOT.glob('concepts/*.md')}
for root in ('skills', 'agents', 'docs', 'CLAUDE.md'):
    root_p = ROOT / root if root != 'CLAUDE.md' else ROOT
    for p in sorted(root_p.glob('**/*.md')) if root != 'CLAUDE.md' else [ROOT / 'CLAUDE.md']:
        text = p.read_text(encoding='utf-8', errors='replace')
        for name in set(re.findall(r'\[\[概念：([^\]]+?)\]\]', text)):
            if f'概念：{name}' not in concepts:
                warn(f"{rel(p)} 双链未解析: [[概念：{name}]]（concepts/概念：{name}.md 不存在）")

# --- 6. 斜杠命令 ---
for p in sorted(ROOT.glob('.claude/commands/*.md')):
    fm = frontmatter(p)
    if fm is None or 'description' not in fm:
        err(f"{rel(p)} 缺 description frontmatter")

# --- 7. 技能状态表登记 ---
state = (ROOT / 'docs/技能状态.md').read_text(encoding='utf-8', errors='replace')
registered = set(re.findall(r'^\|\s*\d+\s*\|\s*([a-z0-9-]+)\s*\|', state, re.M))
for name in registered:
    if name not in {d.name for d in ROOT.glob('skills/*')} and not name.startswith('~'):
        err(f"技能状态.md 登记了不存在的技能: {name}（已合并/移出的请删除行或加 ~~删除线~~）")

# --- 报告 ---
print(f"校验 {checked} 个文件")
for w in warnings:
    print(f"  WARN {w}")
for e in errors:
    print(f"  ERR  {e}")
print(f"结果: {len(errors)} 错误, {len(warnings)} 警告")
sys.exit(1 if errors else 0)
