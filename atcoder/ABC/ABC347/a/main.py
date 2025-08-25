N, K = map(int, input().split())
A = list(map(int, input().split()))

res = []
for i, a in enumerate(A):
    d, m = divmod(a, K)
    if m == 0:
        res.append(d)

print(*res)
