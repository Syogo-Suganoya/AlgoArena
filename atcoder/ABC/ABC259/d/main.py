import sys

sys.setrecursionlimit(10**7)


class UnionFind:
    def __init__(self, n):
        self.parent = [-1] * n

    def find(self, x):
        if self.parent[x] < 0:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def unite(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return
        if self.parent[x_root] > self.parent[y_root]:
            x_root, y_root = y_root, x_root
        self.parent[x_root] += self.parent[y_root]
        self.parent[y_root] = x_root

    def same(self, x, y):
        return self.find(x) == self.find(y)


N = int(input())
sx, sy, tx, ty = map(int, input().split())
circles = [tuple(map(int, input().split())) for _ in range(N)]

uf = UnionFind(N)

# 円同士の接続判定
for i in range(N):
    x1, y1, r1 = circles[i]
    for j in range(i + 1, N):
        x2, y2, r2 = circles[j]
        dx = x1 - x2
        dy = y1 - y2
        dist_sq = dx * dx + dy * dy
        r_sum = r1 + r2
        r_diff = abs(r1 - r2)
        if r_diff * r_diff <= dist_sq <= r_sum * r_sum:
            uf.unite(i, j)

# 始点と終点が属する円の特定
start_indices = []
end_indices = []
for i, (x, y, r) in enumerate(circles):
    if (sx - x) ** 2 + (sy - y) ** 2 == r * r:
        start_indices.append(i)
    if (tx - x) ** 2 + (ty - y) ** 2 == r * r:
        end_indices.append(i)

# 連結判定
for si in start_indices:
    for ti in end_indices:
        if uf.same(si, ti):
            print("Yes")
            sys.exit()

print("No")
