# URL
https://atcoder.jp/contests/adt_medium_20250130_2/tasks/abc278_b

# 元の問題のURL
https://atcoder.jp/contests/abc278/tasks/abc278_b

# 解説
時刻をインクリメントしながら探索します。

`AB:CD` を `AC:BD` にした時の時刻が成立するかを判定します。
`AB` および `CD` は1桁の可能性があるので、0埋めします。

成立したらその `AB:CD` を出力します。
