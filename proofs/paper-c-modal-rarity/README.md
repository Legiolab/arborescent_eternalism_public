# Archived rarity and selection results

This directory preserves the evidence for earlier versions of Paper C. It is not the current recording paper. The current **Recording Capacity and Macroscopic Entropy in Arborescent Eternalism**, version 2.1, uses the [recording supplement](../paper-c-recording-entropy/README.md). Historical proofs and outputs below remain unchanged and retain their original scope.

+# Proof and reproducibility supplement

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
| The selected datum lies in a regulated low sector: per-mode ratio (e*/E*)^N; total-energy rarity has the corrected Irwin–Hall/Chernoff form | `variational_ph_proof.md` |

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

## Record/reset thermodynamics and global MAP control

[record_reset_thermodynamics_v1](computational/record_reset_thermodynamics_v1/) extends the record test with an ideal bath satisfying detailed balance, a driven memory Hamiltonian and explicit work/heat/correlation bookkeeping. Twenty parameter cases verify the first law and nonnegative mean joint entropy production; the same initial ensemble propagated causally gives identical results. A reversible uncopy control restores blank memory at zero heat in the ideal model when the source is available. The protocol and work source are externally given, not derived from AE. Crucially, exhaustive global-history optimisation over up to 262,144 paths selects the trivial all-zero message and constant registers under incomplete thermalisation: the positive ensemble entropy production cannot be attributed to that unique winner. The code, analytic arguments, outputs and limits are provided, and this test is included in the eleven checks in run_all.py.

## Operational recording capacity and preparation-resource bound

[operational_record_capacity_v1](computational/operational_record_capacity_v1/) tests the same device and preparation against every possible classical message. A finite reversible source-preserving recorder with d memory states and e auxiliary states admits at most e universally successful initial resource states, hence counting fraction at most 1/d. Its preparation Shannon entropy obeys H(R)<=log e; with whole-message error delta, H(R)<=log e+h(delta)+delta log(d-1). These are resource-ensemble bounds relative to finite uniform counting, not cosmological or Boltzmann-entropy claims. All 576 one-bit source-preserving reversible devices with a one-bit auxiliary are checked, alongside controlled-CNOT devices up to six bits and 32 approximate bounds. A blank-auxiliary control relocates the necessary resource and copies reversibly without dissipation. Rewarding true device capacity in single-history MAP still selects the trivial realised message; nondegenerate input distributions remain an independent assumption. Conditional operations are thermodynamically accounted for and reproduced causally. Code, algebraic proofs, results and limits are provided; this is included in the twelve computational checks.

## Agentive status and explanatory comparison

[agentive_status_and_explanatory_test.md](agentive_status_and_explanatory_test.md) audits A against the foundational v3.4 and Paper C: represented agentive information, a goal-conditioned compatibility cost, a scalar task/capacity score and the actuality rule have distinct roles. It retains the operational resource bound and the conditional witnesses without treating them as a cosmological law rewarding agents. It specifies causal comparisons with and without supplied special preparation, a matched global comparator, and the outstanding AE-specific explanatory test. No new simulation or actuality law is introduced.


## Integrated preparation and entropy mechanisms

[Retained derivations and scope](integrated_mechanism_results.md) give the corrected regulated volume, late-window selection-compatible bound, five interacting agents and pathwise macroentropy before J. Four self-contained calculation directories and their outputs are included. The complete runner now executes 17 scripts including conserved_source_shell_v1; older counts above describe earlier versions.

