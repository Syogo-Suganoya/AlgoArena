# URL
https://atcoder.jp/contests/adt_medium_20250123_2/tasks/abc241_d

# 元の問題のURL
https://atcoder.jp/contests/abc241/tasks/abc241_d

# 解説
Aをソートします。

3の時は
二分探索でbisect_leftを使います

2の時には
大きい方から出力したいので、A[-1]のような負のインデックスを使います。
bisect_rightを使って、x以上の位置を探索します。
A[bisect_right-k]という感じです。

あとは条件に見合わないものは-1を出力します。
