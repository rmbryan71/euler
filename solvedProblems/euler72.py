# import time
#
# a = 1 / 2
# b = 3 / 5
# c = 2 / 3
#
# my_set = {a, b, c}
#
# upper_bound = 1000000
#
#
# start = time.time()
#
# for i in range(upper_bound + 1, 1, -1):
#     for j in range(2, i + 1):
#         my_set.add(i / j)
#     #print(i, len(my_set))
#     if i % 10000 == 0:
#         snap = time.time()
#         elapsed = snap - start
#         print(int(elapsed / 60), upper_bound - i)
#
# print(len(my_set))


def phi(n):
    result = n

    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n = int(n / p)
            result -= int(result / p)
        p += 1
    if n > 1:
        result -= int(result / n)
    return result


def phi_sum(n):
    result = 0
    for x in range(2, n + 1):
        result += phi(x)
    return result

print(phi_sum(1000000))
