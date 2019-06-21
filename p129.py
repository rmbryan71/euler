import numpy
import itertools
import time


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


def find_least_n(x):
    start = time.time()
    repunits = make_r_list(x)
    print("Repunits list is built", int(time.time()-start))
    for i in itertools.count(1, 2):
        print(i)
        if numpy.gcd(i, 10) == 1:
            if is_no_fit(i, repunits):
                return i



print(find_least_n(1000000))



