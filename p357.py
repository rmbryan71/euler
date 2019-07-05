from functools import reduce
from math import sqrt
import sympy


def factors(n):
    step = 2 if n % 2 else 1
    return set(reduce(list.__add__, ([i, n // i] for i in range(1, int(sqrt(n)) + 1, step) if n % i == 0)))


def is_gen(x):
    myfacts = factors(x)
    for factor in myfacts:
        if not sympy.isprime(factor + (x // factor)):
            return False
    return True


def main(limit):
    count = 1
    for i in range(2, limit, 2):
        if is_gen(i):
            count += i
    print(count)



main(100000000)