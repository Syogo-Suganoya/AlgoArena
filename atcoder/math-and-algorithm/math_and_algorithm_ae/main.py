import math

ax, ay = map(float, input().split())
bx, by = map(float, input().split())
cx, cy = map(float, input().split())

# ベクトルの計算
ABx, ABy = ax - bx, ay - by
BCx, BCy = cx - bx, cy - by
dot = ABx * BCx + ABy * BCy
len_sq = BCx**2 + BCy**2

t = dot / len_sq

if 0 <= t <= 1:
    # 線分上へ射影される場合
    px = bx + t * BCx
    py = by + t * BCy
    dist = math.hypot(ax - px, ay - py)
else:
    # 射影外なら端点との距離
    dist = min(math.hypot(ax - bx, ay - by), math.hypot(ax - cx, ay - cy))

print(dist)
