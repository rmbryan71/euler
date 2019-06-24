import sympy

n = 50000000
result = 2
primes = sympy.primerange(1, n)

for prime in primes:
    if prime < n / 4:
        result += 1
    if prime < n / 16:
        result += 1
    if (prime - 3) % 4 == 0:
        result += 1

print(result)