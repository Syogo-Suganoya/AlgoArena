# 解説
単純に `log2(a)` と `blog2(c)` を比較するのみでは、小数点以下の誤差で正確に判定ができません。
対数の性質を活用して、整数での比較をするようにします。

`blog2(c) = log2(c^b)` となり、`log2(a)`, `blog2(c)` → `a`, `log2(c^b)` の比較で判定できます。

## 問題リンク
https://atcoder.jp/contests/typical90/tasks/typical90_t

## 解説リンク
https://x.com/e869120/status/1385001057512693762
