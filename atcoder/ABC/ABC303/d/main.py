X, Y, Z = map(int, input().split())
S = input()
N = len(S)

# dp[i][j]: i文字目まで入力し、CapsLockの状態がj（0: OFF, 1: ON）のときの最小時間
dp = [[float("inf")] * 2 for _ in range(N + 1)]
dp[0][0] = 0  # 初期状態：CapsLock OFF
dp[0][1] = Z  # CapsLockをONにする

for i in range(N):
    c = S[i]
    if c == "a":
        # 小文字の場合
        dp[i + 1][0] = min(dp[i + 1][0], dp[i][0] + X)  # OFF → OFF
        dp[i + 1][1] = min(dp[i + 1][1], dp[i][1] + Y)  # ON → ON
        dp[i + 1][1] = min(dp[i + 1][1], dp[i][0] + Z + Y)  # OFF → ON
        dp[i + 1][0] = min(dp[i + 1][0], dp[i][1] + Z + X)  # ON → OFF
    else:
        # 大文字の場合
        dp[i + 1][0] = min(dp[i + 1][0], dp[i][0] + Y)  # OFF → OFF
        dp[i + 1][1] = min(dp[i + 1][1], dp[i][1] + X)  # ON → ON
        dp[i + 1][1] = min(dp[i + 1][1], dp[i][0] + Z + X)  # OFF → ON
        dp[i + 1][0] = min(dp[i + 1][0], dp[i][1] + Z + Y)  # ON → OFF

# 最終的な最小時間
print(min(dp[N][0], dp[N][1]))
