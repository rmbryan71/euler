import time
import itertools
import math
import sympy
import functools
import operator as op


def f(x):
    perms = itertools.permutations(range(1, x + 1))
    seps = itertools.combinations_with_replacement(['', ','], x-1)

    for perm in perms:
        print(perm)
    for sep in seps:
        print(sep)

    for perm in perms:
        for set in itertools.product(perm, seps):
            for item in set:
                print(item)

def f1(x):
    primes = sympy.primerange(2, x)
    for set in itertools.combinations(primes, 4):
        print(set)




def main():

    start = time.time()
    print(f1(100))
    print(int(time.time() - start), " seconds to run.")


main()
