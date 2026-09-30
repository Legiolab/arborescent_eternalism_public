# cascade_entropy_before_selection_v1

Exact weighted signs and mean pathwise Boltzmann changes before any J evaluation.

Run from the repository root with Python 3.10+ (standard library only):

```sh
python proofs/paper-c-modal-rarity/computational/cascade_entropy_before_selection_v1/check.py
```

The script writes `results.json` in this directory and exits nonzero on a failed check. Mathematical definitions, assumptions, interpretation and limitations are in [integrated_mechanism_results.md](../../integrated_mechanism_results.md), section 4. `results.json` is the expected exhaustive output; no sampling or fitted parameters are used.
The sibling `five_agent_cascades_v1/model.py` is a required dependency. Its SHA-256 is recorded in the output.
