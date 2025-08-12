# Union-Find（Disjoint Set Union）構造
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # 経路圧縮
        return self.parent[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
        return True


N, M = map(int, input().split())
edges = []
for _ in range(M):
    A, B, W = map(int, input().split())  # A, B: 頂点, W: 辺の長さ
    edges.append((W, A - 1, B - 1))  # 0-index に変換

# 辺を重みの昇順にソート
edges.sort()

uf = UnionFind(N)
mst_cost = 0

for w, a, b in edges:
    if uf.unite(a, b):  # 連結でなければ採用
        mst_cost += w

print(mst_cost)
