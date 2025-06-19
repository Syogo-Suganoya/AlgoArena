from collections import deque

H, W = map(int, input().split())
grid = [input().strip() for _ in range(H)]

# 全体の白マス数をカウント
white_count = sum(row.count(".") for row in grid)

# 距離記録用配列（未訪問は -1）
dist = [[-1] * W for _ in range(H)]

# 幅優先探索（BFS）で最短距離を探索
queue = deque()
if grid[0][0] == ".":
    dist[0][0] = 1  # スタート地点の距離は1
    queue.append((0, 0))

# 上下左右の移動方向
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while queue:
    y, x = queue.popleft()
    for dy, dx in directions:
        ny, nx = y + dy, x + dx
        # 範囲内かつ白マスかつ未訪問
        if 0 <= ny < H and 0 <= nx < W:
            if grid[ny][nx] == "." and dist[ny][nx] == -1:
                dist[ny][nx] = dist[y][x] + 1
                queue.append((ny, nx))

# ゴールに到達できたか？
goal_dist = dist[H - 1][W - 1]
if goal_dist == -1:
    print(-1)  # ゴールできなければ -1
else:
    print(white_count - goal_dist)  # 経路に使わなかった白マス数
