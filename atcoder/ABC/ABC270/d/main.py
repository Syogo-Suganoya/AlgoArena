N, K = map(int, input().split())
A = list(map(int, input().split()))

# dp[i] = i個の石の状態で先手が最大で取れる数
dp = [0] * (N + 1)

for i in range(1, N + 1):
    best = 0
    for a in A:
        # a 個取れる場合だけ
        if i - a >= 0:
            # 後手の最大を引いた分が先手の取り分
            candidate = i - dp[i - a]
            if candidate > best:
                best = candidate
    # i個の石で先手が最大で取れる数を更新
    dp[i] = best
# 残り N 個の石の状態で先手の最大取り分
print(dp[N])
