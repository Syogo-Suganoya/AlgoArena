# Union-Find (DSU) クラス
class DSU:
    def __init__(self, n):
        # 各要素の親を管理。初期状態では自分自身が親
        self.par = list(range(n))
        # 各集合のサイズを管理
        self.sz = [1] * n

    # x の属する集合の代表を取得
    def leader(self, x):
        if self.par[x] == x:
            return x
        # 経路圧縮
        self.par[x] = self.leader(self.par[x])
        return self.par[x]

    # a と b の集合を統合
    def merge(self, a, b):
        a = self.leader(a)
        b = self.leader(b)
        if a == b:
            return a  # すでに同じ集合なら何もしない
        # サイズが小さい方を大きい方にくっつける
        if self.sz[a] < self.sz[b]:
            a, b = b, a
        self.par[b] = a
        self.sz[a] += self.sz[b]
        return a  # 統合後の代表を返す

    # a と b が同じ集合か判定
    def same(self, a, b):
        return self.leader(a) == self.leader(b)


n, q = map(int, input().split())

# DSU インスタンス生成
dsu = DSU(n + 1)

# 各頂点の黒色フラグ（0: 白, 1: 黒）
c = [0] * (n + 1)

# 各集合の黒色の合計数
s = [0] * (n + 1)

for _ in range(q):
    query = list(map(int, input().split()))
    typ = query[0]

    if typ == 1:
        # 操作1: 無向辺の追加
        u, v = query[1], query[2]
        u = dsu.leader(u)
        v = dsu.leader(v)
        if u != v:
            # 集合を統合し、黒のカウントも統合
            w = dsu.merge(u, v)
            s[w] = s[u] + s[v]
            # 統合前のもう一方のリーダーは合計を0に
            s[u ^ v ^ w] = 0

    elif typ == 2:
        # 操作2: 頂点の色反転
        u = query[1]
        leader = dsu.leader(u)
        # 既存の黒カウントを減らす
        s[leader] -= c[u]
        # 色を反転
        c[u] ^= 1
        # 集合の黒カウントを更新
        s[leader] += c[u]

    else:  # typ == 3
        # 操作3: 集合に黒がいるか判定
        u = query[1]
        if s[dsu.leader(u)]:
            print("Yes")  # 黒が1つでも存在
        else:
            print("No")  # 黒が存在しない
