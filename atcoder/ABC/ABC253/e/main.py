MOD = 998244353

N, M, K = map(int, input().split())

# dp[i][a] = 長さ i+1 の数列、最後の要素が a の通り数
dp = [[0] * (M + 1) for _ in range(N)]
for a in range(1, M + 1):
    dp[0][a] = 1  # 最初の要素は自由に選べる

for i in range(1, N):
    # 前の段階の累積和を作る
    prefix = [0] * (M + 2)
    for a in range(1, M + 1):
        prefix[a + 1] = (prefix[a] + dp[i - 1][a]) % MOD

    for a in range(1, M + 1):
        val = 0
        # 小さい側（1..a-K）
        if a - K >= 1:
            val += prefix[a - K + 1]  # sum of dp[i-1][1..a-K]
        # 大きい側（a+K..M）
        if a + K <= M:
            val += (prefix[M + 1] - prefix[a + K]) % MOD
        # K == 0 のときは a 自身を2回数えてしまうので調整
        if K == 0:
            val -= dp[i - 1][a]

        dp[i][a] = val % MOD

# 答えは長さ N の数列すべての合計
print(sum(dp[N - 1]) % MOD)
