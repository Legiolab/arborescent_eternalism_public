# V6.74 — feature invariance and matched chance

## Purpose

Audit the remaining freedom in the V6.73 feature map and test whether goal-sensitive selection distinguishes agency from a matched exogenous random variable.

## Design

One continuous physical target profile is fixed before enumeration and represented through four feature geometries:

- the first three cosine modes;
- an invertible coordinate transformation of exactly the same subspace;
- a rival smooth subspace using modes 0, 1 and 3;
- three local block means.
- a high-frequency modes 3, 4 and 5 negative control that discards the target's registered low-frequency content.

Every geometry is standardised by its own target-blind covariance under the same frozen reference law. This separates harmless coordinate changes from substantive choices of physical observables.

The matched-chance control replaces the goal label by an exogenous variable with the same distribution over base, reversed and neutral targets. It then compares the induced distribution over selected histories.

## Interpretation rules

- A coordinate change must preserve every Mahalanobis cost and the selected history.
- Different physical subspaces need not agree; disagreement identifies a real modelling obligation rather than a numerical failure.
- Exact agreement with matched chance is a no-go for inferring non-random agency from goal-sensitive selection alone.

## Run

```bash
python evidence/j_feature_invariance_v6_74/j_feature_invariance_gate.py
```


