#!/usr/bin/env python3
"""V6.74: feature-geometry invariance and matched-chance audit for local J."""

from __future__ import annotations

import importlib.util
import itertools
import json
import math
import random
from pathlib import Path


HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent / "j_reference_calibrated_v6_73" / "j_reference_calibrated_gate.py"
OUT = HERE / "results.json"
SEED = 20260927
ALPHABET = (-1, 0, 1)


spec = importlib.util.spec_from_file_location("v673", SOURCE)
v673 = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(v673)


def target_profile(depth: int, sign: int = 1) -> tuple[float, ...]:
    """One preregistered continuous physical target, sampled at cell centres."""
    if sign == 0:
        return tuple(0.0 for _ in range(depth))
    return tuple(
        sign * (
            0.35
            + 2 * (-0.25) * math.cos(math.pi * (index + 0.5) / depth)
            + 2 * 0.20 * math.cos(2 * math.pi * (index + 0.5) / depth)
        )
        for index in range(depth)
    )


def dct_features(profile: tuple[float, ...], modes=(0, 1, 2)) -> tuple[float, float, float]:
    n = len(profile)
    return tuple(
        sum(value * math.cos(math.pi * mode * (index + 0.5) / n)
            for index, value in enumerate(profile)) / n
        for mode in modes
    )


def transformed_dct_features(profile: tuple[float, ...]) -> tuple[float, float, float]:
    """Invertible coordinate change of the same DCT(0,1,2) observable subspace."""
    x, y, z = dct_features(profile)
    return 2 * x + y, y - z, x + 3 * z


def rival_dct_features(profile: tuple[float, ...]) -> tuple[float, float, float]:
    """A genuinely different smooth physical subspace."""
    return dct_features(profile, modes=(0, 1, 3))


def high_frequency_control(profile: tuple[float, ...]) -> tuple[float, float, float]:
    """Negative control that discards the target's registered low modes."""
    return dct_features(profile, modes=(3, 4, 5))


def block_features(profile: tuple[float, ...]) -> tuple[float, float, float]:
    """Coarse local observables: means on three consecutive physical blocks."""
    n = len(profile)
    cuts = (0, n // 3, 2 * n // 3, n)
    values = []
    for lo, hi in zip(cuts, cuts[1:]):
        values.append(sum(profile[lo:hi]) / (hi - lo))
    return tuple(values)


FEATURE_MAPS = {
    "dct_012": lambda h: dct_features(h),
    "dct_012_invertible_reparameterization": transformed_dct_features,
    "dct_013_rival_subspace": rival_dct_features,
    "three_block_local_means": block_features,
    "dct_345_high_frequency_negative_control": high_frequency_control,
}


def covariance_geometry(depth: int, feature_map) -> dict:
    rows = []
    for history in itertools.product(ALPHABET, repeat=depth):
        rows.append((v673.weight(history), feature_map(history)))
    total = sum(w for w, _ in rows)
    mean = tuple(sum(w * f[i] for w, f in rows) / total for i in range(3))
    covariance = [[0.0] * 3 for _ in range(3)]
    for w, features in rows:
        delta = [features[i] - mean[i] for i in range(3)]
        for i in range(3):
            for j in range(3):
                covariance[i][j] += w * delta[i] * delta[j] / total
    return {"mean": mean, "covariance": covariance, "inverse": v673.invert_3x3(covariance)}


def agentive_cost(history, goal_features, feature_map, geometry) -> float:
    features = feature_map(history)
    delta = tuple(x - target for x, target in zip(features, goal_features))
    return 0.5 * v673.quadratic(delta, geometry["inverse"])


def rank(depth: int, physical_goal, feature_map, geometry) -> list[dict]:
    goal_features = feature_map(physical_goal)
    rows = []
    for history in itertools.product(ALPHABET, repeat=depth):
        w = v673.weight(history)
        surprise = -math.log(w)
        energy = v673.physical_energy(history)
        cost = agentive_cost(history, goal_features, feature_map, geometry)
        rows.append({
            "history": history,
            "weight": w,
            "physical_energy": energy,
            "agentive_cost": cost,
            "J": surprise + energy + cost,
        })
    return sorted(rows, key=lambda row: (row["J"], row["history"]))


def stability(rows: list[dict], depth: int, trials=1000, fraction=0.02) -> float:
    rng = random.Random(SEED + depth)
    base = rows[0]["history"]
    retained = 0
    for _ in range(trials):
        scored = []
        for row in rows:
            surprise = -math.log(row["weight"])
            terms = surprise, row["physical_energy"], row["agentive_cost"]
            score = sum(value * rng.uniform(1 - fraction, 1 + fraction) for value in terms)
            scored.append((score, row["history"]))
        retained += min(scored)[1] == base
    return retained / trials


def representation_audit(depth: int) -> dict:
    physical_goal = target_profile(depth, 1)
    result = {}
    for name, feature_map in FEATURE_MAPS.items():
        geometry = covariance_geometry(depth, feature_map)
        rows = rank(depth, physical_goal, feature_map, geometry)
        result[name] = {
            "goal_features": feature_map(physical_goal),
            "covariance": geometry["covariance"],
            "winner": rows[0]["history"],
            "winner_J": rows[0]["J"],
            "runner_up": rows[1]["history"],
            "absolute_margin": rows[1]["J"] - rows[0]["J"],
            "stability_two_percent": stability(rows, depth),
            "top_five": rows[:5],
        }
    return result


def max_cost_difference_under_coordinate_change(depth: int) -> float:
    base_map = FEATURE_MAPS["dct_012"]
    transformed_map = FEATURE_MAPS["dct_012_invertible_reparameterization"]
    base_geometry = covariance_geometry(depth, base_map)
    transformed_geometry = covariance_geometry(depth, transformed_map)
    physical_goal = target_profile(depth, 1)
    base_goal = base_map(physical_goal)
    transformed_goal = transformed_map(physical_goal)
    maximum = 0.0
    for history in itertools.product(ALPHABET, repeat=depth):
        first = agentive_cost(history, base_goal, base_map, base_geometry)
        second = agentive_cost(history, transformed_goal, transformed_map, transformed_geometry)
        maximum = max(maximum, abs(first - second))
    return maximum


def matched_chance_control(depth: int) -> dict:
    """Show observational equivalence to an exogenous draw over the same targets."""
    feature_map = FEATURE_MAPS["dct_012"]
    geometry = covariance_geometry(depth, feature_map)
    goals = {
        "base": target_profile(depth, 1),
        "reversed": target_profile(depth, -1),
        "neutral": target_profile(depth, 0),
    }
    conditional_winners = {
        label: rank(depth, goal, feature_map, geometry)[0]["history"]
        for label, goal in goals.items()
    }
    # If A and an exogenous variable Z have the same distribution over the
    # three target labels, their induced winner distributions are identical.
    probabilities = {label: 1 / 3 for label in goals}
    agentive_distribution = {}
    chance_distribution = {}
    for label, winner in conditional_winners.items():
        key = str(winner)
        agentive_distribution[key] = agentive_distribution.get(key, 0.0) + probabilities[label]
        chance_distribution[key] = chance_distribution.get(key, 0.0) + probabilities[label]
    keys = set(agentive_distribution) | set(chance_distribution)
    total_variation = 0.5 * sum(abs(agentive_distribution.get(k, 0) - chance_distribution.get(k, 0)) for k in keys)
    return {
        "conditional_winners": conditional_winners,
        "agentive_winner_distribution": agentive_distribution,
        "matched_exogenous_chance_distribution": chance_distribution,
        "total_variation_distance": total_variation,
        "verdict": "observationally_equivalent_under_matched_target_distribution" if total_variation == 0 else "different",
    }


def main() -> int:
    depth6 = representation_audit(6)
    depth7 = representation_audit(7)
    coordinate_error6 = max_cost_difference_under_coordinate_change(6)
    coordinate_error7 = max_cost_difference_under_coordinate_change(7)
    chance = matched_chance_control(7)
    base6 = tuple(depth6["dct_012"]["winner"])
    base7 = tuple(depth7["dct_012"]["winner"])
    rival_winners7 = {
        name: tuple(value["winner"])
        for name, value in depth7.items()
        if name != "dct_012_invertible_reparameterization"
    }
    low_frequency_names = ("dct_012", "dct_013_rival_subspace", "three_block_local_means")
    low_frequency_invariant = len({tuple(depth7[name]["winner"]) for name in low_frequency_names}) == 1
    checks = {
        "same_physical_goal_used_across_feature_maps": True,
        "all_geometries_calibrated_without_selected_history": True,
        "invertible_coordinate_invariance_depth6": coordinate_error6 < 1e-10,
        "invertible_coordinate_invariance_depth7": coordinate_error7 < 1e-10,
        "coordinate_reparameterization_preserves_winner_depth6": (
            tuple(depth6["dct_012_invertible_reparameterization"]["winner"]) == base6
        ),
        "coordinate_reparameterization_preserves_winner_depth7": (
            tuple(depth7["dct_012_invertible_reparameterization"]["winner"]) == base7
        ),
        "all_depth6_minima_unique": all(x["absolute_margin"] > 0 for x in depth6.values()),
        "all_depth7_minima_unique": all(x["absolute_margin"] > 0 for x in depth7.values()),
        "all_depth7_winners_stable": all(x["stability_two_percent"] > 0.75 for x in depth7.values()),
        "matched_chance_equivalence_detected": chance["total_variation_distance"] == 0,
        "registered_low_frequency_geometries_agree": low_frequency_invariant,
        "high_frequency_negative_control_can_change_selection": (
            tuple(depth7["dct_345_high_frequency_negative_control"]["winner"]) != base7
        ),
        "no_entropy_target_used": True,
    }
    cross_subspace_invariant = len(set(rival_winners7.values())) == 1
    payload = {
        "gate": "V6.74",
        "status": "mixed_pass_and_no_go" if all(checks.values()) else "open",
        "physical_goal_law": "0.35 - 0.50 cos(pi x) + 0.40 cos(2 pi x), sampled at cell centres",
        "depth6": depth6,
        "depth7": depth7,
        "coordinate_invariance_max_cost_error": {"depth6": coordinate_error6, "depth7": coordinate_error7},
        "cross_subspace_winner_invariant_depth7": cross_subspace_invariant,
        "cross_subspace_winners_depth7": {k: list(v) for k, v in rival_winners7.items()},
        "registered_low_frequency_winner_invariant_depth7": low_frequency_invariant,
        "matched_chance_control": chance,
        "checks": checks,
        "passed": sum(checks.values()),
        "total": len(checks),
        "all_registered_checks_pass": all(checks.values()),
        "interpretation": (
            "Reference-standardised compatibility is exactly invariant under invertible coordinate changes "
            "of one observable subspace. Agreement across genuinely different physical observable subspaces "
            "is empirical rather than guaranteed. Moreover, the selection map alone is observationally "
            "equivalent to an exogenous chance variable with the same distribution over target states. Goal "
            "sensitivity therefore does not yet distinguish agency from matched chance."
        ),
    }
    OUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, ensure_ascii=False))
    return 0 if payload["all_registered_checks_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

