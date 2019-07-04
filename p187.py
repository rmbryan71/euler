import math
import time

def is_semi(num):
    cnt = 0

    for i in range(2, int(math.sqrt(num)) + 1):
        while num % i == 0:
            num /= i
            cnt += 1
        if cnt >= 2:
            break
    if num > 1:
        cnt += 1
    return cnt == 2


def main(limit):
    start = time.time()
    count = 0
    for i in range(1, limit):
        if is_semi(i):
            count += 1
            if count % 50000 == 0:
                print(count, i)
    print(count, "less than", limit, "in", int(time.time() - start), "seconds")


main(30)
main(1000)
main(10**4)
main(10**5)
main(10**8)