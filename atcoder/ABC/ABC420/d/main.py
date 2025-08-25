from collections import deque

H, W = map(int, input().split())
maze = [list(input()) for _ in range(H)]

maze2 = []
for row in maze:
    new_row = []
    for c in row:
        if c == "o":
            new_row.append("x")
        elif c == "x":
            new_row.append("o")
        else:
            new_row.append(c)
    maze2.append(new_row)

for i in range(H):
    for j in range(W):
        if maze[i][j] == "S":
            sy, sx = i, j
        elif maze[i][j] == "G":
            gy, gx = i, j

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# BFS
queue = deque()
queue.append((sy, sx, 0, 0))

visited = [[[False, False] for _ in range(W)] for _ in range(H)]
visited[sy][sx][0] = True

while queue:
    y, x, flip, dist = queue.popleft()

    if (y, x) == (gy, gx):
        print(dist)
        break

    for dy, dx in dirs:
        ny, nx = y + dy, x + dx
        if 0 <= ny < H and 0 <= nx < W:
            cell = maze[ny][nx] if flip == 0 else maze2[ny][nx]

            if cell == "#" or cell == "x":
                continue

            new_flip = flip
            if maze[ny][nx] == "?":
                new_flip ^= 1

            if not visited[ny][nx][new_flip]:
                visited[ny][nx][new_flip] = True
                queue.append((ny, nx, new_flip, dist + 1))
else:
    print(-1)
