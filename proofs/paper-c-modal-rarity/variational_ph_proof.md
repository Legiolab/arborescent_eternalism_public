# Restricted variational preparation proof

This public supplement concatenates the preregistered independence, blind-selection and entropy-reveal stages. The order matters: the selector is frozen before the low-entropy macroregion is evaluated.

# AE V6.47A — variational independence audit

## Target

Identify a candidate physical/structural contribution to J_total that can be
specified before any low-entropy macroregion, entropy sign, macrovolume target,
Past-Hypothesis condition or cosmological q_* is inspected.

This gate does not reveal entropy. It audits inputs only.

## Candidate

Use the existing DtN construction already present in the canon.

On the product-star witness,

S_E[H] = (kappa_E/2) sum_e int_0^infty
         ( ||partial_r H_e||^2 + <H_e,L_TT H_e> ) dr,

with boundary value H_e(0)=A.

Eliminating the decaying extensions gives

B_E(A) = (1/2)<A,Omega_E^ADM A>,
Omega_E^ADM = kappa_E b sqrt(L_TT)

on the strictly positive spectrum.

The weighted-complex extension replaces this by a positive operator
Omega_E^ADM = F_E(L_TT)>0 under the accepted conditional hypotheses.

## Forbidden inputs

For V6.47A, construction of B_E / Omega_E may not use:
- Boltzmann/Shannon entropy as a target;
- a low macrovolume threshold;
- a Past-Hypothesis macrocell;
- q_* or the observed cosmological entropy;
- a coefficient chosen after inspecting whether the selected state is low
  entropy;
- an agentive term J_ag.

## Input audit

Allowed inputs actually used by the candidate:
- modal/event extension geometry in the chosen realization of E;
- positive edge/branch rigidity kappa_E;
- branching multiplicity / weighted-complex geometry;
- the independently specified positive TT operator L_TT;
- boundary regularity required to define the DtN map.

No entropy or macro-partition appears in the derivation of the quadratic form.

Therefore the deterministic minimizer

argmin_A B_E(A)=0

can be computed before defining the entropy macroregion.

## Semantics audit

Two semantics must be separated.

### Deterministic argmin

If actualization obeys the provisional linkage law

H* = argmin J_total,

the DtN term has an entropy-blind minimizer A=0.

This passes the V6.47A independence criterion.

However NO-GO-ONTIC-ARGMIN-DERIVATION remains active:
the existence of J does not itself derive the ontic rule H*=argmin J.
Argmin is a separate linkage law.

### Gibbs / probabilistic state

For dnu_E proportional to exp(-B_E/tau)dA, covariance is
tau Omega_E^{-1}.

NO-GO-BOUNDARY-SCALE remains active: positivity of Omega_E does not fix
tau/Omega_E. The scale can make fluctuations arbitrarily broad.

Therefore the probabilistic candidate does NOT pass strong V6.47A independence
for a quantitative Past-Hypothesis claim until the scale is independently
derived.

## Robustness already available

The canon already establishes:
- positivity of the DtN form on the stated positive sector;
- invariance of weighted-complex witnesses under renaming and exact edge
  subdivision;
- conditional argmin stability under a non-zero global gap or local
  non-degenerate Hessian/coercivity.

These are admissible structural robustness properties because they are not
defined using entropy targets.

## Result

**PASS WITH STRICT SCOPE for deterministic argmin.**
**INCONCLUSIVE / SCALE-OPEN for Gibbs semantics.**

V6.47B may proceed only with the deterministic entropy-blind minimizer and must
freeze:
1. the exact DtN candidate;
2. the selection semantics H*=argmin J_phys for this test;
3. all coefficients and boundary conditions;
before defining or evaluating the low-entropy macroregion.

## What this does not establish

- that argmin is the fundamental ontic law;
- the full nonlinear gravitational Past Hypothesis;
- matter-sector low entropy;
- a cosmological q_*;
- uniqueness of J_total beyond the tested physical sector;
- that A or J_ag is needed for the result.

## Next gate

V6.47B — Blind Selection:
compute the selected physical boundary data from the frozen DtN functional
without using an entropy macro-partition.

Only after that result is committed may V6.47C define the independently
motivated physical macroregion and reveal whether the selected data are
exponentially rare.


---

# AE V6.47B — blind variational selection

## Freeze inherited from V6.47A

The candidate is fixed before entropy reveal:

B_E(A) = (1/2)<A,Omega A>

with Omega = Omega_E^ADM strictly positive on the tested TT sector.

Selection semantics for this gate only:

A* = argmin_A B_E(A).

No Gibbs temperature, entropy threshold, macrovolume, Past-Hypothesis region,
q_* or agentive term is permitted.

## Selection theorem

For every non-zero A in the positive TT sector,

<A,Omega A> > 0,

while

B_E(0)=0.

Therefore

A*=0

is the unique global minimizer on that sector.

For a finite-dimensional spectral truncation with eigenvalues omega_j>0,

B_E(Q)=1/2 sum_j omega_j Q_j^2,

so every selected mode satisfies

Q_j*=0.

Under the already stated regularity condition that removes the conjugate
quadrature P, the selected boundary data are

(Q*,P*)=(0,0).

## Blindness statement

The result (Q*,P*)=(0,0) follows only from positivity/coercivity of the frozen
DtN form and the provisional argmin linkage law.

No low-energy threshold e_*, phase-space macrocell, entropy function or volume
ratio is used in obtaining the selected data.

## Perturbation control

If J_total=B_E+R and the positive-sector minimizer is isolated by a gap or
coercive Hessian, sufficiently small entropy-blind perturbations R move or
preserve the minimizer according to the existing argmin-stability theorem.

For the strict zero result in this gate, R is frozen to zero. V6.47C must not
retrofit R after seeing the entropy reveal.

## Failure modes retained

- zero/negative modes invalidate strict uniqueness;
- extending from the tested TT sector to the full ADM/matter system is OPEN;
- the product-star/weighted-complex DtN derivation is conditional and not yet a
  fully covariant E construction;
- H*=argmin J is a linkage postulate, not derived from E alone.

## Result

**PASS — BLIND SELECTION in the tested positive TT sector.**

Frozen output for V6.47C:

(Q*,P*)=(0,0).

This output is now committed before the entropy/macrovolume reveal.

V6.47C is allowed to ask whether this already-frozen selected datum belongs to
an independently defined exponentially rare physical macroregion. It may not
change Omega, the argmin semantics, boundary regularity or selected datum.


---

# AE V6.47C — entropy reveal after blind variational selection

## Frozen input

V6.47B committed before this reveal:

(Q*,P*)=(0,0)

in the tested positive TT sector, obtained from the entropy-blind minimization of

B_E(Q)=1/2 sum_j omega_j Q_j^2, omega_j>0,

plus the frozen regularity condition P=0.

No entropy threshold or macrovolume was used to obtain this datum.

## Independent physical macroregion

Now define the previously established TT inhomogeneity energy on N modes,

H_TT(Q,P)=1/2 sum_j (P_j^2 + lambda_j Q_j^2),

and a bounded ambient phase-space regulator

Gamma_N = product_j { P_j^2 + lambda_j Q_j^2 <= 2 E_* },

with 0<e_*<E_*.

Define the low-inhomogeneity macroregion

C_low = { H_TT < N e_* }

in the product regulator used by the existing canonical calculation.

The accepted volume calculation gives

mu_L(C_low)/mu_L(Gamma_N) = (e_*/E_*)^N

for the stated product construction.

Thus for fixed e_*/E_*<1 the physical macroregion is exponentially rare:

mu_L(C_low)/mu_L(Gamma_N)
= exp[-N log(E_*/e_*)].

## Reveal

For the already frozen selected datum,

H_TT(Q*,P*)=H_TT(0,0)=0.

Therefore for every independently chosen threshold e_*>0,

(Q*,P*) in C_low.

The entropy-blind variational selection lands at the center of every positive
low-inhomogeneity TT macroregion in this regulated sector.

## Strong result within the tested sector

Combining V6.47A-C gives:

independently specified positive DtN action
-> entropy-blind argmin
-> (Q*,P*)=(0,0)
-> membership in an exponentially rare ambient TT macroregion.

The exponential rarity is

(e_*/E_*)^N,

and was not used to choose the minimizer.

This is stronger than merely assuming a rare event-sector weight and projecting
it to low volume: in this sector the variational functional itself selects the
physical datum before the rarity calculation is revealed.

## Critical measure distinction

NO-GO-TT-MEASURE-CONFLATION remains active.

The ambient Liouville rarity statement and the prepared/conditional measure are
different:

- under ambient Liouville measure, neighborhoods of the selected regular datum
  are exponentially rare in N;
- after imposing the regularity surface P=0, the induced measure must be
  separately defined;
- deterministic argmin produces a delta-like selected state, not a claim that
  the low region is typical under ambient Liouville measure.

Therefore the result is a selection-of-an-atypical-datum theorem, not a
derivation that the ambient measure dynamically concentrates there.

## Past-Hypothesis scope

The result is a genuine Past-Hypothesis-like preparation theorem only for the
tested linearized TT inhomogeneity sector.

It does NOT yet establish:
- the full gravitational Past Hypothesis;
- low Weyl curvature in a nonlinear cosmology;
- matter-sector low entropy;
- a regulator-independent cosmological phase-space ratio;
- the physical origin of the argmin linkage law;
- a universal covariant J on the full event complex.

## Verdict

**PASS WITH MAJOR PHYSICAL SCOPE LIMITATION.**

What is now established:

There exists an independently defined variational contribution to J, already
present in the AE canon, whose frozen deterministic minimizer is selected
without entropy input and is subsequently found to lie in an exponentially rare
physical low-inhomogeneity macroregion in the tested TT sector.

This closes the logical circularity test for that sector.

What remains open is physical completion, not the finite/linear logical chain.

## Consequence for Paper C / Foundational

Allowed claim:

'In a controlled linearized gravitational TT sector, an entropy-blind positive
DtN functional selects by argmin the homogeneous boundary datum, which is then
found to occupy an exponentially rare low-inhomogeneity region of the ambient
regulated phase space. This is a conditional variational mechanism for a
Past-Hypothesis-like preparation.'

Forbidden claim:

'AE derives the Past Hypothesis of our universe.'

## Next gate

V6.48 should attack the main remaining physical weakness:
replace the toy/product TT construction by the most covariant available
gravity-sector realization and test whether the positivity/coercivity and
entropy-blind selection survive zero modes, nonlinearities and matter, without
introducing a target low-entropy boundary.
