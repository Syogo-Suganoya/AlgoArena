N = int(input())

d = {"L": None, "R": None}

res = 0
for i in range(N):
    A, S = input().split()
    A = int(A)
    if d[S] is not None:
        res += abs(d[S] - A)
    d[S] = A
print(res)
