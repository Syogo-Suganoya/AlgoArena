# URL
https://atcoder.jp/contests/adt_medium_20250122_2/tasks/abc347_c

# 元の問題のURL
https://atcoder.jp/contests/abc347/tasks/abc347_c

# 解説
まず、Dを重複削除とソートします。modでも割ります。

次にDの間をチェックします。
Dの間隔にB日以上のものがあれば即Yesを返します。
D[-1]はd[0]+modと比較します。

Dをmodで割っているため、Dの値はmod以下になります。
またDの間もmod以下ということになります。

- B以上離れたものなら週跨ぎで休日にできます。
- 上記がある時点で、それ以外の間隔は週内の休日に収められます。
  - modしている都合上、間隔が開いたものがあれば、それ以外の感覚は狭まります。
