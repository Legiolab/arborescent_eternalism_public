#!/usr/bin/env python3
"""Independent two-index preparation/mixing witness; Python standard library only."""
import itertools, math
from math import log, sin, cos, pi, comb
GOAL=(.35,-.25,.20)
R=.20
T=3

def p(j,z):
    b=.08*sin((j+1)*pi*(math.sqrt(5)-1))
    return .5 if z==0 else (.25+b if z==1 else .25-b)

def inverse3(A):
    (a,b,c),(d,e,f),(g,h,i)=A
    det=a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)
    adj=((e*i-f*h,c*h-b*i,b*f-c*e),
         (f*g-d*i,a*i-c*g,c*d-a*f),
         (d*h-e*g,b*g-a*h,a*e-b*d))
    return tuple(tuple(v/det for v in row) for row in adj)

def geometry(n):
    if n < 3:
        raise ValueError('Three-mode covariance requires n >= 3')
    cov=[[0.]*3 for _ in range(3)]
    for j in range(n):
        plus,minus=p(j,1),p(j,-1)
        variance=plus+minus-(plus-minus)**2
        basis=[cos(pi*m*(j+.5)/n)/n for m in range(3)]
        for m in range(3):
            for k in range(3):cov[m][k]+=variance*basis[m]*basis[k]
    return inverse3(cov)

def spatial_score(x,inv):
    n=len(x)
    surprisal=-sum(log(p(j,z)) for j,z in enumerate(x))
    mean=sum(x)/n
    gradients=sum((x[j+1]-x[j])**2 for j in range(n-1))/max(1,n-1)
    curvature=sum((x[j+2]-2*x[j+1]+x[j])**2 for j in range(n-2))/max(1,n-2)
    B=.5*(mean**2+gradients+.25*curvature)
    F=[sum(z*cos(pi*m*(j+.5)/n) for j,z in enumerate(x))/n for m in range(3)]
    delta=[F[m]-GOAL[m] for m in range(3)]
    C=.5*sum(delta[m]*inv[m][k]*delta[k] for m in range(3) for k in range(3))
    return surprisal+B+C

def h(z):return -z*log(z)-(1-z)*log(1-z)

def entropy_mixed(n,low_count,t):
    N=3**n;alpha=(1-R)**t
    in_low=alpha/low_count+(1-alpha)/N
    outside=(1-alpha)/N
    return -low_count*in_low*log(in_low)-(N-low_count)*outside*log(outside) if t else log(low_count)

a=log(.5/.33)
q=.25
geomean=(.25+math.sqrt(.25**2-.08**2))/2
v=.5-.16**2/2
F=(q,-sin(pi*q)/pi,sin(2*pi*q)/(2*pi))
delta=[F[j]-GOAL[j] for j in range(3)]
objective_rate=(delta[0]**2+2*delta[1]**2+2*delta[2]**2)/(2*v)
u=q*log(.5/geomean)+objective_rate
c=u/a
deficit=log(3)-h(c)-c*log(2)
print('a,u,C_rate,u/a,deficit:',a,u,objective_rate,c,deficit)
for n in range(3,11):
    inv=geometry(n)
    best=min((spatial_score(x,inv),x) for x in itertools.product((-1,0,1),repeat=n))
    s=1-R+R/3**n
    common_path_cost=-T*log(s)
    m=sum(comb(n,k)*2**k for k in range(math.floor(c*n)+1))
    values=[entropy_mixed(n,m,t) for t in range(4)]
    assert all(values[t+1]>values[t] for t in range(3))
    print(n,best[1],sum(z*z for z in best[1]),'J=',round(best[0]+common_path_cost,9),
          'mu(L)=',round(m/3**n,9),'entropy=',[round(z,6) for z in values])
