N, M = map(int, input().split())
coupons = [0] * M
for i in range(M):
    arr = list(map(int, input().split()))
    bit = 0
    for j, v in enumerate(arr):
        if v == 1:
            bit |= 1 << j
    coupons[i] = bit

INF = 10**9
dp = [INF] * (1 << N)
dp[0] = 0  # 何もカバーしていない状態は0枚

for mask in range(1 << N):
    if dp[mask] == INF:
        continue
    for c in coupons:
        nxt = mask | c
        if dp[nxt] > dp[mask] + 1:
            dp[nxt] = dp[mask] + 1

ans = dp[(1 << N) - 1]
print(ans if ans != INF else -1)
