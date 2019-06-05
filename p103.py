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

range_bottom = 30
range_top = 44
range_size = range_top - range_bottom

range = [x for x in range(range_bottom, range_top)]
start = time.time()
solutions = 0
tests = 0g
for test in itertools.combinations(range, 7):
    tests += 1
    if is_special7(test):
        print(test, sum(test))
        solutions += 1
        if solutions == 10:
            break
duration = int(time.time() - start)

print(duration, " seconds executions time for ", tests, " tests is ", int(tests / duration), " tests per second in a range of ", range_size)
