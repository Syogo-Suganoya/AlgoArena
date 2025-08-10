# ダイクストラ法で距離一覧を得る関数
def dijkstra(graph, start, N):
    import heapq

    INF = float("inf")
    dist = [INF] * N
    dist[start] = 0
    heap = [(0, start)]
    while heap:
        cost, u = heapq.heappop(heap)
        if cost > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[v] > cost + w:
                dist[v] = cost + w
                heapq.heappush(heap, (dist[v], v))
    return dist


# 入力読み込みなど
N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append((b, c))
    graph[b].append((a, c))

dist_from_start = dijkstra(graph, 0, N)
dist_to_goal = dijkstra(graph, N - 1, N)

for k in range(N):
    print(dist_from_start[k] + dist_to_goal[k])
