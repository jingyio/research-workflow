# Current Idea State

> This file is the current source of truth. Update it deliberately; preserve old states in `snapshots/`.

## Working research question

How should a model represent **local molecular interactions / binding interfaces as an explicit computational object**, so that a local edit or mutation produces an explicit, localized representation change that can be used to predict a change in binding affinity?

## Why this question is interesting

Many structure-based models can consume a complex structure and output affinity-related predictions, but that does not automatically mean the model treats the **interaction state itself** as a first-class object. The current research intuition is that the scientifically meaningful object may be the changing interface/interactions, not merely a new global embedding of the edited complex.

## Current commitments

1. **Problem before architecture.** The real task and generalization regime should be fixed before choosing a model family.
2. **Structure must participate in computation, not only appear as an input modality.** The research value should be visible in how representations are constructed or updated.
3. **Local change matters.** A mutation/edit is local, while its consequences at the interaction interface may involve removed, added, reorganized, or preserved interactions.
4. **Interface/interaction state is a candidate first-class object.** The exact mathematical form is unresolved.
5. **Scientific validity constrains the ML framing.** A convenient CS analogy is not enough if it misrepresents the underlying biomolecular process.
6. **Generalization and data regime are part of the problem definition.** A strong random split result is not sufficient evidence of scientific usefulness.

## Not yet committed

- protein–ligand vs antibody–antigen as the first concrete application;
- atom-level vs residue-level vs hybrid state;
- explicit hand-defined interaction types vs learned pair/interface state;
- delta-only prediction vs joint absolute + delta modeling;
- whether a dynamic/local update should reuse unaffected global representations or simply enforce an interface bottleneck.

## Current strongest hypothesis

A model that explicitly represents and updates the **interaction/interface state** under a local edit may generalize and explain affinity changes better than a model that only re-encodes the entire edited complex into a global representation—provided the state definition respects the relevant geometry/physics and the evaluation split tests meaningful transfer.

This is a hypothesis, not an established fact.

## Evidence required to strengthen it

- direct evidence that existing full-complex/global approaches fail in regimes tied to local interaction change;
- evidence that interface-centric or pair-centric representations improve meaningful generalization, not only random-split accuracy;
- a precise task where “what changed at the interface” is measurable or at least testable;
- data sufficient to separate representation benefit from memorization of complex families;
- evidence that the proposed state/update is not already standard under different terminology.

## Evidence that would weaken or kill it

- strong existing methods already implement essentially the same explicit state-transition object and show no consistent benefit;
- the relevant experimental labels are too sparse/noisy to distinguish the hypothesis;
- local edits routinely induce large global conformational changes that make a local-state assumption systematically invalid for the selected task;
- a much simpler interface-only static representation explains the same gains, making “dynamic update” unnecessary.

## Immediate research goal

Use literature to decide **what the correct real-world instantiation is** and **what existing methods actually compute**, before designing a new architecture.
