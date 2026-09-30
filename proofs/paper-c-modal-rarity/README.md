# Proof and reproducibility supplement

## Paper

**Modal Rarity, Physical Preparation and Entropy in a Tenseless World**

## Public claims supported

| Claim | Evidence |
|---|---|
| Structural-entropy refinement, logarithmic cost, protected-sector selection, geometric rarity transfer, stopping-line calibration, symmetry freedom, physical weight examples, conditional relaxation, bounded-tilt typicality, theorem assumptions and scaling interpretation | `analytic_results.md` |
| Delayed agentive selection at fixed reference weights: 41 paths, exact threshold log(14580), tied rare winners, and no-memory control | `computational/delayed_agentive_selection_v1_6/` |
| The earlier scalar-sigma finite witness is reproducible but is not the calibrated model used for the paper's main claims | `computational/j_generative_common.py` and `computational/results.json` |
| A quadratic target penalty can be calibrated by the target-blind covariance Sigma_w, without a fitted scalar sigma_A | `computational/j_reference_calibrated_v6_73/` |
| Invertible affine reparameterisation preserves Mahalanobis costs and the winner | `computational/j_feature_invariance_v6_74/` |
| A high-frequency negative control can change the selection, and a matched chance variable reproduces the aggregate winner distribution | `computational/j_feature_invariance_v6_74/` |
| Legacy string optimisation and separately prepared ensemble relaxation; the old physical-preparation interpretation is not established (K <= 1 fails at depth 8) | `computational/j_integrated_ph_arrow_v6_75/` |
| Exact optimisation through depth 10 and explicitly uncertified numerical minima through depth 256 | `computational/j_asymptotic_excitation_v6_76/` |
| Legacy ternary string bound: limsup K_n/n <= 0.4691; interpretation as a state on a physical cut requires an explicit bridge | `computational/j_asymptotic_density_bound_v6_77/` |
| General gap-and-competitor theorem: limsup K_n/n <= u/a | `computational/general_ph_class_bound_v6_78/` |
| A positive entropy-blind quadratic contribution has the zero-amplitude argmin in the restricted positive TT sector | `variational_ph_proof.md` |
| The selected datum lies in an exponentially rare regulated macroregion with ratio (e*/E*)^N | `variational_ph_proof.md` |

## Reproduction

```bash
python proofs/paper-c-modal-rarity/computational/run_all.py
```

The delayed-agency witness also runs independently with `python proofs/paper-c-modal-rarity/computational/delayed_agentive_selection_v1_6/check.py`.

The scripts use only the Python standard library. Legacy gates overwrite their result files; the three new checks emit results on standard output, with recorded snapshots provided alongside them. See `analytic_results.md` for the paper proofs and `computational/README.md` for the evidential status of each computational stage.

## Limits

These materials establish finite constructive witnesses, a model-relative asymptotic bound, a general sufficient class theorem and a restricted positive-sector theorem. They do not derive realistic cosmology, a universal Past Hypothesis, a fundamental argmin law or libertarian freedom. The large-depth minima in V6.76 are numerical evidence, not globally certified optima.

## Preparation and entropy constructions added 30 September 2026

| Construction | Verified scope |
|---|---|
| [Spatial preparation/reset](computational/spatial_preparation_reset_v1/) | Bound on x_0; exponential rarity under declared counting; selected histories constant; separately prepared ensemble relaxes. |
| [Local delayed objective](computational/local_delayed_objective_v1/) | 21,952 histories; threshold 7.550030129168326; six winners above threshold have K=0,1,2,3 and strictly increasing Boltzmann macroentropy. |

These are different models and do not combine into one theorem. The local task is deliberately chosen to reward the increasing-entropy class; causal agency and an independent physical motivation for this task are not derived. A late objective may overcome the reference cost of a rare preparation, but this is not universal or cosmological.

The older numerical strings remain reproducible; their physical reading is restricted by the explicit state-on-cut requirement.

## Independent reliable-record test added 30 September 2026

[reliable_record_v1](computational/reliable_record_v1/) defines a faithful nondemolition copying task without an entropy reward or prescribed entropy trajectory. Exhaustive checks cover n=2,4,6,8. Under its uniform reference, every positive reward selects blank-memory preparations, of counting measure 2^(-n). Joint Shannon entropy remains constant; coarse Boltzmann entropy depends on the partition and is not nondecreasing on all winners. For n=6, 62/64 winners have greater final entropy under separate-register counts, but only 42/64 are nondecreasing throughout. A merged-count partition has seven winners with lower final entropy. Identity, SWAP and inversion controls restrict the interpretation. The same records can be obtained by a causal preparation-and-copy protocol, so this test does not uniquely support AE. Code, analytic argument, outputs and limits are provided; it is included in the ten checks in run_all.py.
