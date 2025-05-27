S = input()

# 大文字の数を数える
cnt_upper = sum(1 for c in S if c.isupper())

# 大文字の方が多ければ大文字に、そうでなければ小文字に
if cnt_upper > len(S) - cnt_upper:
    print(S.upper())
else:
    print(S.lower())
