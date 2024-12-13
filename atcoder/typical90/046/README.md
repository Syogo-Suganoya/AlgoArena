# 解説
単純な順列全探索ではTLEになります。
A+B+C を modA+modB+modC に置き換えることによって、計算量を削減します。
A, B, C を mod46 を記録します。
インデックスの合計が46になる位置を探索し、その要素の値の積を累積します。

## 問題リンク
https://atcoder.jp/contests/typical90/tasks/typical90_at

## 解説リンク
https://x.com/e869120/status/1395873457259225091
