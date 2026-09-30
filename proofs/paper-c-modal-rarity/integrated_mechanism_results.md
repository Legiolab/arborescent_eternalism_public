# Preparation, interacting histories and entropy: retained results

This supplement extends Paper C without identifying structural orientation, finite sensitivity, Boltzmann macroentropy and actuality. All logarithms are natural and k_B=1. The supplied models are finite mathematical witnesses. Goals, networks, preparation laws, phase ordering and macro-partitions are declared inputs.

## 1. Correct regulated volume

For N independent positive quadratic canonical oscillator modes, a product regulator E_j <= E_* gives normalized Liouville mode energies U_j=E_j/E_* uniform on [0,1]. The per-mode low sector U_j<r for every j has volume r^N. The different total-energy sector sum U_j<Nr has volume

F_N(Nr) = (1/N!) sum_{j=0}^{floor(Nr)} (-1)^j binom(N,j)(Nr-j)^N.

Proof: inclusion-exclusion subtracts translated simplices cut off by the N upper bounds U_j<=1. Each unbounded simplex of size z has volume z^N/N!. Reflection U_j -> 1-U_j gives F_N(N/2)=1/2. Therefore r^N must not be assigned to the total-energy sector in a product regulator. For 0<r<1/2, exponential Markov inequality gives F_N(Nr)<=exp(-NI(r)), with I(r)=sup_{t>0}[-tr-log((1-exp(-t))/t)]>0. Positivity follows from the derivative at t=0, 1/2-r>0. At N=64,r=1/4 the exact total volume is about 2.724019499e-13, the per-mode product volume 2.938735877e-39. A total-energy regulator instead defines a different denominator and must be specified separately. This correction leaves a positive quadratic zero-amplitude minimizer intact; it changes the rarity assigned to the region.

## 2. Preparation and selection-compatible late growth

Let L be a preparation sector and F a bad-history event. Suppose a candidate probability P has P(L^c)<=delta, a physical conditional reference mu has mu(F|L)<=epsilon, and dP(.|L)/dmu(.|L)<=Lambda. Then

P(F)<=delta+(1-delta)*min(1,Lambda*epsilon)<=delta+Lambda*epsilon.

Proof: the conditional density bound gives P(F|L)<=min(1,Lambda epsilon); expand P(F) by L and L^c and maximize over P(L^c)<=delta. If P(L)=0 the bound is trivial. This is a probability theorem, not a theorem about a Dirac argmin selector or an automatically supplied physical actuality law.

For a reversible sequential n-bit recorder, source x is preserved, memory starts at zero and bit t is copied by CNOT. Exact capacity for every source requires zero memory for this fixed device because its final memory is m_0 XOR x. The macro-partition fixes source, action and phase and observes only memory occupation K; its volume is binom(n,K). At t>=ceil(3n/4), define a good history by ceil(n/4)<=K_t<=floor(3n/4). For uniform independent input bits,

S_B(t)-S_B(0)>=log binom(n,ceil(n/4))

on every good history. At each late t, Hoeffding's inequality bounds the two excluded tails by 2 exp(-n/32): the threshold is at least n/8 from the mean and t<=n. A union bound over W=n-ceil(3n/4)+1 cuts gives epsilon<=min(1,2W exp(-n/32)). The executable computes exact bad-message counts by dynamic programming, cross-checks all messages at n=4,8,12 and continues to n=512. At n=128 epsilon=0.00033736136316438284 and the guaranteed good-history gain is about 69.4681 nats; at n=512 epsilon=1.5048140780711837e-11 and the gain is about 284.7138 nats.

For a parity goal g and compatibility likelihood ell=1-e when parity(x)=g, ell=e otherwise, normalization is 1/2. The selected conditional density is at most 2(1-e)<2, so this bounded goal tilt preserves rarity of exceptions. Both goals nevertheless have exceptional argmin histories: all-zero/even and one-bit/odd messages. The circuit later uncopies and recovers its resources. Its supplied phase schedule is not an autonomous Hamiltonian clock. The window result establishes neither perpetual monotonicity nor growth under every refinement of the partition. If exact source-memory fidelity is also fixed in the macrostate, the reported memory macrovolume growth disappears.

## 3. Five agents within one physical history

The model supplies E as preparation alternatives in conflict, with a partial order of record/action/transport phases; independent events commute and reconvergences retain preparation provenance. Pi evaluates physical registers on these configurations. With k active agents, (k!)^6 record/action serializations are identified as the same physical history. Branch multiplicity does not count these serializations as additional states. A full initial preparation has a unique deterministic continuation. Interactions occur between agents within a history, not between alternatively realized universes.

Registers: 8 environment bits x, 5 memory bits m, 5 initial plan bits p, 8 preserved initial-sample reference bits initialized equal to x_0, and a supplied phase label. Both coupled and replay controls include that reference register. Goal=21 (binary 10101), target XOR masks=(28,32,192,2,33), three rounds. The active mask ranges over all 32 subsets. In each round, m XORs the active low five bits of current x (coupled) or preserved x_0 (replay); decisions are (m XOR p XOR goal) AND mask. Decision i XORs target mask i into x. Transport performs Toffoli (x_0,x_1)->x_7, CNOT x_2->x_6, then rotates all eight bits left. The inverse reverses these gates. The replay variant is a matched register/control comparison, not a demonstrated energetic equivalence.

The declared counting macro-partition fixes memory, plan, goal and phase, observes environment occupation K, and leaves the sample reference unobserved. Its raw volume is 256 binom(8,K); reported volumes divide by constant 256, leaving all entropy differences unchanged. Counting reference states independently allows macrocell states outside the prepared x_ref=x_0 correlation. This explicit coarse-graining is an assumption, not derived thermodynamics.

For the candidate global cost J=-log w+K(x_0)+4 times the number of final active goal errors, w has uniform x and independent plan bits with P(p_i=0)=3/4. Memory readiness supplies m_0=0. The compatibility term contains no entropy trace, but its goal, coefficient and physical interpretation remain model premises. All ties are retained; the displayed H* uses a stated lexicographic convention.

With all five agents, the coupled winner is unique: (x_0,p)=(72,0), environment trace [72,238,230,55], memory trace [8,6,0], decision trace [29,19,21], normalized volumes [28,28,56,56]. Its late gain is log 2. Flipping one initial plan bit throughout all rounds changes the final environment by [5,3,5,3,5] bits for agents 0..4 and changes other agents' decisions [5,0,4,5,5] times. Replay has zero other-agent decision changes. This demonstrates unequal finite influence and feedback cascades, not a Lyapunov exponent or asymptotic chaos.

Controls are essential to the scope: removing the agentive cost still gives growth in the full-mask example; removing the preparation penalty leaves eight winners, only half growing. Across all 32 masks, coupling improves the growing-winner fraction in none, and lowers it for masks 6 and 14. The construction therefore shows coexistence and interaction of AE's assigned roles, not necessity of cascades for entropy growth or a universal growth theorem.

## 4. Entropy before J

The second executable calls only physical run(), not score(), summary() or argmin. For each active subset it enumerates the same 32 plans under exact weights 3^(5-K(p))/1024 and either all 256 x_0 uniformly or nine low-preparation states K(x_0)<=1 uniformly. Memory is blank, reference correlated with x_0, phases supplied. It measures the reference-weighted mean of individual Boltzmann changes, not Shannon entropy of the path distribution. Late gain is [S_B(2)+S_B(3)]/2-S_B(0). Signs are determined with exact integers by comparing V_2 V_3 to V_0^2.

| Full five-agent preparation | Replay mean gain | Coupled mean gain | Replay P(gain>0) | Coupled P(gain>0) |
|---|---:|---:|---:|---:|
| All states | 0.007664696663 | 0.015329393326 | 0.392009735107 | 0.392101287842 |
| K_0<=1 | 1.965672515277 | 1.947114804679 | 0.97265625 | 0.971354166667 |

For low preparation, coupled negative/zero probabilities are respectively 0.009114583333 and 0.01953125. All 32 masks have positive coupled mean gain, including no agents. Coupling raises the mean in 16 masks, lowers it in 15 and leaves one equal. With all states, coupling raises it in 13, lowers it in 4 and leaves 15 equal; only 10 masks have positive coupled mean gain. In the full five-agent low-preparation case coupling reduces the mean by 0.018557710598 nats and positive probability by 0.001302083333.

Thus a declared preparation and reversible physical dynamics can support frequent late macroentropy growth before a candidate whole-history selection. Cascades modulate this growth and can suppress it. Structural extension order does not alone imply a Boltzmann trend. These finite weighted statements are not claims about our universe or a probability law for actualization.

## 5. Explanatory interpretation

AE may unify preparation requirements, physical evaluation, multiple interacting agents and complete-history compatibility in one mechanics. Reproducing an operation causally is compatible with this proposal. A comparator importing the entire modal structure, constraints and global rule reproduces the mechanism; this establishes representational equivalence, not absence of explanatory content. Ordinary memory and agent interactions alone do not uniquely identify AE. The remaining burden is to independently justify the physical reference, partition, preparation/compatibility constraints and actuality rule, and relate them to the observed history. No exclusive empirical signature or completed cosmological explanation is proved here. J is a global evaluator of a block; it is neither a final physical event causing entropy nor an external observer.
