if __name__ == "__main__":
    S = []
    for i in range(2000):
        for j in range(2000):
            count = i * 2000 + j + 1
            if count <= 55:
                S.append((100003 - 200003 * count + 300007 * count * count * count) % 1000000 - 500000)
            else:
                S.append((S[count - 25] + S[count - 56] + 1000000) % 1000000 - 500000)

    ans = 0

    for i in range(2000):
        maxSoFar = 0
        maxEndingHere = 0
        for j in range(2000):
            maxEndingHere = max(maxEndingHere + S[i * 2000 + j], 0)
            maxSoFar = max(maxSoFar, maxEndingHere)
        ans = max(ans, maxSoFar)

    for i in range(2000):
        maxSoFar = 0
        maxEndingHere = 0
        for j in range(2000):
            maxEndingHere = max(maxEndingHere + S[j * 2000 + i], 0)
            maxSoFar = max(maxSoFar, maxEndingHere)
        ans = max(ans, maxSoFar)

    for i in range(2000):
        maxSoFar = 0
        maxEndingHere = 0
        start = i * 2000
        for j in range(i + 1):
            maxEndingHere = max(maxEndingHere + S[start - 1999 * j], 0)
            maxSoFar = max(maxSoFar, maxEndingHere)
        ans = max(ans, maxSoFar)

    for i in range(2000):
        maxSoFar = 0
        maxEndingHere = 0
        start = i * 2000 + 1999
        for j in range(2000 - i):
            maxEndingHere = max(maxEndingHere + S[start + 1999 * j], 0)
            maxSoFar = max(maxSoFar, maxEndingHere)
        ans = max(ans, maxSoFar)

    for i in range(2000):
        maxSoFar = 0
        maxEndingHere = 0
        start = i * 2000
        for j in range(2000 - i):
            maxEndingHere = max(maxEndingHere + S[start + 1999 * j], 0)
            maxSoFar = max(maxSoFar, maxEndingHere)
        ans = max(ans, maxSoFar)

    for i in range(2000):
        maxSoFar = 0
        maxEndingHere = 0
        start = i * 2000 + 1999
        for j in range(i + 1):
            maxEndingHere = max(maxEndingHere + S[start - 1999 * j], 0)
            maxSoFar = max(maxSoFar, maxEndingHere)
        ans = max(ans, maxSoFar)

    print(ans)
