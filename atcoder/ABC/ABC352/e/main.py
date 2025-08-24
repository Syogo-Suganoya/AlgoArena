# 解法：Kruskal法 + Union-Find（DSU）
#
# 各クエリで与えられる集合 S_i 内は「代表頂点」と他の頂点を
# 辺でつなぐだけで十分。すべての組み合わせを列挙する必要はない。
# これで計算量を抑えつつ MST を求める。


class UnionFind:
    def __init__(self, n: int):
        # 各頂点の親を -1 で初期化（根の場合は -サイズ を持つ）
        self.parent = [-1] * n

    def find(self, x: int) -> int:
        # 根を再帰的に探す（経路圧縮あり）
        if self.parent[x] < 0:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        # 2つの集合を統合する（Union by Size）
        x, y = self.find(x), self.find(y)
        if x == y:
            return False
        if self.parent[x] > self.parent[y]:
            x, y = y, x
        self.parent[x] += self.parent[y]
        self.parent[y] = x
        return True

    def same(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def size(self, x: int) -> int:
        return -self.parent[self.find(x)]


N, M = map(int, input().split())
edges = []

for _ in range(M):
    k, c = map(int, input().split())
    vertices = list(map(lambda x: int(x) - 1, input().split()))  # 0-index化
    rep = vertices[0]  # 代表頂点
    for v in vertices[1:]:
        # rep と v を重み c でつなぐ
        edges.append((c, rep, v))

# 辺を重さの小さい順にソート
edges.sort()

uf = UnionFind(N)
ans = 0
used_edges = 0

for c, u, v in edges:
    # まだつながっていなければ採用
    if uf.union(u, v):
        ans += c
        used_edges += 1

# MST が完成するには N-1 本の辺が必要
if used_edges == N - 1:
    print(ans)
else:
    print(-1)
