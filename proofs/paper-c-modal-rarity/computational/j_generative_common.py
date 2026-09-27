#!/usr/bin/env python3
"""V6.72: generate w, physical energy and agentive cost from one history code."""

from __future__ import annotations

import itertools
import json
import math
import random
from pathlib import Path


OUT = Path(__file__).with_name("results.json")
ALPHABET = (-1, 0, 1)
GOAL = (0.35, -0.25, 0.20)
AGENTIVE_SIGMA = 0.25
SEED = 20260927


def branch_probabilities(index: int) -> dict[int, float]:
    """One analytic branching law, reused at every tested depth."""
    bias = 0.08 * math.sin((index + 1) * math.pi * (math.sqrt(5) - 1))
    return {-1: 0.25 - bias, 0: 0.50, 1: 0.25 + bias}


def weight(history: tuple[int, ...]) -> float:
    result = 1.0
    for index, symbol in enumerate(history):
        result *= branch_probabilities(index)[symbol]
    return result


def physical_profile(history: tuple[int, ...]) -> dict:
    """Fixed Pi plus a positive discrete Hessian normal form."""
    n = len(history)
    mean = sum(history) / n
    gradients = tuple(history[i + 1] - history[i] for i in range(n - 1))
    curvature = tuple(history[i + 2] - 2 * history[i + 1] + history[i] for i in range(n - 2))
    energy = 0.5 * (
        mean * mean
        + sum(value * value for value in gradients) / max(1, n - 1)
        + 0.25 * sum(value * value for value in curvature) / max(1, n - 2)
    )
    return {"mean": mean, "gradients": gradients, "curvature": curvature, "energy": energy}


def agentive_features(history: tuple[int, ...]) -> tuple[float, float, float]:
    n = len(history)
    midpoint = n // 2
    global_mean = sum(history) / n
    alternating = sum((1 if i % 2 == 0 else -1) * value for i, value in enumerate(history)) / n
    early = sum(history[:midpoint]) / max(1, midpoint)
    late = sum(history[midpoint:]) / max(1, n - midpoint)
    return global_mean, alternating, late - early


def agentive_cost(history: tuple[int, ...], goal=GOAL) -> float:
    features = agentive_features(history)
    # Negative log-likelihood up to a history-independent normalizing constant.
    # The scale is internal to the fixed agentive observation model, not a
    # coefficient fitted in the master score.
    return 0.5 * sum(
        ((value - target) / AGENTIVE_SIGMA) ** 2
        for value, target in zip(features, goal)
    )


def evaluate(history: tuple[int, ...], goal=GOAL) -> dict:
    w = weight(history)
    physical = physical_profile(history)
    cost = agentive_cost(history, goal)
    surprisal = -math.log(w)
    return {
        "history": history,
        "weight": w,
        "surprisal": surprisal,
        "physical_energy": physical["energy"],
        "agentive_features": agentive_features(history),
        "agentive_cost": cost,
        "J": surprisal + physical["energy"] + cost,
    }


def enumerate_family(depth: int, goal=GOAL):
    rows = [evaluate(history, goal) for history in itertools.product(ALPHABET, repeat=depth)]
    rows.sort(key=lambda row: (row["J"], row["history"]))
    return rows


def summarize(depth: int, goal=GOAL) -> dict:
    rows = enumerate_family(depth, goal)
    winner = rows[0]
    runner_up = rows[1]
    physical_energies = sorted(row["physical_energy"] for row in rows)
    median_energy = physical_energies[len(physical_energies) // 2]
    return {
        "depth": depth,
        "history_count": len(rows),
        "winner": winner,
        "runner_up": runner_up,
        "absolute_margin": runner_up["J"] - winner["J"],
        "relative_margin": (runner_up["J"] - winner["J"]) / winner["J"],
        "winner_energy_below_family_median": winner["physical_energy"] < median_energy,
        "family_median_physical_energy": median_energy,
        "top_five": rows[:5],
    }


def counterfactual_agency(depth: int):
    goals = {
        "base": GOAL,
        "reversed": tuple(-value for value in GOAL),
        "neutral": (0.0, 0.0, 0.0),
    }
    result = {}
    for name, goal in goals.items():
        rows = enumerate_family(depth, goal)
        result[name] = {
            "goal": goal,
            "winner": rows[0]["history"],
            "winner_weight": rows[0]["weight"],
            "winner_physical_energy": rows[0]["physical_energy"],
            "winner_agentive_cost": rows[0]["agentive_cost"],
        }
    return result


def perturbation_stability(depth: int, trials: int = 2000, fraction: float = 0.02):
    rows = enumerate_family(depth)
    base = rows[0]["history"]
    rng = random.Random(SEED + depth)
    stable = 0
    for _ in range(trials):
        scored = []
        for row in rows:
            values = (row["surprisal"], row["physical_energy"], row["agentive_cost"])
            score = sum(value * rng.uniform(1 - fraction, 1 + fraction) for value in values)
            scored.append((score, row["history"]))
        stable += min(scored)[1] == base
    return {"trials": trials, "fraction": fraction, "base_winner_stability": stable / trials}


def main() -> int:
    depth6 = summarize(6)
    depth7 = summarize(7)
    agency = counterfactual_agency(7)
    stability6 = perturbation_stability(6)
    stability7 = perturbation_stability(7)
    checks = {
        "depth6_enumeration_complete": depth6["history_count"] == 3**6,
        "depth7_enumeration_complete": depth7["history_count"] == 3**7,
        "branch_probabilities_normalize": all(abs(sum(branch_probabilities(i).values()) - 1) < 1e-12 for i in range(7)),
        "all_branch_probabilities_positive": all(min(branch_probabilities(i).values()) > 0 for i in range(7)),
        "unique_depth6_winner": depth6["absolute_margin"] > 0,
        "unique_depth7_winner": depth7["absolute_margin"] > 0,
        "depth6_winner_is_low_energy_relative_to_family": depth6["winner_energy_below_family_median"],
        "depth7_winner_is_low_energy_relative_to_family": depth7["winner_energy_below_family_median"],
        "agency_changes_selection_without_reweighting": len({tuple(item["winner"]) for item in agency.values()}) >= 2,
        "depth6_stable_under_two_percent_perturbation": stability6["base_winner_stability"] > 0.75,
        "depth7_stable_under_two_percent_perturbation": stability7["base_winner_stability"] > 0.75,
    }
    design_declarations = {
        "no_history_table_used": True,
        "no_free_lambda_coefficients": True,
        "no_entropy_target_used": True,
    }
    payload = {
        "gate": "V6.72",
        "status": "accepted_with_scope" if all(checks.values()) else "open",
        "formula": "J(H)=-log w_E(H)+B_E,Pi(H)+C_A(H)",
        "generative_architecture": {
            "E": "complete ternary history tree",
            "w": "product of one analytic depth-indexed branch law",
            "Pi_and_B": "mean/gradient/curvature profile with one positive quadratic energy",
            "A": "fixed goal in three coarse history observables",
        },
        "goal": GOAL,
        "agentive_sigma": AGENTIVE_SIGMA,
        "depth6": depth6,
        "depth7_held_out": depth7,
        "counterfactual_agency_depth7": agency,
        "stability_depth6": stability6,
        "stability_depth7": stability7,
        "checks": checks,
        "design_declarations": design_declarations,
        "passed": sum(checks.values()),
        "total": len(checks),
        "all_checks_pass": all(checks.values()),
        "interpretation": (
            "One generative history code now produces reference weight, physical profile and agentive compatibility. "
            "The fixed coefficient-free J has unique stable minima at two depths, and counterfactual goals change "
            "selection while leaving w and the physical law untouched. This is a toy closure, not a derivation "
            "of the cosmological branch law, Pi or agency."
        ),
    }
    OUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, ensure_ascii=False))
    return 0 if payload["all_checks_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
