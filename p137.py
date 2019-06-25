import math


def F(n):
    return int(((1+math.sqrt(5))**n-(1-math.sqrt(5))**n)/(2**n*math.sqrt(5)))


def G(n):
    return(F(2 * n) * F((2 * n) + 1))


for i in range(1, 16):
    print(i, G(i))


