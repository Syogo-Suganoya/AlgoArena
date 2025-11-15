# Union-Find（Disjoint Set Union）の実装
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))  # 親ノード
        self.rank = [0] * n  # 木の高さ（最適化用）

    # 根を取得
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # 経路圧縮
        return self.parent[x]

    # x と y を同じ集合にマージ
    def merge(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return
        # rank が小さい方を大きい方の下に置く
        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        else:
            self.parent[y_root] = x_root
            if self.rank[x_root] == self.rank[y_root]:
                self.rank[x_root] += 1

    # x と y が同じ集合にいるか
    def same(self, x, y):
        return self.find(x) == self.find(y)


n, m = map(int, input().split())
edges = []
for _ in range(m):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    edges.append((u, v, w))

# 初期の答えを全ビット1に設定（30ビット分）
x = (1 << 30) - 1

# 上位ビットから順に試す
for k in range(29, -1, -1):
    # kビットを一時的に0にしてみる
    x ^= 1 << k

    uf = UnionFind(n)
    for u, v, w in edges:
        # この辺の重み w が x のビットに含まれている場合だけ使う
        if (x | w) == x:
            uf.merge(u, v)

    # 0 と n-1 がつながらなければ k ビットは 1 のまま戻す
    if not uf.same(0, n - 1):
        x |= 1 << k

print(x)
