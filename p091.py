import math
from decimal import *
getcontext().prec = 6

# how many right triangles with integer coordinates for two points and third point at the origin

# what is the length of a line segement from 0,0 to x,y?

# what is the length of a line segement from x,y to a,b


def length(a, b, c, d):  #return length of segment with one endpoint at a, b other at c, d
    return Decimal(math.sqrt(((c - a) ** 2) + ((d - b) ** 2)))


def is_right(a, b, c, d):  #return true if points a, b and c, d form a right triangle with the origin
    j = Decimal(length(0, 0, a, b) ** 2)
    k = Decimal(length(0, 0, c, d) ** 2)
    h = Decimal(length(a, b, c, d) ** 2)
    print(j, k, h)
    if (j > 0 and k > 0 and h > 0) and ((j + k == h) or (j + h == k) or (h + k == j)):
        return True
    else:
        return False


gridsize = 8
count = 0

# print(length(0, 0, 2, 1))
# print(is_right(0, 0, 2, 1))


for i in range(0, gridsize + 1):
    for j in range(0, gridsize + 1):
        for l in range(0, gridsize + 1):
            for m in range(0, gridsize + 1):
                print(i, j, l, m, is_right(i, j, l, m))
                count += is_right(i, j, l, m)
print(int(count / 2))
