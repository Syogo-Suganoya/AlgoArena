# 解説
Aを二分探索して、近似値を検索します。
B以上で最も小さいものを検索し、それとその1つ右の要素で、よりBとの差が少ない方を取得します。
その後Bとの差を出力します。

B以下で最も大きいものを検索する方法でも可能です。

Pythonでの二分探索は `bisect.bisect_left` が便利です。

## 問題リンク
https://atcoder.jp/contests/typical90/tasks/typical90_g

## 解説リンク
https://x.com/e869120/status/1379565222541680644
