from collections import Counter
from math import comb

N = int(input())
A = list(map(int, input().split()))

# 出現回数をカウント
count = Counter(A)

# 全体の組み合わせ数
total_pairs = sum(comb(c, 2) for c in count.values())

# 各要素を除外した場合の組み合わせ数
for ai in A:
    c = count[ai]
    # 除外前の組み合わせ数 - 除外した後の組み合わせ数の差分
    new_pairs = total_pairs - comb(c, 2) + comb(c - 1, 2)
    print(new_pairs)
