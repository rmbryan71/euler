limit = 100
result = 0
scores = [n for n in range(1, 21)]
scores += [n * 2 for n in range(1, 21)]
scores += [n * 3 for n in range(1, 21)]
scores += [25, 50]
doubles = [n * 2 for n in range(1, 21)]
doubles += [50]
# end setup

result += len(doubles)  # counts the one-step checkouts

for i in range(0, len(scores)):  # counts miss, hit, double checkouts
    for j in doubles:
        if scores[i] + j < limit:
            result += 1

for i in range(0, len(scores)):  # counts hit, hit, double checkouts
    for j in range(i, len(scores)):
        for k in doubles:
            if scores[i] + scores[j] + k < limit:
                result += 1
print(result)



