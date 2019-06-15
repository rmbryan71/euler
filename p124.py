import sympy
import numpy


def rad(x):
    return numpy.prod(sympy.primefactors(x))

print(sorted(range(1,100001), key=rad)[10000-1])

#
# with open('p124.txt', 'w+') as f:
#     for i in range(1, 100001):
#         f.write(str(i) + "," + str(rad(i)))
#         f.write('\n')
#     f.close()


