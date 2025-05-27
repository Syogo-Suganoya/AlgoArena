# Union-Find（Disjoint Set Union）を実装
class UnionFind:
    def __init__(self, n):
        # 各ノードの親を初期化（-1 は自身が根であることを示す）
        self.par = [-1] * (n + 1)
        # 各連結成分の辺の数を記録
        self.edge = [0] * (n + 1)

    # ノード x の根を見つける
    def root(self, x):
        if self.par[x] < 0:
            return x
        self.par[x] = self.root(self.par[x])  # 経路圧縮
        return self.par[x]

    # ノード x と y を統合する
    def union(self, x, y):
        x = self.root(x)
        y = self.root(y)
        # 辺を追加
        self.edge[x] += 1
        if x == y:
            return
        # サイズが大きい方を x にする
        if self.par[x] > self.par[y]:
            x, y = y, x
        # y を x に統合
        self.par[x] += self.par[y]
        self.par[y] = x
        self.edge[x] += self.edge[y]
        self.edge[y] = 0


# 入力の読み込み
N, M = map(int, input().split())
uf = UnionFind(N)

# 友達関係を Union-Find に追加
for _ in range(M):
    a, b = map(int, input().split())
    uf.union(a, b)

# 操作可能な回数を計算
ans = 0
for i in range(1, N + 1):
    if uf.par[i] < 0:  # 根ノードのみ処理
        v = -uf.par[i]  # 連結成分の頂点数
        e = uf.edge[i]  # 連結成分の辺の数
        ans += v * (v - 1) // 2 - e  # 最大辺数 - 現在の辺数

print(ans)
