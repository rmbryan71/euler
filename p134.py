import itertools
import sympy

# least n for which the last digits are p1 and n is divisible by p2
# start generating multiples of p2 and check for "last digits" == p1

primes = list(sympy.primerange(5, 1000003))


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
    for i in itertools.count(1000000):
        x = b * i  # x is a multiple of b
        if str(x)[-len_a:] == str(a):
            return x


def exgcd(a,b):
    x = 0
    lastx = 1
    y = 1
    lasty = 0
    while b != 0:
        quotient = a/b
        a, b = b, a%b
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient *y, y
    return lastx, lasty, a


def n3(p1, p2):  # input is two consecutive primes
    a = len(str(p1))
    b = p2 - p1
    n = p2
    r, s, d = exgcd(a, n)
    x = r * b
    x = x % n
    return x * a + p1


#
# for j in range(0, 10):
#     a = primes[j]
#     b = primes[j + 1]
#     print(a, b, n(a, b))


result = 0
# for j in range(0, len(primes) - 1):
for i in range(1, len(primes) - 1):
    a = primes[i]
    b = primes[i+1]
    # c = n(a, b)
    d = n3(a, b)
    result += d


print("Result:", result)
