from collections import deque

# 入力処理
H, W = map(int, input().split())
rs, cs = map(lambda x: int(x) - 1, input().split())
rt, ct = map(lambda x: int(x) - 1, input().split())
grid = [input().strip() for _ in range(H)]

# 上下左右への移動（方向）
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
INF = float("inf")

# 最短手数を管理する 3 次元配列 [x][y][方向]
dist = [[[INF] * 4 for _ in range(W)] for _ in range(H)]

# デック初期化
queue = deque()
for d in range(4):
    dist[rs][cs][d] = 0
    queue.append((rs, cs, d))

# BFS の開始
while queue:
    x, y, dir_now = queue.popleft()

    # 4方向の探索
    for i, (dx, dy) in enumerate(directions):
        nx, ny = x + dx, y + dy

        # 範囲外や壁のチェック
        if not (0 <= nx < H and 0 <= ny < W) or grid[nx][ny] == "#":
            continue

        # コスト計算
        cost = dist[x][y][dir_now] + (dir_now != i)

        if cost < dist[nx][ny][i]:
            dist[nx][ny][i] = cost
            if dir_now != i:
                queue.append((nx, ny, i))
            else:
                queue.appendleft((nx, ny, i))

# ゴール地点での最小手数を求める
answer = min(dist[rt][ct])
print(answer)
