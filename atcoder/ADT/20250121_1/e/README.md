# URL
https://atcoder.jp/contests/adt_medium_20250121_1/tasks/abc275_c

# 元の問題のURL
https://atcoder.jp/contests/abc275/tasks/abc275_c

# 解説
点に対して、右斜め下の点を探索し、xとyの距離を測ります。
この時重複を避けるため、真横は除きます。(真下は含みます。)

測った距離の先に点が存在するかを確認します。
4点分あれば、正方形と判定できます。
