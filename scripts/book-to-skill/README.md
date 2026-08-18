# book-to-skill — 读书 → Skill 生成管线

> 把一本书/文档转化为 Claude Code 可加载 skill 的标准流程（Hardtech-VC-OS 的"逐本循环"）。

## 逐本循环 7 步（已验证 11 本书）

1. **预处理**：book_pipeline.py 清洗 NUL / 重建中文标题 / 定位章节
2. **提炼方案呈现 + 用户确认**（精读单元规划）
3. **精读**（带教模式：原文→解读→体系握手→练习→沉淀）
4. **组装 skill**：SKILL.md + chapters/ + patterns + glossary + cheatsheet
5. **3 问验证**（已知答案——防乱编）
6. **镜像**：方法论层（4 文件）同步 03.Skills/ → repo
7. **沉淀 + RWP 回写**（概念页/执行日志/仲裁规则）

## 脚本用法

```bash
# 中文书：重建标题结构（守正示例：4篇31章119节）
python book_pipeline.py --md "守正.md" --slug shou-zheng --mode headings

# 英文书：清洗 NUL + 定位章节
python book_pipeline.py --md "Investment-Valuation.md" --slug damodaran --mode clean

# 英文书：精选章节提取（IV VC 精选示例：Ch13/22-24）
python book_pipeline.py --md "IV.md" --slug damodaran --mode chapters --select 13,22,23,24
```

## 已验证案例（2026-08-17/18）

| 书 | 模式 | 产出 skill |
|:--|:--|:--|
| 穷查理宝典 | 精读为主 | poor-charlie-almanack（11 单元）|
| 守正 | headings | shou-zheng |
| 硬科技浪潮 | locate | hardtech-wave |
| Investment Valuation | clean+chapters(33%) | damodaran-valuation |
| 科技成果转化文档 | clean | tech-transfer |
| 下一个风口 | locate | next-windfall |
| 私募尽调手册 | locate | pe-dd-handbook |

## 注意
- 版权：书全文不入 repo（03.Skills/ 只镜像 SKILL.md 摘要级 4 文件）
- 精读产出（概念页/深度卡）走 RWP 回写，不入 skill 目录
