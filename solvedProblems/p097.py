# find the last 10 digits of 28433×2^7830457+1
import numpy


x = (28433 * (2 ** 7830457)) + 1

y = x % 10000000000

print(y)
