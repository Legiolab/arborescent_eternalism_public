#!/usr/bin/env python3
"""Bounded deterministic checks of a collective Hamiltonian recorder interface."""
import json
import math
import time
from collections import Counter
from fractions import Fraction
from pathlib import Path
import numpy as np
N=8
Q=N+1
DENOMINATOR=1024
NOISE=Fraction(1,8)

def swap_sites(m,i,j):
    return m ^ ((1<<i)|(1<<j)) if ((m>>i)&1)!=((m>>j)&1) else m

def display_units(m,error=Fraction(0)):
    value=Fraction(DENOMINATOR*m.bit_count()+m,DENOMINATOR)+error
    return (value+Fraction(1,2)).numerator//(value+Fraction(1,2)).denominator

def occupation_trace(source,initial):
    m=initial
    trace=[m.bit_count()]
    for i in range(N):
        m ^= source & (1<<i)
        trace.append(m.bit_count())
    return tuple(trace)

def main():
    started=time.monotonic();checks={};states=range(1<<N)
    p=np.arange(Q)
    fourier=np.exp(2j*np.pi*np.outer(p,p)/Q)/math.sqrt(Q)
    generator=fourier@np.diag(2*np.pi*p/Q)@fourier.conj().T
    shift=np.roll(np.eye(Q),1,axis=0)
    checks['hermitian_pointer_generator']=bool(np.allclose(generator,generator.conj().T,atol=1e-12,rtol=0))
    checks['hamiltonian_unitary_is_shift_for_every_K']=all(np.allclose(fourier@np.diag(np.exp(-2j*np.pi*k*p/Q))@fourier.conj().T,np.linalg.matrix_power(shift,k),atol=1e-12,rtol=0) for k in range(Q))
    checks['collective_generator_invariant_under_all_site_swaps']=all(swap_sites(m,i,j).bit_count()==m.bit_count() for m in states for i in range(N) for j in range(i+1,N))
    cells=Counter(m.bit_count() for m in states)
    checks['readout_cells_are_binomial']=all(cells[k]==math.comb(N,k) for k in range(Q))
    # q disjoint translations of an initial pointer support must each have size 1.
    allowed=[]
    for support_mask in range(1,1<<Q):
        support={p for p in range(Q) if (support_mask>>p)&1}
        outputs=[{(p+k)%Q for p in support} for k in range(Q)]
        if all(not outputs[k]&outputs[j] for k in range(Q) for j in range(k)):
            allowed.append(support_mask)
    checks['universal_exact_display_forces_singleton_pointer_support']=allowed==[1<<p for p in range(Q)]
    checks['uniform_pointer_has_no_K_information']=all({(p+k)%Q for p in range(Q)}==set(range(Q)) for k in range(Q))
    checks['readout_inverse_for_all_memory_pointer_states']=all(((p+m.bit_count())%Q-m.bit_count())%Q==p for m in states for p in range(Q))
    gains=[math.log(math.comb(N,m.bit_count())) for m in states]
    checks['endpoint_positive_254_of_256']=sum(g>0 for g in gains)==254
    # W=1024*K+m is a fixed weakly unequal linear coupling; exact access resolves all states.
    fine=Counter(DENOMINATOR*m.bit_count()+m for m in states)
    checks['unequal_exact_probe_resolves_all_256_states']=len(fine)==1<<N and all(c==1 for c in fine.values())
    checks['fixed_resolution_preserves_K_despite_unequal_couplings_and_bounded_noise']=all(display_units(m,e)==m.bit_count() for m in states for e in [-NOISE,Fraction(0),NOISE])
    checks['coarse_cells_unchanged']=Counter(display_units(m) for m in states)==cells
    # Available initial occupation plus the known write schedule determines the prepared history.
    prepared_sizes=[]
    distinct_by_source=[]
    for source in states:
        traces=Counter(occupation_trace(source,initial) for initial in states)
        prepared_sizes.append(traces[occupation_trace(source,0)])
        distinct_by_source.append(len(traces))
    checks['full_write_trace_singleton_for_every_prepared_source']=all(size==1 for size in prepared_sizes)
    checks['all_one_source_write_trace_resolves_all_initial_memories']=distinct_by_source[-1]==1<<N
    checks['zero_source_write_trace_only_occupation']=distinct_by_source[0]==Q
    checks['readout_bijection_on_full_memory_pointer_reference']=len({(m,(p+m.bit_count())%Q) for m in states for p in range(Q)})==(1<<N)*Q
    checks['source_preserving_copy_invertible']=all(((m^x)^x)==m for x in states for m in states)
    initial_support={(x,0,0) for x in states}
    final_support={(x,x,x.bit_count()%Q) for x in states}
    checks['fine_joint_support_size_preserved']=len(initial_support)==len(final_support)==1<<N
    result={
        'status':'CONDITIONAL_HAMILTONIAN_PARTITION_WITH_PROTOCOL_COUNTERCONTROL',
        'n':N,'pointer_levels':Q,'arithmetic':'exact integer/rational counting; Fourier identities checked with numpy tolerance 1e-12',
        'numpy_version':np.__version__,'checks':checks,'all_checks_pass':all(checks.values()),
        'endpoint_memory_macrovolume':{'positive':sum(g>0 for g in gains),'histories':1<<N,'mean_gain_nats':sum(gains)/len(gains)},
        'pointer_capacity':{'supports_tested':(1<<Q)-1,'admissible_supports':len(allowed),'support_size':1,'reference_entropy_deficit_nats':math.log(Q),'is_energy_cost':False},
        'robustness':{'coupling_numerators':[DENOMINATOR+(1<<i) for i in range(N)],'coupling_denominator':DENOMINATOR,'nearest_unit_bin_width':1,'noise_bound':str(NOISE),'fine_distinguishable_states':len(fine),'prepared_full_trace_cell_sizes':sorted(set(prepared_sizes))},
        'fine_joint_entropy':{'initial_nats':math.log(len(initial_support)),'final_nats':math.log(len(final_support)),'reason':'invertible copy+pointer permutation preserves uniform support size 256'},
        'limits':['Read stage and allowed operations supplied; universal writer does not intrinsically forbid reciprocal/site/time-resolved read access.',
                  'Uniform collective coupling derives K indistinguishability within this interface; AE does not uniquely derive the interface.',
                  'Quantized finite pointer is an explicit Hermitian model, not a local field or laboratory implementation.',
                  'Resolution and noise bound are apparatus assumptions fixed before counting.',
                  'Pointer readiness is functionally constrained; preparing/resetting it is not thermodynamically explained.',
                  'Macrovolume uses full memory reference, not posterior restricted to prepared histories.',
                  'Endpoint gain is not proof of monotonic growth, heat production or cosmological arrow.'],
        'runtime_seconds':time.monotonic()-started}
    Path(__file__).with_name('results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['status','all_checks_pass','endpoint_memory_macrovolume','pointer_capacity','runtime_seconds']},indent=2))
    return 0 if result['all_checks_pass'] else 1
if __name__=='__main__':raise SystemExit(main())
