N, H, M = map(int, input().split())
A = []
B = []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

# DP[i][m] := i 番目までのモンスターを倒したとき、
# 魔力が m 残っている状態での体力の最大値
# 到達不可の場合は -1
dp = [[-1] * (M + 1) for _ in range(N + 1)]

# 初期状態: モンスター0体倒したとき、魔力 M、体力 H
dp[0][M] = H

# モンスターを順番に倒していく
for i in range(N):
    a = A[i]
    b = B[i]
    for m in range(M + 1):
        if dp[i][m] == -1:
            continue  # 到達不可の状態はスキップ

        # 1. 体力で倒す場合
        if dp[i][m] >= a:
            # 魔力は変わらず、体力が減る
            dp[i + 1][m] = max(dp[i + 1][m], dp[i][m] - a)

        # 2. 魔力で倒す場合
        if m >= b:
            # 魔力が減る、体力はそのまま
            dp[i + 1][m - b] = max(dp[i + 1][m - b], dp[i][m])

# 最大何体倒せるかを求める
for i in range(N, 0, -1):
    if max(dp[i]) >= 0:
        print(i)
        break
