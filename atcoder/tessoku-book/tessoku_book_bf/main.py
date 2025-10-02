# セグメント木（区間最大値用）
class SegTree:
    def __init__(self, n):
        # 配列サイズを2のべき乗に拡張
        self.size = 1
        while self.size < n:
            self.size *= 2
        # セグメント木本体の配列（初期値は0）
        # インデックス1から使用、dat[1]が全体の根
        self.dat = [0] * (self.size * 2)

    # pos番目の要素を x に更新
    def update(self, pos, x):
        pos += self.size  # 葉ノードの位置に変換
        self.dat[pos] = x
        # 親ノードまで上に遡って値を更新
        while pos >= 2:
            pos //= 2
            self.dat[pos] = max(self.dat[pos * 2], self.dat[pos * 2 + 1])

    # 区間[l, r)の最大値を返す
    # a,b: 現在のノードが表す区間
    # u: 現在のノード番号
    def query(self, l, r, a, b, u):
        # 区間が重なっていなければ無視
        if r <= a or b <= l:
            return -(10**9)  # 非常に小さい値で無効化
        # 完全に含まれる場合はこのノードの値を返す
        if l <= a and b <= r:
            return self.dat[u]
        # 部分的に重なる場合は左右の子を探索
        m = (a + b) // 2
        ansl = self.query(l, r, a, m, u * 2)
        ansr = self.query(l, r, m, b, u * 2 + 1)
        return max(ansl, ansr)  # 左右の最大値を返す


# 入力
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
        st.update(pos - 1, x)  # 0-indexに変換
    else:
        # 最大値取得クエリ：2 l r
        l, r = q
        # 区間[l-1, r-1]の最大値を出力
        print(st.query(l - 1, r - 1, 0, st.size, 1))
