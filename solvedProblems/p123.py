import sympy


def p(n):
    return sympy.prime(n)


def r(n):
    return ((p(n)-1)**n + (p(n)+1)**n) % (p(n))**2


c = 0
## always start with and odd number i
i = 7001
while c < 10**9:
    c = r(i)
    i += 2
    print(i, c)
print(i)

# 10**6 == 281
# 10**7 == 809
# 10**8 == 2373
# 10**9 == 7037
# 10**10 ==