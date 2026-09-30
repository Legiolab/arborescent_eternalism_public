#!/usr/bin/env python3
"""Exhaustive falsification test: reliable nondemolition records without entropy rewards.

All initial source/memory pairs are allowed; every history has uniform reference
weight 2**(-2*n). The fixed schedule applies one reversible CNOT per bit.
The late score is 1 iff final memory equals the original, unchanged source.
No entropy, Hamming weight, low-state target, or trajectory order enters the score.
Outputs logical/coarse-grained entropies only, not heat or cosmological claims.
"""
import json
import math
from collections import Counter
from itertools import product

TOL = 1e-12

def entropy(counter):
    total = sum(counter.values())
    return -sum((c / total) * math.log(c / total) for c in counter.values())

def trajectory(n, source, memory):
    states = [(source, memory)]
    for j in range(n):
        memory ^= source & (1 << j)
        states.append((source, memory))
    return states

def sb(n, state, partition):
    s, m = state
    if partition == 'separate_register_counts':
        return math.log(math.comb(n, s.bit_count()) * math.comb(n, m.bit_count()))
    return math.log(math.comb(2*n, s.bit_count() + m.bit_count()))

def direction(delta):
    return 'increase' if delta > TOL else 'decrease' if delta < -TOL else 'equal'

def run(n):
    size = 1 << n
    all_pairs = list(product(range(size), repeat=2))
    winners = []
    # Independent check over ALL allowed preparations: positive beta selects A=1.
    beta = 1.0
    scores = [2*n*math.log(2) - beta * int((m ^ s) == s) for s,m in all_pairs]
    best = min(scores)
    for pair, score in zip(all_pairs, scores):
        if abs(score-best) <= TOL:
            winners.append(pair)
    assert winners == [(s,0) for s in range(size)]
    assert len(set((s,m ^ s) for s,m in all_pairs)) == len(all_pairs)
    # Each CNOT is its own inverse, and reversing the schedule undoes the history.
    for s,m in all_pairs:
        out = trajectory(n,s,m)[-1][1]
        for j in reversed(range(n)):
            out ^= s & (1 << j)
        assert out == m
    traces = [trajectory(n,s,m) for s,m in winners]
    shannon = []
    for t in range(n+1):
        joint = Counter(tr[t] for tr in traces)
        sources = Counter(s for s,m in joint.elements())
        memories = Counter(m for s,m in joint.elements())
        hj, hs, hm = entropy(joint), entropy(sources), entropy(memories)
        shannon.append({'t':t, 'joint':hj, 'source':hs, 'memory':hm,
                        'mutual_information':hs+hm-hj,
                        'sum_marginals_minus_joint':hs+hm-hj})
        assert abs(hj - n*math.log(2)) < TOL
        assert abs(hm - t*math.log(2)) < TOL
    coarse = {}
    for partition in ['separate_register_counts','total_count']:
        end_counts = Counter()
        monotone = 0
        examples = {}
        for s,m in winners:
            values = [sb(n,state,partition) for state in trajectory(n,s,m)]
            tag = direction(values[-1]-values[0])
            end_counts[tag] += 1
            monotone += int(all(b >= a-TOL for a,b in zip(values,values[1:])))
            examples.setdefault(tag, {'source':format(s,f'0{n}b'), 'trace':values})
        coarse[partition] = {'end_counts':dict(end_counts),
                            'nondecreasing_entire_path':monotone,
                            'examples':examples}
    # Controls: no reward -> every preparation; identity -> pre-existing correlations;
    # SWAP -> every preparation records the source but overwrites the source.
    identity = [(s,m) for s,m in all_pairs if m == s]
    swap = [(s,m) for s,m in all_pairs if (m,s)[1] == s]
    assert len(identity)==size and len(swap)==size*size
    assert len([1 for s,m in swap if m==s])==size  # nondemolition subset
    # Above threshold for source bit-count partition is unrelated to the late score.
    examples = {
        'all_zero_source': trajectory(n,0,0),
        'all_one_source': trajectory(n,size-1,0),
    }
    return {'n':n, 'histories_enumerated':len(all_pairs), 'winner_count':len(winners),
            'reference_measure_of_winner_preparations':len(winners)/len(all_pairs),
            'initial_joint_shannon':shannon[0]['joint'],
            'final_joint_shannon':shannon[-1]['joint'],
            'maximum_joint_shannon':2*n*math.log(2),
            'initial_memory_shannon':shannon[0]['memory'],
            'final_memory_shannon':shannon[-1]['memory'],
            'shannon_trace':shannon, 'boltzmann_partitions':coarse,
            'controls':{'no_objective_winners':len(all_pairs),
                        'identity_reliable_preexisting_records':len(identity),
                        'swap_reliable_records':len(swap),
                        'swap_reliable_and_source_preserved':size},
            'counterexample_histories':examples}

if __name__ == '__main__':
    print(json.dumps({'model':'reliable_record_v1',
                     'status':'negative_for_universal_entropy_arrow',
                     'scope':'finite logical reversible register model; no heat bath',
                     'runs':[run(n) for n in [2,4,6,8]]},indent=2))
