import itertools
import sympy

# least n for which the last digits are p1 and n is divisible by p2
# start generating multiples of p2 and check for "last digits" == p1

primes = list(sympy.primerange(5, 1000003))
# primes = list(sympy.primerange(5, 1003))
primes_2 = sympy.primerange(5, 10000000)
# primes = list(sympy.primerange(5, 103))


def n(a, b):  # given two primes, return their n
    len_a = len(str(a))
    for i in itertools.count(1):
        x = b * i  # x is a multiple of b
        if str(x)[-len_a:] == str(a):
            return x


def n2(a, b):  # given two primes, return their n
    len_a = len(str(a))
    for i in primes_2:
        x = b * i  # x is a multiple of b
        if str(x)[-len_a:] == str(a):
            return x


#
# for j in range(0, 10):
#     a = primes[j]
#     b = primes[j + 1]
#     print(a, b, n(a, b))


result = 0
# for j in range(0, len(primes) - 1):
for i in range(1, len(primes)):
    a = primes[i]
    b = primes[i+1]
    # c = n(a, b)
    d = n(a, b)
    result += d
    print(a, b, d)

print("Result:", result)