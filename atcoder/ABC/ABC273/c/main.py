from collections import Counter

N = int(input())
A = list(map(int, input().split()))

# 各値の出現回数をカウント
count = Counter(A)

# 異なる値を降順にソート
unique_values = sorted(count.keys(), reverse=True)

# 出力の構築
for val in unique_values:
    print(count[val])
for _ in range(N - len(unique_values)):
    print(0)
