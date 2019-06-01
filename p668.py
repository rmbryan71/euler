import math
import time
primeset = []

def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]


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


# def fast_is_root_smooth(i):
#     #is there a single prime factor of i greater than sqrt i?
#     r = math.ceil(math.sqrt(i))
#     for j in primes_range(r, i+1):
#         if i % j == 0:
#             # print("Not rs because ", j, " is a prime factor of ", i, " greater than ", r)
#             return False
#     return True


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


def fast_rs_range_counter(a, b):
    counter = 0
    for i in range(a, b+1):
        if fast_is_root_smooth(i):
            counter += 1
    return counter

upperbound = 100000000

start = time.time()
primeset = primes(upperbound)
end = time.time()
print(end - start, " seconds to populate the primes table up to ", upperbound)

# start = time.time()
# print(fast_rs_range_counter(1, upperbound))
# end = time.time()
# print(end - start, " seconds the new way.")
#
# start = time.time()
# print(rs_range_counter(1, upperbound))
# end = time.time()
# print(end - start, " seconds the old way.")


# for i in range(1, 100):
#     if not (is_root_smooth(i) == fast_is_root_smooth(i)):
#         print(i, is_root_smooth(i), fast_is_root_smooth(i))


