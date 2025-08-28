# セグメントツリー (区間最大)
class SegTree:
    def __init__(self, n, e=0):
        self.n = 1
        while self.n < n:
            self.n <<= 1
        self.data = [e] * (2 * self.n)
        self.e = e

    def update(self, i, x):
        # i 番目を max(data[i], x) に更新
        i += self.n
        self.data[i] = max(self.data[i], x)
        while i > 1:
            i >>= 1
            self.data[i] = max(self.data[i * 2], self.data[i * 2 + 1])

    def query(self, l, r):
        # 区間 [l, r) の最大値
        res = self.e
        l += self.n
        r += self.n
        while l < r:
            if l & 1:
                res = max(res, self.data[l])
                l += 1
            if r & 1:
                r -= 1
                res = max(res, self.data[r])
            l >>= 1
            r >>= 1
        return res

    def all_max(self):
        return self.data[1]


N, D = map(int, input().split())
A = list(map(int, input().split()))
MAXV = 5 * 10**5 + 5

seg = SegTree(MAXV)

for a in A:
    l = max(0, a - D)
    r = min(MAXV, a + D + 1)
    best = seg.query(l, r)
    seg.update(a, best + 1)

print(seg.all_max())
