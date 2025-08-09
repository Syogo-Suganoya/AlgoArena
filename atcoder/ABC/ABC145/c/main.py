import itertools
import math

N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]

total_distance = 0
count = 0

# 全順列を生成
for perm in itertools.permutations(range(N)):
    dist = 0
    # 隣り合う点の距離を計算
    for i in range(N - 1):
        x1, y1 = points[perm[i]]
        x2, y2 = points[perm[i + 1]]
        dist += math.hypot(x2 - x1, y2 - y1)  # √((dx)^2 + (dy)^2)
    total_distance += dist
    count += 1

# 平均距離
print(total_distance / count)
