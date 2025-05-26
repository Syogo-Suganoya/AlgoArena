N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

# dp[i][j]: i日目にjの行動をしたときの最大スコア
dp = [[0] * 3 for _ in range(N)]

# 初日（0日目）のスコアはそのまま
for j in range(3):
    dp[0][j] = A[0][j]

# 1日目からN-1日目まで
for i in range(1, N):
    for j in range(3):  # 今日の行動
        for k in range(3):  # 昨日の行動
            if j == k:
                continue  # 同じ行動は連続で選べない
            dp[i][j] = max(dp[i][j], dp[i - 1][k] + A[i][j])

# N-1日目の最大スコアを出力
print(max(dp[N - 1]))
