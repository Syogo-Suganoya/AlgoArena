# URL
https://atcoder.jp/contests/adt_medium_20250204_3/tasks/abc300_b

# 元の問題のURL
https://atcoder.jp/contests/abc300/tasks/abc300_b

# 解説
縦方向のシフトは1からHまで、横方向のシフトは1からWまでです。
シフトをした時に、AとBの全マスが一致しているかを確認します。
というのを全シフトパターン分試します。

縦方向のシフトは`[(+ s) % H]`です。(sがシフトするマス数)
横方向のシフトは`[(+ t) % W]`です。(tがシフトするマス数)
まとめると `A[(+ s) % H][(+ t) % W]` のようになります。
