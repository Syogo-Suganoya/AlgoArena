# URL
https://atcoder.jp/contests/adt_medium_20250128_3/tasks/abc234_d

# 元の問題のURL
https://atcoder.jp/contests/abc264/tasks/abc234_d

# 解説
P[: K]を取得します。
それをソートします。
これの大きい方からK番目を取得するので[-K]で取得します。

これをK - 1からNまでループします。

SortedListを使うと、高速化します。
