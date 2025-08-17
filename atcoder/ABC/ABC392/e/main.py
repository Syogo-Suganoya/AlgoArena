class DSU:
    def __init__(self, n):
        self.n = n
        self.unicnt = [1] * n  # 集合サイズ管理
        self.amari = [[] for _ in range(n)]  # 冗長エッジを保持

    # 根を返す（経路圧縮）
    def root(self, x):
        if self.unicnt[x] <= 0:
            self.unicnt[x] = -self.root(-self.unicnt[x])
            return -self.unicnt[x]
        return x

    # 同じ集合か判定
    def same(self, x, y):
        return self.root(x) == self.root(y)

    # 集合を統合
    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return False
        if self.unicnt[x] < self.unicnt[y]:
            x, y = y, x
        self.unicnt[x] += self.unicnt[y]
        self.unicnt[y] = -x
        # 冗長エッジを統合
        self.amari[x].extend(self.amari[y])
        self.amari[y] = []
        return True


# ------------------------------
# メイン処理
n, m = map(int, input().split())
dsu = DSU(n)

for i in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    if dsu.same(x, y):
        # 同じ集合内なら冗長エッジとして保持
        dsu.amari[dsu.root(x)].append((x, y, i))
    else:
        dsu.unite(x, y)

# 各集合の情報を取得
cc = [(len(dsu.amari[i]), i) for i in range(n) if dsu.root(i) == i]
cc.sort(reverse=True)  # 冗長エッジ数で降順ソート

# 結果出力
print(len(cc) - 1)

pos = 1
for _, root in cc:
    for x, y, idx in dsu.amari[root]:
        if pos < len(cc):
            # 冗長エッジを使って他の集合に接続
            print(idx + 1, x + 1, cc[pos][1] + 1)
            pos += 1
