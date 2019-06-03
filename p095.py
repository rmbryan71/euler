from networkx import nx
from sympy import divisors

from functools import reduce
# limit = 1000000
# result = 0
# chainLength = 0
# numbers = [False]
#
# def sumfactors(n):
#     return sum(reduce(list.__add__, ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0))) - n
#
#
# def chaincheck(n):
#     if sumfactors(n) not in chain.keys():
#         chaincheck(sumfactors(n))
#     return len(chain)
#
#
# for i in range(1, 27):
#     print(i, chaincheck(i))



n = 4
edges = []
while n < 1000000:
    edges.append((n,sum(divisors(n))-n))
    n += 1
G = nx.DiGraph(edges)
print(list(nx.simple_cycles(G)))