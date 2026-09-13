from collections import deque

H, W = map(int, input().split())
A = [list(input()) for _ in range(H)]

danger = [[False] * W for _ in range(H)]

dirs = {">": (0, 1), "<": (0, -1), "^": (-1, 0), "v": (1, 0)}

# 視線処理
for i in range(H):
    for j in range(W):
        if A[i][j] in dirs:
            dx, dy = dirs[A[i][j]]
            x, y = i + dx, j + dy
            while 0 <= x < H and 0 <= y < W:
                if A[x][y] in "#<>^v":
                    break
                if A[x][y] == ".":
                    danger[x][y] = True
                x += dx
                y += dy

# BFS
dist = [[-1] * W for _ in range(H)]
q = deque()

for i in range(H):
    for j in range(W):
        if A[i][j] == "S":
            sx, sy = i, j
        if A[i][j] == "G":
            gx, gy = i, j

q.append((sx, sy))
dist[sx][sy] = 0

while q:
    x, y = q.popleft()
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = x + dx, y + dy
        if not (0 <= nx < H and 0 <= ny < W):
            continue
        if dist[nx][ny] != -1:
            continue
        if A[nx][ny] in "#<>^v":
            continue
        if danger[nx][ny]:
            continue

        dist[nx][ny] = dist[x][y] + 1
        q.append((nx, ny))

print(dist[gx][gy])
