# V6.78 — general PH-like class theorem

## Theorem

Let each length-`n` physical history use one null symbol and `d` excited symbols, and let `K_n(H)` count excited coordinates. Suppose

`J_n(H)=-log w_n(H)+B_n(H)+C_n(H)`

with `B_n,C_n>=0`.

Assume a uniform reference gap

`-log w_n(H)+log w_n(0^n) >= a K_n(H)`

for some `a>0`, and an explicit competitor family `G_n` with excess rate at most `u`:

`limsup [J_n(G_n)+log w_n(0^n)]/n <= u`.

Then every global minimiser obeys

`limsup K_n(H_n*)/n <= u/a`.

Under the uniform physical counting measure, equilibrium excitation density is `d/(d+1)`. If

`u/a < d/(d+1)`,

the selected macrostates retain a positive entropy-density deficit and exponentially small physical volume.

## Meaning

The theorem isolates three sufficient ingredients:

1. reference weight penalises excitation uniformly;
2. other contributions do not cancel that lower bound with negative divergences;
3. at least one explicit low-density competitor has sufficiently low total rate.

The detailed V6.73 ternary generator and DCT geometry are one instance, not part of the theorem's logical form.

## Limits

The conditions are sufficient, not necessary. If `u/a` is above equilibrium, the theorem is silent. It does not show that the minimiser is typical under `w`; rarity is evaluated under a separately specified physical macro-measure. Applying the theorem to cosmology still requires physically deriving the reference gap, competitor, projection and macro-measure.

## Run

```bash
python evidence/general_ph_class_bound_v6_78/general_ph_class_bound_gate.py
```


