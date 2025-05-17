import math

A, B, H, M = map(int, input().split())

# 時針と分針の角度を計算
hour_angle = (H * 60 + M) * 0.5
minute_angle = M * 6

# 針の間の角度を求める
angle = abs(hour_angle - minute_angle)
angle = min(angle, 360 - angle)

# 角度をラジアンに変換
angle_rad = math.radians(angle)

# 余弦定理を用いて距離を計算
distance = math.sqrt(A**2 + B**2 - 2 * A * B * math.cos(angle_rad))

# 結果を出力（20桁の精度で表示）
print("{0:.20f}".format(distance))
