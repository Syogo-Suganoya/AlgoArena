N = int(input())

# 中心 T の座標
tx, ty = N // 2, N // 2

# 各マスの距離を格納
dist = [[0] * N for _ in range(N)]
visited = [[False] * N for _ in range(N)]

# 右、下、左、上の順
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
dir_idx = 0  # 現在の方向

# スタート
x, y = 0, 0
d = 1  # 距離（1から）

while True:
    dist[x][y] = d
    visited[x][y] = True
    d += 1
    # T に着いたら終了
    if (x, y) == (tx, ty):
        break

    # 次の位置を計算
    nx, ny = x + dirs[dir_idx][0], y + dirs[dir_idx][1]

    # 範囲外 or 訪問済みなら方向を切り替え
    if not (0 <= nx < N and 0 <= ny < N) or visited[nx][ny]:
        dir_idx = (dir_idx + 1) % 4  # 右回りに方向を変える
        nx, ny = x + dirs[dir_idx][0], y + dirs[dir_idx][1]

    # 移動
    x, y = nx, ny

dist[tx][ty] = "T"
for row in dist:
    print(*row)
