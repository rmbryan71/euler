import math, sympy, time, multiprocessing, itertools
import numpy as np


def is_bouncy(x):  # Takes a number. True if it's bouncy, False if not.
    digits = [int(i) for i in str(x)]
    directions = []
    for i in range(0, len(digits)-1):
        if digits[i] > digits[i+1]:
            # print("down ")
            directions.append(-1)
        if digits[i] < digits[i+1]:
            # print("up ")
            directions.append(1)
    # print(directions)
    if len(set(directions)) > 1:
        return True
    else:
        return False


def is_b(x):
    s=''.join(sorted(x))
    return not(x == s or x[::-1] == s)


def count_bouncy(x):  # Returns the count of bouncy numbers below x
    sum = 0
    for i in range(1, x + 1):
        sum += is_bouncy(i)
    return sum


def is_half_bouncy(x):  # Returns true if half of the numbers below are bouncy
    goal = x // 2
    if (count_bouncy(x) >= goal):
        return True
    else:
        return False


def percent_bouncy(x):  # Returns percentage of the numbers below x which are bouncy
    return count_bouncy(x)/x


def main():
    start = time.time()
    #print(count_bouncy(538))
    #print(percent_bouncy(21780))

    # for x in itertools.count(1, step=1):  # my original solution, gets the right answer but takes hours
    #     y = percent_bouncy(x)
    #     print(x, y)
    #     if (y >= .99):
    #         break

    c = 0.  # This uses my is_bouncy function with the iterator and conditions from the fast solution
    i = 99
    while c/i<.99:
        i += 1
        if is_bouncy(str(i)):
            c += 1
    print(i)




    # c = 0.  # This code finds the correct answer in 2 seconds.
    # i = 99
    # while c/i<.99:
    #     i += 1
    #     if is_b(str(i)):
    #         c += 1
    # print(i)

    print(int(time.time() - start), " seconds to run.")


main()
