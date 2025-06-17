N = int(input())

# dp[0][i]: 解毒状態
# dp[1][i]: 毒状態
dp = [[0] * (N + 1) for _ in range(2)]

# 初期状態は解毒、毒の両方とも 0 にしてよい（開始前）
dp[0][0] = 0
dp[1][0] = 0

for i in range(1, N + 1):
    X, Y = map(int, input().split())
    if X == 0:
        # 解毒料理
        # 食べない場合,食べた場合
        # 解毒状態ても毒状態でも食べられる
        dp[0][i] = max(dp[0][i - 1], max(dp[0][i - 1], dp[1][i - 1]) + Y)
        # 逆も更新
        dp[1][i] = max(dp[1][i], dp[1][i - 1])
        continue
    # 毒料理
    # 食べない場合,食べた場合
    # 解毒状態しか食べられない
    dp[1][i] = max(dp[1][i - 1], dp[0][i - 1] + Y)
    # 逆も更新
    dp[0][i] = max(dp[0][i], dp[0][i - 1])


print(max(dp[0][-1], dp[1][-1]))
