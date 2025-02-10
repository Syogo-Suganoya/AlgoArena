class DSU:
    """Union-Find（Disjoint Set Union）を使ったグラフの連結判定"""

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.component_count = n  # 連結成分の数

    def find(self, x):
        """x の親を求める（経路圧縮）"""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        """x と y を同じ集合にする"""
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                root_x, root_y = root_y, root_x
            self.parent[root_y] = root_x
            if self.rank[root_x] == self.rank[root_y]:
                self.rank[root_x] += 1
            self.component_count -= 1  # 連結成分の数を減らす


def is_path_graph(n, m, edges):
    """DSU を用いてパスグラフか判定"""
    if m != n - 1:
        return "No"  # パスグラフなら「頂点数 - 1」本の辺が必要

    dsu = DSU(n)
    degree = [0] * n  # 各頂点の次数

    for u, v in edges:
        u -= 1  # 0-index に変換
        v -= 1
        degree[u] += 1
        degree[v] += 1
        dsu.union(u, v)

    # すべての頂点が連結されているか
    if dsu.component_count != 1:
        return "No"

    # 各頂点の次数が 2 以下（端の2頂点は1、それ以外は2）
    degree.sort()
    return "Yes" if degree[-1] <= 2 and degree.count(1) == 2 else "No"


n, m = map(int, input().split())  # 頂点数, 辺の数
edges = [tuple(map(int, input().split())) for _ in range(m)]

print(is_path_graph(n, m, edges))
