import sympy, numpy
count = 1
limit = 2000
n = 0
number = 0

while count < limit:
    n += 1
    if sympy.isprime(6 * n - 1) and sympy.isprime(6 * n + 1) and sympy.isprime(12 * n + 5):
        count += 1
        number = 3 * n * n - 3 * n + 2
        if count <= limit:
            break
    if sympy.isprime(6 * n + 5) and sympy.isprime(6 * n - 1) and sympy.isprime(12 * n - 7) and n is not 1:
        count += 1
        number = 3 * n * n - 3 * n + 2
print(number, count, n)

