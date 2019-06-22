import sympy
import time
import numpy
import itertools


def a(x):
    if numpy.gcd(x, 10) > 1:
        return False
    z = 1
    for i in itertools.count(1):
        if z % x == 0:
            return i
        z = 10 * z + 1


assert a(7) == 6
assert a(41) == 5
assert a(17) == 16


results = []
for i in itertools.count(5, 2):
    if numpy.gcd(i, 10) == 1:
        if not sympy.isprime(i):
            if (i - 1) % a(i) == 0:
                results.append(i)
                if len(results) == 25:
                    print("Answer is", sum(results))
                    break
                print(len(results), i)
