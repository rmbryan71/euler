import sympy

n = 50000000
result = 2
primes = sympy.primerange(1, n)

for prime in primes:
    if prime < (n // 4):
        result += 1
    if prime < (n // 16):
        result += 1
    if (prime - 3) % 4 == 0:
        result += 1
print(result)

# n = 50000000
# solutions = []
# for u in range(1, n):
#     for v in range(1, n):
#         if u * v > n:
#             break
#         if (u + v) % 4 == 0:
#             if (3 * v) > u:
#                 if ((3 * v - u) % 4) == 0:
#                     solutions.append(u * v)
#
# uniques = [x for x in solutions if solutions.count(x) == 1]
# print(len(uniques))
