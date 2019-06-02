import numpy as np

def all_triplets(limit):
    c, m = 0, 2
    lengths=[]

    while True:
        for n in range(1, m):
            a = m * m - n * n
            b = 2 * m * n
            c = m * m + n * n

            if c > limit:
                return lengths
            wire_length = a + b + c
            lengths.append(wire_length)
            print(a, b, c, wire_length)
        m += 1

print(all_triplets(1000))