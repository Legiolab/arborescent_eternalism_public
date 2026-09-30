# Restricted positive-sector variational preparation

## Physical premises

On a product-star extension with boundary amplitude q and a strictly positive transverse-traceless operator L, specify an entropy-independent quadratic action

S=(kappa/2) sum_edges integral_0^infinity [||partial_r H||^2+<H,L H>] dr,

with kappa>0, b branches, decaying extensions and H(0)=q. Modewise minimization gives H_j(r)=q_j exp(-sqrt(lambda_j)r). Substitution yields B(q)=<q,Omega q>/2, Omega=kappa b sqrt(L)>0. More general extension geometries require their own positive Dirichlet-to-Neumann operator; no universal geometry is proved here.

## Conditional selection theorem

For a finite positive spectrum, B(q)=sum_j omega_j q_j^2/2, omega_j>0. Hence B(q)>=0 with equality only at q=0. Given argmin selection for this functional, q*=0 is the unique minimizer. If a separate regularity condition removes the conjugate quadrature p, (q*,p*)=(0,0). A candidate full cost with other terms does not inherit this conclusion automatically: perturbation control requires a stated gap or coercivity bound. Zero/negative modes invalidate strict positivity.

Neither a macro-partition nor a low-energy threshold is needed to obtain the minimizer. Argmin actuality remains an additional hypothesis, not a consequence of positivity.

## Correct volume after selection

Define oscillator energies E_j=(p_j^2+lambda_j q_j^2)/2 and the product regulator Gamma_N={E_j<=E_* for all j}. Liouville energies U_j=E_j/E_* are independently uniform on [0,1]. A per-mode low sector E_j<e_* for all j has fraction (e_*/E_*)^N. A total-energy sector sum E_j<N e_* instead has fraction F_N(Nr), r=e_*/E_*, with

F_N(Nr)=(1/N!) sum_{j=0}^{floor(Nr)}(-1)^j binom(N,j)(Nr-j)^N.

At r=1/2 this equals 1/2, not 2^-N. For fixed 0<r<1/2 it is at most exp(-N I(r)) with positive Chernoff rate I(r). See [the exact derivation](integrated_mechanism_results.md#1-correct-regulated-volume) and [the executable](computational/preparation_volume_v1/).

The selected zero datum belongs to both sectors for every positive threshold. Its membership is independent of the rarity calculation. Exponential rarity of the total-energy sector requires r<1/2; the earlier formula r^N for that sector under a product regulator was incorrect and is replaced here.

## Scope

Ambient Liouville volume differs from an induced measure after imposing p=0 and from a point-mass argmin actuality rule. The ambient volume does not describe the probability of the selected datum. The construction establishes conditional zero-amplitude preparation in a regulated linear positive sector, with declared physical measures. It does not derive a nonlinear gravity/matter Past Hypothesis, regulator-independent cosmological entropy, an autonomous entropy arrow or a fundamental actuality law. Gibbs covariance tau Omega^-1 additionally depends on an independently justified scale tau; positivity alone does not fix the fluctuation amplitude.
