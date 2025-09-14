class S:
    def __init__(self, val=0, length=0, res=0):
        self.val = val
        self.len = length
        self.res = res


def op(l: S, r: S) -> S:
    """セグメント木の結合関数"""
    res = S()
    res.val = l.val + r.val
    res.len = l.len + r.len
    res.res = l.res + r.res
    res.res += l.len * r.val
    res.res -= l.val * r.len
    return res


def e() -> S:
    """単位元"""
    return S(0, 0, 0)


class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.size = 1
        while self.size < self.n:
            self.size *= 2
        self.data = [e() for _ in range(2 * self.size)]
        # 初期値をセット
        for i in range(self.n):
            self.data[self.size + i] = data[i]
        # 木を構築
        for i in reversed(range(1, self.size)):
            self.data[i] = op(self.data[2 * i], self.data[2 * i + 1])

    def prod(self, l, r):
        """区間 [l, r) の値を取得"""
        l += self.size
        r += self.size
        sml = e()
        smr = e()
        while l < r:
            if l & 1:
                sml = op(sml, self.data[l])
                l += 1
            if r & 1:
                r -= 1
                smr = op(self.data[r], smr)
            l >>= 1
            r >>= 1
        return op(sml, smr)


# 入力処理
n, q = map(int, input().split())
a = list(map(int, input().split()))

# 初期値を計算
ini = []
cur = S(0, 1, 0)
ini.append(cur)
for i in range(1, n + 1):
    cur = S(cur.val + a[i - 1], 1, 0)
    ini.append(cur)

# セグメント木作成
seg = SegmentTree(ini)

# クエリ処理
for _ in range(q):
    l, r = map(int, input().split())
    l -= 1  # 0-indexに変換
    ans = seg.prod(l, r + 1).res
    print(ans)
