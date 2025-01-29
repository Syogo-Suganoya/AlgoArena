# URL
https://atcoder.jp/contests/adt_medium_20250128_1/tasks/abc248_d

# 元の問題のURL
https://atcoder.jp/contests/abc248/tasks/abc248_d

# 解説
各値の登場位置をdictで取得します。
Aを順に見ていくので、dictも必然的に昇順になります。
dict[X]からL以上の最初の位置、R以下の最後の位置を二分探索で取得します。
R-Lが個数になります。
