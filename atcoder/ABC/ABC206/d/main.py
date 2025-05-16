class UnionFind:
    # 初期化：親をすべて -1（自分が根でサイズ1）に設定
    def __init__(self, n):
        self.parent = [-1] * n

    # xの根を探す（経路圧縮）
    def find(self, x):
        if self.parent[x] < 0:
            return x
        # 再帰的に根を探して、親を根に更新（経路圧縮）
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    # xとyを合併（サイズが大きい方に小さい方を合体）
    def unite(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        # すでに同じグループなら何もしない
        if x_root == y_root:
            return False
        # 小さい集合が大きい集合に吸収されるようにする（rankではなくsizeベース）
        if self.parent[x_root] > self.parent[y_root]:
            x_root, y_root = y_root, x_root
        self.parent[x_root] += self.parent[y_root]  # サイズ更新
        self.parent[y_root] = x_root  # 親を更新
        return True

    # xを含むグループのサイズを返す
    def size(self, x):
        return -self.parent[self.find(x)]


N = int(input())
A = list(map(int, input().split()))

# Aの要素は最大でも2×10^5までなので、十分に大きいサイズのUnionFindを用意
uf = UnionFind(2 * 10**5 + 1)

# 回文になるように前後のペアを比較して、異なっていればグループ化（同一値にする必要あり）
for i in range(N // 2):
    a = A[i]
    b = A[N - 1 - i]
    uf.unite(a, b)

# 各グループの代表要素を取り出して、サイズから操作回数（サイズ - 1）を計算
groups = {}
for i in range(2 * 10**5 + 1):
    root = uf.find(i)
    # サイズが2以上のグループだけ対象にする（-1より小さい = 要素数2以上）
    if uf.parent[root] < -1:
        groups[root] = uf.size(root)

# 各グループ内で全て同じ値に統一するのに必要な回数は「サイズ - 1」
res = sum(size - 1 for size in groups.values())
print(res)
