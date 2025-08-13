N, S = map(int, input().split())
A = list(map(int, input().split()))

# dp[i][x]: カード1〜iで合計xが可能か
dp = [[False] * (S + 1) for _ in range(N + 1)]
dp[0][0] = True

# predecessor[i][x] に「どこから来たか (prev_i, prev_x)」を記録
pre = [[None] * (S + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    a = A[i - 1]
    for x in range(S + 1):
        # カード i を選ばない場合
        if dp[i - 1][x]:
            dp[i][x] = True
            pre[i][x] = (i - 1, x)
        # カード i を選ぶ場合
        if x >= a and dp[i - 1][x - a]:
            dp[i][x] = True
            pre[i][x] = (i - 1, x - a)

# S を作ることができるかチェック
if not dp[N][S]:
    print(-1)
else:
    res = []
    i, x = N, S
    # 足跡をたどって選ばれたカードを集める
    while i > 0:
        pi, px = pre[i][x]
        if px is None:
            break
        # 「x が変わった」ならカード i を選んだ証拠
        if px != x:
            res.append(i)
        i, x = pi, px

    res.reverse()
    print(len(res))
    print(*res)
