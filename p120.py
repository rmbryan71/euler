import math
import multiprocessing
import time


def f(a, n):
    return ((a-1)**n + (a+1)**n) % (a**2)


def max_f(a):
    max = 0
    for x in range(a**2):
        if f(a, x) > max:
            max = f(a, x)
    return max

def beta_max_f(x):
    return x**3*(-6 - 2*x)/((x + 1)**2*(x - 1)**3)

start = time.time()
p = multiprocessing.Pool()
my_range = range(3, 50)
maxes = p.map(beta_max_f, my_range)
print(list(maxes))
print(int(time.time() - start), "seconds")
