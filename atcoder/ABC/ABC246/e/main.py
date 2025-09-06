from collections import deque

# 入力
N = int(input())
sx, sy = map(int, input().split())
gx, gy = map(int, input().split())
grid = [list(input()) for _ in range(N)]

# 0-index 化
sx -= 1
sy -= 1
gx -= 1
gy -= 1

# 斜め4方向
dirs = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

INF = 10**18
# dist[x][y][d] = (x,y) に d方向で到達したときの手数
dist = [[[INF] * 4 for _ in range(N)] for _ in range(N)]

# dequeで01-BFS
dq = deque()

# スタート地点は、どの方向から始めても0手
for d in range(4):
    dist[sx][sy][d] = 1
    dq.append((sx, sy, d))

while dq:
    x, y, d = dq.popleft()
    for nd, (dx, dy) in enumerate(dirs):
        nx, ny = x + dx, y + dy
        if not (0 <= nx < N and 0 <= ny < N):
            continue
        if grid[nx][ny] == "#":
            continue

        # コスト計算
        cost = dist[x][y][d] + (d != nd)
        if cost < dist[nx][ny][nd]:
            dist[nx][ny][nd] = cost
            if d == nd:
                dq.appendleft((nx, ny, nd))  # コスト0なら前
            else:
                dq.append((nx, ny, nd))  # コスト1なら後ろ

# ゴールの最小値を取る
ans = min(dist[gx][gy])
print(ans if ans != INF else -1)
