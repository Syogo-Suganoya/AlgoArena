class UnionFind:
    def __init__(self):
        self.parent = dict()

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def unite(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        if rx != ry:
            self.parent[ry] = rx

    def same(self, x, y):
        return self.find(x) == self.find(y)


N = int(input())
uf = UnionFind()
nodes = set()

# 入力を受け取って、UnionFindでマージ
for _ in range(N):
    a, b = map(int, input().split())
    uf.unite(a, b)
    nodes.add(a)
    nodes.add(b)

# 1階と同じ連結成分の中で最大の階を探す
root1 = uf.find(1)
ans = 1

for node in nodes:
    if uf.find(node) == root1:
        ans = max(ans, node)

print(ans)
