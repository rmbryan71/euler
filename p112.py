import math, sympy, time, multiprocessing, itertools
import numpy as np


def is_bouncy(x):  # True if it's boucy, False if not.
    return True


def main():
    start = time.time()
    is_bouncy(1)

    print(int(time.time() - start), " seconds to run.")


main()
