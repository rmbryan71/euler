import itertools
from itertools import chain, combinations

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


myset = [4, 5, 9, 55, 77, 121, 181, 313, 434, 484, 505, 545, 595, 636, 676, 818]

for set in powerset(myset):
    if sum(set) == 4164:
        print(set, len(set))