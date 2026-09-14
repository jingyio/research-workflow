# Prompt — 执行已批准的 Literature Cycle

执行当前已批准的 cycle。目标不是最大化论文数量，而是最大化 **decision-changing evidence**。

必须：

1. 按 cycle 中选定的 2–5 条互补 route 搜索；
2. 同时寻找支持和反驳证据；
3. 技术 claim 优先 primary paper；
4. 对候选进行 triage，仅保留能贡献不同 method/evidence class 的论文；
5. 将候选注册进 `paper_pool.csv` 和必要的 search log；
6. 对真正高价值论文建立/更新 Paper Card；
7. 对每篇重要论文回答：
   - 预测/研究目标是什么？
   - 输入、输出、监督信号是什么？
   - 显式 computational object 是什么？
   - mutation/edit 后什么发生变化，什么保持不变？
   - interface / structure / change 是显式还是隐式？
   - dataset / split / generalization 设置是什么？
   - 最重要 failure mode 是什么？
   - 它支持、削弱、冲突还是重构当前 claim？
8. 更新 claim ledger、contradiction log、research map、gap map、reading queue；
9. 严格区分“论文证据”和“Agent/研究者推断”。

输出语言：分析与综合使用简体中文；论文标题、query、模型/数据集名保留原文。

若剩余问题已经必须通过代码、数据或实验回答，停止扩张文献并明确标记，不要硬凑更多论文。

本阶段可以形成临时判断，但最终 Idea State 更新放在 `03_close_cycle.md`。
