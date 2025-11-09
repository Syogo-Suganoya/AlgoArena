N = int(input())
parts = [tuple(map(int, input().split())) for _ in range(N)]

# 頭の総重量の上限は全部のWの合計まで
total_W = sum(W for W, _, _ in parts)

# DP[w] = 頭の重量合計が w のときの最大値（頭H合計 + 体B合計）
dp = [-1] * (total_W + 1)
dp[0] = 0  # 頭0のとき初期値0

for W, H, B in parts:
    # DPを逆順に更新して重複カウントを防ぐ
    for w_h in range(total_W - W, -1, -1):
        if dp[w_h] == -1:
            continue
        # 頭にする場合
        dp[w_h + W] = max(dp[w_h + W], dp[w_h] + H)
        # 体にする場合
        dp[w_h] = max(dp[w_h], dp[w_h] + B)

# 最終的な答えを探索
ans = 0
for w_h in range(total_W + 1):
    w_b = total_W - w_h  # 体の重量合計
    if w_h <= w_b:  # 頭の重量 ≤ 体の重量
        ans = max(ans, dp[w_h])

print(ans)
