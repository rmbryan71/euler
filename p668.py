import math
import time
import multiprocessing


def maxpfactor(n):
    maxprime = -1
    if n == 0:
        return 0

    while n % 2 == 0:
        maxprime = 2
        n >>= 1  # equivalent to n /= 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            maxprime = i
            n = n / i

    if n > 2:
        maxprime = n

    return int(maxprime)


def is_root_smooth(i):
    if maxpfactor(i) < math.sqrt(i):
        return True
    else:
        return False


def root_smooth_counter(y):
    counter = 0
    for i in range(1, y+1):
        if is_root_smooth(i):
            counter += 1
    return counter


def rs_range_counter(a, b):
    counter = 0
    for i in range(a, b+1):
        if is_root_smooth(i):
            counter += 1
    return counter

start = time.time()
print(rs_range_counter(1, 1000000))
end = time.time()
print(end - start, " seconds.")