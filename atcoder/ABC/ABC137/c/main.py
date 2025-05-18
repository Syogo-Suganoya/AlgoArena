from collections import Counter

N = int(input())
S = [input() for _ in range(N)]

# 各文字列をソートして共通のキーに変換
normalized = ["".join(sorted(s)) for s in S]

# アナグラムとして同一キーの出現回数を数える
count = Counter(normalized)

# 組み合わせ数を集計
# nC2 = n*(n-1)/2
res = 0
for c in count.values():
    res += c * (c - 1) // 2

print(res)
