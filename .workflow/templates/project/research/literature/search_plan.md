# Search Plan

> Generated/edited per cycle. `scripts/build_search_plan.py` provides a deterministic first pass; an agent should refine it.

## Cycle objective

Decide which concrete biomolecular task best exposes the value (or failure) of explicit interaction/interface-state modeling under local edits or mutations.

## Priority routes

1. R1 Direct Neighbor
2. R2 Representation / State
3. R4 Domain / Physics
4. R5 Data / Generalization
5. R6 Failure / Negative Evidence
6. R9 Executable Baseline

## Inclusion criteria

- primary research or high-value benchmark/data papers;
- clearly defined affinity / affinity-change target;
- enough methodological detail to identify what is represented and how a mutation/edit is processed;
- papers that materially inform task selection, generalization, or failure modes.

## Exclusion / deprioritization

- generic drug-discovery surveys with no decision-relevant details;
- docking-only work with no relevance to affinity-change representation;
- papers selected solely for high citation count;
- papers whose only connection is the word "structure".

## Stop rule

Stop each route when new papers no longer add a new representation class, contradictory result, dataset/split regime, scientific constraint, or executable baseline.
