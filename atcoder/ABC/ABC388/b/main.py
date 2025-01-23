N, D = map(int, input().split())
ts = []
ls = []
for _ in range(N):
    T, L = map(int, input().split())
    ts.append(T)
    ls.append(L)


for i in range(1, D + 1):
    res = 0
    for j in range(N):
        res = max(res, ts[j] * (ls[j] + i))
    print(res)
