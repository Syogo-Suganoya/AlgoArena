from collections import deque

N = int(input())
black_cells = []
for _ in range(N):
    X, Y = map(int, input().split())
    black_cells.append((X, Y))

directions = [(-1, -1), (-1, 0), (0, -1), (0, 1), (1, 0), (1, 1)]
visited = set()


def bfs_connected_components(start_x, start_y):
    queue = deque([(start_x, start_y)])
    visited.add((start_x, start_y))

    while queue:
        x, y = queue.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # すでに訪問済み or 壁（0 のような）ならスキップ
            if (nx, ny) in visited or (nx, ny) not in black_cells:
                continue

            # 訪問リストに追加し、キューに入れる
            visited.add((nx, ny))
            queue.append((nx, ny))


component_count = 0

# すべてのマスを調べる
for cell in black_cells:
    if cell not in visited:
        bfs_connected_components(cell[0], cell[1])
        component_count += 1  # 新しい連結成分が見つかったらカウント

print(component_count)
