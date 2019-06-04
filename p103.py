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

testset = (11, 18, 19, 20, 22, 24)
print(is_special6((testset)))