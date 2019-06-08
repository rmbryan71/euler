from sympy import factorint as fac
import operator
from itertools import combinations as combs



def genval(i):
        a,s = fac(i).values(),1
        for i in range(1,len(a)+1):
                 s += sum((reduce(operator.mul,data) for data in combs(a,i)))*(2**(i-1))
        return s