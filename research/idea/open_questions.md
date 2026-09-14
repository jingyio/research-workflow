# Open Questions

Rank by **expected impact on the research direction**, not by how easy they are to answer.

| Priority | Question | Type | Why it can change the direction | Literature-resolvable? | Status |
|---:|---|---|---|---|---|
| 1 | What exactly do the strongest affinity-change models represent and update after a mutation/edit? | representation | Determines whether the proposed "state" is novel or only renamed | yes | open |
| 2 | Which application setting best isolates local interaction-state change: protein–ligand, antibody–antigen, or mutation-induced affinity change more generally? | formulation/domain | Determines task, data, baselines and scientific narrative | yes | open |
| 3 | Which split/generalization regime is scientifically meaningful and where do current models fail? | data/generalization | Determines whether any gain is meaningful | yes | open |
| 4 | Can a local/interface update assumption survive conformational change, induced fit, and long-range effects? | domain/physics | Could kill an overly local model | partly | open |
| 5 | What is the minimal explicit state object: contacts, pair features, local geometry, interaction types, energy-like terms, or learned interface tokens? | representation/mechanism | Determines the hypothesis that can be tested | partly | open |
| 6 | How much experimental delta-affinity data is actually available and diverse enough for modern ML? | data | Could constrain the entire project | yes | open |
