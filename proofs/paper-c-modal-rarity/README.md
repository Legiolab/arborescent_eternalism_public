# Proof and reproducibility supplement

## Paper

**Modal Rarity, Physical Preparation and Entropy in a Tenseless World**

## Public claims supported

| Claim | Evidence |
|---|---|
| Structural-entropy refinement, logarithmic cost, protected-sector selection, geometric rarity transfer, stopping-line calibration, symmetry freedom, physical weight examples, conditional relaxation and bounded-tilt typicality | `analytic_results.md` |
| The earlier scalar-sigma finite witness is reproducible but is not the calibrated model used for the paper's main claims | `computational/j_generative_common.py` and `computational/results.json` |
| The agentive term can be calibrated by the target-blind covariance Sigma_w, without a fitted scalar sigma_A | `computational/j_reference_calibrated_v6_73/` |
| Invertible affine reparameterisation preserves Mahalanobis costs and the winner | `computational/j_feature_invariance_v6_74/` |
| A high-frequency negative control can change the selection, and a matched chance variable reproduces the aggregate winner distribution | `computational/j_feature_invariance_v6_74/` |
| Low preparation and entropy-increasing relaxation coexist in one finite construction, with the K <= 1 failure at depth 8 retained | `computational/j_integrated_ph_arrow_v6_75/` |
| Exact optimisation through depth 10 and explicitly uncertified numerical minima through depth 256 | `computational/j_asymptotic_excitation_v6_76/` |
| For the calibrated ternary model, limsup K_n/n <= 0.4691 < 2/3 and the entropy-density deficit is positive | `computational/j_asymptotic_density_bound_v6_77/` |
| General gap-and-competitor theorem: limsup K_n/n <= u/a | `computational/general_ph_class_bound_v6_78/` |
| A positive entropy-blind quadratic contribution has the zero-amplitude argmin in the restricted positive TT sector | `variational_ph_proof.md` |
| The selected datum lies in an exponentially rare regulated macroregion with ratio (e*/E*)^N | `variational_ph_proof.md` |

## Reproduction

```bash
python proofs/paper-c-modal-rarity/computational/run_all.py
```

The scripts use only the Python standard library and overwrite their `results.json` files deterministically. See `analytic_results.md` for the paper proofs and `computational/README.md` for the evidential status of each computational stage.

## Limits

These materials establish finite constructive witnesses, a model-relative asymptotic bound, a general sufficient class theorem and a restricted positive-sector theorem. They do not derive realistic cosmology, a universal Past Hypothesis, a fundamental argmin law or libertarian freedom. The large-depth minima in V6.76 are numerical evidence, not globally certified optima.
