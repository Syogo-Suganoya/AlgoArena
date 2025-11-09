H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
P = list(map(int, input().split()))

# dp[i][j]: マス (i,j) に到達する「直前」に必要な最小コイン数
# ゴール (H-1, W-1) から逆順に計算していく
INF = 10**18
dp = [[INF] * W for _ in range(H)]

# 最後の日（ゴール）では、A[h-1][w-1]枚を回収後にP[last_day]枚を払う必要がある。
# つまり、その日の前に必要なコインは max(0, P[-1] - A[H-1][W-1])。
dp[H - 1][W - 1] = max(0, P[-1] - A[H - 1][W - 1])

# 逆から動く（ゴール→スタート）
for i in reversed(range(H)):
    for j in reversed(range(W)):
        day = i + j  # そのマスに到達する日（0-index）
        if i < H - 1:
            # 下のマスに行く場合に、次で必要なコインを満たすための条件を逆算
            need = max(0, dp[i + 1][j] + P[day] - A[i][j])
            dp[i][j] = min(dp[i][j], need)
        if j < W - 1:
            # 右のマスに行く場合も同様に
            need = max(0, dp[i][j + 1] + P[day] - A[i][j])
            dp[i][j] = min(dp[i][j], need)

# スタート時に必要なコイン数が答え
print(dp[0][0])
