# URL
https://atcoder.jp/contests/adt_medium_20250130_1/tasks/abc304_d

# 元の問題のURL
https://atcoder.jp/contests/abc304/tasks/abc304_d

# 解説
二分探索で苺がどのピースに配置されるかを特定します。
bisect_leftを使うことで、苺がどのラインにあるかがわかります。
xとyがどのラインになるかを求めて、{座標:個数}のdictを求めます。

苺があるピース数もlen(dict)で取得し、そのピース数より総ピース数が少なければminは0です。
maxはdictのmaxです。
