import itertools
import math
limit = 1000


def make_sq_list(limit):
    result = []
    for i in range(1, int(math.sqrt(limit) + 1)):
        result.append(i * i)
    return result


assert (len(make_sq_list(10**4))) == 100


for x in itertools.count(8600):
    print(x)
    mysquares = make_sq_list(2 * x + 1)
    y_list = []
    z_list = []
    for sq in mysquares:
        if sq < x:
            if (x - sq) in mysquares:
                if (x + x - sq) in mysquares:
                    y_list.append(x - sq)
    # y_list is a [] of potentials y
    for y in y_list:
        for sq in mysquares:
            if sq < y:
                if (y - sq) in mysquares:
                    if (y + y - sq) in mysquares:
                        print(x, y, y - sq)
                        break
    # # z_list is a [] of potentials z
    # for z in z_list:
    #     for sq in mysquares:
    #         if sq < z:
    #             if (z - sq) in mysquares:
    #                 if (z + z - sq) in mysquares:
    #                     print(x, y_list, z)
    #                     break
