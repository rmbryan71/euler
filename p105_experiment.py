import itertools, time, multiprocessing


def test_equalities(inputset):
    for x in itertools.combinations(inputset, 2):
        #for z in inputset if z not in x:
        #    if z == sum(x):
                return 0
    else:
        return sum(inputset)

with open('p105_sets.txt') as f:
#with open('p105_timingset') as f:
    data = [[int(num) for num in line.split(',')] for line in f]
f.close()

pool = multiprocessing.Pool(4)
start = time.time()

print(sum((pool.map(test_equalities, data))))
print(time.time() - start, " seconds.")
