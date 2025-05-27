from collections import Counter

N, Q = map(int, input().split())
T = list(map(int, input().split()))

# 各カード番号の出現回数をカウント
cnt = Counter(T)

# 奇数回出現するカードの種類数を数える
odd_count = sum(1 for v in cnt.values() if v % 2 == 1)

# N - 奇数回出現するカードの種類数を出力
print(N - odd_count)
