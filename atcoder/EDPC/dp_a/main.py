N = int(input())
h = list(map(int, input().split()))

# dp[i]：i段目までにかかる最小コスト（または最小回数）
INF = float("inf")
dp = [INF] * N
dp[0] = 0  # 最初は0回のコストでいける

for i in range(N - 1):
    # 1段飛ばしでいける場合
    dp[i + 1] = min(dp[i + 1], dp[i] + abs(h[i + 1] - h[i]))
    # 2段飛ばしでいける場合
    if i + 2 < N:
        dp[i + 2] = min(dp[i + 2], dp[i] + abs(h[i + 2] - h[i]))

print(dp[-1])
