# 从零开始部署指南（Deployment Guide）

> 两级路径：5 分钟体验（不装任何东西）→ 30 分钟部署（本地跑通第一个项目）。

## 一级 · 5 分钟体验（零安装）

1. 打开初筛台：https://justinjchen-cornell.github.io/Hardtech-Venture-Capital-OS/
2. 填 14 个字段（项目名/赛道/阶段/元事实等级/技术/团队/市场/订单/收入）
3. 点"生成基本评判"——得到：三选项分类 + 死亡清单 + 三把尺评分 + ESK + MatMax + 失败概率 + 决策门 + 下一步动作

> 适合：先感受框架是否适合你，不需要任何安装。

## 二级 · 30 分钟部署（本地跑通第一个项目）

### 前置条件
- 已安装 Claude Code
- 已安装 Python 3
- 已安装 book-to-skill（可选，仅当要转新书）

### 第 1 步：拉取项目（2 分钟）
```bash
git clone https://github.com/Justinjchen-Cornell/Hardtech-Venture-Capital-OS.git
cd Hardtech-Venture-Capital-OS
```

### 第 2 步：安装子代理（2 分钟）
```bash
cp agents/*.md ~/.claude/agents/
# 验证：ls ~/.claude/agents/ 应看到 8 个 .md
```

### 第 3 步：加载技能（2 分钟）
```bash
# 本地已转好的 skill（若无，从 03.Skills/ 复制方法论镜像）
cp -r 03.Skills/*/ ~/.claude/skills/ 2>/dev/null || echo "跳过（本地无 skill 时需先转书）"
```

### 第 4 步：进入项目目录（自动加载决策纪律）
```bash
cd 09.BiZZ/06.VC   # 或你的项目目录——CLAUDE.md 自动生效
```

### 第 5 步：跑第一个项目（15 分钟）
```bash
# 方式 A：快速初筛（不用写代码）
#   打开 index.html 填表 → 得到 60 秒评判

# 方式 B：完整管线（按协议 5 阶段）
#   在 Claude Code 中说：
#   "对 {项目名} 按管线执行协议跑阶段 1（赛道评估+技术尽调+转化评估）"
#   → 按 docs/rules/管线执行协议.md 的输入/输出/交接逐步骤执行
#   → 每步产出用 templates/pipeline/0X-*.md 模板
```

### 第 6 步：转新书（可选，10 分钟/本）
```bash
cd scripts/book-to-skill
python book_pipeline.py --md "书.md" --slug 新skill --mode auto
# 然后按"逐本循环 7 步"精读 → 组装 skill → 3 问验证
```

## 常见问题（FAQ）

| 问题 | 处理 |
|:--|:--|
| 子代理模型报错？| 确认 agents/*.md 里 model 为 deepseek-v4-flash/pro（你的环境路由）|
| push 失败（代理问题）？| `git -c http.proxy= -c https.proxy= push` |
| skill 加载不出来？| 确认 SKILL.md 在 ~/.claude/skills/{slug}/ 下，格式含 name+description |
| 初筛台和管线结论不一致？| 正常——初筛台=决策门 1-2 快速版，管线=全 5 门深度版 |
| 需要 11 本书全文？| 版权原因不入 repo；本地 02.MD/ 有已转文本 |

## 局限性（诚实声明）
- 本系统是**辅助决策工具**，不是自动投资机器人——最终判断由你负责
- 不能替代你对创始人的直觉判断（AI 看数据，你看人）
- 在中国硬科技场景构建验证，其他市场/赛道可能不适用
- **AI 可能出错**——所有输出需人工复核；关键事实以一手文件为准（元事实 ≥L3）
