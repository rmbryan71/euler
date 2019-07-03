import functools
import itertools
import operator as op

set = [1, 2, 3, 4]
count = 0

for x in itertools.permutations(set):
    count += 1
print(count)

def choose(n, r):
    r = min(n, n-r)
    numerator = functools.reduce(op.mul, range(n, n-r, -1), 1)
    denom = functools.reduce(op.mul, range(1, r + 1, 1))
    return numerator / denom


def Catalan(n):
    return choose(2 * n, n) / (n + 1)

n=12
result = 0
for i in range(2, 5):
    result += choose(n, i) * (choose(n - 1, i) / 2)
    result -= choose(n, 2 * i) * Catalan(i)
print(result)

def p_106():
    def genseq(l):
        for c in ['A','B','.']:
            if l==1:
                yield c
            else:
                for s in genseq(l-1): yield c+s

    def checkseq(s):
        if s.count('A')!=s.count('B') or s.count('A')<2 or s.index('A')>s.index('B'):
            return False

        acc = 0
        for c in s:
            if c=='A':
                acc+=1
            elif c=='B':
                acc-=1
                if acc<0: return True
        return False

    cnt=0
    for s in genseq(12):
        if checkseq(s):
            print(s)
            cnt+=1
    print(cnt)

p_106()