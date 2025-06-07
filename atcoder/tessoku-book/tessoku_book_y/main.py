H, W = map(int, input().split())
maze = [list(input()) for _ in range(H)]

# dp[i][j]: マス (i, j) に到達する方法の数
dp = [[0] * W for _ in range(H)]
dp[0][0] = 1 if maze[0][0] == "." else 0

for i in range(H):
    for j in range(W):
        if maze[i][j] == "#":
            continue
        if j + 1 < W and maze[i][j + 1] == ".":
            dp[i][j + 1] += dp[i][j]
        if i + 1 < H and maze[i + 1][j] == ".":
            dp[i + 1][j] += dp[i][j]

print(dp[-1][-1])
