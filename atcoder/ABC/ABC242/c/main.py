MOD = 998244353  # 答えを求める際の法（オーバーフロー防止）

N = int(input())  # パスワードの桁数

# dp[d][i] := 長さ d の整数で、末尾が i の平坦数の個数
dp = [[0] * 10 for _ in range(N + 1)]

# 1桁目（d=1）は、1〜9のいずれも1通りずつ存在する
for i in range(1, 10):
    dp[1][i] = 1

# 2桁目以降をDPで更新
for d in range(2, N + 1):
    for i in range(1, 10):
        # i の前に来られるのは i-1, i, i+1 のいずれか
        for j in [i - 1, i, i + 1]:
            if 1 <= j <= 9:
                dp[d][i] = (dp[d][i] + dp[d - 1][j]) % MOD

# 最後の桁が1〜9のすべての数を合計して答えにする
print(sum(dp[N][1:]) % MOD)
