MOD = 10**9 + 7

S = input()
N = len(S)
T = "chokudai"

# dp[i][j]: S の i 文字目まで見て、T の j 文字目まで作る方法の数
dp = [[0] * (len(T) + 1) for _ in range(N + 1)]

dp[0][0] = 1  # 初期状態：何も選ばずに何も作らない

for i in range(N):
    for j in range(len(T) + 1):
        # 今の文字を使わない場合（スキップ）
        dp[i + 1][j] = (dp[i + 1][j] + dp[i][j]) % MOD

        # 今の文字を使う場合
        if j < len(T) and S[i] == T[j]:
            dp[i + 1][j + 1] = (dp[i + 1][j + 1] + dp[i][j]) % MOD

print(dp[-1][-1])
