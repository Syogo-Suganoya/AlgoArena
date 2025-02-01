# URL
https://atcoder.jp/contests/adt_medium_20250130_2/tasks/abc309_d

# 元の問題のURL
https://atcoder.jp/contests/abc309/tasks/abc309_d

# 解説
BFSを用いて、1のノード、N1+N2のノードからの最大距離を求めます。
その距離の和に+1したものが解です。

1のノード、N1+N2のノードは非連結です。
求める値は2つのグループを繋いだ時の最大距離なので、
まず各グループの最大距離を求めます。

各グループの最大距離とそのグループ間を繋ぐ経路の距離1の和が解になります。
