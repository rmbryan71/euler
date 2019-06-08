from timeit import default_timer as timer
import itertools as it
import numpy as np
import operator as op


def pfpowers(pfs, maxpow):
    """
    returns list of possible exponents a,b,c,d... where maxpow =a>=b>=c...of a
    list of prime factors 2,3,5,7...in order such that 2^a*3^b*4^c...is an ascending sequence.
    """
    ps = []
    for a in it.combinations_with_replacement([x for x in range(maxpow, 0, -1)], len(pfs)):
        ps.append(list(a))
    ranks = []
    ps = ps[::-1]
    ranks = sorted([(i, myprod(ps[i], pfs)) for i in range(len(ps))], key=op.itemgetter(1))
    rps = []
    for i in range(len(ps)):
        rps.append(ps[ranks[i][0]])
    return rps


def divisibility(powers):
    """
    returns the number of divisors of a natural number, given a list of the
    exponents of its prime factors
    """
    d = 1
    for x in powers:
        d *= (2 * x + 1)
    return d


def myprod(primes, powers):
    p = 1
    for i in range(len(primes)):
        if powers[i] == 0:
            break
        p *= int(int(primes[i]) ** int(powers[i]))
    return p


def erat2a():
    """primes generator"""
    D = {}
    yield 2
    for q in it.islice(it.count(3), 0, None, 2):
        p = D.pop(q, None)
        if p is None:
            D[q * q] = 2 * q  # use here 2 * q
            yield q
        else:
            x = p + q
            while x in D:
                x += p
            D[x] = p


def dr(m):
    """
    returns the minimum value of n for which the diophantine equation 1/x + 1/y = 1/n
    has more than m solutions
    """


    start = timer()
    print('Diophantine reciprocal equation: 1/x + 1/y = 1/n')
    primes = []
    prime = erat2a()
    while 1:
        primes.append(next(prime))
        if np.prod(primes) > m ** 2:
            break
    primes.append(next(prime))

    pfs = []
    powers = []
    solutions = [np.inf]
    pindex = 0
    minsol = np.inf
    while len(pfs) < len(primes):
        pfs.append(primes[pindex])
        for pmax in range(1, 5):
            powers = pfpowers(pfs, pmax)
            for a in powers:
                if np.prod([2 * a[x] + 1 for x in range(len(pfs))]) > 2 * m - 1:
                    solutions.append(myprod(pfs, a))
                    if solutions[-1] < minsol:
                        minsol = solutions[-1]
                        amin = a
                    break
        pindex += 1
    print('Least value of n for which the number of solutions exceeds', m, '=', minsol)
    print('Prime factors:', amin)
    print('Prime factor powers:', pfs[:len(amin)])
    print('Number of solutions:', (divisibility(amin) + 1) // 2)
    print('Elapsed time', timer() - start)

dr(4000000)