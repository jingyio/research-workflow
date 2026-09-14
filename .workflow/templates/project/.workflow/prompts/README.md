# Prompt Router

本目录保存可重复使用的多阶段研究 prompt。日常使用时无需复制长 prompt；Codex/Agent 读过根目录 `AGENTS.md` 后，直接使用短命令即可。

| 短命令 | Prompt | 阶段 |
| --- | --- | --- |
| `启动研究会话` | `00_session_bootstrap.md` | 恢复上下文 |
| `启动下一轮文献调研` | `01_plan_cycle.md` | 规划，不搜索 |
| `执行本轮调研` | `02_execute_cycle.md` | 搜索、筛选、精读、更新证据 |
| `收尾本轮调研` | `03_close_cycle.md` | 综合、更新 idea、handoff |
| `精读这篇论文` | `04_deep_read_paper.md` | 单篇深读 |
| `做本周研究总结` | `05_weekly_synthesis.md` | 周期性综合 |
| `同步 ChatGPT 历史` | `reconcile_chatgpt_history.md` | 历史校正 |

所有分析性输出默认使用简体中文。搜索 query、论文标题、模型/数据集名称可保留英文。
