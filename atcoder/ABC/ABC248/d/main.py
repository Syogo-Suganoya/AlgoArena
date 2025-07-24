from bisect import bisect_left, bisect_right
from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
Q = int(input())

# 各値xの出現位置を記録（1-indexed）
pos = defaultdict(list)
for i, a in enumerate(A):
    pos[a].append(i + 1)

for _ in range(Q):
    L, R, X = map(int, input().split())
    if X not in pos:
        print(0)
        continue
    # Xの出現位置リストから[L, R]の範囲にある数を数える
    l = bisect_left(pos[X], L)
    r = bisect_right(pos[X], R)
    print(r - l)
