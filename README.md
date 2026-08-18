# 🎯 Hardtech Venture Capital OS

> A Claude Code-powered decision operating system for early-stage **hardtech VC** — built on an 11-book knowledge foundation, 5 specialist subagents, a 7-step executable deal pipeline, and a web-based 60-second screening dashboard. Origin: **Chengdu, China**.

<p align="center">
  <img src="assets/logo.svg" width="120" alt="HVOS logo"/>
</p>

<p align="center">
  <a href="https://justinjchen-cornell.github.io/Hardtech-Venture-Capital-OS/"><img src="https://img.shields.io/badge/Live%20Dashboard-GitHub%20Pages-blueviolet?style=for-the-badge" alt="Dashboard"/></a>
  <img src="https://img.shields.io/badge/Books-11%20Skills-success?style=for-the-badge" alt="11 books"/>
  <img src="https://img.shields.io/badge/Agents-5-blue?style=for-the-badge" alt="5 agents"/>
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="MIT"/>
</p>

---

## 🚀 Live Demo — 60-Second Screening Dashboard

**Drop in project facts → get a structured first-pass verdict** — five frameworks fused into one client-side engine (no backend, runs entirely in your browser):

[**Open the Screening Dashboard**](https://justinjchen-cornell.github.io/Hardtech-Venture-Capital-OS/)

The dashboard encodes the system's core screening logic: three-option classification, six-item death list, three rulers (team / market / tech), ESK scoring, MatMax TRL×CRL, sign-based investing, and decision gates — output as a verdict card with risks and prioritized next actions.

---

## 🏗️ Architecture

```mermaid
graph TB
    subgraph L1["Layer 1 · CLAUDE.md — Decision Rules"]
        R1["Constitution · 8 Iron Rules"]
        R2["Framework Arbitration · 11 Rules"]
        R3["Pipeline Protocol · Decision Gates"]
    end

    subgraph L2["Layer 2 · 11 Skills — On-Demand Book Knowledge"]
        S1["Poor Charlie · Shou Zheng · Hardtech Wave"]
        S2["Tech Transfer · Venture Deals · Value 3.0"]
        S3["Growth Stocks · My PE · Damodaran · Windfall · DD Handbook"]
    end

    subgraph L3["Layer 3 · 5 Subagents — Specialist Workers"]
        A1["sector-scanner"] --> A2["tech-dd"]
        A2 --> A3["valuation-analyst"]
        A3 --> A4["tech-transfer-advisor"]
        A4 --> A5["deal-negotiator"]
    end

    subgraph L4["Layer 4 · Pipeline — 7-Step Executable Protocol"]
        P1["1 · Screen"] --> P2["2 · Filter"]
        P2 --> P3["3 · Deep DD"]
        P3 --> P4["4 · Valuation"]
        P4 --> P5["5 · Conversion"]
        P5 --> P6["6 · Terms"]
        P6 --> P7["7 · IC Memo"]
    end

    L1 --> L2 --> L3 --> L4
```

## ✨ Highlights

- **11-book knowledge system** — from Munger's mental models to Damodaran's valuation, each distilled into an on-demand skill (verified by 3-question tests)
- **5 specialist subagents** — sector scanning (ESK + cycles), technical DD (three rulers + 9 numbers), valuation (12-step method library), tech-transfer (TRL / CRL / MatMax), deal structuring
- **Executable pipeline protocol** — every step defines input / process / output / handoff / exception branches (SOP, not prose)
- **5 decision gates** — mandatory before any investment decision (meta-facts ≥ L3, death list clean, good-ball check, Will-B-P ≥ 60, counter-arguments)
- **Framework arbitration rules** — 11 rules built on *dialectical unity of opposites* for resolving conflicts between frameworks
- **Meta-fact checklist** — evidence levels L1–L4 for facts that drive valuation (a verbal claim is not a contract)
- **Knowledge write-back protocol (RWP)** — four write-back channels so the system gets smarter with every execution
- **Scenario trigger matrix** — 10 daily scenes mapped to actions (BP 60s screen / founder 15-min prep / post-investment monitoring / quarterly audit)
- **Chengdu 4+6 focus** — anchored to the city's strategic emerging & future industries, data-driven convergence (no preset sector bias)

## 🚦 Quick Start

```bash
# 1. Load the decision rules (project-level CLAUDE.md)
cd 09.BiZZ/06.VC

# 2. Install subagents
cp agents/*.md ~/.claude/agents/

# 3. Use the system
#    "Run the 7-step pipeline on {project}" — follow 管线执行协议
#    "Open the screening dashboard" → index.html / GitHub Pages
```

## 📚 The 11-Book Foundation

| Layer | Book | Core Contribution |
|:--|:--|:--|
| Operating system | *Poor Charlie's Almanack* | Mental models · circle of competence · inversion · misjudgment psychology |
| Scale | *Hardtech Wave* | ESK framework · five technology paradigms |
| Cycle | *The Next Windfall* | New-quality transformation · timing & foam |
| Due diligence | *Shouzheng* · *My PE Views* · *Growth Tech Stocks* | Three rulers · 9-number DD · 20% rule |
| Valuation | *Value Investing 3.0* · *Investment Valuation* | BMP framework · DCF / multiples / startup |
| Conversion | *Tech Commercialization* (Tsinghua PBCSF) | TRL×CRL · MatMax · five-stage funnel |
| Terms | *Venture Deals* | E/C clauses · term sheet · negotiation |
| Handbook | *PE & DD Handbook* | 13 research elements · sign-based investing |

## 🏙️ Chengdu 4+6 Focus (candidate map, data-driven)

- **4 emerging**: new energy / new materials / low-altitude economy / aerospace
- **6 future**: quantum · bio-manufacturing · brain-computer · hydrogen & fusion · embodied AI · 6G
- No preset sector bias — the pipeline converges by project samples (≥10) × local endowment × cognitive reach

## 📁 Directory

```
CLAUDE.md · index.html (screening dashboard) · README.md
docs/rules/    framework arbitration · pipeline protocol v1.2 · RWP · scenario matrix
03.Skills/     11 skill mirrors (methodology only)
06.Concepts/   42 linked concept pages
agents/        5 subagents
scripts/       deal sourcing + book-to-skill pipeline
templates/     project card + 8 pipeline output templates
examples/      end-to-end demo (Zheng project)
docs/          design docs · constitution · book map
```

## 🗺️ Roadmap

- [x] 11-book knowledge system + 5 subagents
- [x] Executable pipeline protocol + decision gates
- [x] Meta-fact evidence levels + framework arbitration (dialectical)
- [x] Scenario trigger matrix + hybrid info collection
- [x] Screening dashboard (GitHub Pages)
- [ ] Portfolio / post-investment monitoring module
- [ ] Chengdu channel sourcing automation (enterprise-data mining)
- [ ] IC meeting workflow

## 📄 License

MIT © Justinjchen-Cornell

---

# 🇨🇳 中文版

# 🎯 Hardtech Venture Capital OS — 成都早中期硬科技投资决策操作系统

> 基于 Claude Code 的投资决策操作系统：11 本书方法论 × 5 个专项子代理 × 7 步可执行管线 × 浏览器端 60 秒初筛台。立足成都，面向早中期硬科技。

## 🚀 在线演示：项目初筛台

**把项目资料丢进去 → 60 秒出基本评判**——五个框架（穷查理 / 守正 / 硬科技浪潮 / MatMax / 迹象法）融合为纯前端引擎：

[**打开初筛台**](https://justinjchen-cornell.github.io/Hardtech-Venture-Capital-OS/)

输出：三选项分类 · 死亡清单六条 · 三把尺评分 · ESK · MatMax 定位 · 失败概率 · 决策门检查 · 下一步动作。

## 🏗️ 架构：知识三层 + 业务一条管线

```mermaid
graph TB
    subgraph L1["层 1 · CLAUDE.md — 决策纪律"]
        R1["宪法 · 8 条铁律"]
        R2["框架仲裁 · 11 条规则"]
        R3["管线协议 · 决策门"]
    end

    subgraph L2["层 2 · 11 个 Skill — 按需加载的书本知识"]
        S1["道（穷查理）· 术（守正）· 尺度（硬科技浪潮）"]
        S2["转化 · 条款 · 估值 3.0 · 长期基本面"]
        S3["本土实战 · 估值圣经 · 周期 · 工作手册"]
    end

    subgraph L3["层 3 · 5 个子代理 — 专项专家"]
        A1["赛道扫描"] --> A2["技术尽调"]
        A2 --> A3["估值分析"]
        A3 --> A4["转化顾问"]
        A4 --> A5["谈判设计"]
    end

    subgraph L4["层 4 · 管线 — 7 步可执行协议"]
        P1["① 赛道扫描"] --> P2["② 初步筛选"]
        P2 --> P3["③ 深度尽调"]
        P3 --> P4["④ 估值分析"]
        P4 --> P5["⑤ 转化评估"]
        P5 --> P6["⑥ 交易结构"]
        P6 --> P7["⑦ IC 备忘录"]
    end

    L1 --> L2 --> L3 --> L4
```

## ✨ 核心特性

- **11 本书方法论**——每本蒸馏为按需加载的 skill（含 3 问验证）
- **可执行管线协议**——每步定义输入 / 处理 / 输出 / 交接 / 异常（SOP 而非散文）
- **决策门 5 道**——投决前必过（元事实≥L3 / 死亡清单无致死 / 好球对照 / Will-B-P≥60 / 反向观点）
- **框架仲裁规则 11 条**——对立统一思维解决框架冲突（如：纪律底线刚性 × 路径柔性）
- **元事实清单**——支撑估值的事实分级验证（口头 L1 ≠ 合同 L3）
- **知识回写协议（RWP）**——四类回写，让体系越用越聪明
- **场景触发矩阵**——收 BP 60 秒初筛 / 见创始人 15 分钟准备 / 投后五大监控 / 季度宪法审计
- **成都 4+6 候选地图**——不预设焦点，数据驱动收敛

## 🚦 快速开始

```bash
cd 09.BiZZ/06.VC          # 进入项目目录（自动加载决策纪律）
cp agents/*.md ~/.claude/agents/   # 安装 5 个子代理
# 打开 index.html 使用初筛台；完整项目走管线协议 7 步
```

## 📄 License

MIT © Justinjchen-Cornell
