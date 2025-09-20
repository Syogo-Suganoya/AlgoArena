from collections import defaultdict

N, M, K = map(int, input().split())
d = defaultdict(list)
res = []

for _ in range(K):
    A, B = map(int, input().split())
    d[A].append(B)
    if len(d[A]) == M:
        res.append(A)

print(*res)
