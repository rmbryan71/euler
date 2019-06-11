import time
import itertools
import math
import sympy
import functools
import operator as op


def f(length, m):  # length of row = length, block size is m
    result = [1] + [0] * length
    #print(result)
    for i in range(1, len(result)):
        result[i] += result[i-1]
        if i >= m:
            result[i] += result[i - m]
    return result[-1] - 1


def main():

    start = time.time()
    print (f(5, 2))
    print(int(time.time() - start), " seconds to run.")


main()
