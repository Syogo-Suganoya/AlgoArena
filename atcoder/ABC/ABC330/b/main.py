N, L, R = map(int, input().split())
A = list(map(int, input().split()))

res = []
for a in A:
    if a < L:
        res.append(L)
    elif a > R:
        res.append(R)
    else:
        res.append(a)

print(*res)
