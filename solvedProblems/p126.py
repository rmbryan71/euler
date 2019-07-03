import numpy
import numpy.polynomial.polynomial as poly

x = numpy.array([22, 46, 78, 118, 154])
x_new = numpy.array([22, 46, 78, 118, 1000])
y = numpy.array([2, 4, 5, 8, 10])
#
# print(numpy.cbrt(22))
# print(numpy.cbrt(46))
# print(numpy.cbrt(78))
# print(numpy.cbrt(118))
# print(numpy.cbrt(154))
# print(numpy.cbrt(1000))

coeffs = poly.polyfit(x, y, 1)
ffit = poly.polyval(x_new, coeffs)
#print(ffit)


def C(x, y, z, n):
    return 2*(x*y + y*z + x*z) + 4*(x+y+z + n -2)*(n-1)

print(C(3,2,1,8))