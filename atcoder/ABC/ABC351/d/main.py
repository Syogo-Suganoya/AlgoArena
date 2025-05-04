from collections import deque

# 入力
y, x = map(int, input().split())
graph = [list(input()) for _ in range(y)]

# 4方向移動（上下左右）
move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# 磁石の隣マスに '*' を置く（磁力の影響範囲）
for i in range(y):
    for j in range(x):
        if graph[i][j] == "#":
            for dy, dx in move:
                ni, nj = i + dy, j + dx
                if 0 <= ni < y and 0 <= nj < x and graph[ni][nj] != "#":
                    graph[ni][nj] = "*"

ans = 1

# BFS による連結成分探索
for i in range(y):
    for j in range(x):
        if graph[i][j] == ".":
            now_num = 1  # 現在の連結成分の`.`の数
            nei_set = set()  # 隣接する'*'の集合（重複を避けるためset）

            queue = deque()
            queue.append((i, j))
            graph[i][j] = "#"  # 訪問済みとしてマーク

            while queue:
                sy, sx = queue.popleft()
                for dy, dx in move:
                    ny, nx = sy + dy, sx + dx
                    if 0 <= ny < y and 0 <= nx < x:
                        if graph[ny][nx] == ".":
                            graph[ny][nx] = "#"  # 訪問済みに変更
                            now_num += 1
                            queue.append((ny, nx))
                        elif graph[ny][nx] == "*":
                            nei_set.add((ny, nx))  # 隣接する'*'を記録

            # 今の連結成分で移動可能なマス数の最大値を更新
            ans = max(ans, now_num + len(nei_set))

# 結果出力
print(ans)
