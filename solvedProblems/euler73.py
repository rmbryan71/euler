import time
start = time.time()
upper_bound = 12000
my_set = set()

for i in range(1, upper_bound + 1):
    for j in range(2, i):
        k = j / i
        if 1 / 3 < k < 1 / 2:
                my_set.add(i / j)
    print(i, len(my_set))

end = time.time()
print(len(my_set), end - start)
