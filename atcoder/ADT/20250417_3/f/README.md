# URL
https://atcoder.jp/contests/adt_medium_20250417_3/tasks/abc275_c

# 元の問題のURL
https://atcoder.jp/contests/abc275/tasks/abc275_c

# 解説
まず点Aと点Bの組み合わせを全ループします。

点Aに対し、点Bであるかをまず判定します。
重複なく正方形をカウントするためです。

次に、点Cと点Dを求めます。
点ABの距離分を離して、CとDを求めます。

CとDにポーンが置いてあれば、正方形です。
