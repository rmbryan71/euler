import math
import decimal


# def f(x):
#     z = ((math.sqrt((8 * (x ** 2)) - (8 * x) + 1)) - (2 * x) + 1) / 2
#     y = ((math.sqrt((8 * (x ** 2)) - (8 * x) + 1)) - (2 * x) + 1) // 2
#     if abs(z - y) < 10**-200:
#         return y
#     else:
#         return 0
#
#
# for blue in range(707106459000, 7071064591000):
#     red = f(blue)
#     if red > 0:
#         total = red + blue
#         print(red, blue, total)
#         if total >= 1000000000000:
#             print("done, answer is:")
#             print(blue)
#             break

b = 15
n = 21

while True:
    btemp = (b * 3) + (2 * n) - 2
    ntemp = (b * 4) + (3 * n) - 3
    print(btemp)
    b = btemp
    n = ntemp
    if n > 10**12:
        break
