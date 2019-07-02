import math
import itertools


def f(x):  # true if satisfies conditions of problem
    x = str(x)
    if len(x) < 19:
        return False
    print(x, x[0], x[2], x[4], x[6],)
    if x[0] == 1 and x[2] == 2 and x[4] == 3 and x[6] == 4:
        return True
    else:
        return False


def is_square(n):
    ## Trivial checks
    if type(n) != int:  ## integer
        return False
    if n < 0:      ## positivity
        return False
    if n == 0:      ## 0 pass
        return True

    ## Reduction by powers of 4 with bit-logic
    while n&3 == 0:
        n=n>>2

    ## Simple bit-logic test. All perfect squares, in binary,
    ## end in 001, when powers of 4 are factored out.
    if n&7 != 1:
        return False

    if n==1:
        return True  ## is power of 4, or even power of 2


    ## Simple modulo equivalency test
    c = n%10
    if c in {3, 7}:
        return False  ## Not 1,4,5,6,9 in mod 10
    if n % 7 in {3, 5, 6}:
        return False  ## Not 1,2,4 mod 7
    if n % 9 in {2,3,5,6,8}:
        return False
    if n % 13 in {2,5,6,7,8,11}:
        return False

    ## Other patterns
    if c == 5:  ## if it ends in a 5
        if (n//10)%10 != 2:
            return False    ## then it must end in 25
        if (n//100)%10 not in {0,2,6}:
            return False    ## and in 025, 225, or 625
        if (n//100)%10 == 6:
            if (n//1000)%10 not in {0,5}:
                return False    ## that is, 0625 or 5625
    else:
        if (n//10)%4 != 0:
            return False    ## (4k)*10 + (1,9)


    ## Babylonian Algorithm. Finding the integer square root.
    ## Root extraction.
    s = (len(str(n))-1) // 2
    x = (10**s) * 4

    A = {x, n}
    while x * x != n:
        x = (x + (n // x)) >> 1
        if x in A:
            return False
        A.add(x)
    return True


for a in range(0, 10):
    for b in range(0, 10):
        for c in range(0, 10):
            for d in range(0, 10):
                for e in range(0, 10):
                    for f in range(0, 10):
                        for g in range(0, 10):
                            for h in range(0, 10):
                                for i in range(0, 10):
                                    x = str('1' + str(a) + '2' + str(b) + '3' + str(c) + '4' + str(d) + '5' + str(e) + '6' + str(f) + '7' + str(g) + '8' + str(h) + '9' + str(i) + '0')
                                    if is_square(int(x)):
                                        print(int(x), math.sqrt(int(x)))

