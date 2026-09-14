# Changelog

## 0.4.0 - 2026-09-14

- Added a prompt router so Codex/agents can be controlled with short Chinese commands instead of repeatedly pasting long prompts.
- Added reusable multi-stage prompts for session bootstrap, cycle planning, cycle execution, cycle closing, paper deep-reading, and weekly synthesis.
- Set Simplified Chinese as the default language for research outputs while preserving original paper metadata and useful English search queries.
- Synced the prompt system and language policy into the clean-project template.
- Added explicit `language_policy` to the research profile.
- Fixed GitHub Actions to install pytest before running the test suite.


## 0.3.0 - 2026-09-14

- Simplified the repository root to the public entry files only.
- Moved workflow internals (`SKILL`, handoff, prompts, config, reusable templates) into `.workflow/`.
- Moved Chinese usage guide and project governance documents into `docs/`.
- Updated scripts, templates, agent contracts, and documentation for the new paths.
- Preserved `AGENTS.md` at the root for agent auto-discovery.

## 0.2.1 - 2026-09-14

- Expanded both READMEs into an end-to-end usage guide.
- Added first-run, per-session, ChatGPT reconciliation, literature-cycle, paper-card, idea-snapshot, and GitHub safety workflows.
- Verified README commands against the actual script CLI.

## 0.2.0

- Added a git-ignored first private AIDD idea seed with research context, idea genealogy, current hypothesis, negative memory, unresolved questions, and literature/concept memory.
- Added explicit source-precedence and reconciliation policy for historical ChatGPT conversations.
- Added `build_bootstrap_packet.py` for starting new agent sessions from public state + private seed.
- Added `bootstrap_from_chatgpt.py` for one-command AIDD filtering and reconciliation-packet generation from an official ChatGPT export.
- Added `make_reconciliation_packet.py` and two agent prompts for bootstrap/reconciliation.
- Expanded privacy documentation: exports are provenance, not authoritative research truth.

## 0.1.0

- Initial public scaffold.
- Implemented literature-research module.
- Added versioned Idea State and negative-memory mechanism.
- Added ChatGPT export normalization.
- Added complementary research lenses and deterministic query-pack generation.
- Added paper cards, claim ledger, contradiction log, gap map and reading queue.
- Added placeholder interfaces for reproduction, datasets, experiments and writing.
