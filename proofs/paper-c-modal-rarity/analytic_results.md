# Analytic results used in Paper C

This note supplies a compact proof record for the structural and measure-theoretic propositions used in **Modal Rarity, Physical Preparation and Entropy in a Tenseless World**. It complements, but does not enlarge, the computational claims in `computational/`.

## 1. Entropy under projective refinement

Let a finite disjoint frontier have weights `W(v)`, and let its children satisfy
`W(c)=W(v)q(c|v)` with `sum_c q(c|v)=1`. Then

`SE(F_{n+1}) = SE(F_n) + sum_v W(v) Ent(q(.|v))`.

Indeed, substitute the product into `-sum_c W(c)log W(c)`, split the logarithm, and sum first over the children of each parent. The first term is the coarse entropy and the second is the weighted conditional entropy. Hence genuine non-degenerate refinement increases structural entropy, while unary refinement contributes zero.

## 2. Uniqueness of logarithmic additive cost

Suppose continuous `f:(0,1] -> R` satisfies `f(xy)=f(x)+f(y)` and `f(1)=0`. Put `g(t)=f(exp(-t))` for `t>=0`. Then `g(s+t)=g(s)+g(t)`; continuity yields `g(t)=kt`, so `f(W)=-k log W`. If Boltzmann-style recovery is required for one unequal pair `W_i != W_j`, then `(W_i/W_j)^k=W_i/W_j`, which fixes `k=1`. An equal-weight vector alone cannot fix the coefficient.

## 3. Protected-sector minimisation

Let `L` be a non-empty proper sector of a finite history class. Assume the base cost `B_E` has gap

`Delta = min_{H notin L} B_E(H) - min_{H in L} B_E(H) > 0`.

For `V=J_hist+alpha J_act`, if `osc(V)<Delta`, every minimiser of `J_total=B_E+V` lies in `L`. Choose `H_0` minimising `B_E` in `L`. For every `H` outside `L`,

`J_total(H)-J_total(H_0) >= Delta-osc(V) > 0`.

Finiteness gives existence; uniqueness follows whenever the restriction to `L` has a unique minimiser. This is a sufficient gap theorem, not a derivation of agency.

## 4. Geometric rarity transfer

Let `e:X->Y` be Lipschitz between equal finite dimensions. Let the source and target densities obey `rho_X >= rho_X,min > 0` and `rho_Y <= rho_Y,max`, and suppose `|Jac e| <= K_Jac`. For every measurable sector `B` with measurable image, the area formula gives

`mu(e(B)) <= integral_B rho_Y(e(x)) |Jac e(x)| dx <= C nu_0(B)`,

where `C=rho_Y,max K_Jac/rho_X,min`. Consequently,

`I_phys(B)=-log mu(e(B)) >= -log nu_0(B)-log C`.

Injectivity and a positive lower Jacobian are not needed for this upper bound. They would be needed for a two-sided comparison.

An explicit example is `X={0,1}x[0,1]` with sheet densities `0.4` and `0.6`, `Y=[0,1]` with Lebesgue measure, and `e(s,x)=x^2`. Here `K_Jac=2` and `C=5`. The critical point at the root does not invalidate the upper bound. In contrast, `e(s,x)=sqrt(x)` maps an interval of length `epsilon` to one of length `sqrt(epsilon)`, so no uniform upper constant exists.

## 5. Stopping-line calibration

Let `{B_i}` be a finite complete prefix-free stopping line whose cylinders are disjoint and exhaustive, and put `p_i=nu_0(B_i)`. Then `sum_i p_i=1`. If the selected history lies in `B_*`, its modal surprisal is `-log p_*`. Applying the geometric result sector by sector gives

`I_phys(B_*) >= -log p_* - log C`,

and, after weighting and summing,

`sum_i p_i I_phys(B_i) >= Ent(p)-log C`.

Thus `p_*<1/C` is sufficient for a positive selected-sector lower bound, and `Ent(p)>log C` is sufficient for a positive reference-average lower bound. These are sufficient conditions, not converses.

For a transitive 64-sector illustration with `p_*=1/64` and `C=5`, the first bound is `log(64/5)`, about `2.55` nats. If a goal sector refines `B_*` with conditional weight `r`, its mass is `p_*r` and its additive modal cost gains `-log r`.

## 6. Symmetry and physical weight laws

If a finite frontier has automorphism orbits `O_1,...,O_k`, every invariant probability law is specified by orbit masses `m_j>=0`, `sum_j m_j=1`, with `p(x)=m_j/card(O_j)` for `x in O_j`. The invariant-law simplex therefore has dimension `k-1`; symmetry fixes a unique law exactly when the action is transitive.

For one isolated branch and one symmetric pair, the invariant spectra are
`(a,(1-a)/2,(1-a)/2)`, `0<=a<=1`. Structure alone therefore does not fix the weights.

In the full-branch interval class, intervals of widths `a_i` map affinely onto `[0,1]` with slopes `s_i=1/a_i`. Lebesgue transfer gives branch probabilities `a_i=1/s_i`; a cylinder has weight `product_t 1/s_{i_t}` and cost `sum_t log s_{i_t}`. The example `(s_1,s_2,s_3)=(2,3,6)` yields `(1/2,1/3,1/6)`. A two-step goal that first enters branch 2 or 3 and then branch 3 has weight `(1/2)(1/6)=1/12` and cost `log 12`.

For a finite root-flux illustration, the density `f(x)=1+2x` on `[0,1]` has total flux `2`. Three equal coordinate sectors have fluxes `4/9`, `2/3`, and `8/9`, hence probabilities `(2/9,1/3,4/9)`. This is only a finite model of how an independently supplied reduced physical measure could determine outgoing weights.

## 7. Conditional preparation and relaxation

Let a sector `B` have reference mass `q>0`, and let its physical preparation region `L` be a union of cells in a finite equal-volume partition with `0<mu(L)<=Cq<1`. Let `pi` be uniform on all cells, prepare `p_0=pi(.|L)`, and use

`K_lambda=lambda I+(1-lambda)P_pi`, `0<=lambda<1`,

where `P_pi` sends every distribution to `pi`. Then

`D(p_0||pi)=-log mu(L) >= -log(Cq)>0`,

and

`p_t=lambda^t p_0+(1-lambda^t)pi`.

For `0<lambda<1`, Shannon entropy strictly increases at successive finite times until equilibrium and `D(p_t||pi)` strictly decreases. For `lambda=0`, equilibrium is reached after one step. This theorem assumes the preparation rule and kernel; it does not derive them from event rarity alone.

With 100 equal cells, a one-cell source preparation has entropy `0` and deficit `log 100`, while a two-cell goal preparation has entropy `log 2` and deficit `log 50`.

## 8. Typicality under a bounded Gibbs tilt

If a bad set has reference probability at most `exp(-cn)` and a normalised Gibbs reweighting has cost oscillation at most `bn`, then

`P_tilt(bad) <= exp(bn) P_ref(bad) <= exp(-(c-b)n)`.

Hence a positive exponential rarity rate of at least `c-b` survives when `c>b`. This preserves an independently established typicality estimate; it neither derives the reference rarity nor proves an argmin claim.

## 9. Interpretive load of the asymptotic theorem

The reference-gap assumption

`-log w_n(H)+log w_n(0^n) >= a K_n(H)`, with `a>0`,

means that the null symbol is the local mode of the reference law: every excitation carries at least `a` units of additional surprisal. In the explicit calibrated model, ablating the agentive term makes the null history the minimiser. The theorem therefore does not derive Past-Hypothesis-like preparation from rootedness alone. Its physical application requires both an argmin actualisation rule and an independently justified alignment, through the physical projection and macro-description, between the modal null sector of `w` and low physical inhomogeneity. If that alignment fails, a small value of `K_n` need not denote a low-entropy physical macrostate.

The entropy-density corollary also assumes that the ternary coordinates count physical microstates uniformly. If the coordinates are only descriptive code symbols, raw type counting has no thermodynamic force; a separate measure bridge, such as the geometric rarity-transfer result above, is required. The combinatorial estimate is the standard method-of-types bound; see Cover and Thomas (2006, chap. 11).

Finally, the calibrated Mahalanobis term is extensive. The feature coordinates are history averages and their covariance under the product law scales as `Sigma_w=O(1/n)`. Therefore `Sigma_w^-1=O(n)`, and a fixed non-zero feature mismatch contributes `O(n)` to the cost. This blocks the incorrect inference that the null history is automatically a zero-rate competitor while the objective is active.

The retained V6.75 failure is consistent with this scaling picture. The preregistered sector `K<=1` passes at depths six and seven but fails at depth eight, where the minimiser has `K=2`. A sector with a fixed absolute excitation count is not stable when the selected histories approach a non-zero excitation density. The scale-stable asymptotic statement is instead the density bound `limsup K_n/n<=u/a`.

## Background references

- Callender, C. (2004). Measures, explanations and the past: Should “special” initial conditions be explained? *The British Journal for the Philosophy of Science, 55*(2), 195–217. https://doi.org/10.1093/bjps/55.2.195
- Cover, T. M., & Thomas, J. A. (2006). *Elements of Information Theory* (2nd ed.). Wiley. https://doi.org/10.1002/047174882X
- Goldstein, S. (2001). Boltzmann’s approach to statistical mechanics. In J. Bricmont, D. Dürr, M. C. Galavotti, G. Ghirardi, F. Petruccione, & N. Zanghì (Eds.), *Chance in Physics: Foundations and Perspectives* (Lecture Notes in Physics, Vol. 574, pp. 39–54). Springer. https://doi.org/10.1007/3-540-44966-3_3

## Scope

The results above prove conditional structural, geometric and probabilistic implications. They do not derive a realistic cosmological reference measure, the event-to-physical map, the alignment of the reference mode with low physical inhomogeneity, an initial macroregion, an agentive ontology, an argmin actualisation law, or a fundamental relaxation dynamics. The calibrated variational and asymptotic results have separate proof records in `computational/` and `variational_ph_proof.md`.
