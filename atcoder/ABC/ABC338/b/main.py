from collections import Counter

S = input()

c = Counter(S)
max_count = max(c.values())

# 同率があったら、辞書順で一番早いものを出力する
for ch in sorted(c.keys()):
    if c[ch] == max_count:
        print(ch)
        break
