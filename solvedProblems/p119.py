import time
import itertools
import math
import sympy
# import functools
# import operator as op


def dig_sum(x):  # return the sum of digits of x
    result = 0
    for char in str(x):
        result += int(char)
    return result


def is_power_of(y, x):  # True if x is some power of nontrivial y
    if y is 1:
        return False
    while x % y == 0:
        x = x / y
    return x == 1


# x is the big number
def beta_is_power_of(y, x):  # need a faster check based on log y(x) is int
    y = math.log(y)
    if y == 0:
        return False
    d = math.log(x) / y
    return d == int(d)


def is_valid(n):
    dsum = sum(map(int, str(n)))
    return dsum ** int(round(math.log(n, dsum))) == n if dsum > 1 else n < 2


def sympy_test(x):
    return sympy.is_Pow


def is_dig_sum_pow(x):  # True if x is a digit sum power
    return is_power_of(dig_sum(x), x)


def main():
    start = time.time()
    assert is_power_of(8, 512)
    assert is_power_of(28, 614656)
    assert not is_power_of(6, 37)
    assert beta_is_power_of(8, 512)
    assert beta_is_power_of(28, 614656)
    assert not beta_is_power_of(6, 37)
    assert dig_sum(512) is 8
    assert dig_sum(614656) is 28
    assert is_dig_sum_pow(512)
    assert is_dig_sum_pow(614656)
    assert not is_dig_sum_pow(37)
    assert not is_dig_sum_pow(39847239874)
    assert is_valid(3904305912313344)

    # a = []
    # for i in range(11, 614657):
    #     if is_dig_sum_pow(i):
    #         a.append(i)
    # print(a)

    # a = []
    # i = 11
    # while len(a) < 30:
    #     if is_dig_sum_pow(i):
    #         a.append(i)
    #         print(len(a))
    #     i += 1
    # print(a)
    # print(a[30])

    # a = []
    # i = 11
    # target = 12
    # while len(a) < target:
    #     if is_valid(i):
    #         print(len(a), i, int(time.time() - start))
    #         a.append(i)
    #     i += 1
    # print("a sub", target, "is", a[target - 1])

    valid_list = []
    while len(valid_list) < 31:
        for a in range(100):
            for b in range(100):
                c = a**b
                if len(str(c)) > 1:
                    if dig_sum(c) == a:
                        if c not in valid_list:
                            valid_list.append(c)

    valid_list.sort()
    print(valid_list)
    print(valid_list[30])


    print(int(time.time() - start), " seconds to run.")


main()
