# Idea-Driven Research Workflow

这是一个面向**持续演化研究 idea** 的文献调研工作流。它不是“帮你搜更多论文”，而是维护一个可版本化的 Idea State，并把每个真正影响研究方向的不确定性路由到互补的文献检索视角。

当前仓库只完整实现 **Literature Research（科研文献调研）** 子模块。Baseline 复现、数据集、实验、论文写作模块只保留空接口，方便未来扩展而不重构目录。

## 核心闭环

```text
ChatGPT / 研究讨论历史
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

---

## 仓库结构：研究内容和 workflow 引擎分开

根目录刻意保持精简。真正需要长期维护的研究内容都放在 `research/`，Agent 规则、prompt、配置和模板等 workflow 内部文件统一收进隐藏目录 `.workflow/`。

```text
.
├── README.md
├── AGENTS.md                  # Agent 自动发现入口
├── LICENSE
├── NOTICE
├── pyproject.toml
├── .workflow/                 # 工作流内部：SKILL / handoff / config / prompts / templates
├── research/                  # 研究本体：idea / literature / private memory
├── modules/                   # 未来模块占位
├── docs/                      # 使用说明、架构、项目文档
├── scripts/                   # 辅助命令
└── tests/
```

可以把它理解为：

- **`research/`：你在研究什么；**
- **`.workflow/`：系统如何帮助你研究；**
- **`docs/`：人应该如何理解和使用它；**
- **`modules/`：以后要扩展到哪里。**

`CHANGELOG`、`ROADMAP`、`CONTRIBUTING` 等项目治理文件统一放在 `docs/project/`，不再堆在主目录。

---

# 使用方法

> 如果你只想知道“拿到 ZIP 后应该做什么”，从这里开始。

## 最推荐的 Codex 使用方式：只发短命令

这一版已经把多阶段 prompt 全部固化到：

```text
.workflow/prompts/
```

根目录 `AGENTS.md` 同时充当 **Prompt Router**。因此 Codex 打开仓库并读取 `AGENTS.md` 后，你日常不需要再次复制长 prompt，只需要发送下面这些短命令：

| 你发给 Codex 的话 | Codex 自动加载 | 用途 |
| --- | --- | --- |
| `启动研究会话` | `00_session_bootstrap.md` | 恢复当前研究上下文，不搜索 |
| `启动下一轮文献调研` | `01_plan_cycle.md` | 设计一轮 decision-oriented cycle，不搜索 |
| `执行本轮调研` | `02_execute_cycle.md` | 正式检索、筛选、精读并更新证据 |
| `精读这篇论文` | `04_deep_read_paper.md` | 单篇论文深读并写 Paper Card |
| `收尾本轮调研` | `03_close_cycle.md` | 综合证据、更新 Idea State、写 handoff |
| `做本周研究总结` | `05_weekly_synthesis.md` | 生成本周决策型研究总结 |
| `同步 ChatGPT 历史` | `reconcile_chatgpt_history.md` | 用历史聊天校正当前 seed |

例如第一次在本地仓库里打开 Codex，只需要：

```text
启动研究会话
```

确认它恢复的 research state 没有偏差后，再发：

```text
启动下一轮文献调研
```

它会先给出本轮要解决的决策问题、互补 route、检索 query、反证路线和 stop condition，**不会直接开始大范围搜索**。你认可这个 cycle 后再发：

```text
执行本轮调研
```

完成后发：

```text
收尾本轮调研
```

这样一轮完整的调研过程就会被落盘，而不是只留在 Codex 会话中。

### 默认输出语言

研究结论、Idea Delta、Decision Update、Paper Card 分析、gap synthesis、weekly update 等默认全部使用**简体中文**。以下内容原则上保留英文/原文：

- 论文原始标题；
- 作者、模型、数据集名称；
- DOI / arXiv / URL；
- 代码符号；
- 搜索 query；
- 需要保持精确含义的术语。

必要时第一次出现可采用 `中文（English）`，后续直接使用更自然的表达。

## 0. 环境要求

仓库脚本只依赖 Python 3。建议使用 Python 3.10+。

进入仓库：

```bash
cd idea-driven-research-workflow
```

可选：先运行测试和文献状态检查，确认仓库完整：

```bash
python -m pytest -q
python scripts/audit_literature.py
```

## 1. 第一次打开仓库：先建立研究上下文

本 ZIP 已经包含一份**不会上传 GitHub 的私有 AIDD seed**：

```text
research/private/idea_seed/
```

它包含当前研究问题、idea 演化、已否决方向、未解决问题和已有论文/概念记忆。

第一次使用时，先运行：

```bash
python scripts/build_bootstrap_packet.py
```

生成：

```text
research/private/bootstrap_packet.md
```

然后在仓库根目录打开 Codex / Claude Code 等 Agent，只需要发送：

```text
启动研究会话
```

`AGENTS.md` 会自动把这个短命令路由到项目内置的 bootstrap prompt。**这一步的目的不是开始搜论文，而是先让新的 Agent 理解“现在研究到哪里了”。**

## 2. 每次开始新的研究会话

建议 Agent 至少读取：

```text
AGENTS.md
.workflow/SKILL.md
research/idea/current.md
research/idea/rejected.md
research/idea/open_questions.md
research/literature/synthesis/weekly_update.md
.workflow/handoff.md
```

如果希望把私有 seed 也带入当前会话，先重新运行：

```bash
python scripts/build_bootstrap_packet.py
```

然后读取：

```text
research/private/bootstrap_packet.md
```

推荐直接发送：

```text
启动下一轮文献调研
```

完整规划 prompt 已保存在 `.workflow/prompts/01_plan_cycle.md`，不需要每次重新书写。

## 3. 以后拿到 ChatGPT 官方导出时

ChatGPT 官方导出通常会包含 `conversations.json`。**不要把原始导出复制进 Git 管理范围。**

最简单的方式：

```bash
python scripts/bootstrap_from_chatgpt.py /path/to/conversations.json
```

脚本会：

1. 基于当前 seed 和 research profile 自动生成筛选关键词；
2. 从完整聊天历史里筛选可能相关的 AIDD 对话；
3. 生成规范化 digest；
4. 生成 reconciliation packet；
5. 要求 Agent 比较“历史讨论”和“当前研究状态”，而不是重新总结所有聊天。

默认产物位于本地私有目录，例如：

```text
research/imports/chatgpt/latest_digest.md
research/private/reconciliation_packet.md
```

然后让 Agent：

```text
Read the reconciliation packet.
For each historical idea, label it as:
confirm / refine / contradict / obsolete / new / uncertain.
Later explicit research decisions override earlier brainstorming.
Only update the current Idea State when the historical evidence materially changes it.
```

### 手动筛选 ChatGPT 导出

如果你想自己指定关键词，可以直接运行：

```bash
python scripts/ingest_chatgpt_export.py /path/to/conversations.json \
  --out research/imports/chatgpt/latest_digest.md \
  --keywords "binding affinity,interface,state,structure,mutation,antibody,ligand"
```

然后生成 reconciliation packet：

```bash
python scripts/make_reconciliation_packet.py \
  research/imports/chatgpt/latest_digest.md
```

## 4. 开始一轮真正的文献调研

### Step 4.1：不要先搜论文，先选一个“决策问题”

打开：

```text
research/idea/open_questions.md
```

选择一个**如果答案不同，就可能改变研究方向**的问题。

例如：

```text
在 binding-affinity change prediction 中，
是否已经存在把局部 interface state 作为显式、可更新计算对象的方法？
```

不要把一轮调研定义为：

```text
“帮我搜一下 antibody affinity 相关论文”
```

而应定义为：

```text
“寻找能够支持、削弱或直接否定 claim X 的证据。”
```

### Step 4.2：生成互补检索路线

先查看：

```text
research/literature/routes.md
```

然后生成第一版 query pack：

```bash
python scripts/build_search_plan.py
```

输出会写入文献搜索计划。一次 cycle 通常只需要选择 **2–5 个互补 lens**，例如：

- Direct-neighbor
- Representation/state
- Data/generalization
- Failure/negative evidence
- Novelty/collision

不要为了“全面”把九个 lens 全部跑一遍。

### Step 4.3：建立 Literature Cycle

每轮调研都应该记录：

```text
要解决的决策问题
→ 为什么现在需要解决
→ 使用哪些 route
→ 找到了什么证据
→ 哪些观点互相冲突
→ 还剩什么不确定性
→ 是否应该修改 idea
```

相关目录：

```text
research/literature/cycles/
```

原则：**一轮 cycle 对应一个研究决策，而不是一个关键词。**

## 5. 找到一篇值得保留的论文后

创建 Paper Card：

```bash
python scripts/new_paper.py \
  --key graphinity \
  --title "Graphinity" \
  --year 2024
```

然后填写生成的 Paper Card。不要只写摘要，要重点记录：

- 论文真正解决什么问题；
- 输入 / 输出 / supervision 是什么；
- 显式表示了什么对象；
- 哪些表示在 mutation / edit 后会变化；
- interface / structure 在计算图中如何参与；
- 数据集和 split；
- OOD / leakage / generalization 风险；
- 最重要的 failure case；
- 它支持、削弱或否定了当前哪条 claim；
- 哪部分是论文事实，哪部分是你的推断。

更新文献索引：

```bash
python scripts/update_literature_index.py
```

检查证据结构：

```bash
python scripts/audit_literature.py
```

### 可选：下载 arXiv 论文

如果论文来自 arXiv：

```bash
python scripts/fetch_arxiv.py ARXIV_ID paper_key
```

如果还需要 source：

```bash
python scripts/fetch_arxiv.py ARXIV_ID paper_key --source
```

下载内容默认不应作为公开仓库的一部分提交。

## 6. 文献读到什么时候停止

不要因为还能搜到论文就继续扩张 paper pool。

当下面三个条件同时满足时，当前 route 应停止：

1. 最近新增论文在“影响研究决策的维度”上高度重复；
2. 没有出现新的 contradiction、mechanism class 或 failure mode；
3. 剩下的不确定性更适合通过代码、数据或实验解决，而不是继续阅读。

这时应该进入 synthesis，而不是继续搜。

## 7. 一轮调研结束后必须做什么

至少更新：

```text
research/literature/evidence/claim_ledger.csv
research/literature/synthesis/gap_map.md
research/literature/synthesis/weekly_update.md
.workflow/handoff.md
```

如果证据真的改变了研究问题，则再更新：

```text
research/idea/current.md
research/idea/decision_log.md
research/idea/rejected.md
research/idea/open_questions.md
```

**不要让重要结论只存在于 ChatGPT 对话里。**

## 8. Idea 发生明显变化时

先保存旧状态：

```bash
python scripts/snapshot_idea.py --label before-interface-reframing
```

再修改：

```text
research/idea/current.md
```

并在：

```text
research/idea/decision_log.md
```

记录：

```text
旧判断是什么
→ 哪些新证据出现
→ 为什么旧判断不再成立
→ 新判断是什么
→ 哪些问题因此被新增/删除
```

如果某个方向被明确否掉，把它写入：

```text
research/idea/rejected.md
```

这样未来的 Agent 不会无意中把它重新包装成“新 idea”。

## 9. 提交到 GitHub 前

公开仓库建议只包含可公开的 workflow、Paper Card、evidence 和 synthesis。

下面内容默认应该保持私有：

```text
research/private/
research/imports/chatgpt/
原始 ChatGPT export
下载的论文 PDF / source
本地 cache
```

推送前必须检查：

```bash
git status
```

确认没有原始聊天、未发表敏感笔记或本地 PDF 被意外加入。

## 10. 如果你想从这个 workflow 新建另一个研究项目

运行：

```bash
python scripts/init_project.py ~/Research/my-new-project
```

初始化器只创建缺失文件，不会覆盖已经存在的研究笔记。

---

## 最推荐的日常工作流

```text
① build_bootstrap_packet
        ↓
② 选择一个 high-impact open question
        ↓
③ 设计 2–5 条互补 literature routes
        ↓
④ 搜索 + 筛 paper
        ↓
⑤ 为真正重要的论文创建 Paper Card
        ↓
⑥ 更新 claim ledger / contradiction / gap map
        ↓
⑦ 判断：idea 被支持、削弱、否定还是需要收缩？
        ↓
⑧ 必要时 snapshot + 更新 Idea State
        ↓
⑨ 更新 handoff
        ↓
⑩ 下一次会话继续
```

核心原则只有一句：

> **不要以“读了多少论文”衡量进度，而要以“消除了哪些会改变研究决策的不确定性”衡量进度。**

---

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

## 当前 AIDD 初始化方向

仓库放入了一个经过泛化的初始问题：

> 如何把局部 molecular interaction / binding interface 作为显式计算对象，使局部 edit / mutation 引起的表示变化能够被直接建模，并用于预测 binding-affinity change？

当前刻意不锁死 protein–ligand 或 antibody–antigen 场景，因为“应该在哪个真实问题上实例化”本身就是第一轮文献调研需要回答的问题。

## Research Memory、Literature Evidence 与 Research Decision

三者必须分开：

```text
Research Memory
≠ Literature Evidence
≠ Current Research Decision
```

私有 seed 中出现的研究直觉只是 **memory / hypothesis**，不能因为它被重复讨论过就当成领域事实。

只有经过论文原文、数据、代码或实验核验的内容才能进入 Evidence Ledger；只有当证据足够改变研究判断时，才进入 Decision Log / Current Idea State。

## 开源安全

默认 `.gitignore` 会忽略：

- 原始 ChatGPT export；
- `research/private/`；
- ChatGPT digest / reconciliation 中的本地私有材料；
- 下载的论文 PDF / LaTeX source；
- 本地 cache。

公开 GitHub 前仍建议执行 `git status` 做最后检查。

## 其他模块状态

目前只有 Literature Research 模块可用。以下模块故意保持 placeholder：

- baseline reproduction；
- dataset engineering；
- experiments；
- writing / submission。

它们保留目录接口，以便未来逐步扩展而不打乱当前仓库结构。

## 致谢与许可证

固定文件结构、handoff 和 research skeleton 的基本思想受到 `skJack/research-workflow` 启发（Apache-2.0）。本仓库针对“动态 idea 驱动的文献调研”进行了独立重构。详见 `NOTICE`。

本项目采用 Apache-2.0 License。
