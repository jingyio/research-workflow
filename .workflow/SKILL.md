---
name: idea-driven-literature-workflow
description: Maintain a versioned research idea and run complementary, targeted literature investigations that update claims, gaps, contradictions, and the reading queue. Use when importing ChatGPT research history, refining a research direction, planning a literature search, adding papers, testing novelty, or deciding what to read next.
license: Apache-2.0
---

# Idea-Driven Literature Research

## Objective

把持续演化的研究 idea 转化为**可追踪证据的研究地图**。优化目标是 research decision information，而不是论文数量。

## Language contract

默认以**简体中文**输出所有研究结论、综合分析、Idea Delta、Decision Update、Paper Card 中的分析性内容和用户可见报告。以下内容保留英文或原文更合适：论文标题、作者、数据集、模型名、代码标识符、DOI/arXiv、搜索 query，以及需要精确保留的术语。

## Phase 0 — Load state

按顺序读取：

1. `research/idea/current.md`
2. `research/idea/rejected.md`
3. `research/idea/decision_log.md`
4. `research/idea/open_questions.md`
5. `research/literature/synthesis/weekly_update.md`
6. `.workflow/handoff.md`

如果本地存在 `research/private/bootstrap_packet.md`，在稳定状态之后读取。若提供 ChatGPT digest，也在稳定状态之后读取。

## Phase 1 — Reconstruct Idea Delta

不要总结整段对话，而是将新材料与当前状态比较。输出：

```text
Idea Delta
- 新增承诺：
- 发生变化的承诺：
- 新近否决：
- 重新打开（必须有明确新证据）：
- 新增开放问题：
- 术语/ framing 变化：
- 未变化的核心：
```

规则：

- 提及频率 != 重要性；
- 后来的明确否决优先于早期热情；
- 区分“有趣类比”和“研究承诺”；
- 区分经验事实和研究直觉；
- 当应用范围未确定时保留不确定性；
- 实质修改前先 snapshot。

## Phase 2 — Convert the idea into claims and uncertainties

将重要 statement 分类为：

- `C-FORM`: problem/formulation claim
- `C-REP`: representation/state claim
- `C-MECH`: mechanism claim
- `C-DOMAIN`: domain/physics claim
- `C-DATA`: data/generalization claim
- `C-NOVEL`: novelty/collision claim
- `C-FEAS`: feasibility/executable-baseline claim

然后问：**什么文献观察结果会改变这条 claim？**

如果没有任何文献证据可能改变它，那么它很可能属于实现/实验问题，不应继续消耗文献预算。

## Phase 3 — Route the research

从 `research/literature/routes.md` 中选择最小互补集合。重大方向判断默认考虑：

- 一个 direct-neighbor route；
- 一个 representation/mechanism route；
- 一个 domain/physics 或 data/generalization route；
- 一个 failure/negative-evidence route；
- novelty/collision 仅在问题表述足够稳定后展开。

不要机械运行所有 route。

## Phase 4 — Search and triage

每条 route：

1. 写清楚要减少什么不确定性；
2. 给出 inclusion / exclusion criteria；
3. 使用多种 query 表述；
4. 技术 claim 优先 primary paper；
5. 将候选注册到 `paper_pool.csv`；
6. 按 **expected decision value** 排序。

高 decision value 的论文通常能够：

- 证伪核心假设；
- 暴露几乎相同的既有方法；
- 界定真正的现实任务/label；
- 揭示数据不足、泄漏或 split 问题；
- 提供直接实例化 idea 的机制；
- 为下一阶段提供可执行 code/data。

## Phase 5 — Read using paper cards

重要论文在 `research/literature/papers/` 下建立独立目录并填写 `card.md`。

必须严格区分：

- 论文明确声称/证明了什么；
- 你的推断；
- 它如何影响当前 idea；
- 什么仍未验证。

不要写与 decision 无关的通用摘要。

## Phase 6 — Synthesize across papers

更新：

- `evidence/claim_ledger.csv`
- `evidence/contradiction_log.md`
- `synthesis/research_map.md`
- `synthesis/gap_map.md`
- `synthesis/reading_queue.md`
- `synthesis/weekly_update.md`

一个好的 gap 不是“论文很少”，而是 problem definition、representation、mechanism、data、evaluation 或 scientific validity 之间存在可明确描述的错配。

## Phase 7 — Update idea or stop

每轮以中文给出：

```text
Decision Update
- 哪条 claim 发生了变化？
- 导致变化的证据：
- 置信度：之前 -> 之后
- 排除了什么？
- 当前最高价值问题是什么？
- 下一步不确定性还能通过文献解决吗？
```

若下一步必须依赖代码/数据/实验，则将其标记为向未启用模块的 handoff，而不是无限继续搜索。

## Stop conditions

当以下任一趋势明确时停止该 route：

- 新论文几乎不再增加 decision-relevant 信息；
- 方法/结果类别已经饱和；
- contradiction 已经足以定位真正未决变量；
- 下一步是 executable uncertainty，而非 bibliographic uncertainty。

## Anti-patterns

- 没有 decision question 的 topic dump；
- 只读支持自己想法的工作；
- 用综述作为技术 claim 的唯一证据；
- 因关键词没搜到就宣称 novelty；
- 让 LLM 替代精确 citation/source tracking；
- 每次会话从头重写 idea；
- 因新论文使用相似词汇而复活已经否决的 framing。
