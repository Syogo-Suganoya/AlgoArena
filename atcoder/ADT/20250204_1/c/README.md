# URL
https://atcoder.jp/contests/adt_medium_20250204_1/tasks/abc325_b

# 元の問題のURL
https://atcoder.jp/contests/abc325/tasks/abc325_b

# 解説
24時間のケースを1つずつみていきます。

Xの時差を加算して、それが9~18時の間なら、Wを加算します。
この時、X+ループ値が24を超える可能性があるため、mod24をします。

そうして計算した合計値をループをするたびに、最大値を更新します。
最後に最大値を出力します。

