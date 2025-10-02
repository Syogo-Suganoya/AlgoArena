N = int(input())
A = list(map(int, input().split()))

# dp[l][r]: 区間 [l, r] を1つにしたときの値
dp = [[0] * N for _ in range(N)]

# 長さ1はそのまま
for i in range(N):
    dp[i][i] = A[i]

# 区間の長さごとに計算
for length in range(2, N + 1):
    for l in range(N - length + 1):
        r = l + length - 1
        # 今の手番が先手か後手かを判定
        if (length % 2) == (N % 2):  # 先手の番
            dp[l][r] = max(dp[l + 1][r], dp[l][r - 1])
        else:  # 後手の番
            dp[l][r] = min(dp[l + 1][r], dp[l][r - 1])

print(dp[0][N - 1])
