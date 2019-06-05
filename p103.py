import itertools


def set_sum(inputset):
    return sum(inputset)


def is_special6(inputset): #test for N = 6
    if not len(inputset) == 6:
        return False
    for b in itertools.permutations(inputset, 4):
        b = set(b)
        c = set(inputset).symmetric_difference(set(b))
        #print(b, c)
        if set_sum(b) <= set_sum(c):
            return False
    return True


def is_special7(inputset): #test for N = 7
    if not len(inputset) == 7:
        return False
    for b in itertools.permutations(inputset, 4):
        b = set(b)
        c = set(inputset).symmetric_difference(set(b))
        #print(b, c)
        if set_sum(b) <= set_sum(c):
            return False
    return True


range = [x for x in range(1, 26)]
minsum = 500

for test in itertools.combinations(range, 6):
    if is_special6(test):
        if set_sum(test) < minsum:
            minsum = set_sum(test)
            print(test, minsum)

