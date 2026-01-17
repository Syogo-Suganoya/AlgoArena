# Union-Find を自前実装
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size_ = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def merge(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.size_[x] < self.size_[y]:
            x, y = y, x
        self.parent[y] = x
        self.size_[x] += self.size_[y]

    def size(self, x):
        return self.size_[self.find(x)]


# ===== 入力 =====
n, m = map(int, input().split())
edges = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    edges[u].append(v)
    edges[v].append(u)

# 0〜k のみの連結を管理
uf_small = UnionFind(n)
# 外側も含めた連結を管理
uf_large = UnionFind(n)

ans = []

# k を 0 から順に増やす
for k in range(n):
    for v in edges[k]:
        if v < k:
            # 内側同士の辺
            uf_small.merge(k, v)
        else:
            # 外側につながる辺
            uf_large.merge(k, v)

    # 0〜k が連結でないなら -1
    if uf_small.size(0) <= k:
        print(-1)
    else:
        # 外側につながっている頂点数
        print(uf_large.size(0) - (k + 1))
