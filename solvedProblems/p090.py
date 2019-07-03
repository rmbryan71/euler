from itertools import combinations
counter=0
set = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
winnerset=[]
superset=[]
tests=0

for x in combinations(set, 6):
    for y in combinations(set, 6):
        tests +=1
        if (0 in x and 1 in y) or (1 in x and 0 in y):
            if (0 in x and 4 in y) or (4 in x and 0 in y):
                if(0 in x and (6 in y or 9 in y)) or ((6 in x or 9 in x) and 0 in y):
                    if (1 in x and (6 in y or 9 in y)) or ((6 in x or 9 in x) and 1 in y):
                        if (2 in x and 5 in y) or (5 in x and 2 in y):
                            if (3 in x and (6 in y or 9 in y)) or ((6 in x or 9 in x) and 3 in y):
                                if (4 in x and (6 in y or 9 in y)) or ((6 in x or 9 in x) and 4 in y):
                                    if (8 in x and 1 in y) or (1 in x and 8 in y):
                                        winner = [x, y]
                                        superset.append(winner)
                                        converse = [y, x]
                                        if winner not in winnerset and converse not in winnerset:
                                            winnerset.append(winner)
                                    #else:
                                        #print(winner, winnerset, " duplicate")
    #                             else:
    #                                 print(x, y, " can't make 81.")
    #                         else:
    #                             print(x, y, " can't make 64 or 49.")
    #                     else:
    #                         print(x, y, " can't make 36.")
    #                 else:
    #                     print(x, y, " can't make 25.")
    #             else:
    #                 print(x, y, " can't make 16.")
    #         else:
    #             print(x, y, " can't make 09.")
    #     else:
    #         print(x, y, " can't make 04")
    # else:
    #     print(x, y, " can't make 01.")


print(len(winnerset), len(superset), tests)

for winner in winnerset:
    #print(winner)
    converse = []
    for a in reversed(winner):
        converse.append(a)
    if converse not in superset:
        print(converse)
    if winner == converse:
        print(winner, converse)