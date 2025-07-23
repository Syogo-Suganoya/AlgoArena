from collections import deque

H, W = map(int, input().split())
maze = [list(input()) for _ in range(H)]

# "o" の位置を見つける
points = []
for i in range(H):
    for j in range(W):
        if maze[i][j] == "o":
            points.append((i, j))

# スタートとゴール
sx, sy = points[0]
gx, gy = points[1]

# BFS の準備
dist = [[-1] * W for _ in range(H)]
dist[sx][sy] = 0
q = deque()
q.append((sx, sy))

# 移動方向（上下左右）
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 範囲内かつ未訪問なら
        if 0 <= nx < H and 0 <= ny < W and dist[nx][ny] == -1:
            dist[nx][ny] = dist[x][y] + 1
            q.append((nx, ny))

# ゴールまでの距離を出力
print(dist[gx][gy])

"""
H, W = map(int, input().split())
maze = [list(input()) for _ in range(H)]

oをスタートとし、もう一方のoをゴールとする最短経路
壁はない、範囲外にはいけない
"""
