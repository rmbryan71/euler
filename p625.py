from sympy.ntheory import totient, divisors

limit = 10**4
print((sum([sum([n*totient(d)//d for d in divisors(n)]) for n in range(1, limit)]) % 998244353))