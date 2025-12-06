from collections import deque

H, W = map(int, input().split())
grid = [list(input()) for _ in range(H)]

# 4方向移動
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs(sy, sx):
    """(sy, sx) をスタートとしたときの全マスへの最短距離を返す"""
    dist = [[-1] * W for _ in range(H)]
    q = deque()
    q.append((sy, sx))
    dist[sy][sx] = 0

    while q:
        y, x = q.popleft()
        for dy, dx in dirs:
            ny, nx = y + dy, x + dx

            # 迷路外 or 壁 → 進めない
            if not (0 <= ny < H and 0 <= nx < W):
                continue
            if grid[ny][nx] == "#":
                continue

            # 未訪問なら距離を入れてキューへ
            if dist[ny][nx] == -1:
                dist[ny][nx] = dist[y][x] + 1
                q.append((ny, nx))

    return dist


ans = 0

# 全ての道マスを BFS のスタートにする
for i in range(H):
    for j in range(W):
        if grid[i][j] == ".":  # 道マスのみ
            dist = bfs(i, j)

            # dist の中で最大値をとる
            for y in range(H):
                for x in range(W):
                    if dist[y][x] != -1:
                        ans = max(ans, dist[y][x])

print(ans)
