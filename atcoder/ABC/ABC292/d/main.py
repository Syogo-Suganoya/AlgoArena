from collections import defaultdict


# Union-Find クラスの定義
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))  # 各頂点の親を初期化（自分自身）
        self.size = [1] * n  # 各集合のサイズを管理

    # 根を探す（経路圧縮あり）
    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    # 2つの集合を統合する
    def unite(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return  # 既に同じ集合なら何もしない
        if self.size[x_root] < self.size[y_root]:
            x_root, y_root = y_root, x_root
        self.parent[y_root] = x_root  # y_root を x_root に繋ぐ
        self.size[x_root] += self.size[y_root]


N, M = map(int, input().split())
uf = UnionFind(N)

edge_count = defaultdict(int)  # 各連結成分の辺の数を管理

edges = [tuple(map(int, input().split())) for _ in range(M)]
for u, v in edges:
    u -= 1  # 0-indexed に変換
    v -= 1
    uf.unite(u, v)  # 辺を張る（連結成分を統合）

# 各連結成分の辺の数を数える
for u, v in edges:
    u -= 1
    edge_count[uf.find(u)] += 1  # u が属する連結成分の辺の数を増やす

# 各連結成分の頂点の数を数える
component_size = defaultdict(int)
for i in range(N):
    root = uf.find(i)
    component_size[root] += 1

# 各連結成分ごとに、条件「頂点数=辺数」を満たすか確認
for root in component_size:
    if component_size[root] != edge_count[root]:
        print("No")
        break
else:
    # すべての連結成分で条件を満たした
    print("Yes")
