from math import sqrt, floor, ceil


def is_square(n):
    if n<1:
        return False
    else:
        for i in range(int(n/2)+1):
            if (i*i)==n:
                return True
        return False


def pell_solve(D, m):
    """
    Description:

        Solves the Pell equation x^2 - D*y^2 = m

    Input:

        D - nonsquare int
        m - int

    Output:

        (x0, y0) - minimal solution to x^2 - D*y^2 = 1
        prim_sols - list of primitive solutions for each solution class to x^2 - D*y^2 = m

    """
    assert not is_square(D), 'D cannot be a perfect square'
    if m * m >= D:
        return _pell_solve_2(D, m)
    else:
        return _pell_solve_1(D, m)


def _pell_solve_1(D, m):  # m^2 < D
    root_d = int(floor(sqrt(D)))
    a = int(floor(root_d))
    P = int(0)
    Q = int(1)
    p = [int(1), int(a)]
    q = [int(0), int(1)]
    i = int(1)
    x0 = int(0)
    y0 = int(0)
    prim_sols = []
    test = int(0)
    while not (Q == 1 and i % 2 == 1) or i == 1:
        test = p[i] ** 2 - D * (q[i] ** 2)
        if test == 1:
            x0 = p[i]
            y0 = q[i]
        test = (m / test)
        if is_square(test) and test >= 1:
            test = int(test)
            prim_sols.append((test * p[i], test * q[i]))
        i += 1
        P = a * Q - P
        Q = (D - P ** 2) / Q
        a = int(floor((P + root_d) / Q))
        p.append(a * p[i - 1] + p[i - 2])
        q.append(a * q[i - 1] + q[i - 2])
    return (x0, y0), prim_sols


def _pell_solve_2(D, m):  # m^2 >= D
    prim_sols = []
    t, u = _pell_solve_1(D, 1)[0]
    if m > 0:
        L = int(0)
        U = int(floor(sqrt(m * (t - 1) / (2 * D))))
    else:
        L = int(ceil(sqrt(-m / D)))
        U = int(floor(sqrt(-m * (t + 1) / (2 * D))))
    for y in range(L, U + 1):
        y = int(y)
        x = (m + D * (y ** 2))
        if is_square(x):
            x = int(sqrt(x))
            prim_sols.append((x, y))
            if not ((-x * x - y * y * D) % m == 0 and (
                    2 * y * x) % m == 0):  # (x,y) and (-x,y) are in different solution classes, so add both
                prim_sols.append((-x, y))
    return (t, u), prim_sols


gen = (x for x in range(4, 1001) if not is_square(x))

max_x = 0
max_x_maker = 0

for i in gen:
    if pell_solve(i, 1)[0][0] > max_x:
        print(i, pell_solve(i, 1)[0][0])
        max_x = pell_solve(i, 1)[0][0]
        max_x_maker = i
print('Finished. Max x is when D = ', max_x_maker)


























import sys
from math import sqrt

# def obtenerFraccionContinua(A, x):
#     a0 = int(sqrt(x))
#     d = 1
#     m = 0
#     a = 0
#
#     prim = True
#
#     if a0*a0 != x:
#         while (a != 2*a0):
#             m = d*a - m
#             d = (x - m * m) / d
#             a = int((a0 + m) / d)
#             if not prim:
#                 A.append(a)
#             prim = False
#
#
# def result(A, num, den, i, maximo):
#     if i >= maximo:
#         return num*A[i] + 1, A[i]
#     else:
#         rnum, rden = result(A, den, A[i+1], i+1, maximo)
#         num = num*rnum + rden
#         den = rnum
#         return num, den
#
#
# def main():
#     print("Pell Equation")
#     print("x^2 - D*y^2 = 1")
#     print(" ")
#     if len(sys.argv) > 1:
#         d = int(sys.argv[1])
#     else:
#         d = int(input("Enter the desired D to solve for: "))
#
#     A = []
#     if d >= 0:
#         a0 = int(sqrt(d))
#         #A.append(a0)
#         obtenerFraccionContinua(A, d)
#
#     longCiclo = len(A)-1
#     p=1
#     q=0
#
#     if longCiclo > 0:
#         if longCiclo%2 == 0:
#             p, q = result(A, A[0], A[1], 1, longCiclo-2)
#         else:
#             A += A[1:] +A[1:]
#             p, q = result(A, A[0], A[1], 1, 2*longCiclo-1)
#
#     print("--------------------------------------------")
#     print("Fundamental solution for D = " + str(d) + ": ")
#     print("x = " + str(p))
#     print("y = " + str(q))
#
# main()