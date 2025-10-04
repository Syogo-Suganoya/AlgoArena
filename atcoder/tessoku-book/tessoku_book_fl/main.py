import heapq

INF = 10**18


def dijkstra(n, adj, start):
    dist = [INF] * (n + 1)
    dist[start] = 0
    hq = [(0, start)]
    while hq:
        d, u = heapq.heappop(hq)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(hq, (nd, v))
    return dist


N, M = map(int, input().split())
adj = [[] for _ in range(N + 1)]
rev = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    adj[a].append((b, c))
    adj[b].append((a, c))
    rev[b].append((a, c))
    rev[a].append((b, c))

# 1 からの最短距離
dist1 = dijkstra(N, adj, 1)
# N からの最短距離（逆向きでも同じグラフなので rev でもいい）
distN = dijkstra(N, adj, N)

total = dist1[N]
ans = 0
for v in range(1, N + 1):
    if dist1[v] + distN[v] == total:
        ans += 1

print(ans)
