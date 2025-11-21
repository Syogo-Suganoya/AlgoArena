from collections import deque

H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

# S の位置を探す
for i in range(H):
    for j in range(W):
        if S[i][j] == "S":
            si, sj = i, j

# S の上下左右
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# S の隣の '.' に ID を振る
id_grid = [[0] * W for _ in range(H)]
start_points = []
cur_id = 1

for dx, dy in dirs:
    ni, nj = si + dx, sj + dy
    if 0 <= ni < H and 0 <= nj < W and S[ni][nj] == ".":
        id_grid[ni][nj] = cur_id
        start_points.append((ni, nj, cur_id))
        cur_id += 1

# 隣に '.' が2つ未満なら閉路は作れない
if len(start_points) < 2:
    print("No")
    exit()

# BFS キュー
q = deque(start_points)

while q:
    x, y, c = q.popleft()

    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if not (0 <= nx < H and 0 <= ny < W):
            continue
        if S[nx][ny] == "#":
            continue
        if (nx, ny) == (si, sj):
            continue  # S は使わない

        if id_grid[nx][ny] == 0:
            # 初めて訪問 → 今のIDで塗る
            id_grid[nx][ny] = c
            q.append((nx, ny, c))
        else:
            # すでに別IDで塗られている → 閉路あり！
            if id_grid[nx][ny] != c:
                print("Yes")
                exit()

# ここまで来たら閉路なし
print("No")
