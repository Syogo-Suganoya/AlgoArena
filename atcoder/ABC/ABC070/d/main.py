from collections import deque

# 入力
N = int(input())  # 頂点数
graph = [[] for _ in range(N)]

# 辺の情報を読み込む（無向グラフ）
for _ in range(N - 1):
    a, b, c = map(int, input().split())
    graph[a - 1].append((b - 1, c))  # 0-index に変換
    graph[b - 1].append((a - 1, c))

Q, K = map(int, input().split())
K -= 1  # 0-index に変換

# K から各頂点への距離を BFS で計算する
dist = [-1] * N  # 未訪問を -1 で初期化
dist[K] = 0
queue = deque([K])

while queue:
    current = queue.popleft()
    for neighbor, cost in graph[current]:
        if dist[neighbor] == -1:  # 未訪問なら
            dist[neighbor] = dist[current] + cost
            queue.append(neighbor)

# 各クエリに対して K を経由した距離を計算
for _ in range(Q):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    # K から x までの距離 + K から y までの距離
    print(dist[x] + dist[y])
