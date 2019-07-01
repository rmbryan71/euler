import time


def pythagoreanTriplets(limits):
    results = []
    c, m = 0, 2

    # Limiting c would limit
    # all a, b and c
    while c < limits:

        # Now loop on n from 1 to m-1
        for n in range(1, m):
            a = m * m - n * n
            b = 2 * m * n
            c = m * m + n * n

            # if c is greater than
            # limit then break it
            if c > limits:
                break

            #print(a, b, c)
            results.append([a, b, c])

        m = m + 1
    return results


def f(x):
    a = x[0]
    b = x[1]
    c = x[2]
    if (c * c) % ((b - a) ** 2) == 0:
        return True
    else:
        return False


start = time.time()
# mymax = (10**8)
mymax = 10**8
mytriplets = pythagoreanTriplets(int(mymax * .75))
# mytriplets = pythagoreanTriplets(int(mymax))
winners = []
for trip in mytriplets:
    if f(trip) and (sum(trip) < mymax):
        winners.append(trip)
print(len(winners), "of", mymax)
end = time.time()
print(int(end - start), "seconds")
# for winner in winners:
#     print(winner, sum(winner))
