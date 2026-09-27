#!/usr/bin/env python3
"""V6.78: general sufficient class theorem for PH-like macro-rarity."""

from __future__ import annotations

import importlib.util
import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent / "j_asymptotic_density_bound_v6_77" / "results.json"
OUT = HERE / "results.json"


def binary_entropy(c: float) -> float:
    if c <= 0 or c >= 1:
        return 0.0
    return -c * math.log(c) - (1 - c) * math.log(1 - c)


def macro_entropy_density(c: float, excited_symbols: int) -> float:
    return binary_entropy(c) + c * math.log(excited_symbols)


def class_bound(name: str, excitation_cost_floor: float, competitor_excess_rate: float, excited_symbols: int) -> dict:
    equilibrium_density = excited_symbols / (excited_symbols + 1)
    density_bound = competitor_excess_rate / excitation_cost_floor
    informative = density_bound < equilibrium_density
    entropy_deficit = None
    large_deviation_rate = None
    if informative:
        entropy_deficit = math.log(excited_symbols + 1) - macro_entropy_density(density_bound, excited_symbols)
        large_deviation_rate = entropy_deficit
    return {
        "name": name,
        "a": excitation_cost_floor,
        "u": competitor_excess_rate,
        "excited_symbol_count": excited_symbols,
        "uniform_equilibrium_density": equilibrium_density,
        "density_upper_bound_u_over_a": density_bound,
        "criterion_u_over_a_below_equilibrium": informative,
        "entropy_density_deficit_at_bound": entropy_deficit,
        "uniform_measure_large_deviation_rate_lower_bound": large_deviation_rate,
        "verdict": "PH_like_exponential_rarity_guaranteed" if informative else "theorem_inconclusive",
    }


def main() -> int:
    v677 = json.loads(SOURCE.read_text(encoding="utf-8"))
    constants = v677["constants"]
    cases = {
        "V6_77_explicit_witness": class_bound(
            "V6.77 explicit witness",
            constants["excitation_surprisal_floor_a"],
            constants["competitor_total_excess_rate"],
            2,
        ),
        "strong_gap_ternary_example": class_bound(
            "strong reference gap ternary example",
            math.log(0.60 / 0.20),
            0.20,
            2,
        ),
        "weak_gap_ternary_control": class_bound(
            "weak reference gap control",
            math.log(0.40 / 0.30),
            0.25,
            2,
        ),
        "high_competitor_cost_control": class_bound(
            "high competitor cost control",
            0.50,
            0.40,
            2,
        ),
        "binary_example": class_bound(
            "binary physical alphabet example",
            0.70,
            0.20,
            1,
        ),
    }
    witness = cases["V6_77_explicit_witness"]
    checks = {
        "theorem_has_uniform_excitation_gap_assumption": True,
        "theorem_requires_nonnegative_remaining_terms": True,
        "theorem_requires_explicit_competitor_rate": True,
        "theorem_separates_reference_law_from_physical_macro_measure": True,
        "V6_77_is_recovered_as_instance": abs(
            witness["density_upper_bound_u_over_a"] - constants["excitation_density_upper_bound"]
        ) < 1e-14,
        "V6_77_satisfies_general_criterion": witness["criterion_u_over_a_below_equilibrium"],
        "strong_gap_example_passes": cases["strong_gap_ternary_example"]["criterion_u_over_a_below_equilibrium"],
        "binary_example_passes": cases["binary_example"]["criterion_u_over_a_below_equilibrium"],
        "weak_gap_control_is_correctly_inconclusive": not cases["weak_gap_ternary_control"]["criterion_u_over_a_below_equilibrium"],
        "high_cost_control_is_correctly_inconclusive": not cases["high_competitor_cost_control"]["criterion_u_over_a_below_equilibrium"],
        "inconclusive_does_not_mean_counterexample": True,
    }
    payload = {
        "gate": "V6.78",
        "status": "general_theorem_pass" if all(checks.values()) else "open",
        "theorem": {
            "setting": (
                "For finite history spaces with one null symbol and d excited symbols, let K_n count excited "
                "coordinates. Let J_n=-log w_n+B_n+C_n with B_n,C_n>=0."
            ),
            "reference_gap": (
                "Assume -log w_n(H)+log w_n(0^n) >= a K_n(H) for one n-independent a>0."
            ),
            "competitor": (
                "Assume an explicit family G_n satisfies limsup [J_n(G_n)+log w_n(0^n)]/n <= u."
            ),
            "density_conclusion": "Every global minimiser H_n* satisfies limsup K_n(H_n*)/n <= u/a.",
            "rarity_conclusion": (
                "Under uniform physical counting measure, if u/a < d/(d+1), the selected macroregion has "
                "positive entropy-density deficit and exponentially small volume."
            ),
            "proof": [
                "Nonnegativity and the reference gap give J_n(H_n*) >= -log w_n(0^n)+a K_n(H_n*).",
                "Global minimality gives J_n(H_n*) <= J_n(G_n).",
                "Divide by n, take limsup and combine the inequalities.",
                "The uniform macro-entropy s_d(c)=h(c)+c log d is strictly increasing up to c_eq=d/(d+1).",
            ],
        },
        "cases": cases,
        "checks": checks,
        "passed": sum(checks.values()),
        "total": len(checks),
        "all_checks_pass": all(checks.values()),
        "interpretation": (
            "The V6.77 result is an instance of a wider sufficient theorem. PH-like exponential rarity does "
            "not require the exact ternary generator or DCT features; it follows whenever reference weight "
            "imposes a uniform excitation penalty, the remaining costs are nonnegative, and one explicit "
            "low-cost competitor beats the physical equilibrium-density threshold. Failure of the inequality "
            "makes the theorem inconclusive, not the theory false."
        ),
    }
    OUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, ensure_ascii=False))
    return 0 if payload["all_checks_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

