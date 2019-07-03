result = 0
for i in range(1,10):
    t1 = 1
    t2 = 1
    for j in range(1,10):
        if i == j:
            continue
        else:
            t1 *= 11 - j
            t2 *= i - j
    result += (t1 * ((i-1)/t2))
print(result)


def findnext(x):
    l = len(x)
    if l == 1:
        return x[0]
    return x[-1] + findnext([x[i+1] - x[i] for i in range(l-1)])

def u(n):
    return sum([(-n)**i for i in range(11)])

U = [u(i+1) for i in range(11)]

total = 0
for n in range(1,11):
    fit = findnext(U[:n])
    if fit != U[n]:
        total += fit
print(total)