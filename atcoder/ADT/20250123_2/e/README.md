# URL
https://atcoder.jp/contests/adt_medium_20250123_2/tasks/abc317_c

# 元の問題のURL
https://atcoder.jp/contests/abc317/tasks/abc317_c

# 解説
DFSで解けます。
DFSで各地点を始点とした時の最長を探索し、それらの最大値を出力します。

**通常のDFSと異なる点**
- グラフのバリューを(接点, 長さ)というようにタプルにして、長さも管理します。
- dfsの引数に現時点までの距離を持たせます。
