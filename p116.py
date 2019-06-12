import time
import itertools
import math
import sympy
import functools
import operator as op


def f(length, m):  # length of row = length, block size is m
    result = [1] + [0] * length
    for i in range(1, len(result)):
        result[i] += result[i-1]
        if i >= m:
            result[i] += result[i - m]
            print(result)
    return result[-1] -1


def main():

    start = time.time()
    result = 0
    for i in range(2, 5):
        result += f(50, i)
    print(result)
        #print(i, int(time.time() - start), " seconds to run.")


main()
