N, X = map(int, input().split())

# dp[i][j]：i回目の操作後にjに到達できるかどうか
dp = [[False] * (X + 1) for _ in range(N + 1)]

# 初期状態：0回の操作で位置0には確実にいる
dp[0][0] = True

# 各操作を処理
for i in range(N):
    a, b = map(int, input().split())
    for j in range(X + 1):
        if dp[i][j]:
            # i回目の操作でaまたはbを足した位置に進める
            if j + a <= X:
                dp[i + 1][j + a] = True
            if j + b <= X:
                dp[i + 1][j + b] = True

# 最終的にXにちょうど到達できるかを判定
print("Yes" if dp[-1][-1] else "No")
