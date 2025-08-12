import heapq

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]  # 1-indexed

for _ in range(M):
    A, B, C = map(int, input().split())
    # 無向グラフの場合は両方向に辺を追加
    graph[A].append((B, C))
    graph[B].append((A, C))

# ダイクストラ法
INF = float("inf")
dist = [INF] * (N + 1)
dist[1] = 0  # 始点1の距離は0
pq = [(0, 1)]  # (距離, 頂点)

while pq:
    cost, u = heapq.heappop(pq)
    if cost > dist[u]:
        continue  # 既に確定済み

    for v, w in graph[u]:
        new_cost = cost + w
        if new_cost < dist[v]:
            dist[v] = new_cost
            heapq.heappush(pq, (new_cost, v))

# 出力（頂点1から各頂点までの最短距離）
for i in range(1, N + 1):
    print(dist[i] if dist[i] != INF else -1)
