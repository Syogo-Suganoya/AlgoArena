import networkx as nx

N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]

G = nx.DiGraph()
G.add_nodes_from(range(1, N + 1))
G.add_edges_from(edges)

# トポロジカルソート
try:
    # 辞書順最小を優先するには sorted で入次数0のノードから取る方法
    order = list(nx.lexicographical_topological_sort(G))
    print(*order)
except nx.NetworkXUnfeasible:
    # サイクルがある場合
    print(-1)
