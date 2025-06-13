class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))  # 各人の親（最初は自分自身）
        self.size = [1] * n  # 各グループの人数

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # 経路圧縮
        return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return False  # すでに同じグループ
        if self.size[x_root] < self.size[y_root]:
            x_root, y_root = y_root, x_root
        self.parent[y_root] = x_root
        self.size[x_root] += self.size[y_root]
        return True

    def group_sizes(self):
        # 各グループの代表者だけに人数を集計
        sizes = {}
        for i in range(len(self.parent)):
            root = self.find(i)
            sizes[root] = sizes.get(root, 0) + 1
        return sizes.values()


N, M = map(int, input().split())
uf = UnionFind(N)

# 入力：友達のペア M 組
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1  # 0からスタートするように調整
    b -= 1
    uf.union(a, b)

# 各グループごとの人数を取得
group_sizes = uf.group_sizes()

# 各グループで「全員が友達」になるときの友達の数（完全グラフ）
total_possible_friends = sum(size * (size - 1) // 2 for size in group_sizes)

# そこから、元々の友達の数（M）を引いたら答え
print(total_possible_friends - M)
