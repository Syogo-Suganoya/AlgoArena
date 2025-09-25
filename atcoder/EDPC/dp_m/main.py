MOD = 10**9 + 7

# 入力
N, M = map(int, input().split())
a = list(map(int, input().split()))

# dp[j] := 現在までで合計 j 個の飴を作る方法の数
dp = [0] * (M + 1)
dp[0] = 1  # 0 個の飴を配る方法は 1 通り（何も配らない）

for i in range(N):
    # 次の種類までの DP を格納する配列
    ndp = [0] * (M + 1)

    # 累積和 cum[j+1] = dp[0] + dp[1] + ... + dp[j]
    cum = [0] * (M + 2)
    for j in range(M + 1):
        cum[j + 1] = (cum[j] + dp[j]) % MOD

    # j 個の飴を配る場合の方法数を計算
    for j in range(M + 1):
        # i 番目の種類から取る飴の個数は最大 a[i] まで
        # 左端は j - a[i] （負にならないように max(0, j-a[i])）
        left = max(0, j - a[i])
        # 累積和を使って和を高速計算
        ndp[j] = (cum[j + 1] - cum[left]) % MOD

    # 更新
    dp = ndp

# M 個の飴を配る方法の数を出力
print(dp[M])
