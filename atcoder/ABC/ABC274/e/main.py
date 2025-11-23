import sys

input = sys.stdin.readline

from math import inf

# ---- 入力 ----
N, M = map(int, input().split())
# 街の座標
cities = [tuple(map(int, input().split())) for _ in range(N)]
# 宝箱の座標
boosters = [tuple(map(int, input().split())) for _ in range(M)]

# 原点を加えて全地点のリスト
points = [(0, 0)] + cities + boosters
P = len(points)

# 都市と宝箱の区切り
city_idx = list(range(1, N + 1))  # 街のインデックス
booster_idx = list(range(N + 1, P))  # 宝箱のインデックス


# ---- 距離行列を作る ----
def dist(p1, p2):
    # ユークリッド距離
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5


D = [[0] * P for _ in range(P)]
for i in range(P):
    for j in range(P):
        D[i][j] = dist(points[i], points[j])

# ---- bitDP ----
# dp[mask][i] = これまでに訪れた地点の集合 mask で最後に i にいるときの最小時間
dp = [[inf] * P for _ in range(1 << P)]
dp[1][0] = 0  # 原点だけ訪問済み

for mask in range(1 << P):
    for u in range(P):
        if dp[mask][u] == inf:
            continue
        # 現在速度 = 2^(訪れた宝箱の数)
        booster_count = sum((mask >> b) & 1 for b in booster_idx)
        speed = 2**booster_count
        # 次に訪れる地点
        for v in range(1, P):
            if mask & (1 << v):
                continue  # すでに訪問済み
            dp[mask | (1 << v)][v] = min(
                dp[mask | (1 << v)][v], dp[mask][u] + D[u][v] / speed
            )

# ---- 街をすべて訪れた集合で原点に戻る ----
res = inf
full_cities_mask = sum(1 << i for i in city_idx) | 1  # 原点 + 全街
for mask in range(1 << P):
    if (mask & full_cities_mask) != full_cities_mask:
        continue  # 全街訪問していない
    for u in range(P):
        if dp[mask][u] < inf:
            booster_count = sum((mask >> b) & 1 for b in booster_idx)
            speed = 2**booster_count
            res = min(res, dp[mask][u] + D[u][0] / speed)

print(res)
