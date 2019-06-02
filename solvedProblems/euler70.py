import itertools

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


def is_permutation(a, b):
    a_ascending = "".join(sorted(str(a)))
    b_ascending = "".join(sorted(str(b)))
    return a_ascending == b_ascending


def min_filter_first(z):
    global_minimum_ratio = 100
    global_minimum_index = 0

    for x in range(z, 2, -1):
        if x / phi(x) < global_minimum_ratio:
            # is phi(x) a permutation of x?
            if is_permutation(x, phi(x)):
                # print(x, phi(x))
                global_minimum_ratio = x / phi(x)
                global_minimum_index = x
    return global_minimum_index, global_minimum_ratio


def perm_filter_first(z):
    global_minimum_ratio = 100
    global_minimum_index = 0

    for x in range(2, z):
        if is_permutation(x, phi(x)):
            if x / phi(x) < global_minimum_ratio:
                # print(x, phi(x))
                global_minimum_ratio = x / phi(x)
                global_minimum_index = x
    return global_minimum_index, global_minimum_ratio


scope = 10 ** 7

# print(perm_filter_first(scope))
print(min_filter_first(scope))



