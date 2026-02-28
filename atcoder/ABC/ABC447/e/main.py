# mod 998244353 を使う
MOD = 998244353


# ==============================
# Union-Find（Disjoint Set Union）
# ==============================
class UnionFind:
    def __init__(self, n):
        # 親配列（最初は自分自身が親）
        self.parent = list(range(n))
        # 木のサイズ管理（ランク代わり）
        self.size = [1] * n

    # 根を探す（経路圧縮あり）
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    # 同じ集合かどうか判定
    def same(self, x, y):
        return self.find(x) == self.find(y)

    # 集合を併合
    def merge(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False

        # 小さい木を大きい木にくっつける
        if self.size[x] < self.size[y]:
            x, y = y, x

        self.parent[y] = x
        self.size[x] += self.size[y]
        return True


# ==============================
# メイン処理
# ==============================
n, m = map(int, input().split())

u = []
v = []
cost = []

# cost[i] = 2^(i+1) になるように作っている
# C++では modint で累積していた
cur = 2
for i in range(m):
    a, b = map(int, input().split())
    a -= 1  # 0-index化
    b -= 1
    u.append(a)
    v.append(b)

    if i == 0:
        cost.append(2)
    else:
        cur = (cur * 2) % MOD
        cost.append(cur)

uf = UnionFind(n)

ans = 0
cnt = n  # 連結成分数

# 後ろから見る（＝コストの大きい順）
for i in reversed(range(m)):
    # まだ別の集合なら
    if not uf.same(u[i], v[i]):
        # 連結成分が3以上あるなら普通にマージ
        if cnt > 2:
            uf.merge(u[i], v[i])
            cnt -= 1

        # すでに2成分以下なら、
        # この辺は採用せずコスト加算
        else:
            ans = (ans + cost[i]) % MOD

print(ans)
