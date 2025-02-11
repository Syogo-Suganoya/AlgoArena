class DSU:
    """Union-Find（経路圧縮 + ランク）"""

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.size = [1] * n
        self.edge_count = [0] * n  # 連結成分ごとのエッジ数

    def find(self, x):
        """親を見つける（経路圧縮）"""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def unite(self, x, y):
        """x と y を連結（ランク考慮）"""
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            self.edge_count[rx] += 1  # 既に同じグループならエッジ数を増やす
            return
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        self.size[rx] += self.size[ry]
        self.edge_count[rx] += self.edge_count[ry] + 1
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1

    def get_size(self, x):
        """x の属する連結成分のサイズを取得"""
        return self.size[self.find(x)]

    def get_edge_count(self, x):
        """x の属する連結成分のエッジ数を取得"""
        return self.edge_count[self.find(x)]


# 入力処理
N, M = map(int, input().split())
dsu = DSU(N)

for _ in range(M):
    A, B = map(int, input().split())
    dsu.unite(A - 1, B - 1)  # 0-indexed に変換

# 追加できるエッジの合計を求める
max_operations = 0
seen = set()

for i in range(N):
    root = dsu.find(i)
    if root not in seen:
        seen.add(root)
        n = dsu.get_size(root)  # 連結成分のノード数
        m = dsu.get_edge_count(root)  # 連結成分のエッジ数
        max_operations += n * (n - 1) // 2 - m

# 結果出力
print(max_operations)
