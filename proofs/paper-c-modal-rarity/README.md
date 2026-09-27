# Proof and reproducibility supplement

## Paper

**Modal Rarity, Physical Preparation and Entropy in a Tenseless World**

## Public claims supported

| Claim | Evidence |
|---|---|
| One generated ternary history supplies reference weight, physical cost and agentive compatibility | `computational/j_generative_common.py` |
| Unique minima at depths 6 and 7 | `computational/results.json` |
| Stability under 2 percent perturbations: 99.05 percent and 100 percent | `computational/results.json` |
| Changing only the represented goal can change the selected history while w and the physical law remain fixed | `computational/results.json` |
| A positive entropy-blind quadratic contribution has the zero-amplitude argmin in the restricted positive TT sector | `variational_ph_proof.md` |
| The selected datum lies in an exponentially rare regulated macroregion with ratio (e*/E*)^N | `variational_ph_proof.md` |

## Reproduction

```bash
python proofs/paper-c-modal-rarity/computational/j_generative_common.py
```

The script uses only the Python standard library and overwrites `results.json` deterministically.

## Limits

These materials establish a finite constructive witness and a restricted positive-sector theorem. They do not derive realistic cosmology, a universal Past Hypothesis, a fundamental argmin law or libertarian freedom.
