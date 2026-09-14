# Idea-Driven Research Workflow

## Codex 快捷指令

Agent 读取根目录 `AGENTS.md` 后，日常只需使用：`启动研究会话`、`启动下一轮文献调研`、`执行本轮调研`、`精读这篇论文`、`收尾本轮调研`、`做本周研究总结`。长 prompt 位于 `.workflow/prompts/`，研究输出默认使用简体中文。


这是一个面向**持续演化研究 idea** 的文献调研工作流。它不是“帮你搜更多论文”，而是维护一个可版本化的 Idea State，并把每个真正影响研究方向的不确定性路由到互补的文献检索视角。

当前仓库只完整实现 **Literature Research（科研文献调研）** 子模块。Baseline 复现、数据集、实验、论文写作模块只保留空接口，方便未来扩展而不重构目录。

## 核心闭环

```text
ChatGPT/研究讨论历史
        ↓
Idea State 重建与增量变化（idea delta）
        ↓
关键 claim / unresolved question
        ↓
多视角互补检索
        ↓
Paper Card + Evidence Ledger
        ↓
Gap / Contradiction / Decision Synthesis
        ↓
更新 Idea State
```

## 为什么不是普通“文献综述模板”

普通 AI 辅助调研很容易变成：

```text
提问 → 大范围搜索 → 一堆论文 → 更多概念 → idea 漂移 → 再搜索
```

本工作流要求每轮调研先回答：

1. **当前 idea 到底是什么？**
2. **哪些想法已经被否掉，不能被新 Agent 随手复活？**
3. **哪几个未知问题最可能改变方向？**
4. **应该从哪些互补视角找证据？**
5. **新论文究竟改变了哪个判断？**

## 多视角调研 Lens

- **Direct-neighbor**：最接近当前研究问题的工作。
- **Representation/state**：模型显式表示什么对象，哪些对象会被更新。
- **Mechanism/architecture**：实现该 idea 所需要的计算机制。
- **Domain/physics**：抽象是否符合真实科学过程与物理/生物约束。
- **Data/benchmark/generalization**：监督信号、数据量、split、泄漏、OOD。
- **Failure/negative evidence**：类似方法在哪些情况下失效。
- **Adjacent-field analogy**：从 CV、几何学习、系统、因果等邻域寻找可迁移机制。
- **Novelty/collision**：想法的组合是否已经被别人做过。
- **Executable baseline**：是否存在可执行的代码/数据，为后续复现模块做准备。

## 关键文件

- `research/idea/current.md`：当前唯一有效的 idea 状态。
- `research/idea/rejected.md`：已经否决的 framing/假设及原因。
- `research/idea/decision_log.md`：方向变化的原因，而不是仅记录结果。
- `research/idea/open_questions.md`：当前最值得用文献解决的问题。
- `research/literature/routes.md`：不同未知问题应该走哪种调研路线。
- `research/literature/papers/`：一篇论文一张 Paper Card。
- `research/literature/evidence/claim_ledger.csv`：claim 到证据的可追溯关系。
- `research/literature/synthesis/gap_map.md`：真正的 research gap，而不是“没人做过”。
- `.workflow/handoff.md`：跨 Agent / 跨会话继续工作的交接状态。

## ChatGPT 导出如何接入

原始 ChatGPT 导出默认不进入 git。先规范化：

```bash
python scripts/ingest_chatgpt_export.py /path/to/conversations.json \
  --out research/imports/chatgpt/latest_digest.md \
  --keywords "binding affinity,interface,state,structure,mutation,antibody,ligand"
```

然后让 Agent 阅读：

```text
AGENTS.md
.workflow/SKILL.md
research/idea/current.md
research/idea/rejected.md
research/idea/decision_log.md
research/imports/chatgpt/latest_digest.md
```

Agent 的任务不是重新总结全部聊天，而是识别：

- 新出现的稳定观点；
- 被明确否掉的旧方向；
- 研究问题边界的收缩或扩大；
- 从“直觉”升级成“有证据判断”的部分；
- 新增的关键未知问题；
- 需要启动或停止的调研路线。

## 针对当前 AIDD 方向的初始化

仓库已经放入一个经过泛化的初始问题：

> 如何把局部 molecular interaction / binding interface 作为显式计算对象，使局部 edit / mutation 引起的表示变化能够被直接建模，并用于预测 binding-affinity change？

当前刻意不锁死 protein–ligand 或 antibody–antigen 场景，因为“应该在哪个真实问题上实例化”本身就是第一轮文献调研需要回答的问题。

## 开源安全

默认 `.gitignore` 会忽略：

- 原始 ChatGPT export；
- `research/private/`；
- 下载的论文 PDF / LaTeX source；
- 本地 cache。

公开 GitHub 前仍建议执行 `git status` 做最后检查。

## 致谢与许可证

固定文件结构、handoff 和 research skeleton 的基本思想受到 `skJack/research-workflow` 启发（Apache-2.0）。本仓库针对“动态 idea 驱动的文献调研”进行了独立重构。详见 `NOTICE`。

本项目采用 Apache-2.0 License。
