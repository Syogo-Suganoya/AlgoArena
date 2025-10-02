# 区間和用のセグメント木クラス
class SegTree:
    def __init__(self, n):
        # 配列サイズを 2 のべき乗に拡張
        self.size = 1
        while self.size < n:
            self.size *= 2
        # セグメント木本体の配列（全ノードを0で初期化）
        # 完全二分木なのでサイズは 2*size
        self.dat = [0] * (self.size * 2)

    # pos 番目の要素を x に更新する
    def update(self, pos, x):
        pos += self.size  # 葉ノードに対応する位置に変換
        self.dat[pos] = x  # 値を更新
        # 親ノードに向かって区間和を再計算
        while pos >= 2:
            pos //= 2
            self.dat[pos] = (
                self.dat[pos * 2] + self.dat[pos * 2 + 1]
            )  # 左右の子の和を格納

    # 区間 [l, r) の合計を返す
    # a, b: 現在のノードが表す区間
    # u: 現在のノード番号
    def query(self, l, r, a, b, u):
        # 区間が全く重なっていない場合
        if r <= a or b <= l:
            return 0
        # 区間が完全に含まれている場合
        if l <= a and b <= r:
            return self.dat[u]
        # 部分的に重なる場合は左右の子に分けて計算
        m = (a + b) // 2
        sumv = self.query(l, r, a, m, u * 2)  # 左側の合計
        sumv += self.query(l, r, m, b, u * 2 + 1)  # 右側の合計
        return sumv


# 入力処理
N, Q = map(int, input().split())
qry = [list(map(int, input().split())) for _ in range(Q)]

# セグメント木を作成
st = SegTree(N)

# クエリ処理
for q1 in qry:
    t, *q = q1
    if t == 1:
        # 更新クエリ：1 pos x
        pos, x = q
        st.update(pos - 1, x)  # 0-index に変換して更新
    else:
        # 区間和クエリ：2 l r
        l, r = q
        # 区間 [l-1, r-1] の合計を出力
        print(st.query(l - 1, r - 1, 0, st.size, 1))
