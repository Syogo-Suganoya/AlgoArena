# URL
https://atcoder.jp/contests/adt_medium_20250129_2/tasks/abc263_b

# 元の問題のURL
https://atcoder.jp/contests/abc263/tasks/abc263_b

# 解説
Nから遡って、1まで戻るのに何回遡るのかをカウントします。

Pのインデックスは2から始まっています。つまり値からインデックスを参照する際は `-2` する必要があります。
あとは、この操作を何回行うと値が1になるかを計算し出力します。
