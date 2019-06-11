import math, sympy, time, multiprocessing, itertools, functools
import operator as op


# 1 is red
# 0 is gray
# reds must appear in groups of 3 or more
# groups of reds must have at least one gray between them
# no gray cell can cause a row to be invalid
# a red cell causes a row to be invalid if it is not in a set of 3 or more


def is_legal(x):  # takes a list and returns true if every cell follows the rules
    length = len(x)
    # print(length)
    for i in range(0, length):
        #  print(i)
        if x[i] == 1:
            if i == 0:
                if x[1] == 0 or x[2] == 0:
                    return False
            if i == 1:
                if not (x[0] == 1 and x[2] == 1):
                    if not(x[2] == 1 and x[3] == 1):
                        return False
            if 1 < i < (length - 2):
                if not (x[i-2] == 1 and x[i-1] == 1):
                    if not (x[i-1] == 1 and x[i+1] == 1):
                        if not (x[i+2] == 1 and x[i+1] == 1):
                            return False
            if i == (length - 2):
                if not (x[length - 4] == 1 and x[length - 3] == 1):
                    if not (x[length - 3] == 1 and x[length - 1] == 1):
                        return False
            if i == (length - 1):
                if not (x[length - 3] == 1 and x[length - 2] == 1):
                    return False
    return True


def main(z):
    start = time.time()

    count = 0
    for y in itertools.product([0, 1], repeat=z):
        if is_legal(y):
            count += 1
            #  print(y)
    # print("step ", z, "results", count, " ways to fill ", 2**z, " boxes", time.time() - start, " seconds to run.")
    print("step ", z, "results", count)


for i in range(26, 50):
    main(i)
