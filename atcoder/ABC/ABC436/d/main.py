from collections import deque

H, W = map(int, input().split())
maze = [list(input()) for _ in range(H)]

warp = {}
for i in range(H):
    for j in range(W):
        c = maze[i][j]
        if c.islower():
            warp.setdefault(c, []).append((i, j))

INF = 10**18
dist = [[INF] * W for _ in range(H)]

dq = deque()
dq.append((0, 0))
dist[0][0] = 0

vis = set()

while dq:
    x, y = dq.popleft()

    if (x, y) == (H - 1, W - 1):
        print(dist[x][y])
        exit()

    # 徒歩4方向
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < H and 0 <= ny < W:
            if maze[nx][ny] != "#" and dist[nx][ny] == INF:
                dist[nx][ny] = dist[x][y] + 1
                dq.append((nx, ny))

    # ワープ先
    c = maze[x][y]
    if c.islower() and c not in vis:
        for nx, ny in warp[c]:
            if dist[nx][ny] == INF:
                dist[nx][ny] = dist[x][y] + 1
                dq.append((nx, ny))
        vis.add(c)

print(-1)
