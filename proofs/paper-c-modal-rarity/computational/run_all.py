#!/usr/bin/env python3
"""Run the complete public Paper C computational chain."""

from pathlib import Path
import subprocess
import sys


HERE = Path(__file__).resolve().parent
SCRIPTS = (
    HERE / "operational_record_capacity_v1" / "check.py",
    HERE / "record_reset_thermodynamics_v1" / "check.py",
    HERE / "reliable_record_v1" / "check.py",
    HERE / "spatial_preparation_reset_v1" / "check.py",
    HERE / "local_delayed_objective_v1" / "check.py",
    HERE / "j_generative_common.py",
    HERE / "j_reference_calibrated_v6_73" / "j_reference_calibrated_gate.py",
    HERE / "j_feature_invariance_v6_74" / "j_feature_invariance_gate.py",
    HERE / "j_integrated_ph_arrow_v6_75" / "j_integrated_ph_arrow_gate.py",
    HERE / "j_asymptotic_excitation_v6_76" / "j_asymptotic_excitation_gate.py",
    HERE / "j_asymptotic_density_bound_v6_77" / "j_asymptotic_density_bound_gate.py",
    HERE / "general_ph_class_bound_v6_78" / "general_ph_class_bound_gate.py",
)


def main() -> int:
    for script in SCRIPTS:
        print(f"Running {script.relative_to(HERE)}", flush=True)
        completed = subprocess.run(
            [sys.executable, str(script)],
            stdout=subprocess.DEVNULL,
            check=False,
        )
        if completed.returncode:
            print(f"FAILED: {script.relative_to(HERE)}", file=sys.stderr)
            return completed.returncode
    print(f"PASS: {len(SCRIPTS)} computational gates")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
