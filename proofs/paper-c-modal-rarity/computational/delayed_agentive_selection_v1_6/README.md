# Delayed agentive selection witness for Paper C v1.6

This finite calculation reproduces Section 9.6 of *Modal Rarity, Physical
Preparation and Entropy in a Tenseless World*. Run from the repository root:

```bash
python proofs/paper-c-modal-rarity/computational/delayed_agentive_selection_v1_6/check.py
```

Only the Python standard library is required. The script uses exact rational
weights for path enumeration and the weight ratio; logarithms are used for the
reported threshold and score comparisons.

## Fixed physical data

There are three ordered macrostate labels, `0 < 1 < 2`. Their entropy ordering
is stipulated in the finite witness; the Markov matrix is not a derivation of
cosmological relaxation. The reference initial weights and transition matrix
are fixed before evaluating the agentive score:

```text
mu = (0.01, 0.09, 0.90)
K  = ((0.90, 0.10, 0),
      (0.05, 0.90, 0.05),
      (0,    0.10, 0.90))
w(x0,x1,x2,x3) = mu[x0] K[x0,x1] K[x1,x2] K[x2,x3]
```

Exactly 41 four-state histories have positive reference weight. No agentive
term acts during the first two transitions. On the last transition only,
`q(H)` is nonzero when `x2=1` and `x3=2`. For this action, `q(H)` is `1`,
`0.05`, or `0` if the complete history began at `0`, `1`, or `2`. The memory
variant assumes that the later objective can depend on a record of the
earlier trajectory; it does not establish the physical origin of that record
or of the objective.

The full selection cost is `J_beta(H)=-log w(H)+C_A(H)`, where
`C_A(H)=beta(1-q(H))>=0` for `beta>=0`. The constant `beta` does not change the
argmin, so the script compares `-log w(H)-beta q(H)`.

## Exhaustive results

| Case | Global winners |
|---|---|
| `beta=0` | `2222`, weight `0.6561` |
| `beta<log(14580)` | `2222` |
| `beta=log(14580)` | Tie: `2222`, `0012`, `0112` |
| `beta>log(14580)` | Tie: `0012`, `0112`, each weight `0.000045` |

The exact reference-weight ratio is
`w(2222)/w(0012)=0.6561/0.000045=14580`, hence the threshold
`log(14580)=9.5874060056...`. Enumeration excludes every other admissible
history at that threshold.

As a control, set `q(H)=1` for every final `1 -> 2` action regardless of the
initial state. Among these scored histories, `2112` and `2212` have the
largest reference weight, `0.00405`; at `beta=10` they win globally. Thus
late goal sensitivity alone does not make the rare initial preparation win.

This calculation demonstrates conditional global selection at fixed reference
weights. It does not imply that an adult action physically causes an earlier
preparation, derive the preparation from physics, establish free will, prove
ensemble relaxation, or prove a pathwise thermodynamic arrow. The calibrated
Mahalanobis model and asymptotic `u/a` result in the other proof folders are
different constructions; their numerical bound does not transfer to this
finite witness.
