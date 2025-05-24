from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

count = defaultdict(int)  # 出現回数を記録する辞書
pairs = 0

for num in A:
    complement = 100000 - num
    pairs += count[complement]  # complementがこれまでに出現していればペアが成立
    count[num] += 1  # numの出現回数を更新

print(pairs)
