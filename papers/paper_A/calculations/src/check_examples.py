#!/usr/bin/env python3
import json
from pathlib import Path

def prefix_tree(histories, depth):
    levels=[]
    for n in range(depth+1):
        levels.append(sorted({h[:n] for h in histories}))
    edges=[]
    for n in range(depth):
        for child in levels[n+1]:
            edges.append([child, child[:-1]])
    return levels, edges

def phantom_ray_check(max_depth=8):
    # Globally admissible infinite histories are binary sequences of finite support.
    # For every finite n, the prefix 1^n is locally realised by a finite-support history.
    local=[]
    for n in range(1,max_depth+1):
        prefix="1"*n
        witness=prefix+"0"*max_depth
        local.append({"depth":n,"prefix":prefix,"finite_support_witness":witness})
    return {
        "all_tested_prefixes_locally_realised": all(local),
        "candidate_infinite_ray": "111...",
        "globally_admissible_under_finite_support_rule": False,
        "finite_checks": local,
    }

def factorisation_check():
    # Redundant labels A1/A2 encode the same record '0'.
    G={"root":["A1","A2"],"A1":["B"],"A2":["B"],"B":[]}
    q={"root":"","A1":"0","A2":"0","B":"01"}
    classes={}
    for g,x in q.items():
        classes.setdefault(x,[]).append(g)
    return {"presentation":G,"quotient_classes":classes,
            "redundancy_removed": classes["0"]==["A1","A2"]}

def concurrency_check():
    serialisations=["ab","ba"]
    configuration={"ab":"{a,b}","ba":"{a,b}"}
    return {"serialisations":serialisations,
            "same_configuration": len(set(configuration.values()))==1,
            "diamond":["{}","{a}","{b}","{a,b}"]}

def main():
    histories=["000","001","010","100"]
    levels,edges=prefix_tree(histories,3)
    result={
      "prefix_example":{"histories":histories,"levels":levels,"edges":edges},
      "phantom_ray":phantom_ray_check(),
      "factorisation":factorisation_check(),
      "independent_events":concurrency_check(),
      "interpretation":"Finite computational sanity checks only; analytic propositions remain proved in the paper."
    }
    out=Path(__file__).resolve().parents[1]/"expected_outputs"/"results.json"
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(result,indent=2))

if __name__=="__main__":
    main()
