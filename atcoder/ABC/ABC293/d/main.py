# Union-Find の実装（簡易版）
class UF:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def unite(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False  # すでに同じグループ → サイクル発生
        self.parent[ry] = rx
        return True


N, M = map(int, input().split())
uf = UF(N + 1)

cycle = 0
for _ in range(M):
    a, _, c, _ = input().split()  # 色情報は無視
    a, c = int(a), int(c)
    if not uf.unite(a, c):
        cycle += 1  # 同じグループだった → サイクル

# 最終的なグループ数を数える
roots = set(uf.find(i) for i in range(1, N + 1))
groups = len(roots)
tree = groups - cycle

print(cycle, tree)
