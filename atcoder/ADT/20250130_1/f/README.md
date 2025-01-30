# URL
https://atcoder.jp/contests/adt_medium_20250130_1/tasks/abc212_c

# 元の問題のURL
https://atcoder.jp/contests/abc330/tasks/abc212_c

# 解説
まずAとBをソートします。
Aを1つずつみていきます。
Bから二分探索をします。
探索した値の前後をチェックします。idxとidx-1。

これをより差が少ないペアをAから全探索します

最後にペアの絶対値の差を出力します。
