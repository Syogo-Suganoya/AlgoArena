N = int(input())
A = list(map(int, input().split()))

d = {}
res = []
for i in range(N):
    if A[i] in d:
        res.append(d[A[i]])
    else:
        res.append(-1)
    d[A[i]] = i + 1
print(*res)
