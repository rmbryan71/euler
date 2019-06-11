import time
import itertools
import math
import sympy
import functools
import operator as op


def f(x):  # 28 seconds for 10**9
    for y in range(1, x):
        z = y


def g(x):  # takes 50 seconds and freezes my machine while executing
    z = []
    for y in range(1, x):
        z.append(y)


def h(x):
    for y in range(1, x):
        print(y)


def main():

    for a in range(1, 8):
        start = time.time()
        h(10**a)
        print(a, int(time.time() - start), "seconds.")


main()
