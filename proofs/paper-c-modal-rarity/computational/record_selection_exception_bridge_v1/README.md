# record_selection_exception_bridge_v1

Reversible recording, exact late-window counts and a bounded compatibility tilt.

Run from the repository root with Python 3.10+ (standard library only):

```sh
python proofs/paper-c-modal-rarity/computational/record_selection_exception_bridge_v1/check.py
```

The script writes `results.json` in this directory and exits nonzero on a failed check. Mathematical definitions, assumptions, interpretation and limitations are in [integrated_mechanism_results.md](../../integrated_mechanism_results.md), section 2. `results.json` is the expected exhaustive output; no sampling or fitted parameters are used.
