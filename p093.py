from operator import add, sub, mul, truediv
from itertools import permutations, combinations, product
# ops = {'-', '+', '*', '/'}
# digits = {1, 2, 3, 4}


# def check(a, b, c, d, x): # can digits a, b, c, d be combined to form int x?
#     if not (a < b < c < d < 10):
#         raise Exception('check function received improper combination')
#     if (d - c) / (b - a) == x:
#         return True
#     if (d - c) * b * a == x:
#         return True
#     if (d - ((c - b) * a)) == x:
#         return True
#     if ((d / a) * (c - b)) == x:
#         return True
#     return False
#
# for i in range(1, 10):
#     print(i, check(1, 2, 3, 4, i))

# for set in itertools.combinations(digits, 4):
#     for each in itertools.permutations(set):
#         for op in itertools.combinations_with_replacement(ops, 3):
#             print(each[0], op[0], each[1], op[1], each[2], op[2], each[3])

# oplist = (add, sub, mul, truediv)
# bracketings = (
# 	lambda f,g,h, a,b,c,d: f(a,g(b,h(c,d))),
# 	lambda f,g,h, a,b,c,d: f(a,g(h(b,c),d)),
# 	lambda f,g,h, a,b,c,d: f(g(a,b),h(c,d)),
# 	lambda f,g,h, a,b,c,d: f(g(a,h(b,c)),d),
# 	lambda f,g,h, a,b,c,d: f(g(h(a,b),c),d)
# 	)
#
# def findresults(digitlist):
#     results = set()
#     for digits in permutations(digitlist, 4):
#         for ops in product(oplist, oplist, oplist):
#              for f in bracketings:
#                 try:
#                     result = f(*ops, *digits)
#                 except:
#                     continue
#                 if result>0 and int(result)==result:
#                     results.add(int(result))
#     return results
#
# def runlength(s):
#     i = 0; while i+1 in s: i+=1
#     return i
#
# print(max(combinations(range(1,10),4),
#           key=lambda d: runlength(findresults(d))))


import time, itertools

start = time.time()
max_combo = [0, ()]
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def operate(x, y, case):
    if case == 1:
        return x + y
    elif case == 2:
        return x - y
    elif case == 3:
        return x * y
    elif case == 4 and y != 0:
        return x / y
    else:
        return 0


for z in list(itertools.combinations(digits, 4)):  # All the possible strings
    numbers = set()
    for x in list(itertools.permutations(z)):
        for y in list(itertools.product([1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4])):  # Different operators
            numbers.add(operate(operate(operate(x[0], x[1], y[0]), x[2], y[1]), x[3], y[2]))  # abcd
            numbers.add(operate(operate(x[0], operate(x[1], x[2], y[1]), y[0]), x[3], y[2]))  # a(bc)d
            numbers.add(operate(operate(x[0], x[1], y[0]), operate(x[2], x[3], y[2]), y[1]))  # ab(cd)
            numbers.add(operate(x[0], operate(operate(x[1], x[2], y[1]), x[3], y[2]), y[0]))  # a(bcd)
            numbers.add(operate(x[0], operate(x[1], operate(x[2], x[3], y[2]), y[1]), y[0]))  # a(b(cd))
    numbers = sorted(list(numbers))
    integers = []
    for item in numbers:
        if item == int(item) and item >= 1:
            integers.append(item)
    counter = 1
    while True:
        if counter in integers:
            counter += 1
        else:
            break
    if counter > max_combo[0]:
        max_combo = (counter, z)

print(max_combo, "found in", time.time() - start, "seconds")


