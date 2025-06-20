X, Y, Z = map(int, input().split())  # 小文字, 大文字, CapsLock のコスト
S = input()
N = len(S)

INF = float("inf")
dp = [[INF] * (N + 1) for _ in range(2)]  # dp[0]: CapsLock OFF, dp[1]: ON
dp[0][0] = 0  # 最初は CapsLock OFF でコスト0

for i in range(N):
    c = S[i]
    # 小文字を入力したいとき
    if c == "a":
        # 現在 CapsLock OFF → 小文字入力 = X
        dp[0][i + 1] = min(dp[0][i + 1], dp[0][i] + X)
        # 現在 CapsLock ON → 小文字入力 = Y
        dp[1][i + 1] = min(dp[1][i + 1], dp[1][i] + Y)
        # 状態切り替えも考慮
        dp[1][i + 1] = min(dp[1][i + 1], dp[0][i] + Z + Y)  # OFF → ON → a
        dp[0][i + 1] = min(dp[0][i + 1], dp[1][i] + Z + X)  # ON → OFF → a
    elif c == "A":
        dp[0][i + 1] = min(dp[0][i + 1], dp[0][i] + Y)
        dp[1][i + 1] = min(dp[1][i + 1], dp[1][i] + X)
        dp[1][i + 1] = min(dp[1][i + 1], dp[0][i] + Z + X)
        dp[0][i + 1] = min(dp[0][i + 1], dp[1][i] + Z + Y)

print(min(dp[0][N], dp[1][N]))
