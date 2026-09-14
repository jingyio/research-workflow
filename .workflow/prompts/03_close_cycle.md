# Prompt — 收尾/关闭 Literature Cycle

基于当前 cycle 的 repository evidence 做**决策型综合**。不要只写 literature summary。

用中文完成并落盘：

## 1. 一句话结论
从 `SUPPORT / WEAKEN / REJECT / NARROW / UNRESOLVED` 中选择最合适的结论，并说明对象是哪条 claim。

## 2. 最关键证据
只列真正改变判断的 evidence，并给出来源。

## 3. 反例与矛盾
哪些证据互相冲突？冲突可能来自 task、data、split、representation、mechanism 还是 evaluation？

## 4. Idea Delta
- 新增；
- 改变；
- 削弱/条件化；
- 否决；
- 未改变；
- 新开放问题。

## 5. Decision Update
- 哪条 claim 改变；
- 置信度 before -> after；
- 排除了什么；
- 什么证据会再次反转当前判断。

## 6. 下一步
给出唯一最高价值的下一问题，并判断它是：
- literature-resolvable；
- code/data/experiment-resolvable；
- 暂时不值得继续。

## 7. Repository updates
按证据强度更新必要文件：
- `research/literature/evidence/claim_ledger.csv`
- `research/literature/evidence/contradiction_log.md`
- `research/literature/synthesis/gap_map.md`
- `research/literature/synthesis/weekly_update.md`
- `research/idea/current.md`（只有证据足够时）
- `research/idea/decision_log.md`
- `research/idea/rejected.md`
- `research/idea/open_questions.md`
- `.workflow/handoff.md`

重大 Idea State 修改前先 snapshot。不要因为一轮搜索没找到同类方法就宣称 novelty。
