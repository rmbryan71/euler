from functools import reduce

def sumfactors(n):
    return sum(reduce(list.__add__, ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0))) - n

def chaincheck(n):
    print(sumfactors(n), chaincheck(sumfactors(n)))

print(chaincheck(220))