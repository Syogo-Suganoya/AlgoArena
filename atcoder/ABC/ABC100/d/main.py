N, M = map(int, input().split())
X, Y, Z = [], [], []
for _ in range(N):
    x, y, z = map(int, input().split())
    X.append(x)
    Y.append(y)
    Z.append(z)

INF = 10**18
ans = -INF
# a, b, c の符号を全探索 (-1 or +1)
for a in [-1, 1]:
    for b in [-1, 1]:
        for c in [-1, 1]:
            # 各ケーキの「価値」を計算
            vals = [a * X[i] + b * Y[i] + c * Z[i] for i in range(N)]
            # 大きい順に M 個選べばよい
            vals.sort(reverse=True)
            total = sum(vals[:M])
            ans = max(ans, total)

print(ans)
