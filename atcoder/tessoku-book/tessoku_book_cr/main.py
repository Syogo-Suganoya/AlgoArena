N, W = map(int, input().split())
weights = []
values = []

for _ in range(N):
    w, v = map(int, input().split())
    weights.append(w)
    values.append(v)

# 最大価値の合計を求める
Vmax = sum(values)

INF = 10**18
dp = [INF] * (Vmax + 1)
dp[0] = 0

for i in range(N):
    w = weights[i]
    v = values[i]
    for j in range(Vmax, v - 1, -1):
        dp[j] = min(dp[j], dp[j - v] + w)

# 重量 W 以下で得られる最大価値
ans = 0
for v in range(Vmax + 1):
    if dp[v] <= W:
        ans = max(ans, v)

print(ans)
