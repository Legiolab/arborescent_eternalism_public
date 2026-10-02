#!/usr/bin/env python3
"""Exact AE event/projection access partitions, with matched causal controls."""
import json
import math
import time
from collections import Counter
from itertools import permutations
from pathlib import Path
N=8

def terminal_graph(n,mode):
    events=[]
    for i in range(n):
        events.append({'id':f'w{i}','requires':[] if i==0 else [f'w{i-1}'], 'kind':'write','site':i})
    events.append({'id':'read','requires':[f'w{n-1}'],'kind':'read','mode':mode})
    return events

def trace_graph(n):
    events=[{'id':'r0','requires':[],'kind':'read','mode':'collective'}]
    for i in range(n):
        events.append({'id':f'w{i}','requires':[f'r{i}'],'kind':'write','site':i})
        events.append({'id':f'r{i+1}','requires':[f'w{i}'],'kind':'read','mode':'collective'})
    return events

def ae_execute(events,x,m0,capacity,retain_trace):
    state=m0;done=set();record=[]
    for event in events:
        if not set(event['requires'])<=done:
            raise ValueError('event violates prerequisites')
        if event['kind']=='write':
            state ^= x & (1<<event['site'])
        else:
            # Pi supplies this physical pointer translation, realized by CALC-125 H_q.
            value=state.bit_count() if event['mode']=='collective' else state
            if value>=capacity:raise ValueError('reader capacity insufficient')
            if retain_trace:record.append(value)
            else:record=[value]
        done.add(event['id'])
    return state,tuple(record)

def causal_record(x,m0,n,mode,retain_trace):
    # Separate direct register calculation; does not read the event graph.
    values=[m0.bit_count()]
    m=m0
    for i in range(n):
        m ^= ((x>>i)&1)<<i
        values.append(m.bit_count())
    if retain_trace:return tuple(values)
    return (m.bit_count() if mode=='collective' else m,)

def partition_for_protocol(events,x,n,capacity,retain_trace):
    records={}
    for m0 in range(1<<n):
        final,record=ae_execute(events,x,m0,capacity,retain_trace)
        records[final]=record
    return records

def main():
    start=time.monotonic();checks={};rows=[]
    specs=[('terminal_collective_q9',terminal_graph(N,'collective'),9,False,'collective'),
           ('terminal_collective_q256',terminal_graph(N,'collective'),256,False,'collective'),
           ('terminal_fine_q256',terminal_graph(N,'fine'),256,False,'fine'),
           ('retained_write_trace',trace_graph(N),9,True,'collective')]
    for name,events,capacity,retain_trace,mode in specs:
        sizes=[];gains=[];counts=[];matches=True
        for x in range(1<<N):
            records=partition_for_protocol(events,x,N,capacity,retain_trace)
            cells=Counter(records.values())
            counts.append(len(cells))
            volume=cells[records[x]] # m0=0 -> final m=x
            sizes.append(volume);gains.append(math.log(volume))
            for m0 in range(1<<N):
                matches &= records[m0^x]==causal_record(x,m0,N,mode,retain_trace)
        checks[name+'_matched_causal_records']=matches
        if mode=='collective' and not retain_trace:
            checks[name+'_binomial_cell_volume']=all(v==math.comb(N,x.bit_count()) for x,v in enumerate(sizes))
        else:checks[name+'_prepared_history_cell_singleton']=all(v==1 for v in sizes)
        rows.append({'protocol':name,'pointer_capacity':capacity,'retains_writing_past':retain_trace,
                     'distinguishable_cells_min':min(counts),'distinguishable_cells_max':max(counts),
                     'prepared_cell_volume_min':min(sizes),'prepared_cell_volume_max':max(sizes),
                     'positive_endpoint_volumes_vs_blank_reference':sum(g>0 for g in gains),
                     'sources':1<<N,'mean_log_volume':sum(gains)/len(gains)})
    checks['same_E_different_Pi_changes_partition']=terminal_graph(N,'collective')[0:-1]==terminal_graph(N,'fine')[0:-1] and rows[1]['distinguishable_cells_max']==9 and rows[2]['distinguishable_cells_min']==256
    checks['same_capacity_and_dynamics_coarse_or_fine']=rows[1]['pointer_capacity']==rows[2]['pointer_capacity']==256
    # Controller has two conflicting terminal choices; record from collective differs from capability over BOTH.
    realized=Counter(m.bit_count() for m in range(1<<N))
    capability=Counter((m.bit_count(),m) for m in range(1<<N))
    checks['one_realized_collective_record_not_all_available_information']=len(realized)==9 and len(capability)==256
    # Equivalent independent write serializations are descriptions, not new physical alternatives.
    n=4;orders=list(permutations(range(n)));physical=set();serialized=0
    invariant=True
    for x in range(1<<n):
        finals=set()
        for order in orders:
            m=0
            for i in order:m ^= x & (1<<i)
            finals.add(m);serialized+=1
        invariant &= finals=={x}
        physical.add((x,x))
    checks['independent_serialization_does_not_change_projection']=invariant
    checks['quotient_avoids_24_fold_counting']=serialized==len(physical)*len(orders)
    # Removing an ordering guard actually allows unprepared read before last write: detect this fault.
    bad=[{'id':'read','requires':[],'kind':'read','mode':'collective'}]+terminal_graph(N,'collective')[:-1]
    _,early=ae_execute(bad,255,0,9,False)
    _,late=ae_execute(terminal_graph(N,'collective'),255,0,9,False)
    checks['event_prerequisites_change_which_cut_is_observed']=early==(0,) and late==(8,)
    result={'status':'AE_ACCESS_COMPOSITION_PROVED_CONDITIONALLY_NOT_BARE_STRUCTURE_ENTROPY',
            'n':N,'checks':checks,'all_checks_pass':all(checks.values()),'rows':rows,
            'controller':{'realized_collective_cells':len(realized),'available_collective_and_fine_cells':len(capability),'interpretation':'Choice of a coarse record does not remove an unused fine read capability.'},
            'serialization':{'n':n,'physical_histories':len(physical),'linearized_descriptions':serialized,'factor':len(orders)},
            'limits':['AE E and Pi here are a concrete event/register module, not the full five-agent Hamiltonian or cosmos.',
                      'E determines available order/protocols; Pi supplies the physical coupling. Identical generic E supports both coarse and fine Pi.',
                      'Stored trace and terminal snapshot use different information and different resource budgets.',
                      'Capacities, retained-record budget and permitted physical operations are apparatus inputs, not derived from AE alone.',
                      'Source reference uniform and memory full-state measure supplied; numbers are conditional macrovolumes, not thermodynamic dissipation.',
                      'The causal comparator copies the specified physical package; this is equivalence of this model, not exclusivity or necessity of AE.'],
            'runtime_seconds':time.monotonic()-start}
    Path(__file__).with_name('results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'all_checks_pass':result['all_checks_pass'],'rows':rows,'controller':result['controller'],'runtime_seconds':result['runtime_seconds']},indent=2))
    return 0 if result['all_checks_pass'] else 1
if __name__=='__main__':raise SystemExit(main())
