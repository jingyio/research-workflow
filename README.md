# Idea-Driven Research Workflow

[中文说明](docs/README.zh-CN.md)

A living, evidence-traceable research workflow for turning an evolving research idea into **targeted, complementary literature investigation**.

This repository is intentionally **not** a full research lifecycle framework yet. The literature-research module is implemented; baseline reproduction, datasets, experiments, and writing are reserved as empty interfaces for future expansion.

The workflow is designed for researchers who use ChatGPT / Codex / Claude while ideas are still changing. Instead of treating every conversation as a new literature review, it maintains a versioned **Idea State**, routes each uncertainty to the right literature lens, and records which evidence actually changed the research direction.

## Why this exists

A common failure mode in AI-assisted research is:

`conversation -> broad search -> many papers -> more concepts -> idea drift -> repeat`

This repository enforces a different loop:

`conversation history -> idea delta -> uncertainty/claim -> complementary search routes -> evidence -> synthesis -> idea update`

The goal is not to read more papers. The goal is to reduce uncertainty around the decisions that matter to the research idea.

## Core concepts

### 1. Idea State is the source of truth

`research/idea/current.md` records the current research question, commitments, rejected framings, unresolved questions, and evidence thresholds. Previous states are immutable snapshots under `research/idea/snapshots/`.

### 2. Literature is routed by uncertainty, not by topic alone

The literature module uses complementary lenses:

- **Direct-neighbor**: closest papers solving almost the same problem.
- **Representation/state**: what objects are explicitly represented and updated.
- **Mechanism/architecture**: computational mechanisms that could realize the idea.
- **Domain/physics**: whether the abstraction respects the underlying scientific process.
- **Data/benchmark/generalization**: labels, splits, leakage, OOD and data sufficiency.
- **Failure/negative evidence**: where similar methods fail or overclaim.
- **Adjacent-field analogy**: transferable ideas from geometry, vision, systems, causality, etc.
- **Novelty/collision**: whether the proposed combination already exists.
- **Executable baseline**: papers with code/data that can anchor later reproduction.

A search cycle should cover multiple lenses, but it should stop when additional papers are redundant rather than informative.

### 3. ChatGPT exports are input evidence, not truth

Raw exports are private by default. `scripts/ingest_chatgpt_export.py` normalizes exported conversations into a local digest. An agent then compares that digest with the current Idea State and updates only the parts that genuinely changed.

Repeated statements are not automatically treated as important. Rejected directions and reversals are explicitly preserved so an agent does not resurrect old ideas accidentally.

### 4. Claims and evidence are separate

Every important research claim should be traceable through:

`idea claim -> search route -> paper card -> evidence ledger -> synthesis -> idea delta`

Agent inference must be labeled separately from what a paper actually supports.

## Repository layout

The root is intentionally small. Research artifacts stay in `research/`; workflow internals stay in the hidden `.workflow/` directory; human-facing documentation stays in `docs/`.

```text
.
├── README.md                  # public entry point
├── AGENTS.md                  # agent contract; keep at root for auto-discovery
├── LICENSE
├── NOTICE
├── pyproject.toml
├── .workflow/                 # workflow engine internals
│   ├── SKILL.md
│   ├── handoff.md
│   ├── config/
│   ├── prompts/
│   └── templates/
├── research/                  # the actual research state and literature assets
│   ├── idea/
│   ├── imports/               # local/private imports
│   ├── literature/
│   └── private/               # git-ignored private seed and packets
├── modules/                   # future research modules; currently placeholders
├── docs/                      # usage, architecture, project docs
├── scripts/                   # CLI helpers
└── tests/
```

The intended mental model is simple:

- **`research/` = your research**;
- **`.workflow/` = how the system runs**;
- **`docs/` = how humans understand it**;
- **`modules/` = future expansion points**.

Project meta-docs such as changelog, roadmap, and contribution guidance live under `docs/project/` instead of cluttering the root.

## How to use

If you just downloaded the repository, follow this lifecycle. The workflow is intentionally organized around research decisions rather than around collecting papers.

### Codex / agent quick commands

Long prompts are versioned inside `.workflow/prompts/`. After Codex has opened this repository and read `AGENTS.md`, you can operate the workflow with short Chinese commands instead of re-pasting multi-stage instructions:

```text
启动研究会话
启动下一轮文献调研
执行本轮调研
精读这篇论文
收尾本轮调研
做本周研究总结
同步 ChatGPT 历史
```

`AGENTS.md` acts as a prompt router and loads the corresponding prompt automatically. Research-facing conclusions and synthesis default to **Simplified Chinese**; original paper titles, identifiers, model/dataset names, and useful English search queries remain unchanged.

A recommended first Codex session is simply:

```text
启动研究会话
```

Then, after checking whether the reconstructed state is correct:

```text
启动下一轮文献调研
```

The planning stage intentionally does **not** search yet; it creates a decision-oriented cycle for human approval before execution.

### 0. Check the repository

Python 3.10+ is recommended. From the repository root:

```bash
python -m pytest -q
python scripts/audit_literature.py
```

### 1. Bootstrap the current research state

This ZIP includes a git-ignored private AIDD seed under `research/private/idea_seed/`. Generate a single context packet before starting a new research session:

```bash
python scripts/build_bootstrap_packet.py
```

Then open Codex / your research agent in the repository root and send only:

```text
启动研究会话
```

The root `AGENTS.md` routes that short command to the stored bootstrap prompt. The point of this step is to recover the current research state before searching.

### 2. Start every literature session from a decision-relevant question

Read at least:

```text
research/idea/current.md
research/idea/rejected.md
research/idea/open_questions.md
research/literature/synthesis/weekly_update.md
.workflow/handoff.md
```

Choose one open question whose answer could materially change the research direction. Do not define a cycle as “find papers about X.” Define it as “find evidence that can support, weaken, falsify, or refine claim X.”

Generate a deterministic first-pass query pack with:

```bash
python scripts/build_search_plan.py
```

Use only 2-5 complementary lenses per cycle unless there is a clear reason to expand.

### 3. Import an official ChatGPT export later

When `conversations.json` becomes available, reconcile it with the current seed rather than replacing the current state:

```bash
python scripts/bootstrap_from_chatgpt.py /path/to/conversations.json
```

The workflow filters likely relevant conversations and creates a digest plus a reconciliation packet. Historical items should be classified as:

```text
confirm / refine / contradict / obsolete / new / uncertain
```

Later explicit decisions take precedence over earlier brainstorming.

For manual filtering:

```bash
python scripts/ingest_chatgpt_export.py /path/to/conversations.json \
  --out research/imports/chatgpt/latest_digest.md \
  --keywords "binding affinity,interface,state,structure,mutation,antibody,ligand"

python scripts/make_reconciliation_packet.py \
  research/imports/chatgpt/latest_digest.md
```

### 4. Add papers only when they matter to the current decision

Create a paper card:

```bash
python scripts/new_paper.py \
  --key graphinity \
  --title "Graphinity" \
  --year 2024
```

A useful card should capture more than the abstract: problem definition, input/output/supervision, explicit represented objects, what changes under mutation/edit, how interface/structure enters computation, dataset/split, generalization or leakage risks, failure cases, which current claim it affects, and a clear separation between paper-supported facts and your inference.

Refresh the index and audit the evidence structure:

```bash
python scripts/update_literature_index.py
python scripts/audit_literature.py
```

Optional arXiv retrieval:

```bash
python scripts/fetch_arxiv.py ARXIV_ID paper_key
python scripts/fetch_arxiv.py ARXIV_ID paper_key --source
```

Downloaded paper files should remain local/private.

### 5. End each literature cycle with synthesis

At minimum, update:

```text
research/literature/evidence/claim_ledger.csv
research/literature/synthesis/gap_map.md
research/literature/synthesis/weekly_update.md
.workflow/handoff.md
```

If the evidence changes the idea, also update:

```text
research/idea/current.md
research/idea/decision_log.md
research/idea/rejected.md
research/idea/open_questions.md
```

Important conclusions should not live only inside a chat window.

### 6. Snapshot before a major idea change

```bash
python scripts/snapshot_idea.py --label before-interface-reframing
```

Then update `current.md` and record the reasoning in `decision_log.md`: old belief, new evidence, why the old belief failed, new belief, and which open questions were added or removed. Explicitly rejected directions belong in `rejected.md`.

### 7. Stop reading when reading is no longer the right tool

Stop a route when all three hold:

1. recent additions are redundant on decision-relevant axes;
2. no new contradiction, mechanism class, or failure mode appears;
3. the remaining uncertainty is better answered by code, data, or experiment.

At that point, synthesize instead of expanding the paper pool.

### 8. Push to GitHub safely

Private material should remain outside the public commit, including:

```text
research/private/
research/imports/chatgpt/
raw ChatGPT exports
downloaded PDFs / source archives
local caches
```

Always inspect:

```bash
git status
```

before pushing.

### 9. Bootstrap another project from this workflow

```bash
python scripts/init_project.py ~/Research/my-new-project
```

The initializer creates missing files and does not overwrite existing research notes.

### Recommended daily loop

```text
build bootstrap packet
        ↓
choose one high-impact open question
        ↓
select 2-5 complementary literature routes
        ↓
search and screen papers
        ↓
create Paper Cards only for decision-relevant papers
        ↓
update evidence / contradictions / gap map
        ↓
decide whether the idea is supported, weakened, falsified, or narrowed
        ↓
snapshot + update Idea State if needed
        ↓
update handoff
```

The primary progress metric is **not the number of papers read; it is the amount of decision-relevant uncertainty removed**.

## Recommended operating rhythm

**At the start of a research session**

1. Build/read the bootstrap packet when private context is useful.
2. Read `current.md`, `rejected.md`, and `open_questions.md`.
3. Read the latest synthesis and `.workflow/handoff.md`.
4. Pick a decision-relevant uncertainty before searching.

**When the idea changes**

1. Snapshot the old state.
2. Update `current.md` and `decision_log.md`.
3. Mark literature claims that became stale.
4. Rebuild only affected search routes.

**When adding a paper**

1. Create a paper card.
2. Record what question it answers.
3. Separate paper-supported facts from inference.
4. Record contradiction/failure evidence, not only positive support.
5. Update the evidence matrix and reading queue.

## Search stop rule

Do not keep expanding the paper pool merely because papers exist. Stop a route when all three hold:

1. the last several additions are mostly redundant on the decision-relevant axes;
2. no new contradiction or mechanism class appears;
3. the remaining uncertainty is better resolved by code/data/experiment than by more reading.

## Public vs private material

The repository is safe-by-default for public GitHub use:

- raw ChatGPT exports are ignored;
- local private notes can live under `research/private/` and are ignored;
- downloaded PDFs / source archives are ignored;
- paper cards, evidence tables, and public synthesis can be committed selectively.

Always run `git status` before pushing.

## Current seeded research direction

The included `research/idea/current.md` is initialized with a generalized AIDD question around **making local molecular interaction/interface structure an explicit computational object whose representation changes under local edits or mutations, and using that change to predict binding-affinity effects**. It intentionally keeps the exact application boundary (e.g. protein–ligand vs antibody–antigen) open until the evidence map is stronger.

## Status of other modules

Only the literature module is active. The following are intentionally placeholders:

- baseline reproduction;
- dataset engineering;
- experiments;
- writing/submission.

They exist so future expansion does not require reorganizing the repository.

## Attribution

The fixed-file handoff philosophy and project-skeleton idea are inspired by `skJack/research-workflow` (Apache-2.0). This repository is an independent reimplementation specialized for evolving-idea literature research. See `NOTICE`.

## License

Apache License 2.0. See `LICENSE`.
