A, B = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# dp[i][j] := 左に残り i 個、右に残り j 個の状態で先手−後手差の最大値
dp = [[0] * (B + 1) for _ in range(A + 1)]

# 後ろから DP
for i in range(A + 1):
    for j in range(B + 1):
        res = -(10**18)

        # 左から取る場合
        if i > 0:
            val = a[A - i]
            res = max(res, val - dp[i - 1][j])
        # 右から取る場合
        if j > 0:
            val = b[B - j]
            res = max(res, val - dp[i][j - 1])

        dp[i][j] = res if i != 0 or j != 0 else 0

# 先手の合計 = (全体の和 + 差) // 2
total = sum(a) + sum(b)
print((total + dp[A][B]) // 2)
