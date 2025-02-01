H, W = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(H)]

directions = [(0, 1), (1, 0)]
gx, gy = H - 1, W - 1


def dfs(x, y, visited):
    res = 0
    # ゴール地点に到達した場合
    if x == gx and y == gy:
        return 1

    # 訪問済みにする
    visited.append(grid[x][y])

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if not (0 <= nx < H and 0 <= ny < W):
            continue
        if grid[nx][ny] in visited:
            continue

        # 再帰的に探索
        res += dfs(nx, ny, visited)

    # 探索が終わったら現在地を未訪問に戻す（バックトラッキングが必要なら）
    visited.remove(grid[x][y])
    return res


print(dfs(0, 0, []))
