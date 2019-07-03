#How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime fourth power?

import itertools
import numpy

def sieve(n):
    "Return all primes <= n."
    np1 = n + 1
    s = list(range(np1)) # leave off `list()` in Python 2
    s[1] = 0
    sqrtn = int(round(n**0.5))
    for i in range(2, sqrtn + 1): # use `xrange()` in Python 2
        if s[i]:
            # next line:  use `xrange()` in Python 2
            s[i*i: np1: i] = [0] * len(range(i*i, np1, i))
    return filter(None, s)

primes = list(sieve(500))

solutions = []

for set in itertools.combinations_with_replacement(primes,3):
    for perm in itertools.permutations(set):
        candidate = (perm[0] ** 2) + (perm[1] ** 3) + (perm[2] ** 4)
        if candidate < 50000000 and solutions.count(candidate) == 0:
            solutions.append(candidate)
            print(perm[0], perm[1], perm[2], candidate, len(solutions))
    #print(set[0], set[1], set[2])

solutions.sort(reverse=True)
print(solutions[0], len(solutions))
