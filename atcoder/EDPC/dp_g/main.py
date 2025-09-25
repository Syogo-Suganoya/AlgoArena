from collections import deque

# 入力例
N, M = map(int, input().split())  # 頂点数、辺数
edges = [tuple(map(int, input().split())) for _ in range(M)]

# 0-index に直す場合
edges = [(u - 1, v - 1) for u, v in edges]

# 隣接リスト作成
adj = [[] for _ in range(N)]
indeg = [0] * N
for u, v in edges:
    adj[u].append(v)
    indeg[v] += 1

# トポロジカルソート
queue = deque([i for i in range(N) if indeg[i] == 0])
topo_order = []
while queue:
    u = queue.popleft()
    topo_order.append(u)
    for v in adj[u]:
        indeg[v] -= 1
        if indeg[v] == 0:
            queue.append(v)

# DP（最長経路を求める例）
dp = [0] * N
for u in topo_order:
    for v in adj[u]:
        dp[v] = max(dp[v], dp[u] + 1)

print(max(dp))
