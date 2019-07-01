def f(l):
    r = 0
    a = 2
    x = -1
    y = -1

    for i in range(0, l//2):
        r += a
        a = (a + a) - x
        r += a
        a = (a * 4) - y
        x = (y - x) / 2
        y = 14 + (19 * x) - (y + y)
    return r

print(f(30))