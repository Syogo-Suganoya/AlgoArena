D, G = map(int, input().split())
p = []
c = []
for _ in range(D):
    pi, ci = map(int, input().split())
    p.append(pi)
    c.append(ci)

INF = 10**9
dp = [INF] * (G + 1)
dp[0] = 0

for i in range(D):
    ndp = dp[:]
    for s in range(G + 1):
        if dp[s] == INF:
            continue
        # 0問～p[i]-1問だけ解く場合
        for k in range(p[i]):
            score = k * 100 * (i + 1)
            ns = min(G, s + score)
            ndp[ns] = min(ndp[ns], dp[s] + k)
        # 全問解く場合（ボーナス含む）
        score = p[i] * 100 * (i + 1) + c[i]
        ns = min(G, s + score)
        ndp[ns] = min(ndp[ns], dp[s] + p[i])
    dp = ndp

print(dp[G])
