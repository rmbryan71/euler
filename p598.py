from collections import defaultdict
from fractions import Fraction as fr

# The relevant prime values
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83,
          89, 97]

# The multiplicities d from the decomposition of 100!
multiples = [97, 48, 24, 16, 9, 7, 5, 5, 4, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]


# Compute the largest prime factor of n
def max_prime_fact(n):
    i = 0
    while n != 1:
        if n % primes[i] == 0:
            n = n // primes[i]
        else:
            i += 1
    return primes[i]


# Construct a dictionary of all possible fractions from the most common factor
d = defaultdict(int)
for j in range(0, multiples[0] // 2 + 1):
    d[fr(multiples[0] - j + 1, j + 1)] += 1

# Consider the most common prime factors first
for i in range(1, len(multiples) - 1):
    new = defaultdict(int)
    mult = multiples[i]

    # Using the current multiplicity and the old dictionary of fractions build
    # the new dictionary of fractions
    for j in range(0, mult + 1):
        for key in d:
            value = key * fr(mult - j + 1, j + 1)

            # Do not store fractions containing prime factors that cannot cancel later
            if max_prime_fact(value.numerator) <= multiples[i + 1] + 1:
                if max_prime_fact(value.denominator) <= multiples[i + 1] + 1:
                    new[value] += d[key]
    d = new

# The result
print(d[fr(1, 2)] + d[fr(2, 1)])