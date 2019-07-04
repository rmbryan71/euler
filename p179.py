import time
import math


def countfactors(x):
    count = 1
    for i in range(1, x//2 + 1):
        if x % i == 0:
            count += 1
    return count


def main():
    start = time.time()
    count = 0
    for i in range(1, 1000):
        if countfactors(i) == countfactors(i + 1):
            count += 1
            print(count, i)
    end = time.time()
    print(end - start)
    print(count)

main()
