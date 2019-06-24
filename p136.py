import sympy

# n = 50000000
# result = 2
# primes = sympy.primerange(1, n)
#
# for prime in primes:
#     if prime < n / 4:
#         result += 1
#     if prime < n / 16:
#         result += 1
#     if (prime - 3) % 4 == 0:
#         result += 1

# n = 50000000
n = 100
solutions = []

for u in range(1, n):
    for v in range(1, n // u):
        if (u + v) % 4 == 0 and  3 * v  > u and ((3 * v - u) % 4) == 0:
            z = u * v
            if z not in solutions:
                solutions.append(z)

print(len(solutions))