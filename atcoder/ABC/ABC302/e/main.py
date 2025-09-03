import sys

input = sys.stdin.readline

N, Q = map(int, input().split())

# 各頂点の次数（接続されている辺の数）
deg = [0] * (N + 1)
# 各頂点ごとの隣接リストを持つ
adj = [set() for _ in range(N + 1)]

# 孤立している頂点の数（最初は全部孤立）
isolated = N

for _ in range(Q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        # 1 u v : 辺を追加
        _, u, v = query
        adj[u].add(v)
        adj[v].add(u)
        if deg[u] == 0:
            isolated -= 1
        if deg[v] == 0:
            isolated -= 1
        deg[u] += 1
        deg[v] += 1

    else:
        # 2 v : 頂点 v から辺を全削除
        _, v = query
        for u in list(adj[v]):
            adj[u].remove(v)
            deg[u] -= 1
            if deg[u] == 0:
                isolated += 1
        if deg[v] > 0:
            isolated += 1
        deg[v] = 0
        adj[v].clear()

    print(isolated)
