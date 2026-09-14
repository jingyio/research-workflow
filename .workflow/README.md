# Workflow Internals

This directory contains the reusable machinery of the research workflow. It is intentionally separated from `research/`, which should remain focused on the research itself.

- `SKILL.md` — literature-research execution protocol and Chinese-output contract.
- `handoff.md` — cross-session / cross-agent continuation state.
- `config/` — research profile, language policy, and routing configuration.
- `prompts/` — reusable multi-stage prompts plus the short-command prompt router.
- `templates/` — clean-project templates used by `scripts/init_project.py`.

## Short-command operation

After an agent has read root `AGENTS.md`, the researcher should not need to paste long prompts repeatedly. Typical commands are:

```text
启动研究会话
启动下一轮文献调研
执行本轮调研
精读这篇论文
收尾本轮调研
做本周研究总结
```

`AGENTS.md` maps these commands to files under `.workflow/prompts/`. All research-facing outputs default to Simplified Chinese.

Most day-to-day research work should happen under `research/`, not here.
