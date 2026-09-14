# Prompt — 精读一篇 Decision-Relevant Paper

目标不是复述论文，而是判断它对当前研究问题意味着什么。

先读取当前 Idea State 和对应 literature cycle，再精读指定论文。若不存在 Paper Card，创建一个。

用中文填写/更新：

1. **论文要解决的真实问题**；
2. **输入 / 输出 / supervision**；
3. **核心 computational object / representation**；
4. **forward computation 中结构信息具体在哪里参与**；
5. 若涉及 mutation/edit：**什么变量被改变、什么被固定、change 是否显式表示**；
6. **dataset / split / evaluation protocol**；
7. **关键结果**，仅记录与当前 claim 有关的结果；
8. **failure / limitation / leakage / OOD 风险**；
9. **论文明确支持的事实**；
10. **我们的推断**（必须与事实分栏）；
11. **对当前 idea 的影响**：support / weaken / collide / narrow / irrelevant；
12. **它引出的一个最高价值后续问题**。

不要因为论文使用了相似术语就认定它解决了同一个问题；要比较 computational object、information flow、supervision 和 evaluation。
