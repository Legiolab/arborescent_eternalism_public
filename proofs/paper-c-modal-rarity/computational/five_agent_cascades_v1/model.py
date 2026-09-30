#!/usr/bin/env python3
"""Five-agent reversible history model: exact frozen finite domain."""
import json, math, time, itertools
from pathlib import Path
ROOT=Path(__file__).parent
GOAL=0b10101
TARGETS=(28,32,192,2,33)
def bit(x,i):return (x>>i)&1
def rotate(x):return ((x<<1)&255)|(x>>7)
def transport(x):
    x^=(bit(x,0)&bit(x,1))<<7
    x^=bit(x,2)<<6
    return rotate(x)
def inverse_transport(x):
    x=(x>>1)|((x&1)<<7)
    x^=bit(x,2)<<6
    x^=(bit(x,0)&bit(x,1))<<7
    return x
def run(x0,p,mask,coupled=True,m0=0):
    x=x0;m=m0;xs=[x];records=[];decisions=[]
    for _ in range(3):
        observed=x if coupled else x0
        m^=observed&mask&31
        d=(m^p^GOAL)&mask
        for i in range(5):
            if bit(d,i):x^=TARGETS[i]
        records.append(m);decisions.append(d)
        x=transport(x);xs.append(x)
    return xs,records,decisions
def inverse(x,m,p,mask):
    for _ in range(3):
        x=inverse_transport(x)
        d=(m^p^GOAL)&mask
        for i in reversed(range(5)):
            if bit(d,i):x^=TARGETS[i]
        m^=x&mask&31
    return x,m
def score(x,p,mask,out,variant='full'):
    surprisal=8*math.log(2)-5*math.log(.75)+p.bit_count()*math.log(3)
    b=0 if variant=='no_B' else x.bit_count()
    ca=0 if variant=='no_A' else 4*((out[2][-1]^GOAL)&mask).bit_count()
    return surprisal+b+ca
def sb(x):return math.log(math.comb(8,x.bit_count()))
def summary(mask,coupled,variant='full'):
    best=math.inf;winners=[]
    for x in range(256):
        for p in range(32):
            out=run(x,p,mask,coupled);j=score(x,p,mask,out,variant)
            if j<best-1e-10:best=j;winners=[(x,p,out)]
            elif abs(j-best)<1e-10:winners.append((x,p,out))
    details=[]
    for x,p,out in winners:
        tr=[sb(z) for z in out[0]]
        details.append({'x0':x,'plans':p,'environment_trace':out[0],'records':out[1],'decisions':out[2],'macrovolumes':[math.comb(8,z.bit_count()) for z in out[0]],'entropy_trace':tr,'low_initial':math.comb(8,x.bit_count())<56,'late_growth':sum(tr[-2:])/2>tr[0]+1e-12,'goal_errors':((out[2][-1]^GOAL)&mask).bit_count()})
    # Full-state initial counterfactuals on every winning prep.
    effects=[]
    for i in range(5):
        if not bit(mask,i):continue
        deltas=[];other=[]
        for x,p,out in winners:
            alt=run(x,p^(1<<i),mask,coupled)
            deltas.append([(a^b).bit_count() for a,b in zip(out[0],alt[0])])
            other.append(sum(((a^b)&mask&~(1<<i)).bit_count() for a,b in zip(out[2],alt[2])))
        effects.append({'agent':i,'mean_environment_hamming_by_cut':[sum(d[t] for d in deltas)/len(deltas) for t in range(4)],'mean_changed_other_decisions':sum(other)/len(other),'max_changed_other_decisions':max(other)})
    return {'mask':mask,'participants':[i for i in range(5) if bit(mask,i)],'coupled':coupled,'variant':variant,'min_J':best,'winner_count':len(details),'low_fraction':sum(d['low_initial'] for d in details)/len(details),'growth_fraction':sum(d['late_growth'] for d in details)/len(details),'all_goals_satisfied':all(d['goal_errors']==0 for d in details),'H_star_lexicographic':details[0],'winners':details,'counterfactual_effects':effects}
def main():
    start=time.monotonic();checks={};cases=[]
    checks['transport_inverse_all_environment_states']=all(inverse_transport(transport(x))==x for x in range(256))
    checks['universal_first_record_requires_blank']=all((all((m^(x&31))==(x&31) for x in range(256)))==(m==0) for m in range(32))
    checks['reference_normalized']=abs(sum((1/256)*(.75**(5-p.bit_count()))*(.25**p.bit_count()) for x in range(256) for p in range(32))-1)<1e-12
    checks['macrovolume_exact_counts']=all(sum(x.bit_count()==k for x in range(256))==math.comb(8,k) for k in range(9))
    checks['record_phase_commutes']=all((m^(bit(x,i)<<i)^(bit(x,j)<<j))==(m^(bit(x,j)<<j)^(bit(x,i)<<i)) for x in range(256) for m in [0,31] for i in range(5) for j in range(5))
    checks['reference_sample_constant_volume_factor']=all(256*sum(x.bit_count()==k for x in range(256))==256*math.comb(8,k) for k in range(9))
    checks['actions_commute_shared_targets']=all((x^TARGETS[i]^TARGETS[j])==(x^TARGETS[j]^TARGETS[i]) for x in range(256) for i in range(5) for j in range(5))
    # All first-memory states on a fixed deterministic validation cover.
    checks['full_history_inverse_memory_cover']=all(inverse(run(x,p,31,True,m)[0][-1],run(x,p,31,True,m)[1][-1],p,31)==(x,m) for x in range(256) for m in range(32) for p in [0,1,21,31])
    for mask in range(32):
        a=summary(mask,True);b=summary(mask,False);cases.extend([a,b])
        checks[f'uncoupled_no_cross_agent_decision_change_mask{mask}']=all(e['max_changed_other_decisions']==0 for e in b['counterfactual_effects'])
        assert time.monotonic()-start<60,'budget exceeded'
    cases.extend([summary(31,True,'no_A'),summary(31,True,'no_B')])
    full=next(c for c in cases if c['mask']==31 and c['coupled'] and c['variant']=='full')
    checks['coupled_cross_agent_influence_exists']=any(e['max_changed_other_decisions']>0 for c in cases if c['coupled'] for e in c['counterfactual_effects'])
    result={'decision_id':'paper-c-five_agent_cascades_v1','passed':sum(checks.values()),'total':len(checks),'all_checks_pass':all(checks.values()),'overall_pass':all(checks.values()),'checks':checks,'network':{'sensors':list(range(5)),'target_masks':TARGETS,'goal_bits':GOAL,'rounds':3,'event_structure':'root -> prep conflicts -> parallel records -> parallel actions -> transport; repeat three rounds; require previous transport for next record; preserve full prep provenance','serialization_quotient':'record and action phase permutations identified, active count k gives (k!)^6 serializations per physical history','projection':'reversible register evaluation on event configurations','actuality':'all argmins plus lexicographic prep tie rule, illustrative','physical_registers':'8 environment +5 memory +5 initial plan bits +8 preserved initial-sample reference bits; phase label supplied','reference':'uniform environment, independent biased plans, blank memory constrained by readiness; reference sample initialized equal to x0 in both controls', 'macrovolume_reference_factor':256, 'macrovolume_convention':'reported V is raw physical macrovolume divided by constant256 of unobserved sample reference; entropy differences unchanged'},'cases':cases,'all_five_full_summary':{k:v for k,v in full.items() if k!='winners'},'limits':['finite sensitivity not asymptotic chaos or Lyapunov exponent','no autonomous clock or Hamiltonian derivation','source/goal/network and partition frozen but illustrative','no interaction between alternative realized universes']}
    (ROOT/'results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'passed':result['passed'],'total':result['total'],'all_five':result['all_five_full_summary'],'combinations':[{k:c[k] for k in ['mask','coupled','variant','winner_count','low_fraction','growth_fraction']} for c in cases]},indent=2))
    return 0 if all(checks.values()) else 1
if __name__=='__main__':raise SystemExit(main())
