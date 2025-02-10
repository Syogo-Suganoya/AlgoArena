# URL
https://atcoder.jp/contests/adt_medium_20250205_3/tasks/abc372_c

# 元の問題のURL
https://atcoder.jp/contests/abc372/tasks/abc372_c

# 解説
最初にABCのカウントをします。
置き換える文字の前後1文字をチェックします。全部で3文字取得ということです。
元の文字がABCならカウントを-1します。
置き換え後がABCになるならカウントを+1します。

単純なシミュレーション数え上げではTLEになります。
