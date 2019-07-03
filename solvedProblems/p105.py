import itertools, time, multiprocessing
counter = 0

def is_special(inputset):

    n = len(inputset)
    sortedset = sorted(inputset)
    print(sortedset)

    if(sortedset[0] + sortedset[1]) <= sortedset[-1]:
        return False
    if (sortedset[0] + sortedset[1] + sortedset[2]) <= (sortedset[-1] + sortedset[-2]):
        return False
    if (sortedset[0] + sortedset[1] + sortedset[2] + sortedset[3]) <= (sortedset[-1] + sortedset[-2] + sortedset[-3]):
        return False
    if n >= 9:
        if (sortedset[0] + sortedset[1] + sortedset[2] + sortedset[3] + sortedset[4]) <= (sortedset[-1] + sortedset[-2] + sortedset[-3] + sortedset[-4]):
            return False
    if n >= 11:
        if (sortedset[0] + sortedset[1] + sortedset[2] + sortedset[3] + sortedset[4] + sortedset[5]) <= (sortedset[-1] + sortedset[-2] + sortedset[-3] + sortedset[-4] + sortedset[-5]):
            return False

    for x in itertools.permutations(inputset):
        b = [x[0], x[1]]
        c = [x[3], x[2]]
        if sum(b) == sum(c):
            return False

    for x in itertools.permutations(inputset):
        b = [x[0], x[1], x[2]]
        c = [x[3], x[4], x[5]]
        if sum(b) == sum(c):
            return False

    if n >= 8:
        for x in itertools.permutations(inputset):
            b = [x[0], x[1], x[2], x[3]]
            c = [x[4], x[5], x[6], x[7]]
            if sum(b) == sum(c):
                return False
    if n >= 10:
        for x in itertools.permutations(inputset):
            b = [x[0], x[1], x[2], x[3], x[4]]
            c = [x[5], x[6], x[7], x[8], x[9]]
            if sum(b) == sum(c):
                return False

    if n == 12:
        for x in itertools.permutations(inputset):
            b = [x[0], x[1], x[2], x[3], x[4], x[5]]
            c = [x[6], x[7], x[8], x[9], x[10], x[11]]
            if sum(b) == sum(c):
                return False
    return True


def if_sum(a):
    if is_special(a):
        return sum(a)
    else:
        return 0

answer = 0
with open('p105_sets.txt') as f:
#with open('p105_timingset') as f:
    data = [[int(num) for num in line.split(',')] for line in f]
f.close()

# for i in range(0, 100):
#     j = data[i]
#     inner_start = time.time()
#     if is_special(j):
#         answer += sum(j)
#         print(i, " is special. size = ", len(j), " duration = ", time.time() - inner_start)
#         print(answer, j)
#     else:
#         print(i, " is not special", len(j), " duration = ", time.time() - inner_start)

pool = multiprocessing.Pool(4)
start = time.time()
#j = [sum(i) for i in data if is_special(i)]
print(sum((pool.map(if_sum, data))))

