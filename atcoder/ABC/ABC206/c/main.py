from collections import Counter

N = int(input())
A = list(map(int, input().split()))

# 全体の異なるペア数の合計：N個から異なるペアを選ぶ → N*(N-1)//2
total_pairs = N * (N - 1) // 2

# 各要素の個数をカウント
c = Counter(A)

# 重複している値の中で、同じ値のペアを数える
# 例えば 3 が 4回出てくれば、その中で選ぶペアは 4*(4-1)//2 = 6通り
same_value_pairs = sum(v * (v - 1) // 2 for v in c.values())

# 異なる値同士のペア数 = 全体のペア数 - 同じ値同士のペア数
print(total_pairs - same_value_pairs)
