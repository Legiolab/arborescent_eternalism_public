# V6.73 — reference-calibrated agentive geometry

## Purpose

Remove the free scalar `sigma_A` from the V6.72 agentive term without choosing a replacement coefficient after seeing the selected history.

## Candidate

The projection supplies a physical trajectory. Its first three fixed cosine modes define `F(H)`. Before any goal is evaluated, the frozen reference law `w` induces the covariance `Sigma_w` of those observables. Agentive compatibility is then

`C_A(H) = 0.5 (F(H)-g_A)^T Sigma_w^-1 (F(H)-g_A)`.

This is dimensionless and has no scalar agentive precision. `A` supplies the target `g_A`; it does not alter `w`, `Pi`, the feature map or the covariance.

The term is extensive. The three features are history averages, so under the product reference law their covariance satisfies `Sigma_w=O(1/n)`. Consequently `Sigma_w^-1=O(n)`, and a fixed non-zero mismatch contributes `O(n)` to `C_A`. This scaling is why the null history is not a zero-excess-rate competitor when the objective remains active.

## Falsification gates

- exhaustive depth-six and depth-seven enumeration;
- unique minima at both depths;
- transport of the depth-six covariance to depth seven without recalibration;
- goal changes selection while `w` and the physical cost remain frozen;
- winner stability under registered two-per-cent perturbations;
- selected physical energy below the family median;
- no entropy target and no per-history table.

## Scope

The covariance construction is a principled internal calibration, not a derivation of the unique physical observables relevant to agency. It also makes the scale of `C_A` depend on the fixed reference geometry. That is allowed because `A` does not remodel `w`, but it creates a new obligation: justify why reference-standardised physical mismatch is the correct agentive likelihood in a realistic model.

## Run

```bash
python evidence/j_reference_calibrated_v6_73/j_reference_calibrated_gate.py
```

