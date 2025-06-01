class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def unite(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return False  # すでに同じ連結成分
        self.parent[y_root] = x_root
        return True


N, M = map(int, input().split())
uf = UnionFind(N)
res = 0

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1  # 0-indexed に変換
    b -= 1
    if not uf.unite(a, b):
        res += 1  # 閉路を作る辺

print(res)
