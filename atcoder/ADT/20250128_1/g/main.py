import bisect
from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
Q = int(input())

# クエリのリスト
queries = []
index = N + 2
for _ in range(Q):
    queries.append((map(int, input().split())))
    index += 3

# 前処理：各値の出現位置を記録
positions = defaultdict(list)
for idx, value in enumerate(A):
    positions[value].append(idx + 1)  # 1-indexed のため +1

# クエリの処理
results = []
for L, R, X in queries:
    if X in positions:
        pos_list = positions[X]
        # L 以上の最初の位置
        left = bisect.bisect_left(pos_list, L)
        # R 以下の最後の位置
        right = bisect.bisect_right(pos_list, R)
        # L から R の範囲にある X の個数
        count = right - left
    else:
        count = 0
    print(count)
