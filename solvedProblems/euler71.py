global_max = 0
global_max_index = 0
global_max_numerator = 0

for i in range(1, 1000000):
    j = int(i * 3 / 7) - 1
    k = j / i
    if k < (3 / 7) and (k > global_max):
        print(k)
        global_max = k
        global_max_index = i
        global_max_numerator = j
print(global_max_numerator)