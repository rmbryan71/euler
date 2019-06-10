import math, sympy, time, multiprocessing, itertools, functools
import operator as op


def is_b(x):
    s=''.join(sorted(x))
    return not(x == s or x[::-1] == s)


def ncr(n, r):
    r = min(r, n-r)
    numer = functools.reduce(op.mul, range(n, n-r, -1), 1)
    denom = functools.reduce(op.mul, range(1, r+1), 1)
    return numer / denom


def non_bouncy(x):
    return ncr(x + 9, x) + ncr(x + 10, x) - (10 * x) - 2


def main():
    start = time.time()

    print(non_bouncy(6))
    print(non_bouncy(10))
    print(non_bouncy(100))

    print(int(time.time() - start), " seconds to run.")


main()
