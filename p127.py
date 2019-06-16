import sympy, numpy
import math
import time
import itertools

def rad(x):
    return numpy.prod(sympy.primefactors(x))


def is_hit(a, b, limit):
    if a >= b:
        return False
    c = a + b
    if c > limit:
        return False
    if math.gcd(a, b) == 1:
        if math.gcd(b, c) == 1:
            if math.gcd(a, c) == 1:
                if rad(a * b * c) < c:
                    return c
    return False


limit = itertools.repeat(1000)
limit_int = 1000
start = time.time()
count = 0
result = 0
a = range(1, limit_int//2)
b = range(1, limit_int//2)
wins = map(is_hit, a, b, limit)
wins = list(wins)

print(len(wins), sum(wins), limit, int(time.time() - start))