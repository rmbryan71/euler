def f(x):
    answer = 0
    for i in range(1, x):
        if i % 3 == 0 or i % 5 == 0:
            answer += i

    return answer

print(f(10))
print(f(1000))