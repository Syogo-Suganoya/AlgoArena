from collections import deque

H, W = map(int, input().split())
grid = [input().rstrip() for _ in range(H)]
A, B, C, D = map(int, input().split())
A -= 1
B -= 1
C -= 1
D -= 1

INF = 10**18
dist = [[INF] * W for _ in range(H)]
dist[A][B] = 0

dq = deque()
dq.append((A, B))

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

while dq:
    x, y = dq.popleft()
    if x == C and y == D:
        break

    # cost 0 moves
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < H and 0 <= ny < W:
            if grid[nx][ny] == "." and dist[nx][ny] > dist[x][y]:
                dist[nx][ny] = dist[x][y]
                dq.appendleft((nx, ny))

    # cost 1 moves (kick)
    for dx, dy in dirs:
        for k in (1, 2):
            nx, ny = x + dx * k, y + dy * k
            if 0 <= nx < H and 0 <= ny < W:
                if dist[nx][ny] > dist[x][y] + 1:
                    dist[nx][ny] = dist[x][y] + 1
                    dq.append((nx, ny))

ans = dist[C][D]
print(ans if ans < INF else -1)
