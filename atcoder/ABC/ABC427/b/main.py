N = int(input())


def f(x):
    return sum(map(int, str(x)))


A = 1

for i in range(N - 1):
    A += f(A)

print(A)
