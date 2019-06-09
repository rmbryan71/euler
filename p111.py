import math, sympy, time, multiprocessing


def populate_prime_table():  # turns out to be a bad idea, don't use.
    with open('primes.txt', "a") as myfile:
        for prime in sympy.primerange(0, 10**10):
            myfile.write(str(prime))
            myfile.write(", ")


def m(n, d):  # naive max repeated digits(d) for an n-digit number
    lower_bound = 10**(n-1)
    upper_bound = 10**n - 1
    result = 0
    for x in sympy.primerange(lower_bound, upper_bound+1):
        if str(x).count(str(d)) > result:
            result = str(x).count(str(d))
            #  print(str(x), str(d), result)
    return result


def m10(d):  # naive array of digits and max repetitions of digits in a d-digit number
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
        max = 0
        for prime in primes:
            count = (str(prime).count(str(i)))
            #  print("count of ", str(i), " in ", str(prime), " is ", count)
            if count > max:
                max = count
                #  print("new max is ", max, " for ", i)
        result.append(max)
    return(result)


def main():
    start = time.time()

    print([m(6, x) for x in range(0, 9)])

    print(int(time.time() - start), " seconds to run.")

main()