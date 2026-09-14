# AGENTS.md — Project Operating Contract

Read this file first in every fresh agent session.

## Project scope

This repository currently implements **literature research only**. Do not silently expand into baseline reproduction, dataset engineering, model implementation, experiments, or paper writing. Those modules are placeholders until explicitly activated by the researcher.

## Default language

- **All final research outputs, synthesis, Idea Delta, decision updates, paper-reading conclusions, and user-facing summaries must be written in Simplified Chinese by default.**
- Preserve original paper titles, author names, dataset names, model names, code identifiers, and search queries when English is more precise.
- Technical terms may use `中文（English）` on first use when this improves precision.
- Do not translate citation metadata or invent Chinese paper titles.

## First-read order

1. `research/idea/current.md`
2. `research/idea/rejected.md`
3. `research/idea/decision_log.md`
4. `research/idea/open_questions.md`
5. `research/literature/synthesis/weekly_update.md`
6. `.workflow/handoff.md`
7. `.workflow/SKILL.md` when executing a literature workflow

If `research/private/bootstrap_packet.md` exists locally, read it after the stable public state above.

## Prompt router

Long prompts are stored in `.workflow/prompts/`. When the researcher uses one of the short commands below, load the corresponding prompt and execute it together with this contract and `.workflow/SKILL.md`.

| Researcher command | Prompt to load | Purpose |
| --- | --- | --- |
| `启动研究会话` / `恢复研究上下文` | `.workflow/prompts/00_session_bootstrap.md` | Reconstruct current state before doing research |
| `启动下一轮文献调研` / `规划本轮调研` | `.workflow/prompts/01_plan_cycle.md` | Propose one decision-oriented literature cycle; do not search yet |
| `执行本轮调研` | `.workflow/prompts/02_execute_cycle.md` | Execute the approved cycle and update evidence files |
| `收尾本轮调研` / `关闭本轮调研` | `.workflow/prompts/03_close_cycle.md` | Synthesize evidence and update decisions/handoff |
| `精读这篇论文` | `.workflow/prompts/04_deep_read_paper.md` | Deep-read one decision-relevant paper and update its Paper Card |
| `做本周研究总结` / `周总结` | `.workflow/prompts/05_weekly_synthesis.md` | Produce a Chinese weekly synthesis from repository evidence |
| `同步 ChatGPT 历史` | `.workflow/prompts/reconcile_chatgpt_history.md` | Reconcile historical chat with the current seed |

If the user's instruction is more specific than the stored prompt, the user's current instruction wins. Do not require the user to paste the long prompt again.

## Source-of-truth rules

- `research/idea/current.md` is the current research state.
- `research/idea/snapshots/` is immutable history.
- `research/idea/rejected.md` is negative memory. Do not revive an item unless new evidence directly addresses the rejection reason.
- ChatGPT exports are historical context, not authoritative truth.
- A paper claim and an agent inference must never be merged into one unlabeled statement.

## Literature-research rules

1. Every search cycle starts from a **decision-relevant question**, not a broad topic.
2. Use at least two complementary lenses for important questions.
3. Seek disconfirming evidence intentionally.
4. Prefer primary sources for technical claims.
5. Record exact source identifiers (DOI/arXiv/URL) and evidence locations when available.
6. Keep a paper only when it contributes a distinct method class, result, contradiction, dataset, or framing.
7. Do not equate citation count with relevance.
8. Do not equate “not found” with novelty.
9. Stop reading when the residual uncertainty requires execution/experiments rather than more literature.
10. Update `.workflow/handoff.md` before ending a substantial session.

## Dynamic idea update protocol

When new ChatGPT history or research notes arrive:

1. Extract candidate changes: commitments, reversals, rejected framings, open questions, terminology shifts.
2. Compare against `current.md`; do not rewrite from scratch.
3. Produce an **Idea Delta** with `added / changed / rejected / unresolved / unchanged`.
4. Snapshot before material edits.
5. Update `decision_log.md` with why the change happened and what evidence would reverse it.
6. Rebuild only affected literature routes.

## Public-repository safety

Never commit raw ChatGPT exports, private notes, API keys, credentials, unpublished personal communications, or large downloaded paper artifacts. Use ignored directories. Before suggesting a push, inspect `git status`.

## Naming

Use descriptive names tied to a research question or claim. Avoid `final`, `v2_final`, and date-only names.

## Private seed and history precedence

When `research/private/idea_seed/` is available locally, use it to recover research continuity. It is **memory, not evidence**. If it conflicts with a newer explicit user decision or the public current Idea State, the newer explicit decision wins. Historical ChatGPT exports must be reconciled; never infer truth or commitment from repetition alone.
