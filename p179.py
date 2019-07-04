import time
from math import sqrt
from multiprocessing import Pool
from operator import itemgetter
from functools import reduce


def countfactors(x):
    count = 1
    for i in range(1, x//2 + 1):
        if x % i == 0:
            count += 1
    return x, count


def cfactors(n):
        step = 2 if n % 2 else 1
        return n, len(set(reduce(list.__add__,
                          ([i, n // i] for i in range(1, int(sqrt(n)) + 1, step) if n % i == 0))))


def main():
    limit = 10**7 + 1
    start = time.time()
    factors = []
    p = Pool()
    factors.append(p.map(cfactors, range(1, limit)))
    end = time.time()
    sorted_factors = sorted(factors, key=itemgetter(0))
    count = 0
    for i in (range(0, len(sorted_factors[0]) - 1)):
        if sorted_factors[0][i][1] == sorted_factors[0][i + 1][1]:
            count += 1

    print(end - start)
    print(count)

main()
