import time, sympy, multiprocessing, math

# build a set of primes to work from
# primes = [2, 3, 5, 7, 11, 13, 17]
start = time.time()
primes = list(sympy.primerange(0, 100))
print("primes up to ", primes[-1], " took ", time.time() - start, " seconds.")


# start = time.time()
# int_floor = 1
# int_limit = 100
# ints = list(range(int_floor, int_limit))
# print("ints up to ", int_limit - int_floor, " took ", time.time() - start, " seconds.")


def exponents_of_factors(n):
    exp = []
    counter = 0
    for i in range(0, len(primes)):
        while n % primes[i] == 0:
            n = n / primes[i]
            counter += 1
        if counter > 0:
            exp.append(counter)
            counter = 0
    return exp


def d(n):
    exp = exponents_of_factors(n)
    total = 1
    for i in range(0, len(exp)):
        total *= exp[i] + 1
    return total


def d2(n, primes):
    nod = 1
    remain = n
    


start = time.time()
i = 1
while d(i ** 2) / 2 <= 4000000:
    i += 1

print(i, "is the answer.")
print('Searching took ' + str(time.time() - start) + ' seconds to run.')
