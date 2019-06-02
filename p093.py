import itertools
ops = {'-', '+', '*', '/'}


def check(a, b, c, d, x): # can digits a, b, c, d be combined to form int x?
    return False


def blow(a, b, c, d):
    ints = [a, b, c, d]
    for set in itertools.permutations(ints):
        print(set)


blow(1, 2, 3, 4)


