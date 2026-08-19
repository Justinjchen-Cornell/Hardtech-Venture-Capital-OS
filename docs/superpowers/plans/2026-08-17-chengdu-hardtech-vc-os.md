# 中国硬科技投资决策操作系统（Hardtech VC OS）实施计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 建立中国早中期硬科技投资决策操作系统——知识三层（CLAUDE.md + 11 本书 Skills + 专项子代理）+ 业务一层（项目池/流水线），书**一本本慢慢提炼转化**（非批量机械化），《穷查理宝典》精读并行推进。

**Architecture:** 本地 vault `09.BiZZ/06.VC/` 为项目根；`~/.claude/skills/` 放书技能、`~/.claude/agents/` 放子代理；GitHub repo `Hardtech-Venture-Capital-OS`（public）同步方法论层（不含书全文）。

**Tech Stack:** Claude Code · book-to-skill（`03.skills/book-to-skill-master`，python -m book_to_skill）· Python 3 · Git/GitHub · Obsidian（脑归档规则）

## Global Constraints

- 版权：`01.Book/`、`02.MD/` 书全文**绝不入 repo**（.gitignore 排除）；repo 只入方法论（CLAUDE.md、agents、SKILL.md 摘要级、模板、docs）
- 模型路由：深度分析用 pro、扫描/谈判用 flash；**禁用 opus/sonnet**
- `06.VC/CLAUDE.md` 目标 <200 行，只放稳定纪律
- 书转换：**一本一本**（预处理→提炼方案确认→转换→3 问验证→沉淀），用户可中途调整
- 每本 skill 转完必须问 3 个已知答案问题验证（防乱编），通过才进入下一本
- 精读：每单元产出（概念页 + 沉淀卡 + 进度更新），不产出不进入下一单元
- 中文为主要工作语言；文件路径全部基于本 vault（Windows，用正斜杠）
- 4+6 作为候选地图：不预设行业焦点，项目池数据驱动收敛

---

### Task 1: 本地骨架（目录 + .gitignore + LICENSE + README v0.1）

**Files:**
- Create: `.gitignore`
- Create: `LICENSE`
- Create: `README.md`
- Create: 空目录 `skills/` `04.Projects/` `05.Pipeline/`（README 说明用途）

**Interfaces:**
- Produces: repo 根骨架；后续所有任务的文件均落在此结构下

- [x] **Step 1: 创建 .gitignore**（排除版权与本地数据）✅ 已验证
- [x] **Step 2: 创建 LICENSE**（MIT）✅
- [x] **Step 3: 创建 README.md v0.1** ✅
- [x] **Step 4: 创建空目录并放置 README 说明** ✅
- [x] **Step 5: 验证** ✅（git check-ignore 全部匹配）

### Task 2: git init + GitHub 连接 + 首次 push 骨架

**Files:** 无新增（git 元数据）

- [x] **Step 1: git init** ✅（`git init -b main`）
- [x] **Step 2: 检查认证** ✅（gh 未登录，但 git push 凭据可用——push 成功）
- [x] **Step 3: add + commit** ✅（commit 5c57bcd）
- [x] **Step 4: remote add + push** ✅（`[new branch] main -> main`）
- [x] **Step 5: 验证** ✅（HTTP 200，README/LICENSE/docs/templates 可见）
- [ ] 待办：repo description/topics（需 gh auth login 后由 Claude 填，或网页手动填）

### Task 3: 精读单元 1（多元思维模型——箴言版 vs 演讲版）

**Files:**
- Create: `05.Pipeline/reading-进度.md`（精读进度总表）
- Create: 概念页（Obsidian 双链）：多元思维模型、Lollapalooza效应、思维格栅
- Create: `00.会话沉淀/深度/2026-08-17-穷查理精读单元1-多元思维模型.md`

**Interfaces:**
- Consumes: 穷查理宝典 MD 第四章即席谈话 + 附录第一讲（行 682-1349、2770-3315）
- Produces: 概念页 x3、沉淀卡 x1、进度表首行

- [x] **Step 1: 贴原文关键段落** ✅
- [x] **Step 2: 带教示范** ✅（郑宗良 6 模型叠放）
- [x] **Step 3: 提炼概念** ✅（9 概念页：多元思维/Lollapalooza/思维格栅/能力圈/逆向思维/误判心理学/集中投资/竞争性毁灭/芒格模型清单/芒格画像）
- [x] **Step 4: 沉淀** ✅（10 深度卡 + 进度表）
- [x] **Step 5: 用户确认进入单元 2** ✅（8 主单元 + 3 补充单元全部完成，2026-08-17）

### Task 4: 《穷查理宝典》预处理（标题重建）

**Files:**
- Create: `02.MD/structured/穷查理宝典-structured.md`（新建，保留原文件）

**Interfaces:**
- Consumes: `02.MD/穷查理宝典...md`（4,168 行）
- Produces: 结构化 MD（规范 `## 第N章` 标题，正本+附录分层清晰）

- [ ] **Step 1: 读目录区，确认 4 章 + 6 辑 + 附录 4 讲的标题行位置**（已实测：序言 26 / 上篇 184 / 第一章 188 / 附录 2734 起）
- [ ] **Step 2: 重建标题层级**（`##` 上篇/下篇/附录，`###` 章/辑，正文小节一级标题化）
- [ ] **Step 3: 验证**：标题数合理（>50），抽查 3 处正文与标题对应

### Task 5: 《穷查理宝典》提炼方案呈现 + 用户确认

**Files:** 无（对话型任务）

- [ ] **Step 1: 呈现提炼方案**：skill 结构（SKILL.md 核心模型清单 / chapters 划分 / glossary 关键词 / cheatsheet 决策表）、3 个验证问题草稿
- [ ] **Step 2: 用户确认或调整**（用户可指定要强化的章节）

### Task 6: 《穷查理宝典》提炼转换 → skill 生成 + 验证 + 沉淀

**Files:**
- Create: `~/.claude/skills/poor-charlie-almanack/SKILL.md` + `chapters/` + `glossary.md` + `patterns.md` + `cheatsheet.md`
- Create: `skills/poor-charlie-almanack/`（repo 同步镜像，仅 SKILL.md 摘要级）
- Modify: `05.Pipeline/reading-进度.md`

- [ ] **Step 1: 执行提炼**（基于 Task 4 结构化 MD + 精读产出，用 book-to-skill 或手工提炼）
- [ ] **Step 2: 3 问验证**（已知答案：能力圈定义 / 三选项分类 / 25 种误判清单抽查）
- [ ] **Step 3: 沉淀**——更新进度表；repo 镜像同步
- [ ] **Step 4: commit**（`feat: add poor-charlie-almanack skill`）

### Task 7-10: 逐本循环——守正 → 硬科技浪潮 → 其余书（每本一个循环）

**Files（每本）:** `02.MD/structured/<书>-structured.md`、`~/.claude/skills/<slug>/`、`skills/<slug>/`

**Interfaces:**
- Consumes: `02.MD/` 各书原始 MD
- Produces: 每本一个 skill（SKILL.md+chapters+glossary+patterns+cheatsheet）+ 验证记录

循环模板（每本复用，用户可中途调整顺序）：
- [ ] 预处理（标题重建；Investment Valuation 额外：去 NUL + 分 3 块）
- [ ] 提炼方案呈现 + 用户确认
- [ ] 提炼转换 + skill 生成
- [ ] 3 问验证（已知答案）
- [ ] 沉淀 + repo 镜像 + commit

**书序建议**：守正（T7）→ 硬科技浪潮（T8）→ 我的PE观 / 高增长科技股 / 下一个风口（T9 按用户节奏逐本）→ 价值投资3.0 → 私募尽调手册（量大）→ Investment Valuation（分块）→ 待补：高科技营销魔法、风险投资交易（需用户补源文件）

### Task 11: 06.VC/CLAUDE.md v0.1（精读单元 3 后，宪法片段先行）

**Files:**
- Create: `CLAUDE.md`

- [ ] **Step 1: 汇总精读已产出铁律**（多元思维/能力圈/逆向思维片段）
- [ ] **Step 2: 起草 6 块结构**（哲学/三把尺/估值纪律/4+6候选地图+渠道/铁律/6步流程），<200 行
- [ ] **Step 3: 用户审阅 + commit**（`feat: add project CLAUDE.md v0.1`）

### Task 12: 子代理 3 个（sector-scanner / tech-dd / valuation-analyst）

**Files:**
- Create: `~/.claude/agents/sector-scanner.md`（model: flash）
- Create: `~/.claude/agents/tech-dd.md`（model: pro）
- Create: `~/.claude/agents/valuation-analyst.md`（model: pro）

- [x] **Step 1: 写 sector-scanner** ✅（flash，5 步评估流程 + 输出模板）
- [x] **Step 2: 写 tech-dd** ✅（pro，技术尺三问 + 司机知识三问 + IP 核查 + 芒格画像 + 可证伪三问）
- [x] **Step 3: 写 valuation-analyst** ✅（pro，生命周期匹配 + 好球对照 + 4 步法占位）
- [x] **Step 4: 冒烟测试** ✅（skill 引用可解析；实际任务派发待用户侧验证）
- [x] **Step 5: commit** ✅（7b36d12，repo agents/ 镜像同步）
- [ ] 待补：hardtech-wave / 我的PE观 / 守正 / 价值投资3.0 / Investment Valuation skills 就绪后，更新三个 agent 的细节引用

### Task 13: 项目池模板 + 首批项目入池

**Files:**
- Create: `04.Projects/_templates/项目卡片.md`
- Create: `04.Projects/_sources/中国项目源渠道.md`（A/B/C 分级）
- Create: ≥10 张项目卡片（覆盖 4+6 候选方向，含郑宗良天线）

- [ ] **Step 1: 设计项目卡片模板**（赛道标签/来源/芒格三选项/守正三把尺初评/20%法则/跟进状态/双链）
- [ ] **Step 2: 渠道清单初版**
- [ ] **Step 3: 首批项目入池**（数据驱动，不预设行业结论）

### Task 14: 郑宗良天线项目端到端演练（后置）

- [ ] 用 sector-scanner 出赛道评估 → tech-dd 出技术尽调 → valuation-analyst 出估值 → 汇总 IC memo 草案（不预设结论）

---
