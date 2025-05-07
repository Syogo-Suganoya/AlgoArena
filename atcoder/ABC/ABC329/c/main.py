from itertools import groupby

N = int(input())
S = input()


rle = [(k, sum(1 for _ in g)) for k, g in groupby(S)]

# 各文字の最大回数だけ記録
seen = {}
for char, count in rle:
    if char not in seen or count > seen[char]:
        seen[char] = count

res = sum(seen.values())

print(res)
