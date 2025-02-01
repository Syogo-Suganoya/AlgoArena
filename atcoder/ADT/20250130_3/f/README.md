# URL
https://atcoder.jp/contests/adt_medium_20250130_3/tasks/abc313_c

# 元の問題のURL
https://atcoder.jp/contests/abc313/tasks/abc313_c

# 解説
まず最初に最終的なAの結果を取得します。
最終的なAは、長さNの`int(avg(A))`のリストです。

`avg(A)` が小数点以下が出る場合、sum(A)とNの余りの分だけ、作成したリストに
末尾から1ずつ加算します。

作成したリストをBをおきます。
AとBの各要素の差の絶対値を集計します。

1回の操作で差は2ずつ減っていくので、集計を`//2`します。
結果を出力します。
