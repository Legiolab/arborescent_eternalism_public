# Computational evidence map

The directories form a cumulative and explicitly scoped chain. V6.72 is retained as an earlier finite witness; it is not the model used for the calibrated or asymptotic claims in the paper.

| Version | Role | Evidential status |
|---|---|---|
| V6.72 | Earlier scalar-sigma finite witness | Finite constructive witness only |
| V6.73 | Reference-calibrated Mahalanobis term using Sigma_w | Exact finite enumeration at depths 6 and 7 |
| V6.74 | Affine-coordinate invariance, alternative feature sectors and matched-chance control | Exact finite audit; matched chance is a retained no-go |
| V6.75 | Integrated low-preparation and relaxation construction | Finite pass plus retained failure of K <= 1 at depth 8 |
| V6.76 | Exact minima through depth 10 and large-depth optimisation | Exact through 10; depths 16--256 are explicitly uncertified numerical evidence |
| V6.77 | Analytic excitation-density bound for the V6.73 model | Model-relative asymptotic proof |
| Paper C v1.6 delayed agency | Late objective with trajectory memory, exact reference-weight ratio and no-memory control | Exhaustive finite enumeration; separate from the Mahalanobis asymptotic model |
| V6.78 | Gap-and-competitor class theorem | General sufficient theorem |

Run the complete chain from the repository root:

```bash
python proofs/paper-c-modal-rarity/computational/run_all.py
```

Run the delayed-agency witness separately:

```bash
python proofs/paper-c-modal-rarity/computational/delayed_agentive_selection_v1_6/check.py
```

Each existing gate writes its own `results.json`; the delayed-agency script prints deterministic checks. The code uses only the Python standard library.

The V6.72 output reports eleven executed checks and three separate design declarations. The declarations record how the model was constructed; they are not counted as tests.


The integrated models are preparation_volume_v1, record_selection_exception_bridge_v1, five_agent_cascades_v1 and cascade_entropy_before_selection_v1. See [the derivations](../integrated_mechanism_results.md). The runner executes 17 scripts, including the conserved-source shell control.
