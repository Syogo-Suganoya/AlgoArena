class UnionFind:
    def __init__(self, n):
        self.parent = [-1] * n  # 負なら根かつサイズを表す

    def root(self, x):
        if self.parent[x] < 0:
            return x
        self.parent[x] = self.root(self.parent[x])
        return self.parent[x]

    def size(self, x):
        return -self.parent[self.root(x)]

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return False
        if self.parent[x] > self.parent[y]:
            x, y = y, x
        self.parent[x] += self.parent[y]
        self.parent[y] = x
        return True


N, M = map(int, input().split())
bridges = [tuple(map(int, input().split())) for _ in range(M)]
bridges = [(a - 1, b - 1) for a, b in bridges]  # 0-index化

uf = UnionFind(N)

# 最初（全て壊れている状態）の不便さ
inconvenience = N * (N - 1) // 2
ans = [0] * M

# 壊れる順の逆（= 復活させる順）に処理
for i in range(M - 1, -1, -1):
    ans[i] = inconvenience
    a, b = bridges[i]
    if not uf.same(a, b):
        inconvenience -= uf.size(a) * uf.size(b)
        uf.unite(a, b)

# 出力
for v in ans:
    print(v)
