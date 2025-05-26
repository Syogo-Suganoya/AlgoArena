import heapq

# 入力
N, M = map(int, input().split())
A = list(map(int, input().split()))

# 隣接リスト作成
# (隣接頂点, 辺の重み) のリストを格納
graph = [[] for _ in range(N)]
for _ in range(M):
    u, v, b = map(int, input().split())
    u -= 1  # 0-indexed に直す
    v -= 1
    graph[u].append((v, b))
    graph[v].append((u, b))  # 無向グラフなので両方向

# ダイクストラの準備
INF = 10**18
dist = [INF] * N
dist[0] = A[0]  # 頂点1のコストはA[0]で初期化

# (距離, 頂点) のタプルを優先度付きキューに入れる
h = [(dist[0], 0)]

while h:
    d, u = heapq.heappop(h)
    # すでに更新済みのものなら無視
    if d > dist[u]:
        continue

    # 隣接頂点を確認
    for v, b in graph[u]:
        # 新たなコスト = 今のコスト + 辺の重み + 次の頂点の重み
        new_cost = d + b + A[v]
        if new_cost < dist[v]:
            dist[v] = new_cost
            heapq.heappush(h, (new_cost, v))

# 頂点1は除くので、2からNまでを出力
print(*dist[1:])
