# URL
https://atcoder.jp/contests/adt_medium_20250206_2/tasks/abc220_c

# 元の問題のURL
https://atcoder.jp/contests/abc220/tasks/abc220_c

# 解説
Aを何周するかと最後の調整部分を求めます。

- Aを何周するか:
  - Xとsum(A)の商
- 最後の調整部分:
  - Xとsum(A)の余りが、Aのどの位置で超えるか
    - `bisect_right` を使う
