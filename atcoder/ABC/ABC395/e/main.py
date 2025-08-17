import heapq

N, M, X = map(int, input().split())
G = [[] for _ in range(N)]  # 正方向
RG = [[] for _ in range(N)]  # 逆方向

for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    G[u].append(v)  # 正方向 u→v
    RG[v].append(u)  # 逆方向 v→u

INF = 10**18
dist = [[INF] * 2 for _ in range(N)]  # dist[node][flag]
dist[0][0] = 0
hq = [(0, 0, 0)]  # (距離, 頂点, flag)

while hq:
    d, u, f = heapq.heappop(hq)
    if d > dist[u][f]:
        continue

    # 1. 辺を移動（flag=0 なら G, flag=1 なら RG を使う）
    graph = G if f == 0 else RG
    for v in graph[u]:
        nd = d + 1
        if nd < dist[v][f]:
            dist[v][f] = nd
            heapq.heappush(hq, (nd, v, f))

    # 2. フラグを切り替える（コスト X）
    nf = 1 - f
    nd = d + X
    if nd < dist[u][nf]:
        dist[u][nf] = nd
        heapq.heappush(hq, (nd, u, nf))

# 答えは頂点 N-1 の表裏どちらかの最小値
ans = min(dist[N - 1][0], dist[N - 1][1])
print(ans)
