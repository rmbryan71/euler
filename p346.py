def tostr(n, base):
    convertstring = "0123456789ABCDEF"
    if n < base:
        return convertstring[n]
    else:
        return tostr(n//base, base) + convertstring[n % base]


def f(x, y):  # return true if x is a repunit in base y
    if x <= y:
        if x == 1:
            return True
        else:
            return False
    if x % y != 1:
        return False
    else:
        return f(x // y, y)


