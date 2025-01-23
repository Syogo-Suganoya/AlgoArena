# URL
https://atcoder.jp/contests/adt_medium_20250123_1/tasks/abc312_c

# 元の問題のURL
https://atcoder.jp/contests/abc312/tasks/abc312_c

# 解説
まず、AとBをソートします。
二分探索で、`bisect_right(A) >= M - bisect_left(B)`となる値を探索します。
値が見つかれば、最大値更新をするために、範囲の値を増大して再探索します。
値が見つからなければ、見つけだすために、範囲の値を減少して再探索します。

`M - bisect_left(B)` =  `bisect_right(降順にしたB)`
