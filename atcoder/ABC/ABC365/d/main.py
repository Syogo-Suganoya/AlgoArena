n = int(input())
s = input()

# dp[i][j]: i回目のじゃんけんで、最後に出した手が j(0: R, 1: P, 2: S) のときの最大勝利回数
dp = [[-1] * 3 for _ in range(n + 1)]
dp[0][0] = 0  # 0回目の初期状態: どの手も出してないので勝利回数0
dp[0][1] = 0
dp[0][2] = 0

for i in range(n):
    # もらうDP
    if s[i] == "R":
        # 前回出した手以外を更新する
        # あいこの時、前回maxをとる
        dp[i + 1][0] = max(dp[i][1], dp[i][2])
        # 勝った時は+1
        dp[i + 1][2] = max(dp[i][0], dp[i][1]) + 1
        # 負けの時は更新しない。次のループのmaxで穴埋めされる
    elif s[i] == "P":
        dp[i + 1][1] = max(dp[i][0], dp[i][2]) + 1
        dp[i + 1][2] = max(dp[i][0], dp[i][1])
    elif s[i] == "S":
        dp[i + 1][0] = max(dp[i][1], dp[i][2]) + 1
        dp[i + 1][1] = max(dp[i][0], dp[i][2])

print(max(dp[-1]))
