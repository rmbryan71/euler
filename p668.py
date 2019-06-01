import math
import time

def maxPFactor(n):
    maxPrime = -1

    # Print the number of 2s that divide n
    while n % 2 == 0:
        maxPrime = 2
        n >>= 1  # equivalent to n /= 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            maxPrime = i
            n = n / i

    if n > 2:
        maxPrime = n

    return int(maxPrime)


def is_root_smooth(i):
    if (maxPFactor(i) < math.sqrt(i)):
        return True
    else:
        return False


def root_smooth_counter(y):
    counter = 0
    for i in range(1, y+1):
        if is_root_smooth(i):
            counter += 1
    return counter


upperlimit = 10000000000

#print (int(upperlimit*(1-math.log(2))))


def Hildebrand(x):
    #return int(((1-math.log(2)) * x) + (x / math.log(x)))
    return int((1-math.log(2)) * x)


#for i in range(1000000, 2000000, 10000):
#    a = root_smooth_counter(i)
#    b = Hildebrand(i)
#    print(a, b, a-b, i, int(100*(a-b)/i))

# def Sqrtspeedtest(x):
#     start_time = time.time()
#     for i in range(0, x):
#         y = math.sqrt(x)
#     return("--- %s seconds ---" % (time.time() - start_time))


print(Hildebrand(10000000000))

