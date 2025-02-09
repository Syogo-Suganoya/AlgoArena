from collections import deque


def solve_humidifier(h, w, d, grid):
    # 方向ベクトル (上下左右)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # 加湿器 (H) の位置をキューに追加
    queue = deque()
    visited = [[False] * w for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if grid[i][j] == "H":  # 加湿器の位置
                queue.append((i, j, 0))  # (x座標, y座標, 現在の距離)
                visited[i][j] = True

    # BFSで探索
    while queue:
        x, y, dist = queue.popleft()

        # 現在の距離がDを超えたら探索を終了
        if dist >= d:
            continue

        # 周囲4方向を確認
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < h
                and 0 <= ny < w
                and not visited[nx][ny]
                and grid[nx][ny] == "."
            ):
                visited[nx][ny] = True
                queue.append((nx, ny, dist + 1))

    # 加湿されたマスを数える
    result = sum(row.count(True) for row in visited)
    return result


# 入力の処理
h, w, d = map(int, input().split())
grid = [input().strip() for _ in range(h)]

# 問題を解く
answer = solve_humidifier(h, w, d, grid)

# 結果を出力
print(answer)
