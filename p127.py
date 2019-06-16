import sympy, numpy


def rad(x):
    return numpy.prod(sympy.primefactors(x))

print(numpy.gcd(5,27))
print(rad(504))

