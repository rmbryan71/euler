MAX_P = 1000000000
sum_p = 0
m, t = 2, 1

while True:
    m_n = 3 * t + 2 * m
    t_n = 2 * t + m
    m, t = m_n, t_n
    p = 2 * m + (2 if m % 3 == 1 else -2)
    if p >= MAX_P:
        break
    sum_p += p
print(sum_p)