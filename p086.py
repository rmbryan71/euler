#  sqrt(l^2 + (w+h)^2)
import math


def shortest_path(l,w,h):
    return math.sqrt(l^2 + (w+h)^2)


def is_int_shortest_path(l,w,h):
    return shortest_path(l,w,h).is_integer()


def count_int_solutions(M):
    count = 0
    for l in range(1, M):
        for w in range(1, M):
            for h in range(1, M):
                if is_int_shortest_path(l, w, h):
                    count += 1
    return count


target = 1000000
count = 0
l = 2

while(count < target):
    l +=1
    for wh in range(3, 2*l):
        if math.sqrt(wh*(wh+l) * l).is_integer():
            count += wh/2