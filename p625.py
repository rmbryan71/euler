from sympy.ntheory import totient, divisors
import time
# naive code takes 58 seconds to reach 100,000
# OEIS A018804

for exp in range(1, 6):
    limit = 10**exp
    start = time.time()
    ans = [sum([n*totient(d)//d for d in divisors(n)]) for n in range(1, limit + 1)][-1]
    et = int(time.time() - start)
    print(limit, et, ans)
