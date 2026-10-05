# Recording capacity and macroscopic entropy supplement

Supports **Recording Capacity and Macroscopic Entropy in Arborescent Eternalism**, version 1. The essential proofs and exact late-window counting algorithm are in the manuscript. This supplement supplies executable finite controls for §5.5; it does not replace those proofs.

| Source | Supported control | Domain |
|---|---|---|
| `event_access_controls/check.py` and `results.json` | The AE event executor and an independently implemented causal register calculation give identical records under all four declared protocols. | Eight sites; every source and every initial memory; two terminal collective protocols, terminal fine read and retained writing trace. |
| Same event-control script | All orders of four independent writes have the same projected final state; serializations do not multiply physical histories. | All 24 orders for each of 16 sources, with blank initial memory. |
| `physical_read_controls/check.py` and `results.json` | Effective collective pointer interaction, occupation cells, fine-access/trace countercontrols and the finite-resolution control. | Explicit finite apparatus parameters defined in the script. |

Run independently with Python 3.10+ and the standard library:

```sh
python proofs/paper-c-recording-entropy/event_access_controls/check.py
python proofs/paper-c-recording-entropy/physical_read_controls/check.py
```

Both scripts exit nonzero on failed checks and regenerate the adjacent output. Scientific check fields and counts are deterministic; `runtime_seconds` is execution metadata. No sampling, fitted entropy objective or private import is used.

These are conditional checks of a specified recorder and reader, not a new proof that all AE systems increase entropy. The source law, physical operations, read access and resources remain explicit apparatus assumptions. No thermodynamic heat, physical production of readiness, global actuality law or cosmological preparation is derived.

[Earlier rarity and selection work](../paper-c-modal-rarity/README.md) is archived separately. A script supporting this current paper should be cited through its path at the same immutable commit as this README.
