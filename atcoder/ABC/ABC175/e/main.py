R, C, K = map(int, input().split())
items = [[0] * (C + 1) for _ in range(R + 1)]
for _ in range(K):
    r, c, v = map(int, input().split())
    items[r][c] = v

# dp[j][k] = 現在行で列 j にいて、その行で k 個拾ったときの最大価値
dp = [[-1] * 4 for _ in range(C + 1)]
dp[1][0] = 0
dp[1][1] = items[1][1]

for i in range(1, R + 1):
    # 右方向の遷移（同じ行内）
    for j in range(1, C + 1):
        for k in range(4):
            if dp[j][k] < 0:
                continue
            val = dp[j][k]

            # 右へ進む
            if j + 1 <= C:
                # 拾わない
                dp[j + 1][k] = max(dp[j + 1][k], val)
                # 拾う
                if k < 3:
                    dp[j + 1][k + 1] = max(dp[j + 1][k + 1], val + items[i][j + 1])

    if i == R:  # 最終行は下に行かない
        break

    # 下へ進む → 次の行に配列を渡す
    ndp = [[-1] * 4 for _ in range(C + 1)]
    for j in range(1, C + 1):
        for k in range(4):
            if dp[j][k] < 0:
                continue
            val = dp[j][k]
            # 下に移動した直後は拾った数リセット
            ndp[j][0] = max(ndp[j][0], val)
            # 拾う
            ndp[j][1] = max(ndp[j][1], val + items[i + 1][j])
    dp = ndp

print(max(dp[C]))
