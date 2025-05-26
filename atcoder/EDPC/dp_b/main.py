N, K = map(int, input().split())
h = list(map(int, input().split()))

INF = float("inf")
dp = [INF] * N
dp[0] = 0  # 最初は0回のコストでいける

for i in range(N - 1):
    for j in range(1, K + 1):
        if i + j < N:
            dp[i + j] = min(dp[i + j], dp[i] + abs(h[i + j] - h[i]))
print(dp[-1])
