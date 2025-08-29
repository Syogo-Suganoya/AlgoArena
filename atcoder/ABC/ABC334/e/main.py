import sys

sys.setrecursionlimit(10**7)

MOD = 998244353


# Union-Find
class UnionFind:
    def __init__(self, n):
        self.par = list(range(n))
        self.size = [1] * n

    def find(self, x):
        while self.par[x] != x:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x

    def unite(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.par[y] = x
        self.size[x] += self.size[y]

    def same(self, x, y):
        return self.find(x) == self.find(y)


H, W = map(int, input().split())
grid = [list(input().strip()) for _ in range(H)]


# グリッドを1次元に展開
def idx(r, c):
    return r * W + c


uf = UnionFind(H * W)

# まず緑マス同士をUnion-Findでつなぐ
for r in range(H):
    for c in range(W):
        if grid[r][c] == "#":
            for dr, dc in [(1, 0), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < H and 0 <= nc < W and grid[nr][nc] == "#":
                    uf.unite(idx(r, c), idx(nr, nc))

# 現在の緑成分数 C を数える
seen = set()
C = 0
for r in range(H):
    for c in range(W):
        if grid[r][c] == "#":
            root = uf.find(idx(r, c))
            if root not in seen:
                seen.add(root)
                C += 1

# 赤マスを緑に変えた場合の成分数を計算
total = 0
red_count = 0
for r in range(H):
    for c in range(W):
        if grid[r][c] == ".":
            red_count += 1
            neighbor = set()
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < H and 0 <= nc < W and grid[nr][nc] == "#":
                    neighbor.add(uf.find(idx(nr, nc)))
            x = len(neighbor)
            if x == 0:
                total += C + 1
            else:
                total += C - (x - 1)

# 期待値 = total / red_count （mod 998244353）
inv = pow(red_count, MOD - 2, MOD)  # モジュラ逆数
ans = total * inv % MOD
print(ans)
