import numpy
import itertools
import time
import multiprocessing


def make_r_list(x):
    repunits = [1]
    repstring = '1'
    for i in range(2, x + 1):
        repstring = repstring + '1'
        repunits.append(int(repstring))
    return repunits


def is_no_fit(x, r):  # is there no member of r that divides equally by x?
    for z in r:
        if z % x == 0:
            return False
    return True


def A(x):
    start = time.time()
    if numpy.gcd(x, 10) > 1:
        return False
    z = 1
    for i in itertools.count(1):
        if z % x == 0:
            return i
        z = 10 * z + 1


def test():
    z = 1
    for i in range(1, 10):
        print(i, z)
        z = 10 * z + 1


assert A(7) == 6
assert A(41) == 5
assert A(17) == 16


p = multiprocessing.Pool

limit = 1000000
i = limit - 1
c = 1
while c <= limit:
    c = A(i)
    print(i, c)
    i += 2
print(i - 2)

