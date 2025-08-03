import math

n = int(input())
x0, y0 = map(int, input().split())
x1, y1 = map(int, input().split())

# 中心点O
ox = (x0 + x1) / 2
oy = (y0 + y1) / 2

# A点を中心とした回転前の点ベクトル
x = x0 - ox
y = y0 - oy

# 回転角度（ラジアン）
theta = 2 * math.pi / n

# 回転公式
rx = x * math.cos(theta) - y * math.sin(theta)
ry = x * math.sin(theta) + y * math.cos(theta)

# 中心Oを戻す
rx += ox
ry += oy

print(rx, ry)
