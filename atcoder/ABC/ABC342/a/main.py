from collections import Counter

S = input()
c = Counter(S)

# 登場回数が1の最初の文字を探す
for ch in S:
    if c[ch] == 1:
        print(S.index(ch) + 1)
        break
