def nrect(m, n):
    if m < n: m, n = n, m
    hvr = m*(m + 1) * n*(n + 1) // 4    # Horizontal & vertical
    dr = n*((2*m - n) * (4*n*n - 1) - 3) // 6    # Diagonal
    return hvr + dr

w, h = 47, 43
print("Number of rectanges", sum(nrect(m, n) for m in range(1, w+1) for n in range(1, h+1)))
