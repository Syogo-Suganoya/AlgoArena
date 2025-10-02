# レーベンシュタイン距離

S = input().strip()
T = input().strip()
n = len(S)
m = len(T)

# dp[i][j] を (n+1) x (m+1) で初期化。大きな値を初期値にする
INF = 10**9
dp = [[INF] * (m + 1) for _ in range(n + 1)]

# 初期条件
dp[0][0] = 0
for i in range(1, n + 1):
    dp[i][0] = i
for j in range(1, m + 1):
    dp[0][j] = j

# DP 遷移
for i in range(1, n + 1):
    for j in range(1, m + 1):
        # 削除
        dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1)
        # 挿入
        dp[i][j] = min(dp[i][j], dp[i][j - 1] + 1)
        # 置換または一致
        cost = 0 if S[i - 1] == T[j - 1] else 1
        dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + cost)

# 出力
print(dp[n][m])
