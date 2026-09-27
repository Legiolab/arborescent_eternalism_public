# V6.77 — analytic excitation-density bound

## Result

For global minimisers of the explicit V6.73 finite model,

`limsup K(H_n*)/n <= 0.4691 < 2/3`.

The equilibrium density under the uniform physical counting measure is `2/3`. The bound therefore implies a strictly positive asymptotic entropy-density deficit and exponential macro-rarity within this model class.

## Proof

Every zero symbol has branch probability `0.5`. Every nonzero symbol has probability at most `0.33`. Hence every excitation adds at least

`a=log(0.5/0.33)>0`

to the history surprisal. Since the physical and agentive terms are nonnegative,

`J(H)/n >= log 2 + a K(H)/n`.

For an upper bound, use the explicit competitor that is zero on the first three quarters and `+1` on the last quarter. Irrational-rotation averaging gives its limiting surprisal rate. The exact limiting covariance of the DCT observables gives its agentive rate, while its positive physical energy is subextensive. Since the global minimiser cannot cost more than this competitor, comparison yields the density bound.

## Scope

The theorem is asymptotic but model-relative. It uses the V6.73 branch law, its fixed DCT feature geometry, the nonnegative physical energy and the fixed goal. It proves neither that these laws are cosmological nor that the numerical bound is optimal. Its role is to convert V6.76's numerical separation from equilibrium into an analytic result for the explicit witness.

## Run

```bash
python evidence/j_asymptotic_density_bound_v6_77/j_asymptotic_density_bound_gate.py
```


