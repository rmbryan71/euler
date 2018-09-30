import math
import timeit

def brute_1(x):
    global_max = 0

    for i in range(2, x):
        i_count = 0
        for j in range(1, i):
            if math.gcd(i, j) == 1:
                i_count +=1
        if i/i_count > global_max:
            global_max = i/i_count
            print(i, i/i_count)
        if i % 1000 == 0:
            print(i)


def my_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def my_coprime(a, b):
    return my_gcd(a, b) == 1

def brute_2(x):
    global_max = 0

    for i in range(2, x):
        i_count = 0
        for j in range(1, i):
            if my_coprime(i, j):
                i_count += 1
        if i/i_count > global_max:
            global_max = i/i_count
            print(i, i/i_count)
        if i % 1000 == 0:
            print(i)


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


def euler_method(x):
    global_max = 0
    global_max_index = 0

    for i in range(2, x):
        totient = i / phi(i)
        if totient > global_max:
            global_max = totient
            global_max_index = i
            print(i, totient)
        if i % 1000 == 0:
            print(i)
    print(global_max, global_max_index)

print(euler_method(1000000))