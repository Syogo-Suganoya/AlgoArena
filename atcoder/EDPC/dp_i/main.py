N = int(input())
ps = list(map(float, input().split()))

# DPの表を用意（行：投げた枚数0〜N、列：表の枚数0〜N）
dp = [[0.0] * (N + 1) for _ in range(N + 1)]
dp[0][0] = 1.0  # 今まで投げていないとき、表0枚の確率は100％

for i in range(1, N + 1):
    p = ps[i - 1]
    for j in range(0, i + 1):
        dp[i][j] = dp[i - 1][j] * (1 - p)
        if j > 0:
            dp[i][j] += dp[i - 1][j - 1] * p

# 表の数 > 裏の数 = 表の数 > N/2
ans = sum(dp[N][(N // 2 + 1) :])
print(ans)
