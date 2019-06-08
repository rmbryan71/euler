import math, sympy, time, multiprocessing


def m(n, d): # max repeated digits(d) for an n-digit number
    lower_bound = 10**(n-1)
    upper_bound = 10**n - 1
    result = 0
    for x in sympy.primerange(lower_bound, upper_bound+1):
        if str(x).count(str(d)) > result:
            result = str(x).count(str(d))
            # print(str(x), str(d), result)
    return result


def m10(d): # max repeated digits(d) for a 10 digit number
    lower_bound = 10**9
    upper_bound = 10**10 - 1
    result = 0
    for x in sympy.primerange(lower_bound, upper_bound+1):
        if str(x).count(str(d)) > result:
            result = str(x).count(str(d))
            # print(str(x), str(d), result)
    return result


p = multiprocessing.Pool(4)

start = time.time()
print(list(p.map(m10, range(0, 10))))
print(time.time() - start)



