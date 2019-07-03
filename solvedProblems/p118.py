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


d1primes = sympy.primerange(2, 10)
d2primes = sympy.primerange(11, 100)
d3primes = sympy.primerange(101, 1000)
d4primes = sympy.primerange(1001, 10000)
d5primes = sympy.primerange(10001, 100000)
d6primes = sympy.primerange(100001, 1000000)
d7primes = sympy.primerange(1000001, 10000000)
d8primes = sympy.primerange(10000001, 100000000)
d9primes = sympy.primerange(100000001, 1000000000)


def setpart(a):  # return all partitions of a sequence
    n=len(a)
    # assert n>=1
    if n == 1:
        return [[a]]
    else:
        t = setpart(a[:-1])
        tt = []
        for s in t:
            tt.append(s+[[a[-1]]])
            for i, r in enumerate(s):
                sc = s[:]
                sc[i] = r + [a[-1]]
                tt.append(sc)
        return tt

def is_pan_set(x):
    digits = []
    for item in x:
        for char in str(item):
            digits.append(int(char))
    return sorted(digits) == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def cntprime(da):
    ## example: tonum([0,1,3])=13, tonum([3,0,1])=301
    def tonum(a): return functools.reduce(lambda x,y:10*x+y,a,0)
    return sum(sympy.isprime(tonum(a)) for a in itertools.permutations(da) )


def is_prime_pan_set(x):
    digits = []
    for item in x:
        if not sympy.isprime(item):
            return False
        for char in str(item):
            digits.append(int(char))
    return sorted(digits) == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def cnt(a):
    pr=1
    for da in a:
        tmp = cntprime(da)
        if tmp==0:return 0
        pr *= tmp
    return pr


def find(d):
    return sum(cnt(a) for a in setpart(d))


def main():
    start = time.time()
    result = 0
    print(find(list(range(1, 10))))
    test_a = [2, 5, 47, 89, 631]
    test_b = [179425683]
    assert is_pan_set(test_a) is True
    assert is_prime_pan_set(test_a) is True
    assert is_pan_set(test_b) is True
    assert is_prime_pan_set(test_b) is False
    print(int(time.time() - start), " seconds to run.")


main()