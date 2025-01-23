# URL
https://atcoder.jp/contests/adt_medium_20250122_2/tasks/abc247_d

# 元の問題のURL
https://atcoder.jp/contests/abc247/tasks/abc247_d

# 解説
普通にリストなどで考えると、TLEになります。
なので、ランレングス圧縮を使います。

{x:c}のように数と個数を管理します。

取り出す時、1つの要素のみを超える場合があるので、取出したい値になるまで
要素を探索し、デクリメントします。
