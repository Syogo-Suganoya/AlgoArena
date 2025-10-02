import heapq

# 入力
N, M = map(int, input().split())
G = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c, d = map(int, input().split())
    # (隣接ノード, 距離, 木フラグ) を格納
    G[a].append((b, c, d))
    G[b].append((a, c, d))

# 各頂点について「最短距離」と「そのときの最大木数」を保持
INF = 10**18
dist = [INF] * (N + 1)
wood = [-1] * (N + 1)

# スタートは頂点1、距離0、木0本
dist[1] = 0
wood[1] = 0

# 優先度付きキュー（距離が小さい順）
# 格納する情報は (距離, -木数, 頂点)
# → 木数は多い方が良いので、-wood を使って「小さい順」に比較させる
pq = [(0, 0, 1)]

while pq:
    d, minus_w, u = heapq.heappop(pq)
    w = -minus_w

    # すでにより良い解が見つかっている場合はスキップ
    if d > dist[u]:
        continue
    if d == dist[u] and w < wood[u]:
        continue

    # 隣接ノードを探索
    for v, c, f in G[u]:
        nd = d + c
        nw = w + f
        # 更新条件：
        # 1. 距離が短くなる
        # 2. 距離は同じだが木数が増える
        if nd < dist[v] or (nd == dist[v] and nw > wood[v]):
            dist[v] = nd
            wood[v] = nw
            heapq.heappush(pq, (nd, -nw, v))

# ゴール N の答えを出力
print(dist[N], wood[N])
