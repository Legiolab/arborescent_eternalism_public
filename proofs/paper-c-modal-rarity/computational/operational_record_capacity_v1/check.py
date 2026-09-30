#!/usr/bin/env python3
"""Counterfactual recording capacity, resource accounting and MAP controls.

Shared device/preparation, every possible message, reversible classical maps.
Reuses the prior thermal kernel; no extra bath or entropy reward is introduced.
"""
import importlib.util
import itertools
import json
import math
from pathlib import Path

TOL=1e-10
spec=importlib.util.spec_from_file_location('reset_model',Path(__file__).resolve().parent.parent/'record_reset_thermodynamics_v1'/'check.py')
reset=importlib.util.module_from_spec(spec)
spec.loader.exec_module(reset)

def entropy(probs):
    return -sum(p*math.log(p) for p in probs if p>0)

def bit_devices(n):
    N=1<<n
    capable=[]
    test_cases=0
    for mask,memory in itertools.product(range(N),repeat=2):
        # Gate bit j is CNOT if mask_j=1, identity otherwise.
        outputs=[memory ^ (mask & source) for source in range(N)]
        test_cases+=N
        if outputs==list(range(N)):
            capable.append((mask,memory))
    assert capable==[(N-1,0)]
    return {'n':n,'devices_and_preparations_examined':N*N,
            'counterfactual_messages_checked':test_cases,
            'capable_devices':capable,'initial_memory_support':1,
            'memory_preparation_counting_fraction':1/N}

def arbitrary_reversible_devices():
    # M=one bit, E=one bit: all reversible maps preserving S.
    # For each of the two source inputs choose ANY permutation of (M,E).
    perms=list(itertools.permutations(range(4)))
    counts={}
    checked=0
    for p0,p1 in itertools.product(perms,repeat=2):
        good=[r for r in range(4) if p0[r]//2==0 and p1[r]//2==1]
        assert len(good)<=2  # environment dimension =2
        counts[len(good)]=counts.get(len(good),0)+1
        checked+=1
    assert checked==576 and max(counts)==2
    # Independent reversible implementation using a blank auxiliary E:
    # SWAP(M,E), then CNOT(S,M). Source unchanged; M becomes S, E saves old M.
    ancilla_results=[]
    for source in range(2):
        mapped=[]
        for memory,aux in itertools.product(range(2),repeat=2):
            out_m=aux ^ source
            out_e=memory
            mapped.append(2*out_m+out_e)
            if aux==0:
                assert out_m==source and out_e==memory
        assert len(set(mapped))==4
        ancilla_results.append(mapped)
    assert entropy([.5,.5,0,0])==math.log(2)
    return {'exhaustive_device_count':checked,'capable_preparation_support_histogram':counts,
            'max_allowed_joint_preparation_support':2,'total_joint_states':4,
            'blank_auxiliary_permutations_by_source':ancilla_results,
            'blank_auxiliary_control':{'memory_initial_entropy':math.log(2),
                'aux_initial_entropy':0,'joint_resource_entropy':math.log(2),
                'maximum_joint_resource_entropy':math.log(4),
                'resource_entropy_deficit':math.log(2),
                'ideal_heat':0,'joint_entropy_change':0}}

def approximate_capacity(n,delta,env_dimension):
    d=1<<n
    assert 0<=delta<=1-1/d
    # XOR copying, resource ensemble independent of input. Uniform auxiliary.
    # This distribution maximises preparation entropy at fixed whole-message error.
    memory=[1-delta]+[delta/(d-1)]*(d-1)
    resource=[p/env_dimension for p in memory for _ in range(env_dimension)]
    H=entropy(resource)
    bound=math.log(env_dimension)+reset.h(delta)+delta*math.log(d-1)
    deficit=math.log(d*env_dimension)-H
    assert abs(H-bound)<TOL
    assert deficit>=-TOL
    for source in range(d):
        fidelity=sum(memory[m] for m in range(d) if (m ^ source)==source)
        assert abs(fidelity-(1-delta))<TOL
    return {'n':n,'message_dimension':d,'whole_message_error':delta,
            'environment_dimension':env_dimension,'resource_entropy':H,
            'entropy_upper_bound':bound,'resource_entropy_deficit':deficit,
            'all_messages_checked':d,'fidelity_each_message':1-delta}

def capable_history_map(n,epsilon=5,alpha=.9,kappa=.2,beta=None):
    N=1<<n
    beta=n*kappa+1 if beta is None else beta
    q,K=reset.kernel(epsilon,alpha)
    best=math.inf
    winners=[]
    count=0
    reference_mass=0.0
    for mask,m,s,y in itertools.product(range(N),repeat=4):
        # Capacity is certified independently across all alternative inputs.
        capacity=int(all((m ^ (mask & source))==source for source in range(N)))
        copied=m ^ (mask & s)
        logw=-3*n*math.log(2)+sum(math.log(K[(copied>>j)&1][(y>>j)&1]) for j in range(n))
        reference_mass+=math.exp(logw)
        score=-logw+kappa*mask.bit_count()-beta*capacity
        if score<best-TOL:
            best=score;winners=[(mask,m,s,y)]
        elif abs(score-best)<=TOL:
            winners.append((mask,m,s,y))
        count+=1
    assert abs(reference_mass-1)<TOL
    capable=[(N-1,0,0,0)]
    incapable=[(0,0,s,0) for s in range(N)]
    expected=capable if beta>n*kappa+TOL else (incapable if beta<n*kappa-TOL else incapable+capable)
    assert set(winners)==set(expected)
    return {'n':n,'histories_examined':count,'beta':beta,'controller_cost_per_cnot':kappa,
            'threshold_beta':n*kappa,'winner_count':len(winners),
            'winners_mask_memory_source_reset':winners,
            'all_winners_capable':all(mask==N-1 and m==0 for mask,m,s,y in winners),
            'realised_source_entropy_uniform_tiebreak':math.log(len(set(s for mask,m,s,y in winners))),
            'all_register_histories_constant':all(m==(m^(mask&s))==y for mask,m,s,y in winners)}

def conditional_thermal_operation(p_source,epsilon=5,alpha=.9):
    q,K=reset.kernel(epsilon,alpha)
    source=[1-p_source,p_source]
    # A distribution of actual messages is a SEPARATE input assumption.
    # Capability fixes preparation, but does not select this source distribution.
    initial=[source[0],0,0,source[1]]
    final=[source[s]*K[s][y] for s in range(2) for y in range(2)]
    final_m=[sum(final[2*s+y] for s in range(2)) for y in range(2)]
    delta=entropy(final)-entropy(initial)
    heat=epsilon*(final_m[1]-p_source)
    sigma=delta-heat
    stationary=[source[s]*q[y] for s in range(2) for y in range(2)]
    def kl(rho):
        return sum(r*math.log(r/pi) for r,pi in zip(rho,stationary) if r>0)
    assert abs(sigma-(kl(initial)-kl(final)))<TOL
    assert sigma>=-TOL
    # Propagate causal preparation independently and compare joint probabilities.
    causal=[0.0]*4
    for s in range(2):
        memory=0
        copied=memory ^ s
        for y in range(2):
            causal[2*s+y]+=source[s]*K[copied][y]
    assert causal==final
    return {'source_probability_one':p_source,'epsilon':epsilon,'alpha':alpha,
            'source_entropy':entropy(source),'sigma_joint_mean':sigma,
            'heat_to_memory':heat,'work_on_memory':-heat,
            'delta_joint_entropy':delta,'causal_and_global_conditional_law_equal':True}

if __name__=='__main__':
    result={'model':'operational_record_capacity_v1',
            'capacity_scope':'same device and preparation for all counterfactual classical messages',
            'bit_devices':[bit_devices(n) for n in [1,2,4,6]],
            'arbitrary_reversible_devices':arbitrary_reversible_devices(),
            'approximate_resource_bounds':[approximate_capacity(n,delta,e)
                for n in [1,2,4,6] for delta in [0,.01,.05,.1] for e in [1,4]],
            'history_MAP_with_capacity_reward':[capable_history_map(n,beta=b) for n in [1,2,3] for b in [n*.2-.01,n*.2,n*.2+.01]],
            'conditional_thermal_operations':[conditional_thermal_operation(p)
                for p in [.1,.5,.9]],
            'conclusion':'capacity constrains preparation resources; history MAP still chooses a trivial realised message; no AE-specific arrow'}
    print(json.dumps(result,indent=2))
