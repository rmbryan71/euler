import math
import sympy
import itertools

from math import *
from fractions import gcd


def is_square(n):
    return int(sqrt(n)) == sqrt(n)


# r < d < q
# a > b , a/b = c
# because d^2 = q*r
# cb^2 < cab < ca^2
# n = cabca^2 + cb^2 = a^3*c*2*b + b^2*c = a*a*a*c*c*b + b*b*c
L = 10 ** 12
progressiveSquares = set()
sum_progressive_squares = 0
for a in range(2, int(L ** (1 / 3.) + 1)):
    for b in range(1, a):
        if a * a * a * b * b + b * b >= L: break
        c = 1
        n = a * a * a * c * c * b + b * b * c
        while n < L:
            n = a * a * a * c * c * b + b * b * c
            if is_square(n) and n not in progressiveSquares:
                progressiveSquares.add(n)
                sum_progressive_squares += n
                print(n, b * b * c, a * b * c, a * a * c)
            c += 1

print(sorted(progressiveSquares))
print("answer", sum(progressiveSquares))
print("sum_progressive_squares", sum_progressive_squares)