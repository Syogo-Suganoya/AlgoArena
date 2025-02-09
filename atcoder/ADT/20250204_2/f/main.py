class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # 経路圧縮
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False  # すでに同じグループ → サイクル発生
        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x
        self.parent[root_y] = root_x
        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1
        return True  # 統合成功（サイクルなし）


# 入力
N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]

uf = UnionFind(N)
cycle_count = 0

for u, v in edges:
    u -= 1  # 0-indexed にする
    v -= 1  # 0-indexed にする
    if not uf.union(u, v):  # サイクルが発生したらカウント
        cycle_count += 1

print(cycle_count)
