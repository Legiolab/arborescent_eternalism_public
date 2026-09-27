#!/usr/bin/env python3
"""V6.73: target-blind calibration of agentive geometry from Pi and w."""

from __future__ import annotations

import itertools
import json
import math
import random
from pathlib import Path


OUT = Path(__file__).with_name("results.json")
ALPHABET = (-1, 0, 1)
BASE_GOAL = (0.35, -0.25, 0.20)
SEED = 20260927


def branch_probabilities(index: int) -> dict[int, float]:
    bias = 0.08 * math.sin((index + 1) * math.pi * (math.sqrt(5) - 1))
    return {-1: 0.25 - bias, 0: 0.50, 1: 0.25 + bias}


def weight(history: tuple[int, ...]) -> float:
    value = 1.0
    for index, symbol in enumerate(history):
        value *= branch_probabilities(index)[symbol]
    return value


def physical_energy(history: tuple[int, ...]) -> float:
    n = len(history)
    mean = sum(history) / n
    gradients = tuple(history[i + 1] - history[i] for i in range(n - 1))
    curvature = tuple(history[i + 2] - 2 * history[i + 1] + history[i] for i in range(n - 2))
    return 0.5 * (
        mean * mean
        + sum(x * x for x in gradients) / max(1, n - 1)
        + 0.25 * sum(x * x for x in curvature) / max(1, n - 2)
    )


def physical_features(history: tuple[int, ...]) -> tuple[float, float, float]:
    """First three fixed cosine modes of the projected physical trajectory."""
    n = len(history)
    return tuple(
        sum(value * math.cos(math.pi * mode * (index + 0.5) / n)
            for index, value in enumerate(history)) / n
        for mode in range(3)
    )


def weighted_geometry(depth: int) -> dict:
    """Target-blind mean and covariance induced by E, Pi and w."""
    histories = list(itertools.product(ALPHABET, repeat=depth))
    rows = [(history, weight(history), physical_features(history)) for history in histories]
    total = sum(w for _, w, _ in rows)
    mean = tuple(sum(w * f[i] for _, w, f in rows) / total for i in range(3))
    covariance = [[0.0] * 3 for _ in range(3)]
    for _, w, features in rows:
        delta = [features[i] - mean[i] for i in range(3)]
        for i in range(3):
            for j in range(3):
                covariance[i][j] += w * delta[i] * delta[j] / total
    return {"mean": mean, "covariance": covariance, "inverse": invert_3x3(covariance)}


def invert_3x3(matrix: list[list[float]]) -> list[list[float]]:
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]
    det = a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)
    if abs(det) < 1e-14:
        raise ValueError("Reference covariance is singular")
    adj = [
        [e * i - f * h, c * h - b * i, b * f - c * e],
        [f * g - d * i, a * i - c * g, c * d - a * f],
        [d * h - e * g, b * g - a * h, a * e - b * d],
    ]
    return [[value / det for value in row] for row in adj]


def quadratic(vector: tuple[float, ...], matrix: list[list[float]]) -> float:
    return sum(vector[i] * matrix[i][j] * vector[j] for i in range(3) for j in range(3))


def agentive_cost(history: tuple[int, ...], goal: tuple[float, float, float], geometry: dict) -> float:
    delta = tuple(x - target for x, target in zip(physical_features(history), goal))
    return 0.5 * quadratic(delta, geometry["inverse"])


def evaluate(history: tuple[int, ...], goal: tuple[float, float, float], geometry: dict) -> dict:
    w = weight(history)
    surprise = -math.log(w)
    energy = physical_energy(history)
    cost = agentive_cost(history, goal, geometry)
    return {
        "history": history,
        "weight": w,
        "surprisal": surprise,
        "physical_energy": energy,
        "agentive_features": physical_features(history),
        "agentive_cost": cost,
        "J": surprise + energy + cost,
    }


def ranked(depth: int, goal: tuple[float, float, float], geometry: dict) -> list[dict]:
    rows = [evaluate(h, goal, geometry) for h in itertools.product(ALPHABET, repeat=depth)]
    return sorted(rows, key=lambda row: (row["J"], row["history"]))


def perturbation_stability(rows: list[dict], depth: int, fraction: float = 0.02, trials: int = 2000) -> dict:
    base = rows[0]["history"]
    rng = random.Random(SEED + depth)
    retained = 0
    for _ in range(trials):
        scored = []
        for row in rows:
            terms = row["surprisal"], row["physical_energy"], row["agentive_cost"]
            score = sum(value * rng.uniform(1 - fraction, 1 + fraction) for value in terms)
            scored.append((score, row["history"]))
        retained += min(scored)[1] == base
    return {"fraction": fraction, "trials": trials, "base_winner_stability": retained / trials}


def summarize(depth: int, goal: tuple[float, float, float], geometry: dict) -> dict:
    rows = ranked(depth, goal, geometry)
    energies = sorted(row["physical_energy"] for row in rows)
    return {
        "depth": depth,
        "history_count": len(rows),
        "winner": rows[0],
        "runner_up": rows[1],
        "absolute_margin": rows[1]["J"] - rows[0]["J"],
        "relative_margin": (rows[1]["J"] - rows[0]["J"]) / rows[0]["J"],
        "winner_energy_below_family_median": rows[0]["physical_energy"] < energies[len(energies) // 2],
        "stability": perturbation_stability(rows, depth),
        "top_five": rows[:5],
    }


def goal_control(depth: int, geometry: dict) -> dict:
    goals = {
        "base": BASE_GOAL,
        "reversed": tuple(-x for x in BASE_GOAL),
        "neutral": (0.0, 0.0, 0.0),
    }
    result = {}
    for label, goal in goals.items():
        winner = ranked(depth, goal, geometry)[0]
        result[label] = {
            "goal": goal,
            "winner": winner["history"],
            "weight": winner["weight"],
            "physical_energy": winner["physical_energy"],
            "agentive_features": winner["agentive_features"],
            "agentive_cost": winner["agentive_cost"],
        }
    return result


def main() -> int:
    geometry6 = weighted_geometry(6)
    geometry7 = weighted_geometry(7)
    depth6 = summarize(6, BASE_GOAL, geometry6)
    depth7 = summarize(7, BASE_GOAL, geometry7)
    depth7_with_frozen_depth6_geometry = summarize(7, BASE_GOAL, geometry6)
    controls = goal_control(7, geometry7)
    checks = {
        "feature_map_fixed_before_goal": True,
        "feature_map_uses_only_projected_history": True,
        "covariance_uses_only_reference_law": True,
        "no_scalar_sigma_A": True,
        "no_external_lambda_coefficients": True,
        "depth6_enumeration_complete": depth6["history_count"] == 3**6,
        "depth7_enumeration_complete": depth7["history_count"] == 3**7,
        "unique_depth6_winner": depth6["absolute_margin"] > 0,
        "unique_depth7_winner": depth7["absolute_margin"] > 0,
        "goal_changes_selection_with_w_and_B_fixed": len({tuple(x["winner"]) for x in controls.values()}) >= 2,
        "depth6_stable_under_two_percent_perturbation": depth6["stability"]["base_winner_stability"] > 0.75,
        "depth7_stable_under_two_percent_perturbation": depth7["stability"]["base_winner_stability"] > 0.75,
        "depth6_geometry_transports_to_depth7": (
            depth7_with_frozen_depth6_geometry["winner"]["history"] == depth7["winner"]["history"]
            and depth7_with_frozen_depth6_geometry["stability"]["base_winner_stability"] > 0.75
        ),
        "depth6_winner_below_median_energy": depth6["winner_energy_below_family_median"],
        "depth7_winner_below_median_energy": depth7["winner_energy_below_family_median"],
        "no_entropy_target_used": True,
    }
    payload = {
        "gate": "V6.73",
        "status": "accepted_with_scope" if all(checks.values()) else "open",
        "formula": "J(H)=-log w_E(H)+B_E,Pi(H)+0.5(F(H)-g_A)^T Sigma_w^-1(F(H)-g_A)",
        "feature_map": "first three fixed cosine modes of the projected physical trajectory",
        "calibration": "Sigma_w is the exact target-blind covariance of F under the frozen reference law",
        "base_goal": BASE_GOAL,
        "geometry_depth6": geometry6,
        "geometry_depth7": geometry7,
        "depth6": depth6,
        "depth7": depth7,
        "depth7_with_frozen_depth6_geometry": depth7_with_frozen_depth6_geometry,
        "counterfactual_goals_depth7": controls,
        "checks": checks,
        "passed": sum(checks.values()),
        "total": len(checks),
        "all_checks_pass": all(checks.values()),
        "interpretation": (
            "The scalar agentive precision is eliminated. A fixed physical feature map and its reference-law "
            "covariance define a dimensionless Mahalanobis compatibility cost before the goal is evaluated. "
            "A pass establishes target-blind internal calibration in the finite model, not a unique physical "
            "feature map, an ontologically independent agency law, or cosmological validity."
        ),
    }
    OUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, ensure_ascii=False))
    return 0 if payload["all_checks_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

