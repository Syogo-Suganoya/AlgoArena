from collections import defaultdict

from sortedcontainers import SortedList

d = defaultdict(SortedList)
N = int(input())

for _ in range(N):
    A, B = map(int, input().split())
    d[A].add(B)
    if len(d[A]) > 2:
        d[A].pop(0)  # 先頭を削除（最も小さい値）

# 同じ味のアイス2つを選ぶ場合
same_score = 0
for i in d.values():
    if len(i) == 2:
        same_score = max(same_score, i[-1] + i[-2] // 2)

# 異なる味のアイス2つを選ぶ場合
max_value = -float("inf")
max_key = None

for key, lst in d.items():
    if lst and lst[-1] > max_value:
        max_value = lst[-1]
        max_key = key

second_max_value = -float("inf")
for key, lst in d.items():
    if key != max_key and lst:
        second_max_value = max(second_max_value, lst[-1])

# もし second_max_value が初期値なら unique_score を 0 にする
unique_score = 0 if second_max_value == -float("inf") else max_value + second_max_value

# 最終的な結果
print(max(same_score, unique_score))
