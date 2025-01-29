# URL
https://atcoder.jp/contests/adt_medium_20250128_1/tasks/abc292_c

# 元の問題のURL
https://atcoder.jp/contests/abc292/tasks/abc292_c

# 解説
ABとCDに分けて考えます。
ABを1からNまで、CDはNーABでループし探索します。

次にXの組み合わせ数を考えます。
XはAとBの積です。Xの約数の数がAとBの組み合わせ数になります。

同様にYを求めます。

X*Yの結果を加算していき、ループの最後に出力します。
