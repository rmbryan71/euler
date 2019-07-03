import math, itertools, time
# set of numbers less than x which are sums of consecutive squares
start = time.time()


def is_pal(x):  # true if palindromoe
    return x == int(str(x)[::-1])


def f(x):  # all numbers less than x that are sums of consecutive squares
    results = []
    max = math.floor(math.sqrt(x))
    for i in range(1, max): # lower bound of sequence
        for j in range(i+2, max):
            z = sum(y*y for y in range(i, j))
            if 1 < z < x and z not in results:
                results.append(z)
    return sorted(results)


assert is_pal(595)

for myRange in range(1, 9):
    mySet = f(10**myRange)
    myPals = [x for x in mySet if is_pal(x) and x > 1]

    # print(len(mySet), sum(mySet), mySet)
    # print(len(myPals), sum(myPals), myPals)

    print(sum(myPals), "for", myRange, "took", time.time() - start, "seconds")