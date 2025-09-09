import collections

# 入力の受け取り
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

# 数列 A の各要素の出現回数をカウント
a_count = collections.Counter(A)

# 数列 B の C による変換後の要素の出現回数をカウント
b_transformed = [B[C[j] - 1] for j in range(n)]
b_count = collections.Counter(b_transformed)

# 組み合わせの総数を計算
result = 0
for value in a_count:
    result += a_count[value] * b_count.get(value, 0)

# 結果の出力
print(result)
