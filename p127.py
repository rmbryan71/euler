import sympy, numpy
import math
import time
import itertools

def rad(x):
    return numpy.prod(sympy.primefactors(x))


def f127_a():  # slow but accurate
    for limit in range(1000, 2001, 1500):
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
                                    print(a, b, c)
        print(count, result, limit, int(time.time() - start))


def f127_b(): # junk, slower than A and wrong.
    for limit in range(1000, 2001, 500):
        start = time.time()
        count = 0
        result = 0
        for c in range(1, limit + 1):
            for a in range(1, limit // 2 ):
                b = c - a
                if c < limit:
                    if math.gcd(a, b) == 1:
                        if math.gcd(b, c) == 1:
                            if math.gcd(a, c) == 1:
                                if rad(a * b * c) < c:
                                    count += 1
                                    result += c
        print(count, result, limit, int(time.time() - start))


def is_hit(a, b, c, limit):
    if a < b:
        if c < limit:
            if a + b == c:
                if math.gcd(a, b) == 1:
                    if math.gcd(b, c) == 1:
                        if math.gcd(a, c) == 1:
                            if rad(a * b * c) < c:
                                # print(a, b, c)
                                return a, b, c
    return False


def f127_c():  # experimental
    for limit in range(120000, 120001, 1500):
        start = time.time()
        count = 0
        result = 0
        resultset = []
        myset = []  # every number less than limit that is x^y
        for x in range(1, math.floor(math.sqrt(limit) + 1)):
            for y in range(0, math.floor(math.sqrt(limit) + 1)):
                z = x**y
                if z < limit and z not in myset:
                    myset.append(z)
        #  set is built, now use to make candidate solutions
        for s in itertools.combinations(myset, 2):
            a = min(s)
            b = max(s)
            c = a + b
            if is_hit(a, b, c, limit):
                if [a, b, c] not in resultset:
                    resultset.append([a, b, c])
            c = max(s)
            b = c - a
            if is_hit(a, b, c, limit):
                if [a, b, c] not in resultset:
                    resultset.append([a, b, c])
            if is_hit(b, a, c, limit):
                if [b, a, c] not in resultset:
                    resultset.append([b, a, c])
        dedup = []
        for i in resultset:
            if i not in dedup:
                dedup.append(i)
                # print(i)
        resultset = dedup
        for i in sorted(resultset):
            result += i[2]
            #print(i)
        print(len(resultset), result, limit, int(time.time() - start))

f127_c()