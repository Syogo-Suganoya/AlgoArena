import math

N, K = map(int, input().split())
A = list(map(int, input().split()))
XY = [tuple(map(int, input().split())) for _ in range(N)]

res = 0.0

for i in range(N):
    min_dist_sq = float("inf")
    for a in A:
        dx = XY[i][0] - XY[a - 1][0]
        dy = XY[i][1] - XY[a - 1][1]
        dist_sq = dx * dx + dy * dy
        min_dist_sq = min(min_dist_sq, dist_sq)
    res = max(res, min_dist_sq)

print(math.sqrt(res))
