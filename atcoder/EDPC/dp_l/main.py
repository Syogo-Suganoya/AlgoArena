N = int(input())
A = list(map(int, input().split()))

# dp[l][r] = 区間 [l, r] で先手が取る番のときに得られるスコア差
dp = [[0] * N for _ in range(N)]

# 区間長が1のとき（要素1つだけ）
for i in range(N):
    dp[i][i] = A[i]

# 区間長を2からNまで広げていく
for length in range(2, N + 1):
    for l in range(N - length + 1):
        r = l + length - 1
        # 先頭を取る or 末尾を取る
        take_left = A[l] - dp[l + 1][r]
        take_right = A[r] - dp[l][r - 1]
        dp[l][r] = max(take_left, take_right)

# 最初の区間全体 [0, N-1] の結果が答え
print(dp[0][N - 1])
