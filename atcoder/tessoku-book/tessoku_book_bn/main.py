class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))  # 初期は全員が親
        self.rank = [0] * n  # 木の高さ

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # 経路圧縮
        return self.parent[x]

    def unite(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return
        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        else:
            self.parent[y_root] = x_root
            if self.rank[x_root] == self.rank[y_root]:
                self.rank[x_root] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)


N, Q = map(int, input().split())
uf = UnionFind(N + 1)

for _ in range(Q):
    q, u, v = map(int, input().split())
    match q:
        case 1:
            uf.unite(u, v)
        case 2:
            print("Yes" if uf.same(u, v) else "No")
