# V6.75 — integrated PH-like arrow

## Purpose

Run the explicit fixed `J` and the thermodynamic bridge inside one finite model, without changing parameters between selection, rarity and relaxation.

## Preregistered physical sector

For a ternary projected history, define the excitation observable

`K(H)=sum_i h_i^2`.

The PH-like preparation sector is fixed as the ground state plus the first excitation shell:

`L_n={H:K(H)<=1}`.

Under the uniform counting measure on the finite projected physical phase space,

`mu(L_n)=(1+2n)/3^n`,

so its volume decreases exponentially with depth. Neither `K`, `L_n` nor the physical measure enters `J` as an entropy target.

## Integrated chain

1. Compute `J(H)=-log w_E(H)+B_E,Pi(H)+C_A(H)` exhaustively.
2. Test whether the unique winner lies in `L_n` at depths six, seven and eight, retaining any failure rather than widening `L_n` after inspection.
3. Ablate `A` to determine whether the low source is physically protected rather than agent-created.
4. Start an ensemble at the selected history and apply the independently fixed mixing kernel `P=(1-r)I+rU`.
5. Verify increasing Shannon entropy and decreasing relative entropy to equilibrium.

## Scope

The strict `K<=1` claim passes at depths six and seven but fails at depth eight, where the winner has `K=2`. A separate scaling audit through depth ten observes winner excitation no larger than two; that observation does not establish a bound at arbitrary depth. The gate therefore supplies an integrated finite pass and a no-go for the original fixed sector, not a cosmological derivation. It also does not derive the physical counting measure, coarse graining or mixing kernel, nor imply monotonic Boltzmann entropy along every microscopic realised trajectory.

## Run

```bash
python evidence/j_integrated_ph_arrow_v6_75/j_integrated_ph_arrow_gate.py
```


