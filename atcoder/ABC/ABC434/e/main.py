import sys

# 再帰上限を引き上げる（念のため）
sys.setrecursionlimit(10**6)


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.num_vertices = [1] * n  # 各集合の頂点数 (V)
        self.num_edges = [0] * n  # 各集合の辺の数 (E)

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i != root_j:
            # 異なる集合を結合する場合
            # ランクなどは省略し、単純にi側にjをマージする実装
            self.parent[root_j] = root_i
            self.num_vertices[root_i] += self.num_vertices[root_j]
            self.num_edges[root_i] += (
                self.num_edges[root_j] + 1
            )  # 辺が1本増える（iとjをつなぐ辺）
        else:
            # すでに同じ集合の場合
            self.num_edges[root_i] += 1  # 辺だけ増える

    def get_score(self):
        total_score = 0
        for i in range(len(self.parent)):
            # 根（ルート）である要素だけを集計する
            if self.parent[i] == i:
                v = self.num_vertices[i]
                e = self.num_edges[i]
                # 各連結成分で取れる最大値は min(頂点数, 辺の数)
                total_score += min(v, e)
        return total_score


N = int(input().strip())

queries = []
coords = set()

# 座標の読み込みと、出現する全座標の列挙
for _ in range(N):
    X, R = map(int, input().split())
    u, v = X - R, X + R
    queries.append((u, v))
    coords.add(u)
    coords.add(v)

# 座標圧縮（座標の値が大きい場合に対応するため、0からの連番に変換）
# sorted_coords: 実際の座標値のリスト
# coord_map: 実際の座標値 -> ID(0, 1, 2...)
sorted_coords = sorted(list(coords))
coord_map = {val: i for i, val in enumerate(sorted_coords)}

num_unique_coords = len(sorted_coords)
uf = UnionFind(num_unique_coords)

# グラフの構築（Union-Findで辺を追加していく）
for u_val, v_val in queries:
    u_id = coord_map[u_val]
    v_id = coord_map[v_val]
    uf.union(u_id, v_id)

# 集計結果の出力
print(uf.get_score())
