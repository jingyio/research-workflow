# Complementary Literature Routes

Use these routes as a router, not a checklist. Each route should be attached to a concrete uncertainty.

| Route | Main question | Typical evidence | Main failure it prevents |
|---|---|---|---|
| R1 Direct Neighbor | Who is already solving nearly the same task? | closest primary papers, concurrent work | fake novelty |
| R2 Representation / State | What computational object is explicit? | pair/interface/contact/state representations | renaming an existing representation |
| R3 Mechanism / Architecture | How is local/global information updated or coupled? | message passing, equivariance, attention, local recomputation | architecture-first thinking |
| R4 Domain / Physics | Does the abstraction respect biomolecular behavior? | structural biology, biophysics, domain ML | elegant but scientifically wrong framing |
| R5 Data / Generalization | What data/splits/labels support the claim? | datasets, benchmark protocols, OOD studies | leakage and memorization |
| R6 Failure / Negative Evidence | Where do similar methods fail? | robustness papers, ablations, negative results | confirmation bias |
| R7 Adjacent-field Analogy | Which mechanism exists elsewhere under better-developed theory? | CV/geometric ML/causal/system analogies | narrow local optimum |
| R8 Novelty / Collision | Has the proposed combination already appeared under different words? | synonym-expanded search, citation graph | novelty by vocabulary |
| R9 Executable Baseline | Which paper provides code/data for later falsification? | repos, checkpoints, scripts | literature-only research |

## Default bundles

### Bundle A — Define the real problem
R1 + R4 + R5 + R6

### Bundle B — Test a representation hypothesis
R1 + R2 + R3 + R6 + R8

### Bundle C — Choose a concrete AIDD scope
R1 + R4 + R5 + R9

### Bundle D — Novelty audit
R1 + R2 + R7 + R8

## Complementarity test

Before adding a route, ask: **what different kind of mistake can this route catch?**

If two routes would return the same papers for the same reason, merge them or sharpen their query.
