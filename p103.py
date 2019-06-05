import itertools


def set_sum(inputset):
    return sum(inputset)


def is_special6(inputset): #test for N = 6
    if not len(inputset) == 6:
        return False
    for x in itertools.permutations(inputset):
        b = [x[0], x[1], x[2]]
        c = [x[3], x[4], x[5]]
        #print(b, c, sum(b), sum(c))
        if sum(b) == sum(c):
            #print(False, b, c, sum(b), sum(c))
            return False

    for x in itertools.permutations(inputset):
        b = [x[0], x[1], x[2]]
        c = [x[3], x[4]]
        #print(b, c, sum(b), sum(c))
        if sum(b) <= sum(c):
            #print(False, b, c, sum(b), sum(c))
            return False

    for x in itertools.permutations(inputset):
        b = [x[0], x[1]]
        c = [x[3], x[4]]
        #print(b, c, sum(b), sum(c))
        if sum(b) == sum(c):
            #print(False, b, c, sum(b), sum(c))
            return False

    for x in itertools.permutations(inputset):
        b = [x[0], x[1]]
        c = [x[5]]
        if sum(b) <= sum(c):
            #print(False, b, c, sum(b), sum(c))
            return False
        else:
            print(True, inputset)
            return True


def is_special7(inputset): #test for N = 7
    if not len(inputset) == 7:
        return False

    for x in set(itertools.permutations(inputset)):
        x = set(x)
        b = set(itertools.permutations(x, 2))
        remainderset = x - b
        print(inputset, x, b, remainderset)
        c = set(itertools.permutations(remainderset, 1))
        if sum(b) <= sum(c):
            return False

    for y in itertools.permutations(inputset):
        b = itertools.permutations(y, 2)
        remainderset = inputset - b
        c = itertools.permutations(remainderset, 2)
        #print(b, c, sum(b), sum(c))
        if sum(b) == sum(c):
            return False

    for x in itertools.permutations(inputset):
        b = itertools.permutations(x, 3)
        remainderset = inputset - b
        c = itertools.permutations(remainderset, 2)
        if sum(b) <= sum(c):
            return False

    for x in itertools.permutations(inputset):
        b = itertools.permutations(x, 3)
        remainderset = inputset - b
        c = itertools.permutations(remainderset, 3)
        if sum(b) == sum(c):
            return False

    for x in itertools.permutations(inputset):
        b = itertools.permutations(x, 4)
        remainderset = inputset - b
        c = itertools.permutations(remainderset, 3)
        if sum(b) <= sum(c):
            return False
        else:
            return True

range = [x for x in range(11, 27)]
minsum = 500
count = 0
#print(is_special7([10, 17, 18, 19, 20, 21, 22]))



for test in itertools.combinations(range, 7):
    if is_special7(test):
        print(test, sum(test), minsum)
        if sum(test) == minsum:
            print("tie")
            break
        if sum(test) < minsum:
            minsum = sum(test)
            winner = test
            #print(test, minsum)

print(minsum, winner)

