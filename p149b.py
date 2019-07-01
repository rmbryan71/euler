import time

if __name__ == "__main__":
    S = []
    start = time.time()
    for i in range(2000):
        for j in range(2000):
            count = i * 2000 + j + 1
            if count <= 55:
                S.append((100003 - 200003 * count + 300007 * count * count * count) % 1000000 - 500000)
            else:
                S.append((S[count - 25] + S[count - 56] + 1000000) % 1000000 - 500000)
    end = time.time()


