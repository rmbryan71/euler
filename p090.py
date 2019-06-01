from itertools import combinations
counter=0
set = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
winnerset=[]

for x in combinations(set, 6):
    for y in combinations(set, 6):
        if (0 in x and 1 in y) or (1 in x and 0 in y):
            if (0 in x and 4 in y) or (4 in x and 0 in y):
                if(0 in x and 6 or 9 in y) or (6 or 9 in x and 0 in y):
                    if (1 in x and 6 or 9 in y) or (6 or 9 in x and 1 in y):
                        if (2 in x and 5 in y) or (5 in x and 2 in y):
                            if (3 in x and 6 or 9 in y) or (6 or 9 in x and 3 in y):
                                if (4 in x and 6 or 9 in y) or (6 or 9 in x and 4 in y):
                                    if (8 in x and 1 in y) or (1 in x and 8 in y):
                                        winner = []
                                        for a in x:
                                            winner.append(a)
                                        for b in y:
                                            winner.append(b)
                                        winner.sort()
                                        print(winner)
                                        winnerset.append(winner)

print(len(winnerset))
