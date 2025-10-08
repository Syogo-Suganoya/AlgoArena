class BIT:
    """0-indexed Fenwick Tree"""

    def __init__(self, n):
        self.N = n
        self.tree = [0] * (n + 1)

    def add(self, i, x):
        i += 1
        while i <= self.N:
            self.tree[i] += x
            i += i & -i

    def sum(self, i):
        """[0, i) の累積和"""
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= i & -i
        return res

    def query(self, l, r):
        """[l, r) の累積和"""
        return self.sum(r) - self.sum(l)


# 入力
n, m = map(int, input().split())
a = list(map(int, input().split()))

# 値ごとの出現位置を管理
g = [[] for _ in range(m)]
for i in range(n):
    g[a[i]].append(i)

# BIT を作成
f = BIT(m)
ans = 0

# 初期の転倒数
for i in a:
    ans += f.query(i + 1, m)  # 自分より大きい値の数を加算
    f.add(i, 1)  # 出現を記録
print(ans)

# 回転後の差分を順に計算
for c in range(1, m):
    c1, c2 = 0, 0
    for idx, val in enumerate(g[m - c]):
        # 左側の差分
        c1 += val - idx
        # 右側の差分
        c2 += n - 1 - val - (len(g[m - c]) - 1 - idx)
    ans += c1 - c2
    print(ans)
