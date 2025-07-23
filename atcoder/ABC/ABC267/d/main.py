N, M = map(int, input().split())
A = list(map(int, input().split()))

INF = float("-inf")
# dp[i][j] := i個見て、j個選んだときの最大スコア
dp = [[INF] * (M + 1) for _ in range(N + 1)]
dp[0][0] = 0

for i in range(N):
    for j in range(M + 1):
        # 選ばない
        dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
        # 選ぶ（j+1個目として）
        if j < M:
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + A[i] * (j + 1))

print(dp[N][M])
