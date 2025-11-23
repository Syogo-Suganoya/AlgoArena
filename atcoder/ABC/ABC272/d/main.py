import math
from collections import deque

N, M = map(int, input().split())

# 移動可能な差の組 (dx, dy) を事前計算
moves = []
for dx in range(int(math.isqrt(M)) + 1):
    dy2 = M - dx * dx
    if dy2 < 0:
        continue
    dy = int(math.isqrt(dy2))
    if dy * dy == dy2:
        for sx in [1, -1]:
            for sy in [1, -1]:
                if dx == 0 and sx == -1:
                    continue
                if dy == 0 and sy == -1:
                    continue
                moves.append((sx * dx, sy * dy))

# BFS で最短回数を求める
dist = [[-1] * N for _ in range(N)]
q = deque()
q.append((0, 0))
dist[0][0] = 0

while q:
    x, y = q.popleft()
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and dist[nx][ny] == -1:
            dist[nx][ny] = dist[x][y] + 1
            q.append((nx, ny))

# 出力
for row in dist:
    print(*row)
