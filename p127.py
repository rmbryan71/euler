import sympy, numpy
import math
import time

def rad(x):
    return numpy.prod(sympy.primefactors(x))


for limit in range(1000, 120500, 500):
    start = time.time()
    count = 0
    result = 0
    for a in range(1, limit//2):
        for b in range(a + 1, limit - a):
            c = a + b
            if c < limit:
                if math.gcd(a, b) == 1:
                    if math.gcd(b, c) == 1:
                        if math.gcd(a, c) == 1:
                            if rad(a * b * c) < c:
                                count += 1
                                result += c
    print(count, result, limit, int(time.time() - start))