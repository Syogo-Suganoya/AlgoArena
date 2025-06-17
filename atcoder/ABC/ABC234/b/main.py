import math

N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]

max_dist = 0  # 最大距離の初期値

# すべての2点の組み合わせを全探索
for i in range(N):
    for j in range(i + 1, N):
        x1, y1 = XY[i]
        x2, y2 = XY[j]

        # ユークリッド距離を計算
        dist = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

        # 最大値を更新
        max_dist = max(max_dist, dist)

print(f"{max_dist:.10f}")
