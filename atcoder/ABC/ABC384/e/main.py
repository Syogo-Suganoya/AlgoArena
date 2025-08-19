import heapq

# 入力
H, W, X = map(int, input().split())
x, y = map(int, input().split())
x -= 1  # 0-index に変換
y -= 1

# 番兵として周囲に大きな値を配置
INF = 2_500_000_000_000_000_00
slime_size = [[INF] * (W + 2) for _ in range(H + 2)]

# 中央 H x W マスだけ読み込む
for i in range(H):
    row = list(map(int, input().split()))
    for j in range(W):
        slime_size[i + 1][j + 1] = row[j]

# スタートマスのスライムサイズ
now_size = slime_size[x + 1][y + 1]

# 訪問済みマス
visited = [[False] * (W + 2) for _ in range(H + 2)]

# 優先度付きキュー（最小値優先）
pq = []
heapq.heappush(pq, (0, x + 1, y + 1))
visited[x + 1][y + 1] = True

while pq:
    size, cx, cy = heapq.heappop(pq)

    # 吸収可能かチェック
    if size >= (now_size + X - 1) // X:
        break

    # スライムを吸収
    now_size += size

    # 隣接マスをキューに追加
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = cx + dx, cy + dy
        if not visited[nx][ny]:
            visited[nx][ny] = True
            heapq.heappush(pq, (slime_size[nx][ny], nx, ny))

print(now_size)
