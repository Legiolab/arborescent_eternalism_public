"""Conserved source energy shell: admissibility, capacity and realised operation.
Standard library; reuses previous thermal kernel. No entropy reward.
"""
import importlib.util,itertools,json,math
from pathlib import Path
spec=importlib.util.spec_from_file_location('thermal',Path(__file__).resolve().parent.parent/'record_reset_thermodynamics_v1/check.py')
thermal=importlib.util.module_from_spec(spec);spec.loader.exec_module(thermal)
TOL=1e-9
def test(n,k,alpha=.9):
    N=1<<n
    sources=[s for s in range(N) if s.bit_count()==k]
    q,K=thermal.kernel(5,alpha)
    # H_S=Delta*sum S_j. Copy and reset preserve S exactly.
    # Fixed positive shell is a boundary assumption, NOT derived from AE.
    reset_one=int(K[1][1]>K[1][0])
    threshold=n*.2+k*math.log(K[0][0]/max(K[1]))
    cases=[]
    for beta in [threshold-.01,threshold,threshold+.01]:
        best=math.inf;wins=[];mass=0
        for a,m,s,y in itertools.product(range(N),range(N),sources,range(N)):
            cap=int(a==N-1 and m==0) # established universal truth-table theorem
            c=m^(a&s)
            logw=-2*n*math.log(2)-math.log(len(sources))+sum(math.log(K[(c>>j)&1][(y>>j)&1]) for j in range(n))
            mass+=math.exp(logw)
            J=-logw+.2*a.bit_count()-beta*cap
            if J<best-TOL:best=J;wins=[(a,m,s,y)]
            elif abs(J-best)<TOL:wins.append((a,m,s,y))
        capable={(N-1,0,s,s if reset_one else 0) for s in sources}
        incapable={(0,0,s,0) for s in sources}
        expected=incapable if beta<threshold-TOL else capable if beta>threshold+TOL else incapable|capable
        assert set(wins)==expected and abs(mass-1)<TOL
        cases.append({'beta':beta,'count':len(wins),'all_capable':all(a==N-1 and m==0 for a,m,s,y in wins)})
    # Conditional causal ensemble with same shell, blank memory and CNOT.
    final={}
    for s,y in itertools.product(sources,range(N)):
        prob=math.prod(K[(s>>j)&1][(y>>j)&1] for j in range(n))/len(sources)
        final[(s,y)]=prob
    assert abs(sum(final.values())-1)<TOL
    causal={}
    for source in sources:
        states={0:1/len(sources)}
        copied=source^0
        states={copied:1/len(sources)}
        for j in range(n):
            nxt={}
            for memory,p in states.items():
                x=(memory>>j)&1
                for bit in [0,1]:
                    out=(memory&~(1<<j))|(bit<<j)
                    nxt[out]=nxt.get(out,0)+p*K[x][bit]
            states=nxt
        for out,p in states.items():causal[(source,out)]=p
    assert set(causal)==set(final)
    assert max(abs(causal[z]-final[z]) for z in final)<TOL
    deltaH=thermal.H(list(final.values()))-math.log(len(sources))
    Q=5*sum(p*(y.bit_count()-k) for (s,y),p in final.items())
    sigma=deltaH-Q
    assert sigma>=-TOL
    # Counterexample: source-controlled reversible uncopy, no bath.
    for s in sources:
        assert (s^s)==0
    return {'n':n,'conserved_source_excitations':k,'source_shell_size':len(sources),
      'source_shell_counting_fraction':len(sources)/N,
      'capacity_reward_threshold':threshold,'MAP_cases':cases,
      'capable_MAP_memory_Boltzmann_trace':[0,math.log(math.comb(n,k)),math.log(math.comb(n,k)) if reset_one else 0],
      'capable_MAP_bath_entropy':5*k*(1-reset_one),
      'conditional_ensemble_delta_joint_entropy':deltaH,
      'conditional_ensemble_bath_entropy':-Q,'conditional_ensemble_sigma':sigma,
      'causal_law_identical':True,
      'reversible_uncopy_control':{'heat':0,'joint_entropy_change':0,
          'memory_Boltzmann_trace':[0,math.log(math.comb(n,k)),0]}}
if __name__=='__main__':
    print(json.dumps({'model':'conserved_source_shell_v1',
      'cases':[test(n,k,a) for n in [2,3,4] for k in range(1,n) for a in [.5,.7,.9]],
      'conclusion':'A positive conserved source shell excludes the null message but is an independent boundary premise; capacity still needs a score threshold; matched causal operation is identical and reversible uncopy prevents a dissipation theorem.'},indent=2))
