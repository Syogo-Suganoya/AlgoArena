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


"""
N, W = map(int, input().split())
weights=[]
values=[]
for i in range(N):
    w,v = map(int, input().split())
    weights.append(w)
    values.append(v)

dp[i番目まで荷物を選べる][許容重量]=最大価値
dp[N+1][W+1]

N回ループ i
    W回ループ j
        dp[i+1][j]=max(dp[i+1][j],dp[i][j])
        w+weights[i]がW以下
            dp[i+1][w+weights[i]]=max(dp[i+1][w+weights[i]],dp[i]+values[i])
print(max(dp[-1]))

"""


def ano():
    N, W = map(int, input().split())
    weight = []
    value = []
    for _ in range(N):
        w, v = map(int, input().split())
        weight.append(w)
        value.append(v)

    # dp[i][w]: i番目まで見て、重さw以下で得られる最大価値
    dp = [[0] * (W + 1) for _ in range(N + 1)]

    for i in range(N):
        for w in range(W + 1):
            # 取らない
            dp[i + 1][w] = max(dp[i + 1][w], dp[i][w])
            # 取る（重さ制限OKなら）
            if w + weight[i] <= W:
                dp[i + 1][w + weight[i]] = max(
                    dp[i + 1][w + weight[i]], dp[i][w] + value[i]
                )

    print(max(dp[N]))


# ano()
