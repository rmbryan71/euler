def f(x):
    ways = [1] + [0] * x

    for n in range(1, x):
        for i in range(n, x + 1):
            ways[i] += ways[i - n]

    return ways[-1]

print(f(100))
