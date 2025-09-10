n, k = map(int, input().split())
lr = [tuple(map(int, input().split())) for _ in range(k)]

MOD = 998244353
# dp[i] = マスiに到達する方法の数
# ただし「差分管理」をするので、直接「方法の数」が入るわけではない
dp = [0] * n
dp[0] = 1  # スタート地点には1通り
dp[1] = -1  # 差分管理の都合で -1 を置いておく

# iを左から順に累積しながら進める
for i in range(n):
    if i > 0:
        # 差分配列を累積して、実際のdp[i]の値を求める
        dp[i] += dp[i - 1]
        dp[i] %= MOD  # 毎回modを取る

    # iからジャンプできる範囲 [i+l, i+r]
    for j in range(k):
        l, r = lr[j]
        r += 1  # 差分法では「終点の1つ右」で -dp[i] を加える
        if i + l < n:
            # 区間の始まりに +dp[i]
            dp[i + l] += dp[i]
            dp[i + l] %= MOD
        if i + r < n:
            # 区間の終わり+1に -dp[i]（= MOD - dp[i]）
            dp[i + r] += MOD - dp[i]
            dp[i + r] %= MOD

# ゴール地点に到達する方法の数が答え
print(dp[n - 1])
