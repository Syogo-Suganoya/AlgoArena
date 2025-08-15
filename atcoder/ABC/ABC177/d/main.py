class UnionFind:
    def __init__(self, n):
        # r[i] < 0 の場合は「iが属する集合のサイズ×(-1)」を保持
        # r[i] >= 0 の場合は「iの親ノードのインデックス」を保持
        self.r = [-1] * n

    def root(self, x):
        """要素xの属する集合の代表（根）を返す（経路圧縮あり）"""
        if self.r[x] < 0:
            return x
        self.r[x] = self.root(self.r[x])
        return self.r[x]

    def unite(self, x, y):
        """xとyを同じ集合に統合（union by size）"""
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return False
        # 大きい集合をxにする（サイズは負の値なので比較は逆）
        if self.r[x] > self.r[y]:
            x, y = y, x
        # サイズを加算
        self.r[x] += self.r[y]
        # yの親をxに
        self.r[y] = x
        return True

    def size(self, x):
        """xの属する集合の要素数"""
        return -self.r[self.root(x)]


# 入力処理
N, M = map(int, input().split())
uf = UnionFind(N)

# 辺情報を受け取り、Union-Findで結合
for _ in range(M):
    A, B = map(int, input().split())
    # 0-indexに変換
    A -= 1
    B -= 1
    uf.unite(A, B)

# 最大の友達集合サイズを探す
ans = 0
for i in range(N):
    ans = max(ans, uf.size(i))

print(ans)
