## Layer 0 — Private research memory

`research/private/idea_seed/` is a git-ignored bootstrap layer for unpublished or user-specific research memory. It may contain a richer genealogy and rationale than the public Idea State.

The private seed never counts as literature evidence. Its job is to preserve continuity across agents/sessions and to guide later reconciliation with ChatGPT exports.

Precedence: current explicit decision > public current state > newer curated private seed > historical chat > old brainstorming.

# Architecture

## Layer 1 — Idea State

A compact, versioned model of the current research direction:

- `current.md`: current truth;
- `rejected.md`: negative memory;
- `decision_log.md`: why changes occurred;
- `open_questions.md`: unresolved decision points;
- `snapshots/`: immutable history.

## Layer 2 — Evidence System

The literature module turns papers into decision-relevant evidence:

- search plan and logs;
- paper pool;
- paper cards;
- claim ledger;
- contradiction log;
- research/gap maps;
- reading queue;
- weekly synthesis.

## Layer 3 — Future research modules

Reserved interfaces for:

- baseline reproduction;
- datasets;
- experiments;
- writing.

A literature question should be handed to a future module once it becomes executable rather than bibliographic.
