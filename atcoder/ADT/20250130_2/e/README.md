# URL
https://atcoder.jp/contests/adt_medium_20250130_2/tasks/abc293_c

# 元の問題のURL
https://atcoder.jp/contests/abc293/tasks/abc293_c

# 解説
DFSで解けます。

visitedをリストにして、通過したマスの値を追加していきます。
マスの値が重複したらコンティニューします。

無事ゴールまで到達したら、1を返します。
再帰関数の返り値のインクリメントします。
全ての再帰処理が解決したら、最終的な値を出力します。
