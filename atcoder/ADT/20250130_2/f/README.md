# URL
https://atcoder.jp/contests/adt_medium_20250130_2/tasks/abc310_c

# 元の問題のURL
https://atcoder.jp/contests/abc310/tasks/abc310_c

# 解説
元の文字列をsetに入れていきます。

反転した文字がsetにない場合に限り、setにオリジナル文字を追加します。
これでオリジナル文字と反転文字の両方の存在確認をできます。

最後にsetの長さを出力します。
反転文字をsetに追加しなかったのは、ユニークなオリジナル文字の数のみを出力するためです。
