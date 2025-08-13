import heapq

N, M = map(int, input().split())

# グラフ構築（隣接リスト）
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))  # A→B (コストC)
    graph[B].append((A, C))  # 無向なのでB→Aも追加

# ダイクストラ法
INF = 10**18
dist = [INF] * (N + 1)  # 各頂点までの最小コスト
prev = [-1] * (N + 1)  # 経路復元用
dist[1] = 0

pq = [(0, 1)]  # (現在までのコスト, 頂点)
while pq:
    cost, v = heapq.heappop(pq)
    if cost > dist[v]:
        continue
    for nv, w in graph[v]:
        if dist[nv] > dist[v] + w:
            dist[nv] = dist[v] + w
            prev[nv] = v
            heapq.heappush(pq, (dist[nv], nv))

path = []
cur = N
while cur != -1:
    path.append(cur)
    cur = prev[cur]
path.reverse()

print(*path)
