H, W = map(int, input().split())
maze = [input() for _ in range(H)]

mod = 10**9 + 7


# dp[i][j]: (i, j) に到達する経路数
dp = [[0] * W for _ in range(H)]

# スタート位置
dp[0][0] = 1

# 移動方向: 右と下
directions = [(0, 1), (1, 0)]

for i in range(H):
    for j in range(W):
        # 壁ならスキップ
        if maze[i][j] != ".":
            continue

        # dp[i][j] の値を右・下に「配る」
        for dx, dy in directions:
            ni, nj = i + dx, j + dy
            if 0 <= ni < H and 0 <= nj < W and maze[ni][nj] == ".":
                dp[ni][nj] += dp[i][j]
                dp[ni][nj] %= mod

print(dp[-1][-1])

"""
dp[H][W]=経路数
配るDP
H回ループ i
    W回ループ j
        右、下方向ループ
            マスが.以外
                continue
            dp[i+dx][j+dy]=dp[i][j]+1

print(dp[-1][-1])
"""
