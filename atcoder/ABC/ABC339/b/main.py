H, W, N = map(int, input().split())
grid = [[0] * W for _ in range(H)]  # 0=白, 1=黒

# 初期位置と向き
x, y, dir = 0, 0, 0  # dir: 0=上, 1=右, 2=下, 3=左
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for _ in range(N):
    if grid[x][y] == 0:
        # 白 → 黒にして時計回り
        grid[x][y] = 1
        dir = (dir + 1) % 4
    else:
        # 黒 → 白にして反時計回り
        grid[x][y] = 0
        dir = (dir + 3) % 4

    # 移動（トーラス処理）
    x = (x + dx[dir]) % H
    y = (y + dy[dir]) % W

# 出力
for i in range(H):
    row = "".join("#" if grid[i][j] else "." for j in range(W))
    print(row)
