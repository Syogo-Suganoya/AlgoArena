n, m = map(int, input().split())

x = [0] + list(map(int, input().split()))
b = [0] * (n + 1)
for _ in range(m):
    c, y = map(int, input().split())
    b[c] = y

# dp[i][j] : i 回目終了時に「連続 j 回表」の最大スコア
dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    # (1) 表を出した場合の遷移
    #     連続カウント j が 1 以上のとき
    for j in range(1, i + 1):
        # 直前に連続 j-1 回表 → 今回表で j 回へ
        dp[i][j] = dp[i - 1][j - 1] + x[i] + b[j]

    # (2) 裏を出した場合の遷移
    #     連続カウントはリセットされ 0 になる。
    #     このときは前のすべての状態から遷移可能。
    dp[i][0] = max(dp[i - 1][:i])  # dp[i-1][0..i-1] の最大値

# 最終結果：n 回目終了後の全状態の最大値
print(max(dp[n]))
