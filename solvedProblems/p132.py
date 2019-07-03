import sympy
import time
import math

def r(x):
    z = 1
    for i in range(1, x):
        z = 10 * z + 1
    return z


def big_r(x):
    str = '11111'
    str = str * (x // 5)
    return int(str)


def prime_factors(n):
    """Returns all the prime factors of a positive integer"""
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(int(d))
            n /= d
        d = d + 1
        if d*d > n:
            if n > 1: factors.append(int(n))
            break
    dedup = []
    for factor in factors:
        if factor not in dedup:
            dedup.append(factor)
    return dedup

#
# assert (r(10)) == 1111111111
# assert (len(str(r(137)))) == 137
# assert (big_r(10)) == 1111111111
# assert (len(str(big_r(137)))) == 137


# for z in range(0, 100, 1):
#     x = r(z)
#     p = sympy.primefactors(x)
#     print(z, sum(p), p)

# for exp in range(1, 10):
#     start = time.time()
#     x = big_r(10**exp)
#     print(len(str(x)), "took", int(time.time()-start))
#     # p = sympy.primefactors(x)
#     # print(len(p), sum(p[0:39]), "took", int(time.time()-start), p)

# p = sympy.primefactors(((10 ** (10 ** 3)) - 1) // 9)[0:39]
# print(p)

result = 0
count = 0
primes = list(sympy.primerange(2, 400000))
k = 10 ** 9
i = 0

while count < 40:
    p = 9 * primes[i]
    if pow(10, k, p) == 1:
        count += 1
        result += primes[i]
    i += 1

print(result)