import math, time


def next(x):
    y = str(x)
    accum = 0
    for char in y:
        accum += int(char) ** 2
    return accum


def dest(x):
    if x == 1:
        return 1
    if x == 89:
        return 89
    else:
        return dest(next(x))


def dest_is_89(x):
    if x == 1:
        return False
    if x == 89:
        return True
    else:
        return dest_is_89(next(x))

start = time.time()
counter = 0
for i in range(1, 10000000):
    counter += dest_is_89(i)
print(counter, time.time() - start)