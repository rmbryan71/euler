import unittest

def arealist(inputlist):
    if not len(inputlist) == 6:
        return -1
    else:
        ax, ay, bx, by, cx, cy = [inputlist[i] for i in range(0, 6)]
        l = ax * (by - cy)
        m = bx * (cy - ay)
        n = cx * (ay - by)
        return abs(l + m + n) / 2


def areacoords(ax, ay, bx, by, cx, cy):
    l = ax * (by - cy)
    m = bx * (cy - ay)
    n = cx * (ay - by)
    return abs(l + m + n) / 2


def containsorigin(ax, ay, bx, by, cx, cy):
    a = areacoords(ax, ay, bx, by, cx, cy)
    ab = areacoords(ax, ay, bx, by, 0, 0)
    bc = areacoords(0, 0, bx, by, cx, cy)
    ac = areacoords(ax, ay, 0, 0, cx, cy)
    return a == ab + bc + ac


def test_arealist():
    testlist_a = [15, 15, 23, 30, 50, 25]
    assert arealist(testlist_a) == 222.5


def test_areacoords():
    testcoords_a = [-4, 5, 10, 10, 4, -10]
    ax, ay, bx, by, cx, cy = [testcoords_a[i] for i in range(0, 6)]
    assert areacoords(ax, ay, bx, by, cx, cy) == 125


with open('p102_triangles.txt') as f:
    answer = 0
    data = f.readlines()
    for line in data:
        mylist = [int(a) for a in line.split(',')]
        ax, ay, bx, by, cx, cy = [mylist[i] for i in range(0, 6)]
        answer += containsorigin(ax, ay, bx, by, cx, cy)
print(answer)





