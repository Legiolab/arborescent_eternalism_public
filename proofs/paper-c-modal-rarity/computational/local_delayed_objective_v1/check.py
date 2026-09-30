import itertools, math, json
n,T=6,3
states=list(itertools.product((0,1),repeat=n))
target=(1,1,1,0,0,0)
rows=[]
for x0 in states:
    p0=(.8/20 if sum(x0)==3 else .2/44)
    for moves in itertools.product(range(-1,n),repeat=T):
        x=x0; history=[x]; prob=p0
        for j in moves:
            if j==-1: prob*=.5
            else:
                prob*=1/(2*n)
                y=list(x); y[j]=1-y[j]; x=tuple(y)
            history.append(x)
        # A delayed task reward: the final target and memory of three distinct actions.
        reward=int(x==target and set(moves)=={0,1,2})
        rows.append(( -math.log(prob),reward,x0,moves,[sum(x) for x in history]))
best0=min(r[0] for r in rows)
bestA=min(r[0] for r in rows if r[1])
threshold=bestA-best0
assert abs(threshold-(math.log(8.8)+3*math.log(6)))<1e-12
checks=[]
for beta in (0,threshold-.01,threshold,threshold+.01,10):
    m=min(r[0]-beta*r[1] for r in rows)
    winners=[r for r in rows if abs(r[0]-beta*r[1]-m)<1e-10]
    expected_count = 26 if beta == threshold else (20 if beta < threshold else 6)
    assert len(winners) == expected_count
    if beta > threshold:
        assert all(r[4] == [0,1,2,3] for r in winners)
    checks.append(dict(beta=beta,count=len(winners),initial_K=sorted(set(sum(r[2]) for r in winners)),K_paths=sorted(set(tuple(r[4]) for r in winners))))
# Full ensemble transition, initialized at the selected preparation.
rho={x:float(sum(x)==0) for x in states}
entropies=[]
for t in range(7):
    entropies.append(-sum(p*math.log(p) for p in rho.values() if p))
    new={x:.5*rho[x] for x in states}
    for x in states:
        for j in range(n):
            y=list(x); y[j]=1-y[j]; new[tuple(y)]+=rho[x]/(2*n)
    rho=new
assert all(b>a for a,b in zip(entropies,entropies[1:]))
out=dict(histories=len(rows),threshold=threshold,checks=checks,selected_Boltzmann_entropy=[math.log(math.comb(n,k)) for k in range(4)],ensemble_Shannon_entropy=entropies,initial_macro_fraction=1/64)
print(json.dumps(out,indent=2))
