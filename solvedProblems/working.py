from sympy.ntheory import npartitions
import time

#I got tired of making two different files for every problem, so I'll just work all in one file from now on.


# October 2, 2018 6:32:30 AM : Starting euler 77
# Difficulty is 25%
# What is the first value which can be written as the sum of primes in over five thousand different ways?
# Need to make a list of the first 50k prime numbers or so, then use those as primes in the same was as euler 31 does.


primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]


def count_ways(k, n, primes):
    if k == 0:
        if n % primes[0] == 0:
            return 1
        else:
            return 0
    else:
        c = 0
        for i in range(n // primes[k] + 1):
            c += count_ways(k - 1, n - i * primes[k], primes)
        return c


def euler77():
    for z in range(2, 500):
        print(z, count_ways(len(primes) - 1, z, primes))
# euler77()


# October 3, 2018 7:14:48 AM : Starting euler 78
# 30% difficulty (my highest so far)
# Let p(n) represent the number of different ways in which n coins can be separated into piles.
# For example, five coins can be separated into piles in exactly seven different ways, so p(5)=7.
# Find the least value of n for which p(n) is divisible by one million.
# I am reading: https://en.wikipedia.org/wiki/Partition_%28number_theory%29
# using : https://oeis.org/A000041

euler78answer = 0
while True:
    euler78answer += 1
    if npartitions(euler78answer) % 1000000 == 0:
        print(euler78answer)
        break
    if euler78answer % 1000 == 0:
        print(euler78answer, " , no.")





    




