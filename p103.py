import itertools, time


def set_sum(inputset):
    return sum(inputset)


def is_special6(inputset): #test for N = 6
    if not len(inputset) == 6:
        return False
    for x in itertools.permutations(inputset):
        b = [x[0], x[1], x[2]]
        c = [x[3], x[4], x[5]]
        if sum(b) == sum(c):
            return False

    for x in itertools.permutations(inputset):
        b = [x[0], x[1], x[2]]
        c = [x[3], x[4]]
        if sum(b) <= sum(c):
            return False

    for x in itertools.permutations(inputset):
        b = [x[0], x[1]]
        c = [x[2], x[3]]
        if sum(b) == sum(c):
            return False

    for x in itertools.permutations(inputset):
        b = [x[0], x[1]]
        c = [x[2]]
        if sum(b) <= sum(c):
            return False
        else:
            return True


def is_special7(inputset): #test for N = 7
    if not len(inputset) == 7:
        return False

    for x in itertools.permutations(inputset):
        b = [x[0], x[1]]
        c = [x[2]]
        if sum(b) <= sum(c):
            return False

    for x in itertools.permutations(inputset):
        b = [x[0], x[1]]
        c = [x[3], x[2]]
        if sum(b) == sum(c):
            return False

    for x in itertools.permutations(inputset):
        b = [x[0], x[1], x[2]]
        c = [x[3], x[4]]
        if sum(b) <= sum(c):
            return False

    for x in itertools.permutations(inputset):
        b = [x[0], x[1], x[2]]
        c = [x[3], x[4], x[5]]
        if sum(b) == sum(c):
            return False

    for x in itertools.permutations(inputset):
        b = [x[0], x[1], x[2], x[3]]
        c = [x[4], x[5], x[6]]
        if sum(b) <= sum(c):
            return False
        else:
            return True


# range = [x for x in range(11, 29)]
# start = time.time()
# for test in itertools.combinations(range, 6):
#     if is_special6(test):
#         print(test, sum(test))
# print(int(time.time() - start), " seconds executions time.")

range = [x for x in range(28, 46)]
start = time.time()
solutions = 0
for test in itertools.combinations(range, 7):
    if is_special7(test):
        print(test, sum(test))
        solutions += 1
        if solutions == 10:
            break

print(int(time.time() - start), " seconds executions time.")