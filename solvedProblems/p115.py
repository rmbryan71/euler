import numpy as np

def block_combination_count(minLen, totalLen):
    # pascal's triangle
    pctr = np.zeros(shape=(totalLen + 1, totalLen + 1))

    pctr[0][0] = 1
    for i in range(totalLen):
        pctr[i][0] = 1
        pctr[i][i] = 1
        for j in range(1, i):
            pctr[i][j] = pctr[i - 1][j - 1] + pctr[i - 1][j]

    # nHr = (n+r-1)Cr : combination with repetition
    def H(n, r):
        return pctr[n + r - 1][r]

    k = 1       # number of red blocks (lengths of each block don't matter)
    total = 1.  # separate count 1 for no red block (k=0)
    print(0, total)
    while True:
        target = totalLen - (minLen*k) - (k-1)
        sub_total = 0
        if target < 0:
            break
        for i in range(target + 1):
            sub_total += H(k, i) * H(k+1, target-i)
        print(k, sub_total)
        k += 1
        total += sub_total

    return total


print(block_combination_count(3, 50))
print(block_combination_count(3, 29))
print(block_combination_count(3, 30))
print(block_combination_count(10, 56))
print(block_combination_count(10, 57))

result = 0
i = 100
while result < 1000000:
    i += 1
    result = block_combination_count(50,i)
    print(i, result)