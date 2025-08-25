from collections import deque

INF = 10**9
dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 上下左右の移動


# 1. 通常のBFS：スタート座標(sx, sy)から各マスへの最短距離を求める
def bfs(grid, sx, sy):
    h, w = len(grid), len(grid[0])
    dist = [[INF] * w for _ in range(h)]
    if grid[sx][sy] == "#":  # スタート地点が壁なら到達不可
        return dist
    que = deque()
    dist[sx][sy] = 0
    que.append((sx, sy))
    while que:
        fx, fy = que.popleft()
        for dx, dy in dxy:
            tx, ty = fx + dx, fy + dy
            if not (0 <= tx < h and 0 <= ty < w):
                continue
            if grid[tx][ty] == "#":
                continue
            if dist[tx][ty] > dist[fx][fy] + 1:
                dist[tx][ty] = dist[fx][fy] + 1
                que.append((tx, ty))
    return dist


# 2. グラフ上のBFS：充電ポイントやS,Tをノードとみなし、到達可能関係をたどる
def bfs2(isReachable, s):
    n = len(isReachable)
    seen = [False] * n
    que = deque()
    seen[s] = True
    que.append(s)
    while que:
        f = que.popleft()
        for t in range(n):
            if isReachable[f][t] and not seen[t]:
                seen[t] = True
                que.append(t)
    return seen


# === main ===
h, w = map(int, input().split())
grid = [list(input().strip()) for _ in range(h)]

sx = sy = tx = ty = -1
for i in range(h):
    for j in range(w):
        if grid[i][j] == "S":
            sx, sy = i, j
        if grid[i][j] == "T":
            tx, ty = i, j

n = int(input())
r, c, e = [], [], []
for _ in range(n):
    ri, ci, ei = map(int, input().split())
    r.append(ri - 1)
    c.append(ci - 1)
    e.append(ei)

# SとTも充電ポイント扱いで追加
r.append(sx)
c.append(sy)
e.append(0)  # S
r.append(tx)
c.append(ty)
e.append(0)  # T
n += 2

# 各充電地点 i から BFS して、他の充電地点 j に届くか判定
isReachable = [[False] * n for _ in range(n)]
for i in range(n):
    distMap = bfs(grid, r[i], c[i])
    for j in range(n):
        if distMap[r[j]][c[j]] <= e[i]:  # iからjに届く（残りエネルギー以内）
            isReachable[i][j] = True

# S(=n-2)からBFSして、T(=n-1)にたどり着けるか？
reachable = bfs2(isReachable, n - 2)

print("Yes" if reachable[n - 1] else "No")
