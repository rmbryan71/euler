import time

start_time = time.time()


def createsubsets(mainset):  # create a list of all subsets of mainsets
    subsets = [set()]
    for n in mainset:
        newsets = list(subsets)
        for i in range(0, len(subsets)):
            newsets[i] = newsets[i].union({n})
        subsets += newsets
    return subsets


def checkconditions(
        count):  # check that sum of subset of size n>sum of subset of size n-1:true if smallest n>largest n-1
    countersize = len(count)
    for smallsetsize in range(2, int((countersize + 1) / 2) + 1):
        smallsetsum = sum(count[x] for x in range(0, smallsetsize))
        largesetsum = sum(count[x] for x in range(-1, -smallsetsize, -1))
        if largesetsum >= smallsetsum:
            return False
    # now need to check that no 2 subsets ofhave the same sum

    subsets = createsubsets(set(count))
    sumsfound = set()
    for subset in subsets:
        if sum(subset) not in sumsfound:
            sumsfound.add(sum(subset))
        else:
            return False
    return True


def main():
    file = open("p105_sets.txt", "r")
    setlist = [[int(x) for x in sorted(line[:-1].split(','))] for line in file]
    file.close
    print(sum(sum(currentset) for currentset in setlist if checkconditions(currentset)))
    print('time=', time.time() - start_time, ' seconds')


if __name__ == "__main__":
    main()