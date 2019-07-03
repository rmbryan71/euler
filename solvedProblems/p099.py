import math
import time

start = time.time()
with open('p099_base_exp.txt') as f:
    linenum = 1
    maxvalue = 0
    data = f.readlines()
    pairs = [row.strip() for row in data]
    for pair in pairs:
        a, b = pair.split(',')
        a = int(a)
        b = int(b)
        candidate = (b * math.log(a))
        if candidate > maxvalue:
            #print(linenum)
            maxvalue = candidate
            answer = linenum
        linenum += 1
        print(linenum, int(time.time()-start))
    print('answer is')
    print(answer)



