import time
import itertools
import math
import sympy
import functools
import operator as op


def f(x):
    z = [i for i in itertools.count(x)]
    print z


def main():

    for i in range(1,10):
        start = time.time()
        f(i)

        print(int(time.time() - start), " seconds to run.")


main()
