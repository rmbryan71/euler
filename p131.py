import sympy


def find_cube_root(n):
    lo = 0
    hi = n
    while lo < hi:
        mid = (lo+hi)//2
        if mid**3 < n:
            lo = mid+1
        else:
            hi = mid
    return lo


def is_perfect_cube(n):
    return find_cube_root(n)**3 == n


def p131():
    for i in sympy.primerange(1, 100):
        for j in range(1, 100):
            if is_perfect_cube((j ** 3) + (j * j * i)):
                print(i, j)


def p131b(limit):
    count = 0
    for i in range(1, limit):
        n = (((i + 1) ** 3) - (i ** 3))
        if sympy.isprime(n):
            count += 1
            print(count, n)
        if n >= limit:
            break
    return count

print(p131b(1000000))