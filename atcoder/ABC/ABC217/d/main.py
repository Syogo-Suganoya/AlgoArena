from sortedcontainers import SortedList

# 入力：最初の棒の長さ l とクエリの数 q
l, q = map(int, input().split())

# 木の切れ目のリスト（昇順に保たれる）
# 最初は両端（0とl）だけが切れ目
L = SortedList([0, l])

# クエリを順に処理
for _ in range(q):
    c, x = map(int, input().split())

    if c == 1:
        # クエリ1: 位置 x に切れ目を入れる
        L.add(x)
    else:
        # クエリ2: 位置 x を含む木片の長さを出力
        # x を超えない最小の切れ目のインデックスを探す
        idx = L.bisect_left(x)

        # その前の切れ目と、x を挟んでいるので差をとれば長さ
        print(L[idx] - L[idx - 1])
