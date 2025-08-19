N = int(input())  # N: 木の高さ（葉の数は 3**N）
A = input().rstrip()  # 文字列 A（長さは 3**N、各文字は '0' または '1'）


# 再帰関数 f(l, r)
# 区間 [l, r) に対応する部分木を処理して
# (その区間の最終的な多数決結果, それを反転させるのに必要な最小コスト) を返す
def f(l, r):
    # 葉に到達したとき
    if l + 1 == r:
        # 葉の値は A[l]
        # これを反転させるには1回の操作で済む
        return A[l], 1

    # 区間を3等分して再帰的に処理
    m1 = (2 * l + r) // 3
    m2 = (l + 2 * r) // 3
    val1, cnt1 = f(l, m1)
    val2, cnt2 = f(m1, m2)
    val3, cnt3 = f(m2, r)

    # --- 以下、多数決の結果を求め、それを反転させるコストを計算 ---

    # 3つの部分がすべて同じ値の場合
    if val1 == val2 == val3:
        # 多数決の結果はその値
        # 逆にするには「3つのうち2つを反転させる」必要がある
        # 最小コスト = (3つのコスト合計) - (最大のコスト)
        return val1, cnt1 + cnt2 + cnt3 - max(cnt1, cnt2, cnt3)

    # 2つが同じ値の場合 → その値が多数決の結果
    # 逆にするには、その2つのうち「安い方」だけ反転させればよい
    elif val1 == val2:
        return val1, min(cnt1, cnt2)
    elif val1 == val3:
        return val1, min(cnt1, cnt3)
    elif val2 == val3:
        return val2, min(cnt2, cnt3)


# 根（全区間 [0, 3**N)）を処理して、
# その反転コストだけを出力
print(f(0, 3**N)[1])
