import math, sympy, time, multiprocessing, itertools
import numpy as np


def populate_prime_table():  # turns out to be a bad idea, don't use.
    with open('primes.txt', "a") as myfile:
        for prime in sympy.primerange(0, 10**10):
            myfile.write(str(prime))
            myfile.write(", ")


def m(n, d):  # naive max repeated digits(d) for an n-digit number
    #  returns correct results for 5 digit numbers in 2 seconds
    #  6 digit numbers take 33 seconds
    #  I think this is O(n), so project 7 digits = 300 seconds, 8: 3000, 9:30000, 10:300000 seconds
    #  probably 83 hours for 10 digits
    lower_bound = 10**(n-1)
    upper_bound = 10**n - 1
    result = 0
    for x in sympy.primerange(lower_bound, upper_bound+1):
        if str(x).count(str(d)) > result:
            result = str(x).count(str(d))
            #  print(str(x), str(d), result)
    return result


def m10(d):  # naive array of digits and max repetitions of digits in a d-digit number
    #  not useful. would take longer than a minute (I think it would take 6 hours)
    #  to build the prime table
    lower_bound = 10**(d-1)
    upper_bound = 10**d - 1
    result = []
    primes = []
    inner_start = time.time()
    print("Starting to build prime table from ", lower_bound, " to ", upper_bound)
    for prime in [x for x in sympy.primerange(lower_bound, upper_bound+1)]:
        primes.append(prime)
    print("prime table took ", time.time() - inner_start)
    for i in range(0, 10):
        maxcount = 0
        for prime in primes:
            count = (str(prime).count(str(i)))
            #  print("count of ", str(i), " in ", str(prime), " is ", count)
            if count > maxcount:
                maxcount = count
                #  print("new max is ", max, " for ", i)
        result.append(maxcount)
    return result


def f(x, y):  # returns all prime 10-digit numbers with x or more repetitions of digit y
    result_list = []
    fillercount = 10 - x
    digit_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    fillers = itertools.product(digit_list, fillercount)
    repeat_list = list(itertools.repeat(y, x))
    for fill in fillers:
        test_list = list(repeat_list + list(fill))
        test_set = list(set(itertools.permutations(test_list)))
        for test in test_set:
            mystr = ""
            for digit in test:
                mystr += str(digit)
            if sympy.isprime(int(mystr)) and len(str(int(mystr))) == 10:
                # print(int(mystr), " is prime and has ", x, " or more repetitions of the digit ", y)
                result_list.append(int(mystr))
    return result_list


def g(x):  # returns max number of repeated digit for a 10 digit prime for digit x
    for i in range(10, 1, -1):
        if len(f(i, x)) > 0:
            return i


def main():
    start = time.time()

    #f(9, 6)
    # print(g(0))

    #  print([m(6, x) for x in range(0, 9)])
    answer = 0
    # answer += (sum(f(9, 9)))
    #
    for i in range(0, 10):
        M = g(i)
        solutions = f(M, i)
        N = len(solutions)
        S = sum(solutions)
        print(i, M, N, S, solutions)
        answer += S

    print(answer)

    print(int(time.time() - start), " seconds to run.")


main()
