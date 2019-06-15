# https://oeis.org/A003313
# https://en.wikipedia.org/wiki/Addition-chain_exponentiation


import math

def m(x):
    return math.floor(math.sqrt(x))


assert m(1) == 0
assert m(2) == 1
assert m(3) == 2
assert m(4) == 2
assert m(5) == 3
assert m(6) == 3
assert m(7) == 4
assert m(15) == 5
