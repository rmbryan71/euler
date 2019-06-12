import time
import itertools
import math
import sympy
import functools
import operator as op


def f(x):
    return 1


def main():

    start = time.time()
    print(f(0))
    print(int(time.time() - start), " seconds to run.")


main()
