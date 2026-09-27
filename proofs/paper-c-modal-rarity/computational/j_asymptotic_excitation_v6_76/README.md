# V6.76 — asymptotic excitation density

## Purpose

Replace the overly strict `K<=1` target of V6.75 with the physically relevant criterion: the selected excitation density must remain separated from the uniform equilibrium value `2/3`.

## Exact scale law

The three agentive observables are linear DCT modes of the projected history. Under the independent product law `w`, their means and covariance are finite sums of the branch means and variances. `Sigma_w` can therefore be computed exactly at arbitrary depth without enumerating histories.

## Optimisation audit

- Exhaustive global minima are computed at depths 3 through 10.
- A deterministic multi-start coordinate optimiser must reproduce every certified minimum in that range.
- The validated optimiser is then run at depths 16, 32, 64, 128 and 256.
- Every large-depth result is explicitly labelled uncertified.

For density `c=K/n`, the ternary macro-entropy density is

`s(c)=-c log c-(1-c)log(1-c)+c log 2`.

Uniform equilibrium occurs at `c=2/3`, where `s=log 3`. A positive deficit `log 3-s(c)` implies exponential rarity under the physical counting measure even when `c>0`.

## Scope

Agreement with all exact minima through depth ten validates the optimiser only on that range. Large-depth convergence is numerical evidence, not a certified global or asymptotic theorem. A proof requires a lower bound or a globally certified optimisation method.

## Run

```bash
python evidence/j_asymptotic_excitation_v6_76/j_asymptotic_excitation_gate.py
```


