from fractions import *
def conv_of_e(x):
     period = []
     e = Fraction(0,1)
     for i in range(x - 1):
          if i % 3 == 1:
               period.append(2 * (i + 2) // 3)
          else:
               period.append(1)
     for i in period[::-1]:
          e += i
          e = 1 / e
     e += 2
     return e

e_ = list(str(conv_of_e(100).numerator))
sum_ = 0
for i in e_:
     sum_ += int(i)

print(sum_)