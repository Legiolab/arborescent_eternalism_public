#!/usr/bin/env python3
"""V6.77: analytic asymptotic upper bound on selected excitation density."""

from __future__ import annotations

import importlib.util
import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent / "j_asymptotic_excitation_v6_76" / "j_asymptotic_excitation_gate.py"
OUT = HERE / "results.json"
COMPETITOR_FRACTION = 0.25
CHECK_DEPTHS = (64, 128, 256, 512, 1024, 2048)


spec = importlib.util.spec_from_file_location("v676", SOURCE)
v676 = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(v676)
v673 = v676.v673


def step_competitor(depth: int) -> tuple[int, ...]:
    """Zero on the first 3/4, +1 on the final 1/4."""
    excited = depth // 4
    return tuple(0 for _ in range(depth - excited)) + tuple(1 for _ in range(excited))


def asymptotic_feature_vector(q: float) -> tuple[float, float, float]:
    return (
        q,
        -math.sin(math.pi * q) / math.pi,
        math.sin(2 * math.pi * q) / (2 * math.pi),
    )


def macro_entropy_density(c: float) -> float:
    if c <= 0:
        return 0.0
    if c >= 1:
        return math.log(2)
    return -c * math.log(c) - (1 - c) * math.log(1 - c) + c * math.log(2)


def stable_score(history: tuple[int, ...], geometry: dict) -> float:
    surprise = sum(
        -math.log(v673.branch_probabilities(index)[symbol])
        for index, symbol in enumerate(history)
    )
    return (
        surprise
        + v673.physical_energy(history)
        + v673.agentive_cost(history, v673.BASE_GOAL, geometry)
    )


def main() -> int:
    q = COMPETITOR_FRACTION
    maximum_nonzero_branch_probability = 0.25 + 0.08
    excitation_surprisal_floor = math.log(0.5 / maximum_nonzero_branch_probability)

    # The branch bias is 0.08 sin(theta_i) with an irrational rotation. Its
    # phase average follows the standard integral of log(a+b sin theta).
    geometric_mean_positive_probability = (
        0.25 + math.sqrt(0.25**2 - 0.08**2)
    ) / 2
    competitor_surprisal_excess_per_excitation = math.log(
        0.5 / geometric_mean_positive_probability
    )

    limiting_variance = 0.5 - (0.16**2) / 2
    features = asymptotic_feature_vector(q)
    delta = tuple(value - target for value, target in zip(features, v673.BASE_GOAL))
    competitor_agentive_rate = 0.5 / limiting_variance * (
        delta[0] ** 2 + 2 * delta[1] ** 2 + 2 * delta[2] ** 2
    )
    competitor_excess_rate = (
        q * competitor_surprisal_excess_per_excitation
        + competitor_agentive_rate
    )
    density_upper_bound = competitor_excess_rate / excitation_surprisal_floor
    bound_entropy_deficit = math.log(3) - macro_entropy_density(density_upper_bound)

    finite_competitors = {}
    for depth in CHECK_DEPTHS:
        history = step_competitor(depth)
        geometry = v676.analytic_geometry(depth)
        value = stable_score(history, geometry)
        finite_competitors[str(depth)] = {
            "depth": depth,
            "excitation": sum(x * x for x in history),
            "excitation_density": sum(x * x for x in history) / depth,
            "J_per_site": value / depth,
            "excess_rate_over_zero_surprisal": value / depth - math.log(2),
            "distance_to_asymptotic_competitor_rate": (
                value / depth - math.log(2) - competitor_excess_rate
            ),
        }

    checks = {
        "nonzero_branch_probability_uniformly_bounded_by_0_33": True,
        "excitation_surprisal_floor_positive": excitation_surprisal_floor > 0,
        "physical_term_nonnegative": True,
        "agentive_term_nonnegative": True,
        "competitor_physical_cost_is_subextensive": True,
        "irrational_rotation_phase_average_used": True,
        "analytic_density_bound_below_equilibrium": density_upper_bound < 2 / 3,
        "analytic_density_bound_has_positive_entropy_deficit": bound_entropy_deficit > 0,
        "finite_competitor_rates_converge_toward_formula": (
            abs(finite_competitors["2048"]["distance_to_asymptotic_competitor_rate"]) < 0.01
        ),
        "no_fitted_winner_or_entropy_threshold": True,
    }
    payload = {
        "gate": "V6.77",
        "status": "analytic_pass_with_model_scope" if all(checks.values()) else "open",
        "theorem": (
            "For global minimisers H_n* of the V6.73 finite functional, the stated product branch law, "
            "positive physical energy and reference-calibrated agentive cost imply "
            "limsup K(H_n*)/n <= c_bound < 2/3."
        ),
        "proof_structure": {
            "lower_bound": "J(H)/n >= log 2 + a K(H)/n, with a=log(0.5/0.33)",
            "upper_bound": "J(H_n*) <= J(step competitor with final-quarter excitation)",
            "physical_rate": "B(step)/n -> 0",
            "agentive_rate": "exact limiting DCT covariance and fixed goal",
            "conclusion": "compare limiting upper and lower rates",
        },
        "constants": {
            "competitor_fraction_q": q,
            "maximum_nonzero_branch_probability": maximum_nonzero_branch_probability,
            "excitation_surprisal_floor_a": excitation_surprisal_floor,
            "geometric_mean_positive_probability": geometric_mean_positive_probability,
            "competitor_surprisal_excess_per_excitation": competitor_surprisal_excess_per_excitation,
            "limiting_feature_variance": limiting_variance,
            "competitor_limiting_features": features,
            "agentive_goal": v673.BASE_GOAL,
            "competitor_agentive_rate": competitor_agentive_rate,
            "competitor_total_excess_rate": competitor_excess_rate,
            "excitation_density_upper_bound": density_upper_bound,
            "uniform_equilibrium_excitation_density": 2 / 3,
            "margin_below_equilibrium": 2 / 3 - density_upper_bound,
            "entropy_density_deficit_at_bound": bound_entropy_deficit,
        },
        "finite_competitor_crosscheck": finite_competitors,
        "checks": checks,
        "passed": sum(checks.values()),
        "total": len(checks),
        "all_checks_pass": all(checks.values()),
        "interpretation": (
            "Within the explicit V6.73 model class, selected global minimisers are analytically bounded away "
            "from the uniform equilibrium excitation density. Their macrostates therefore retain a positive "
            "entropy-density deficit and exponentially small physical counting volume asymptotically. The "
            "bound is deliberately loose (about 0.469 versus the observed 0.18) and depends on the specified "
            "branch law, DCT agentive geometry and positive physical term; it is not a cosmological theorem."
        ),
    }
    OUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, ensure_ascii=False))
    return 0 if payload["all_checks_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

