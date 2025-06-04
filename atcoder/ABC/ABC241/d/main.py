import bisect
import sys


# Fenwick Tree（BIT）：要素の個数管理に使用
class FenwickTree:
    def __init__(self, size):
        self.N = size + 2  # 安全に+2
        self.tree = [0] * self.N

    # index i に x を加算する
    def add(self, i, x):
        i += 1  # 1-indexed に変換
        while i < self.N:
            self.tree[i] += x
            i += i & -i

    # index i までの累積和を取得
    def sum(self, i):
        i += 1  # 1-indexed
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= i & -i
        return res

    # 区間 [l, r] の和を取得
    def range_sum(self, l, r):
        return self.sum(r) - self.sum(l - 1)


def main():
    input = sys.stdin.readline
    Q = int(input())

    queries = []
    xs = set()

    # 入力を読み込みつつ、全てのxを収集（圧縮の準備）
    for _ in range(Q):
        tmp = list(map(int, input().split()))
        queries.append(tmp)
        xs.add(tmp[1])

    # 座標圧縮のためにソート
    xs = sorted(xs)
    x_id = {x: i for i, x in enumerate(xs)}  # x → 圧縮後のindex

    ft = FenwickTree(len(xs))  # Fenwick Tree初期化

    for q in queries:
        if q[0] == 1:
            # クエリ1: xを追加
            x = q[1]
            ft.add(x_id[x], 1)

        elif q[0] == 2:
            # クエリ2: x以下の値の中で大きい方からk番目
            x, k = q[1], q[2]
            idx = bisect.bisect_right(xs, x) - 1  # x以下の最大index

            if idx < 0:
                print(-1)
                continue

            # 二分探索：後ろからk番目のindexを探す
            l, r = 0, idx
            res = -1
            while l <= r:
                m = (l + r) // 2
                cnt = ft.range_sum(m, idx)
                if cnt >= k:
                    res = m
                    l = m + 1
                else:
                    r = m - 1

            print(xs[res] if res != -1 else -1)

        else:
            # クエリ3: x以上の値の中で小さい方からk番目
            x, k = q[1], q[2]
            idx = bisect.bisect_left(xs, x)  # x以上の最小index

            if idx >= len(xs):
                print(-1)
                continue

            # 二分探索：前からk番目のindexを探す
            l, r = idx, len(xs) - 1
            res = -1
            while l <= r:
                m = (l + r) // 2
                cnt = ft.range_sum(idx, m)
                if cnt >= k:
                    res = m
                    r = m - 1
                else:
                    l = m + 1

            print(xs[res] if res != -1 else -1)


if __name__ == "__main__":
    main()
