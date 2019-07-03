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
    for limit in range(10000, 10001, 1000):
        start = time.time()
        count = 0
        result = 0
        resultset = []
        littleset = [1]  # every number less than limit that is x^y
        for x in range(1, limit):
            for y in range(2, 17):
                z = x**y
                if z < limit and z not in littleset:
                    littleset.append(z)
        myints = list(range(1, 500))
        myset = littleset + myints
        n = len(myset)
        calculations = math.factorial(n) // (2*(math.factorial(n - 2)))
        print(len(myset), "estimated to take:", calculations//5316, "seconds")

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
            # print(i)
        # print(len(resultset), result, limit, int(time.time() - start))
        for item in resultset:
            itemcount = 0
            for a in item:
                if a in littleset:
                    itemcount += 1
            if itemcount < 2:
                print(item, itemcount)


def gen_root_set(limit):  # returns a list of all numbers less than x that are a^b
    root_set = []
    max_exp = math.floor(math.log2(limit)) + 1
    for x in range(1, limit):
        for y in range(2, max_exp):
            z = x ** y
            if z < limit and z not in root_set:
                root_set.append(z)
    return sorted(root_set)


def setbuilder(x, limit):  # return all combinations of a + b = c < limit
    sets = []
    for i in range(1, ((x // 2) + 1)):  # cases where root is c
        sets.append([i, x - i, x])
    for i in range(1, limit - x):  # case where root is b
        sets.append([i, x, i + x])
    for i in range(x + 1, limit - x):  # case where root is a
        sets.append([x, i, x + i])
    return sorted(sets)


def f127_d(limit):
    total, count = 0, 0
    hits = []
    root_set = gen_root_set(limit)
    print(len(root_set), "roots")
    for root in root_set:
        print(root, root*100 // limit)
        for set in setbuilder(root, limit):
            if is_hit(set[0], set[1], set[2], limit) and set not in hits:
                total += set[2]
                count += 1
                hits.append(set)
    for hit in sorted(hits):
        print(hit[0], hit[1], hit[2])
    print(count, total)


f127_d(10000)
