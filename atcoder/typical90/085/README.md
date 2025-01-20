# 解説
a,b,cを全探索しようとするとTLEになります。

以下のような考え方で計算量を削減できます。

- cをk-(a,b)のような形式にして、cのループを削減する
- a,bはkの倍数以外はスキップする

## 問題リンク
https://atcoder.jp/contests/typical90/tasks/typical90_cg

## 解説リンク
https://x.com/e869120/status/1412541885160189952
