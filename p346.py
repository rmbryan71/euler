# oeis A053696
import math
import fractions
import time

# def tostr(n, base):
#     convertstring = "0123456789ABCDEF"
#     if n < base:
#         return convertstring[n]
#     else:
#         return tostr(n//base, base) + convertstring[n % base]
#
#
# def f(x, y):  # return True if x is a repunit in base y
#     if x <= y:
#         if x == 1:
#             return True
#         else:
#             return False
#     if x % y != 1:
#         return False
#     else:
#         return f(x // y, y)
#
#
# def g(x):  # return True if x is a strong repunit
#     if x == 1:
#         return True
#     count = 0
#     for i in range(2, x):
#         count += f(x, i)
#         if count == 2:
#             return True
#     return False
#
#
# def gsum(x):  # return sum of strong repunits < x
#     start = time.time()
#     result = 0
#     for i in range(1, x):
#         if g(i):
#             result += i
#             print(i, result, int(i*100)//x)
#     seconds = int(time.time() - start)
#     print("elapsed seconds", seconds)
#     print(x / 10**8, "fraction of 10^8")
#     print(((10**8 / x) * seconds) / 60, "estimated minutes for 10^8")
#     return result
#
#
# print(gsum(10**5))
# A linear crawl solution would take longer than 13 days to do 10^8
# so 130000 days to do 10^12, which is 355 years.
# I am going to need a different approach


def gen(x):  # generate all A053696 numbers less than x using (b^n-1)/(b-1), return their sum
    result = [1]
    for n in range(3, 40):
        for b in range(2, 1 + int(math.sqrt(x))):
            y = fractions.Fraction((b ** n - 1), (b - 1))
            # y = ((b ** n - 1) / (b - 1))
            if int(y) == y:
                y = int(y)
                if y < x:
                    # print(n, b, y)
                    result.append(y)
    return sorted(result)


start = time.time()
print(sum(gen(10**12    )), int(time.time() - start))



