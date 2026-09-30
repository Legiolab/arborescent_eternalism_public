#!/usr/bin/env python3
"""Exact regulated volume comparison for independent positive quadratic mode energies."""
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
CHECKS = {}
def check(name, condition):
    CHECKS[name] = bool(condition)
    assert condition, name

def cdf(n, r):
    """Uniform independent mode energies E_j/E_*; exact Irwin-Hall CDF."""
    x = n*r
    if x <= 0: return Fraction(0)
    if x >= n: return Fraction(1)
    return sum(((-1)**j * math.comb(n,j)*(x-j)**n
                for j in range(math.floor(x)+1)), Fraction(0))/math.factorial(n)

def log_mgf_negative(t):
    return math.log(-math.expm1(-t))-math.log(t)

def rate(r):
    """Chernoff rate sup_t>0[-t*r-log E(exp(-t*U))], U uniform[0,1]."""
    if r >= .5: return 0.0
    # Tilted mean = 1/t - 1/(exp(t)-1), strictly decreasing.
    lo, hi = 1e-5, 1/r+1
    for _ in range(100):
        t=(lo+hi)/2
        mean=1/t - (1/math.expm1(t) if t<700 else 0)
        if mean>r: lo=t
        else: hi=t
    t=(lo+hi)/2
    return -t*r-log_mgf_negative(t)

def volume_audit():
    check("N1_uniform_CDF", all(cdf(1,r)==r for r in [Fraction(1,4),Fraction(1,2),Fraction(3,4)]))
    check("N2_triangle",cdf(2,Fraction(1,4))==Fraction(1,8))
    check("sum_region_differs_from_product",cdf(2,Fraction(1,4))!=Fraction(1,4)**2)
    rows=[]
    for n,r in itertools.product([1,2,4,8,16,32,64,128],
                                 [Fraction(1,10),Fraction(1,4),Fraction(2,5),Fraction(1,2),Fraction(3,4)]):
        f=cdf(n,r); I=rate(float(r)); bound=math.exp(-n*I)
        check(f"cdf_range_{n}_{r}",0<=f<=1)
        check(f"cdf_reflection_{n}_{r}",f+cdf(n,1-r)==1)
        check(f"chernoff_{n}_{r}",float(f)<=bound+1e-12)
        if r==Fraction(1,2):check(f"half_volume_{n}",f==Fraction(1,2))
        rows.append({"N":n,"r":str(r),"total_energy_volume":float(f),
          "product_region_volume":float(r**n),"chernoff_rate":I,
          "chernoff_bound":bound,"exact_fraction":str(f)})
    return rows

def main():
    rows=volume_audit()
    result={"passed":sum(CHECKS.values()),"total":len(CHECKS),"all_checks_pass":all(CHECKS.values()),"checks":CHECKS,"rows":rows}
    (HERE/"results.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({"passed":result["passed"],"total":result["total"]}))
    return 0 if all(CHECKS.values()) else 1
if __name__=="__main__":raise SystemExit(main())
