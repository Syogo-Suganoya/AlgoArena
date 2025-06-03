from collections import Counter

S = input()

# 文字列 S の各文字の出現回数をカウント
cnt = Counter(S)

# 出現回数が1回の文字を、元の順序に従って探す
for ch in S:
    if cnt[ch] == 1:
        print(ch)  # 最初に見つかった1回登場の文字を出力
        break
else:
    print(-1)  # 1回だけ登場する文字が存在しない場合
