#!/usr/bin/env python3
"""Exact bath bookkeeping and global-versus-causal record/reset controls.

Units k_B=T=1. Ideal driven bit Hamiltonian E_M=epsilon*M, with
an equilibrium reservoir and an external work source. Not an autonomous device.
"""
import itertools
import json
import math

TOL=1e-10

def h(p):
    return -sum(x*math.log(x) for x in [p,1-p] if x>0)

def H(p):
    return -sum(x*math.log(x) for x in p if x>0)

def kernel(epsilon,alpha):
    q1=1/(1+math.exp(epsilon))
    q=[1-q1,q1]
    K=[[ (1-alpha)*int(x==y)+alpha*q[y] for y in [0,1]] for x in [0,1]]
    assert all(abs(sum(row)-1)<TOL for row in K)
    assert abs(q[0]*K[0][1]-q[1]*K[1][0])<TOL
    assert abs(math.log(K[0][1]/K[1][0])+epsilon)<TOL
    return q,K

def bath_test(epsilon,alpha):
    q,K=kernel(epsilon,alpha)
    # Diagnostic ensemble: unbiased source, selected blank memory, then exact copy.
    # This is the same physical ensemble for both descriptions, not MAP by fiat.
    final_joint=[.5*K[s][y] for s in [0,1] for y in [0,1]]
    p1=.5*(K[0][1]+K[1][1])
    delta_joint=H(final_joint)-math.log(2)
    delta_mem=h(p1)-math.log(2)
    heat_to_memory=epsilon*(p1-.5)
    work_on_device=epsilon*(.5-p1) # quench up, thermal step, quench down
    bath_entropy=-heat_to_memory
    total=delta_joint+bath_entropy
    marginal=delta_mem+bath_entropy
    mutual_initial=math.log(2)
    mutual_final=math.log(2)+h(p1)-H(final_joint)
    assert abs(work_on_device+heat_to_memory)<TOL
    assert total>=-TOL and marginal>=-TOL
    stationary=[.5*q[y] for source in [0,1] for y in [0,1]]
    initial_joint=[.5,0,0,.5]
    def kl(rho):
        return sum(r*math.log(r/pi) for r,pi in zip(rho,stationary) if r>0)
    assert abs(total-(kl(initial_joint)-kl(final_joint)))<TOL
    assert abs(total-marginal-(mutual_initial-mutual_final))<TOL
    # Ensemble average equals the stochastic joint entropy production over paths.
    stochastic=[]
    for s,y in itertools.product([0,1],repeat=2):
        prob=.5*K[s][y]
        sigma=math.log(.5/prob)+epsilon*(s-y)
        stochastic.append({'s':s,'y':y,'probability':prob,'sigma_joint':sigma})
    assert abs(sum(x['probability']*x['sigma_joint'] for x in stochastic)-total)<TOL
    # Causal preparation-and-copy has exactly this joint law, heat, and work.
    causal_joint=[0.0]*4
    for source,initial_memory in itertools.product([0,1],repeat=2):
        initial_probability=.5 if initial_memory==0 else 0.0
        copied_memory=source ^ initial_memory
        for final_memory in [0,1]:
            causal_joint[2*source+final_memory] += initial_probability*K[copied_memory][final_memory]
    assert final_joint==causal_joint
    # Gibbs equilibrium without copy/driving: individual total sigma is zero.
    for x,y in itertools.product([0,1],repeat=2):
        assert abs(math.log(q[x]/q[y])+epsilon*(x-y))<TOL
    # Reset WITHOUT a record, from unbiased independent memory, permits negative
    # individual sigma even though mean sigma is nonnegative (trajectory != mean).
    independent=[]
    for x,y in itertools.product([0,1],repeat=2):
        sigma=math.log(.5/([1-p1,p1][y]))+epsilon*(x-y)
        independent.append({'x':x,'y':y,'probability':.5*K[x][y], 'sigma':sigma})
    assert abs(sum(z['probability']*z['sigma'] for z in independent)-marginal)<TOL
    return {'epsilon':epsilon,'alpha':alpha,'q1':q[1], 'K':K,
            'reset_error_per_bit':p1, 'delta_joint_entropy':delta_joint,
            'delta_memory_entropy':delta_mem,'heat_to_memory':heat_to_memory,
            'bath_entropy_change':bath_entropy,'work_on_device':work_on_device,
            'sigma_joint_mean':total,'sigma_memory_plus_bath_mean':marginal,
            'mutual_information_lost':mutual_initial-mutual_final,
            'record_reset_paths':stochastic,'independent_reset_paths':independent,
            'causal_and_global_conditional_ensembles_equal':True}

def map_test(n,epsilon=5,alpha=.9,beta=1):
    q,K=kernel(epsilon,alpha)
    size=1<<n
    best=math.inf
    winners=[]
    count=0
    reference_mass=0.0
    for s,m,y in itertools.product(range(size),repeat=3):
        copied=m ^ s
        record=int(copied==s)
        logw=-2*n*math.log(2)+sum(math.log(K[(copied>>j)&1][(y>>j)&1]) for j in range(n))
        reference_mass += math.exp(logw)
        score=-logw-beta*record
        if score<best-TOL:
            best=score;winners=[(s,m,y)]
        elif abs(score-best)<=TOL:
            winners.append((s,m,y))
        count+=1
    assert abs(reference_mass-1)<TOL
    if alpha<1 and epsilon>0 and beta>0:
        assert winners==[(0,0,0)]
    if alpha==1 and beta>0:
        assert winners==[(s,0,0) for s in range(size)]
    if alpha<1 and epsilon>0 and beta==0:
        assert winners==[(s,s,0) for s in range(size)]
    return {'n':n,'epsilon':epsilon,'alpha':alpha,'beta':beta,
            'histories_enumerated':count,'winner_count':len(winners),
            'winners':winners,'minimum_score':best,
            'winner_source_entropy_uniform_tiebreak': math.log(len(set(s for s,m,y in winners)))}

if __name__=='__main__':
    bath=[bath_test(e,a) for e in [0,1,3,5,8] for a in [.1,.5,.9,1]]
    maps=[map_test(n) for n in [1,2,4,6]]
    maps += [map_test(4,alpha=1),map_test(4,beta=0)]
    # Reversible uncopy control: source still available -> blank memory, no bath.
    for s in range(64):
        memory=s
        memory ^= s
        assert memory==0
    print(json.dumps({'model':'record_reset_thermodynamics_v1',
        'scope':'ideal reservoir, driven Hamiltonian, external work source; no controller cost',
        'bath_sweep':bath,'global_history_MAP':maps,
        'uncopy_control':{'n':6,'sources_checked':64,'heat':0,'work_ideal':0,
                          'joint_entropy_change':0,'memory_final':'blank'},
        'causal_discrimination':'none for matched preparation and protocol'},indent=2))
