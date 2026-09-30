#!/usr/bin/env python3
"""Weighted pathwise macroentropy before global selection; source model unchanged."""
import importlib.util,json,math,time,hashlib
from pathlib import Path
ROOT=Path(__file__).parent
SOURCE=ROOT.parent/'five_agent_cascades_v1'/'model.py'
spec=importlib.util.spec_from_file_location('five_agents',SOURCE)
model=importlib.util.module_from_spec(spec);spec.loader.exec_module(model)
S=[math.log(math.comb(8,x.bit_count())) for x in range(256)]
def main():
    start=time.monotonic();rows=[];checks={}
    for mask in range(32):
        for low in [False,True]:
            xs=[x for x in range(256) if not low or x.bit_count()<=1]
            summaries=[]
            for coupled in [False,True]:
                mass=0;signs=[0,0,0];sums=[0.0]*4
                for x in xs:
                    for p in range(32):
                        wt=3**(5-p.bit_count())
                        path=model.run(x,p,mask,coupled)[0]
                        gains=[S[y]-S[x] for y in path]
                        volume_difference=math.comb(8,path[2].bit_count())*math.comb(8,path[3].bit_count())-math.comb(8,x.bit_count())**2
                        signs[0 if volume_difference>0 else 1 if volume_difference<0 else 2]+=wt
                        for t in range(4):sums[t]+=wt*gains[t]
                        mass+=wt
                checks[f'normalized_mask{mask}_low{low}_coupled{coupled}']=mass==len(xs)*1024 and sum(signs)==mass
                checks[f'initial_gain_zero_mask{mask}_low{low}_coupled{coupled}']=sums[0]==0
                summaries.append({'coupled':coupled,'mean_entropy_gain_by_cut':[v/mass for v in sums],'late_mean_entropy_gain':(sums[2]+sums[3])/(2*mass),'positive_probability':signs[0]/mass,'negative_probability':signs[1]/mass,'zero_probability':signs[2]/mass})
            a,b=summaries
            rows.append({'mask':mask,'active_agents':mask.bit_count(),'preparation':'low_K<=1' if low else 'all_environment_states','environment_state_count':len(xs),'histories_evaluated_each_variant':len(xs)*32,'summaries':summaries,'coupling_effect_on_mean':b['late_mean_entropy_gain']-a['late_mean_entropy_gain'],'coupling_effect_on_positive_probability':b['positive_probability']-a['positive_probability']})
        assert time.monotonic()-start<60,'budget exceeded'
    checks['paired_first_cycle_identical']=all(r['summaries'][0]['mean_entropy_gain_by_cut'][1]==r['summaries'][1]['mean_entropy_gain_by_cut'][1] for r in rows)
    checks['uniform_no_agents_stationary_macro_mean']=all(abs(v)<1e-12 for r in rows if r['mask']==0 and r['preparation']=='all_environment_states' for q in r['summaries'] for v in q['mean_entropy_gain_by_cut'])
    result={'decision_id':'paper-c-cascade_entropy_before_selection_v1','source_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),'passed':sum(checks.values()),'total':len(checks),'all_checks_pass':all(checks.values()),'overall_pass':all(checks.values()),'checks':checks,'rows':rows,'interpretation':'reference-weighted Boltzmann gains across individual histories, no J selection or ontic law'}
    (ROOT/'results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'passed':result['passed'],'total':result['total'],'full_participation':[r for r in rows if r['mask']==31],'aggregate':{prep:{'positive_mean_masks':sum(r['summaries'][1]['late_mean_entropy_gain']>1e-12 for r in rows if r['preparation']==prep),'positive_coupling_effect_masks':sum(r['coupling_effect_on_mean']>1e-12 for r in rows if r['preparation']==prep),'negative_coupling_effect_masks':sum(r['coupling_effect_on_mean']< -1e-12 for r in rows if r['preparation']==prep)} for prep in ['all_environment_states','low_K<=1']}},indent=2))
    return 0 if all(checks.values()) else 1
if __name__=='__main__':raise SystemExit(main())
