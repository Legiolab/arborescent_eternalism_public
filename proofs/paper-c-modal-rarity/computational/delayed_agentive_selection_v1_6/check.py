"""Exact finite witness for Paper C v1.6, section 9.6.

Run: python delayed_agentive_selection_v1_6.py
Uses only the Python standard library and writes no files.
"""

from fractions import Fraction as F
from itertools import product
from math import log


MU = (F(1, 100), F(9, 100), F(90, 100))
K = (
    (F(9, 10), F(1, 10), F(0)),
    (F(1, 20), F(9, 10), F(1, 20)),
    (F(0), F(1, 10), F(9, 10)),
)
MEMORY_STRENGTH = (F(1), F(1, 20), F(0))


def weight(history):
    """Reference weight fixed before any agentive score is evaluated."""
    x0, x1, x2, x3 = history
    return MU[x0] * K[x0][x1] * K[x1][x2] * K[x2][x3]


def score(history, *, memory=True):
    """A is zero until the final transition, when an agent may act."""
    if history[2:] != (1, 2):
        return F(0)
    return MEMORY_STRENGTH[history[0]] if memory else F(1)


HISTORIES = tuple((h, weight(h)) for h in product(range(3), repeat=4) if weight(h))


def winners(beta, *, memory=True):
    # C_A(H)=beta*(1-score(H)) is non-negative. Subtracting its constant
    # beta leaves the same minimisers as -log(w(H))-beta*score(H).
    costs = [(float(-log(float(w)) - beta * score(h, memory=memory)), h)
             for h, w in HISTORIES]
    minimum = min(c for c, _ in costs)
    return tuple(h for c, h in costs if abs(c - minimum) < 1e-12)


def main():
    assert len(HISTORIES) == 41
    w = dict(HISTORIES)
    assert w[(2, 2, 2, 2)] == F(6561, 10000)
    assert w[(0, 0, 1, 2)] == w[(0, 1, 1, 2)] == F(45, 1_000_000)
    ratio = w[(2, 2, 2, 2)] / w[(0, 0, 1, 2)]
    assert ratio == 14580
    threshold = log(14580)
    assert winners(0) == ((2, 2, 2, 2),)
    assert winners(threshold - 0.01) == ((2, 2, 2, 2),)
    assert set(winners(10)) == {(0, 0, 1, 2), (0, 1, 1, 2)}

    # Exact tie with 2222 at beta=log(14580); floating point is not the
    # source of the equality. Exhaustion below rules out any other contender.
    assert w[(2, 2, 2, 2)] / w[(0, 0, 1, 2)] == 14580
    assert set(winners(threshold)) == {
        (2, 2, 2, 2), (0, 0, 1, 2), (0, 1, 1, 2)
    }

    # With a goal depending only on the same final act (no trajectory memory),
    # the maximum-weight scored paths begin in the common preparation state 2.
    scored = [(w, h) for h, w in HISTORIES if score(h, memory=False)]
    best_scored_weight = max(w for w, _ in scored)
    best_scored = {h for w, h in scored if w == best_scored_weight}
    assert best_scored_weight == F(405, 100_000)
    assert best_scored == {(2, 1, 1, 2), (2, 2, 1, 2)}
    assert set(winners(10, memory=False)) == best_scored

    print('admissible_histories: 41')
    print('baseline_winner: 2222; weight: 0.6561')
    print('rare_winners_above_threshold: 0012, 0112; each weight: 0.000045')
    print(f'exact_weight_ratio: {ratio}; beta_threshold: log(14580) = {threshold:.10f}')
    print('at_threshold: 2222, 0012, 0112 tie')
    print('without_trajectory_memory_at_beta_10: 2112, 2212')
    print('scope: finite conditional witness; no cosmological or pathwise theorem')


if __name__ == '__main__':
    main()
