coins = [2, 3, 5, 7, 11, 13, 17, 23]
number = 10


def count(k, n, coins):
    if k == 0:
        if n % coins[0] == 0:
            return 1
        else:
            return 0
    else:
        c = 0
        for i in range(n // coins[k] + 1):
            c += count(k - 1, n - i * coins[k], coins)
        return c


print(count(len(coins) - 1, number, coins))
