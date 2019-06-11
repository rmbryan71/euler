import time
import itertools
import math
import sympy
import functools
import operator as op


def f(x):
    for z in itertools.count(x):
        print(z)


def main():
    f(7)

    # for a in range(1, 10):
    #     start = time.time()
    #     f(a)
    #     print(a, int(time.time() - start), " seconds.")

main()
