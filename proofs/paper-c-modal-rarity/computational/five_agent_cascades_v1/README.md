# five_agent_cascades_v1

All 32 participation subsets, coupled/replay controls, all candidate-cost winners and finite sensitivity.

Run from the repository root with Python 3.10+ (standard library only):

```sh
python proofs/paper-c-modal-rarity/computational/five_agent_cascades_v1/model.py
```

The script writes `results.json` in this directory and exits nonzero on a failed check. Mathematical definitions, assumptions, interpretation and limitations are in [integrated_mechanism_results.md](../../integrated_mechanism_results.md), section 3. `results.json` is the expected exhaustive output; no sampling or fitted parameters are used.
