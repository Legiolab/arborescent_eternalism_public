# preparation_volume_v1

Exact total-energy and per-mode volumes under a declared product regulator.

Run from the repository root with Python 3.10+ (standard library only):

```sh
python proofs/paper-c-modal-rarity/computational/preparation_volume_v1/check.py
```

The script writes `results.json` in this directory and exits nonzero on a failed check. Mathematical definitions, assumptions, interpretation and limitations are in [integrated_mechanism_results.md](../../integrated_mechanism_results.md), section 1. `results.json` is the expected exhaustive output; no sampling or fitted parameters are used.
