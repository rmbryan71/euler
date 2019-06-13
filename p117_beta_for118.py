import time
import itertools
import math
import sympy
import functools
import operator as op


def f(length):  # length of row = length, block sizes are 2, 3, and 4
    result2 = [1] + [0] * length
    result3 = [1] + [0] * length
    result4 = [1] + [0] * length
    for i in range(1, len(result2)):
        result2[i] += result2[i-1]
        if i >= 2:
            result2[i] += result2[i-2]
    for i in range(1, len(result3)):
        result3[i] += result3[i-1]
        if i >= 3:
            if i-3 >= 2:
                result3[i] += result3[i-2]
            result3[i] += result3[i-3]
    for i in range(1, len(result4)):
        result4[i] += result4[i-1]
        if i >= 4:
            if i-4 >= 3:
                result4[i] += result4[i-3]
            if i-4 >= 2:
                result4[i] += result4[i-2]
            if i-7 >= 2:
                result4[i] += result4[i-3]
            if i-5 >= 3:
                result4[i] += result4[i-2]
            result4[i] += result4[i-4]
    return result2[-1] + result3[-1] + result4[-1] - 2


def f1(m, min, max):
    result = 1
    cache = []
    if m <= min:
        return result
    if cache[m] != 0:
        return cache[m]
    for bs in range(min, max):
        for i in range(0, m-bs):
            result += f1(m - bs, min, max)
    cache[m] = result
    return result


def f116(length, m):  # length of row = length, block size is m
    result = [1] + [0] * length
    for i in range(1, len(result)):
        result[i] += result[i-1]
        if i >= m:
            result[i] += result[i - m]
            print(result)
    return result[-1]


def f117(x):
    if x < 0:
        return 0
    if x is 0:
        return 1
    else:
        return f117(x-1) + f117(x-2) + f117(x-3) + f117(x-4) + f117(x-5) + f117(x-6) + f117(x-7) + f117(x-8) + f117(x-9)


def main():
    start = time.time()
    assert f(5) == 15
    #assert f117(5) == 15

    print(f117(9))

    print(int(time.time() - start), " seconds to run.")


main()
