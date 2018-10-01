import math
import time

def fac_sum(x):
    result = 0
    x = str(x)
    for i in range(0, len(x)):
        result += math.factorial(int(x[i]))
    return result


def fac_chain(x):
    a = x
    b = fac_sum(x)
    result = [a, b]
    if a == b:
        return result
    while True:
        a = b
        b = fac_sum(a)
        if b in result:
            return result
        else:
            result.append(b)


start = time.time()
answer = 0
for i in range(2, 1000000):
    j = len(fac_chain(i))
    if j == 60:
        answer += 1
    if i % 10000 == 0:
        et = time.time()-start
        print(i, answer, et / i * 10000)
print(answer, time.time()-start)
