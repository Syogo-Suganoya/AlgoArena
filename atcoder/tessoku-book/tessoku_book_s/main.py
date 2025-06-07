N, W = map(int, input().split())
weights = []
values = []

for i in range(N):
    w, v = map(int, input().split())
    weights.append(w)
    values.append(v)

# dp[i][j]: i番目までの荷物を使って、重さがj以下のときの最大価値
# iは0からNまで、jは0からWまで
dp = [[0] * (W + 1) for _ in range(N + 1)]

# i: 荷物を何番目まで使うか（0スタート）
for i in range(N):
    # j: 許容重量
    for j in range(W + 1):
        # i番目の荷物を取らない場合
        dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])

        # i番目の荷物を取る場合、ただし重量オーバーしないときだけ
        if j + weights[i] <= W:
            dp[i + 1][j + weights[i]] = max(
                dp[i + 1][j + weights[i]], dp[i][j] + values[i]
            )

print(max(dp[-1]))
