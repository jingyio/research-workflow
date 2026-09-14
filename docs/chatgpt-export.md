# Using ChatGPT Exports Safely

## Recommended strategy: seed first, export later

You do **not** need an official ChatGPT export to start. This repository ships with a local, git-ignored private seed under `research/private/idea_seed/`.

The seed is a curated reconstruction of the current research direction. It is research memory, not scientific evidence.

Build a one-file bootstrap packet at any time:

```bash
python scripts/build_bootstrap_packet.py
```

The generated `research/private/bootstrap_packet.md` can be given to ChatGPT/Codex/Claude or another research agent at the beginning of a session.

## When an official ChatGPT export arrives

Raw exports can contain unrelated personal conversations, unpublished ideas, and sensitive material. Keep them outside the repository or under ignored paths.

The easiest workflow is:

```bash
python scripts/bootstrap_from_chatgpt.py /path/to/conversations.json
```

This command:

1. reads topic anchors from the private seed and `.workflow/config/research_profile.json`;
2. selects likely AIDD-related conversations;
3. writes a normalized digest to `research/imports/chatgpt/latest_digest.md`;
4. builds `research/private/reconciliation_packet.md`.

The raw export is never copied into a tracked file.

## Why reconciliation, not re-summarization?

Old chat is historical provenance. It can contain discarded ideas, temporary enthusiasm, misunderstandings, and repeated unresolved questions. The agent should compare history against the current state and label meaningful items as:

`confirm / refine / contradict / obsolete / new / uncertain`.

A later explicit rejection takes precedence over older speculative mentions. Repetition is not evidence.

## Manual normalization

You can still call the lower-level normalizer directly:

```bash
python scripts/ingest_chatgpt_export.py /path/to/conversations.json \
  --out research/imports/chatgpt/latest_digest.md \
  --keywords "binding affinity,interface,state,structure,mutation,antibody,ligand"

python scripts/make_reconciliation_packet.py \
  research/imports/chatgpt/latest_digest.md
```

## Privacy boundary

These are ignored by git by default:

- `research/imports/chatgpt/*` except `.gitkeep`;
- all of `research/private/`;
- raw PDFs/sources and local caches.

Before publishing, still run `git status` and inspect staged files manually.
