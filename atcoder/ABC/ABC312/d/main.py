MOD = 998244353
S = input()
N = len(S)

# dp[i][j] := i文字まで使って、開き括弧-閉じ括弧がjの数え上げ
dp = [[0] * (N + 2) for _ in range(N + 1)]
dp[0][0] = 1  # 初期状態、何も使っていない・深さ0は1通り

for i in range(N):
    for j in range(N + 1):
        if S[i] == "(" or S[i] == "?":
            dp[i + 1][j + 1] = (dp[i + 1][j + 1] + dp[i][j]) % MOD
        if S[i] == ")" or S[i] == "?":
            if j > 0:
                dp[i + 1][j - 1] = (dp[i + 1][j - 1] + dp[i][j]) % MOD

print(dp[N][0])  # 最後に差が0になっているものだけが正しい括弧列
