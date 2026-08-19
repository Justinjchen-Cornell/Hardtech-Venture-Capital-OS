# 🎯 Hardtech Venture Capital OS

> A Claude Code-powered decision operating system for early-stage **hardtech VC** — built on an 11-book knowledge foundation, 5 specialist subagents, a 7-step executable deal pipeline, and a web-based 60-second screening dashboard. Origin: **China, China**.

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


## 🔗 Knowledge Chain — 11 Books → Handbook → Agents

```mermaid
graph TD
    A["Poor Charlie (Way) · Mental Models"] --> B["Shou Zheng (Skill) · Three Rulers"]
    B --> C["Hardtech Wave (Scale) · ESK / 5 Paradigms"]
    C --> D["Tech Transfer (Conversion) · TRL-CRL"]
    D --> E["Venture Deals (Terms) · E/C Clauses"]
    E --> F["Value Investing 3.0 + IV (Valuation) · BMP / DCF"]
    F --> G["Growth Tech Stocks (Fundamentals) · 20% Rule"]
    G --> H["My PE Views (Local Practice) · 9 Numbers"]
    H --> I["The Next Windfall (Cycles) · Timing & Foam"]
    I --> J["PE & DD Handbook (Workbook)<br/>13 Research Elements + Sign-Based Investing"]
    J --> K["Agents<br/>sector-scanner template + tech-dd sign check"]
```

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
- **China 4+6 focus** — anchored to the city's strategic emerging & future industries, data-driven convergence (no preset sector bias)

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

## 🏙️ China 4+6 Focus (candidate map, data-driven)

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
- [ ] China channel sourcing automation (enterprise-data mining)
- [ ] IC meeting workflow

## 📄 License

**Apache License 2.0** — commercial use, modification, and redistribution are permitted, provided that the copyright notice and NOTICE file are retained.

© Justinjchen-Cornell · See [LICENSE](LICENSE) and [NOTICE](NOTICE).

---

---

[🇨🇳 中文版](README.zh-CN.md)
