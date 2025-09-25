N = int(input())
A = list(map(int, input().split()))

# 累積和の計算
prefix_sum = [0] * (N + 1)
for i in range(N):
    prefix_sum[i + 1] = prefix_sum[i] + A[i]

# dp の初期化
dp = [[float("inf")] * N for _ in range(N)]

# 基本ケース
for i in range(N):
    dp[i][i] = 0

for length in range(2, N + 1):
    # 区間の左端 l を 0 から N-length まで動かす
    # 区間が長さ length になるように
    for l in range(N - length + 1):
        r = l + length - 1  # 区間の右端 r を計算

        # 区間 [l..r] をどこで分割するか k を試す
        # k は l から r-1 まで
        for k in range(l, r):
            # dp[l][r] に区間を分割してまとめる場合の最小コストを更新
            # dp[l][k] : 左側の区間をまとめるコスト
            # dp[k+1][r] : 右側の区間をまとめるコスト
            # prefix_sum[r+1] - prefix_sum[l] : 左右をまとめる最後の合体コスト
            dp[l][r] = min(
                dp[l][r],
                dp[l][k] + dp[k + 1][r] + prefix_sum[r + 1] - prefix_sum[l],
            )

# 結果の出力
print(dp[0][N - 1])
