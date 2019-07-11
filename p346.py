import math

def tostr(n, base):
    convertstring = "0123456789ABCDEF"
    if n < base:
        return convertstring[n]
    else:
        return tostr(n//base, base) + convertstring[n % base]


def f(x, y):  # return True if x is a repunit in base y
    if x <= y:
        if x == 1:
            return True
        else:
            return False
    if x % y != 1:
        return False
    else:
        return f(x // y, y)


def g(x):  # return True if x is a strong repunit
    if x == 1:
        return True
    count = 0
    for i in range(2, x):
        count += f(x, i)
        if count == 2:
            return True
    return False

#
# sum = 0
# for i in range(1, 10**10):
#     if g(i):
#         sum += i
#         print(i, sum, int(i*100)//10**12)
# print(sum)

# Maybe it would be faster to make all the base 2 repunits, then base 3 repunits,

#oeis A053696


def gen(limit):
    b = 2
    while (b^3 - 1)/(b-1) <= limit:
        k = 3

        print(b)

gen(10000)
