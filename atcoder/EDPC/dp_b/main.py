N, K = map(int, input().split())
h = list(map(int, input().split()))
dp = [float("inf")] * N
dp[0] = 0

for i in range(1, N):
    for j in range(1, min(K, i) + 1):
        dp[i] = min(dp[i], dp[i - j] + abs(h[i] - h[i - j]))

print(dp[N - 1])
