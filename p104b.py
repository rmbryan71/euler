# I am making this file so that I can continue work on p104 while my original code is still running, in case it finds an answer.

def fib(n):
    v1, v2, v3 = 1, 1, 0    # initialise a matrix [[1,1],[1,0]]
    for rec in bin(n)[3:]:  # perform fast exponentiation of the matrix (quickly raise it to the nth power)
        calc = v2*v2
        v1, v2, v3 = v1*v1+calc, (v1+v3)*v2, calc+v3*v3
        if rec=='1':    v1, v2, v3 = v1+v2, v1, v2
    return v2

def fib_tail(n):

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_tail(n - 1) + fib_tail(n - 2)

def is_tail_pan(n):
    y = []
    x = str(n % 1000000000)
    for char in str(x):
        y.append(char)
    y.sort()
    if y == ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        return True
    else:
        return False


def is_head_pan(x):
    y = []
    x = str(x)
    x = x[:9]
    for char in str(x):
        y.append(char)
    y.sort()
    if y == ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        return True
    else:
        return False

x = 500
cont = True
while cont == True:
    y = fib_tail(x)
    if is_tail_pan(y):
        print(x, " is tail pan.")
        z = fib(x)
        if is_head_pan(z):
            print(x, " is both head and tail pan.")
            cont = False
    x += 1



