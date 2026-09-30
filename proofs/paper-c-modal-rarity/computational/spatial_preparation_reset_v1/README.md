# Spatial preparation with a reset kernel

This is a new finite stochastic toy model, not a physical reinterpretation proved equivalent to the earlier string witness. It separates spatial site j from physical time t. Python 3, standard library only; covariance inverse requires n >= 3.

## Reproduce
```bash
python proofs/paper-c-modal-rarity/computational/spatial_preparation_reset_v1/check.py
```
Compare standard output with results.txt. Enumeration covers every one of the 3^n initial states for n=3,...,10, using the exact continuation reduction below. Numerical scores use floating-point arithmetic; the analytic bound is independent of finite numerical optimisation.

## Model and proof
On X_n={-1,0,1}^n, K(x)=sum_j x_j^2. Histories are (x_0,...,x_T), with preparation r_Sigma(H)=x_0. These are the physical state and history spaces of the toy model; no nontrivial AE event-to-spacetime projection is derived.

Let b_j=0.08 sin((j+1) pi(sqrt(5)-1)), p_j(0)=0.5, p_j(+1)=0.25+b_j and p_j(-1)=0.25-b_j. Set p_n=product_j p_j. The independent counting measure is mu_n(x)=3^{-n}. Its typical excitation density is 2/3; under p_n it is 1/2.

The dynamics is P_n(x,y)=(1-r)1_{x=y}+r3^{-n}, with r=0.2 in the script. The history weight is w(H)=p_n(x_0) product_t P_n(x_t,x_{t+1}). The criterion is J=-log w+B_n(x_0)+C_n(x_0).

B_n is the nonnegative mean/gradient/curvature cost implemented in check.py. The three spatial cosine features are F_m(x)=n^{-1} sum_j x_j cos(pi m(j+1/2)/n), m=0,1,2. C_n is the quadratic target penalty (F-g)^T Cov_p(F)^{-1}(F-g)/2, g=(0.35,-0.25,0.20). The covariance does not justify the target or an agentive interpretation.

Every transition is at most s_n=1-r+r3^{-n}, with equality exactly on the diagonal. At each fixed preparation the best continuation is constant. Consequently J_eff(x)=-log p_n(x)+B_n(x)+C_n(x)-T log s_n, and the time term cancels in comparisons. This holds even for T=T(n), specifically for this kernel and preparation-only extra costs.

Since p_j(+/-1)<=0.33, J(H)>=b_n+aK(x_0), where b_n=n log2-T log s_n and a=log(0.5/0.33).
Compare a minimiser with the constant continuation of a profile G_n that is zero on the first three quarters of sites and +1 on the last quarter. Minimality gives
aK(x_0*) <= J_spatial(G_n)-n log2.

With q=1/4, m_+=(0.25+sqrt(0.25^2-0.08^2))/2, and v=0.4872:
u_ref=q log(0.5/m_+).
F(G_n) tends to (q,-sin(pi q)/pi,sin(2pi q)/(2pi)).
n Cov_p(F) tends to diag(v,v/2,v/2).
Writing delta=F_limit-g, u_obj=(delta_0^2+2delta_1^2+2delta_2^2)/(2v).
B_n(G_n)/n tends to zero. Hence
limsup K(x_0*)/n <= c=u/a=0.4690783862920194,
where u=0.19490931393295022. This is an upper bound, not the measured density of a minimiser.

## Counting and entropy
The macrocell K=k contains binom(n,k)2^k states. For c<2/3, mu_n(K<=floor(cn)) has exponent
Delta(c)=log3-h(c)-c log2=0.08223826039954041.
The limsup bound guarantees eventual membership in K/n<=c+epsilon, for every epsilon>0 with c+epsilon<2/3. Taking epsilon down to zero gives the limiting deficit. The exponent depends on the counting measure; under p_n the corresponding rate is D(c||1/2), approximately 0.0019135.

The separate ensemble prescription rho_0=mu_n(.|K<=floor(cn)) yields rho_t=(1-r)^t rho_0+[1-(1-r)^t]mu_n. Strict concavity gives increasing Shannon entropy. Selection of one history does not generate this ensemble prescription.

## Limits and ablation
Every selected history is constant: its Boltzmann macroentropy does not increase. Removing C_n selects the unique all-zero preparation and constant continuation, since p_n already favours zero and B_n>=0. The reset is global and does not conserve energy. No cosmological law, physical justification of the counting measure, general projection bound, causal agent, or universal thermodynamic arrow is established.

## Provenance
Initial formulas and standalone reproduction were supplied in the 30 September 2026 preparation note, based on V6.73/V6.77 at commit 58f6f1d2694404b1376a840e79b7640033c3f075. This directory publishes the distinct two-index construction with explicit scope. The original string calculations are retained for provenance.
