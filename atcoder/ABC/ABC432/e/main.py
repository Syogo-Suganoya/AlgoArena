class SegTree:
    """セグメントツリー (区間和 + 区間j*値の和)"""

    def __init__(self, size):
        self.N = 1
        while self.N < size:
            self.N <<= 1
        self.data = [(0, 0)] * (2 * self.N)  # (count, sum_j)

    def set(self, i, val):
        """インデックスiにval=(count, sum_j)をセット"""
        i += self.N
        self.data[i] = val
        while i > 1:
            i >>= 1
            self.data[i] = self._op(self.data[i * 2], self.data[i * 2 + 1])

    def get(self, i):
        return self.data[i + self.N]

    def prod(self, l, r):
        """[l, r)の区間和を返す"""
        l += self.N
        r += self.N
        sml = (0, 0)
        smr = (0, 0)
        while l < r:
            if l & 1:
                sml = self._op(sml, self.data[l])
                l += 1
            if r & 1:
                r -= 1
                smr = self._op(self.data[r], smr)
            l >>= 1
            r >>= 1
        return self._op(sml, smr)

    @staticmethod
    def _op(a, b):
        # 区間和
        return (a[0] + b[0], a[1] + b[1])


# --- 定数 ---
C = 500010
st = SegTree(C)


def add(x):
    cnt, s = st.get(x)
    cnt += 1
    s += x
    st.set(x, (cnt, s))


def delete(x):
    cnt, s = st.get(x)
    cnt -= 1
    s -= x
    st.set(x, (cnt, s))


# --- 入力 ---
n, q = map(int, input().split())
A = list(map(int, input().split()))
for val in A:
    add(val)

for _ in range(q):
    t, *rest = map(int, input().split())
    if t == 1:
        x, y = rest
        x -= 1
        delete(A[x])
        A[x] = y
        add(A[x])
    else:
        l, r = rest
        ans = 0
        if l > r:
            ans = l * n
        else:
            # [0, l) のcount * l
            cnt, _ = st.prod(0, l)
            ans += l * cnt
            # [l, r] の sum_j
            _, ssum = st.prod(l, r + 1)
            ans += ssum
            # [r+1, C) のcount * r
            cnt, _ = st.prod(r + 1, C)
            ans += r * cnt
        print(ans)
