class BIT:
    def __init__(self, n):
        """
        BIT（Fenwick Tree）の初期化
        n: 配列のサイズ（1-indexedで扱う）
        """
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i, x):
        """
        i: 1-indexed の位置
        x: 加算する値
        """
        while i <= self.n:
            self.bit[i] += x
            i += i & -i  # 最下位ビットを足して次の更新位置へ

    def sum(self, i):
        """
        1 から i までの累積和を返す
        """
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def range_sum(self, l, r):
        """
        l から r までの累積和を返す
        """
        return self.sum(r) - self.sum(l - 1)


# ===== main =====
N, Q = map(int, input().split())
S = input().strip()

# 文字列の隣接同じ文字の場所を管理する BIT
bad_bit = BIT(N)

# 初期値を設定：隣接同じ文字の箇所を 1 とする
for i in range(N - 1):
    if S[i] == S[i + 1]:
        bad_bit.add(i + 1, 1)  # BITは1-indexedなので i+1


def toggle_at(idx):
    """
    idx の位置の状態を反転（0 <-> 1）
    """
    cur = bad_bit.range_sum(idx, idx)
    bad_bit.add(idx, -1 if cur else 1)


for _ in range(Q):
    t, L, R = map(int, input().split())
    if t == 1:
        # 文字を反転した場合に影響する隣接箇所のみを更新
        if L > 1:
            toggle_at(L - 1)  # 左側との比較
        if R < N:
            toggle_at(R)  # 右側との比較
    else:
        # L～R-1 の範囲に隣接同文字があれば "No"
        print("Yes" if bad_bit.range_sum(L, R - 1) == 0 else "No")
