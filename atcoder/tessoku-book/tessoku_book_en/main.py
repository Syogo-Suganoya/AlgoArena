import sys

sys.setrecursionlimit(10**7)


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def unite(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        else:
            self.parent[ry] = rx
            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1
        return True


N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]
# edges は (A_i, B_i, C_i)

# 重みが大きい順にソート
edges.sort(key=lambda x: -x[2])

uf = UnionFind(N + 1)
total = 0
count = 0

for a, b, c in edges:
    if uf.unite(a, b):
        total += c
        count += 1
        if count == N - 1:
            break

print(total)
