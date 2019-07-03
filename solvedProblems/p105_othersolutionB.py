import itertools


def test_set(candidate):
    N = len(candidate)
    M = 0
    for k in range(1, N + 1):
        numbers = set()
        for choice in itertools.combinations(candidate, k):
            s = sum(choice)
            if s <= M or s in numbers:
                return 0
            numbers.add(s)
        M = max(numbers)
    return sum(candidate)


sol = 0
with open("p105_sets.txt", 'r') as sets:
    for candidate in sets:
        candidate = [int(d) for d in candidate.split(',')]
        sol += test_set(candidate)

print(sol)