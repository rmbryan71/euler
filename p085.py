#  M(M+1)(N)(N+1)/4

best_count = 0
best_area = 0
target = 2000000

for N in range(1, 1500):
    for M in range(1, 1500):
        x = int((M*(M+1)*N*(N+1)/4))
        if abs(target-x) < abs(target-best_count):
            best_count = x
            best_area = N * M
            print(N, M, best_count, best_area)




