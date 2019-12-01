import itertools
from numpy import prod


m = []
inputfile = open('p345_example.txt', 'r')
for line in inputfile.readlines():
    m.append([int(x) for x in line.split(',')])

size = 5
maxsum = 0
rows = range(0, size)
columns = range(0, size)
for row in itertools.permutations(rows, size):
    for column in itertools.permutations(columns, size):
        k = []
        for i in range(size):
            k.append(m[column[i]][row[i]])
        if sum(k) > maxsum:
            maxsum = sum(k)
print(maxsum)




