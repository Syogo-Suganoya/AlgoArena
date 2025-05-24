import math

x1, y1, r1 = map(int, input().split())
x2, y2, r2 = map(int, input().split())

# 中心間の距離を計算
dx = x1 - x2
dy = y1 - y2
d = math.hypot(dx, dy)

# 半径の和と差を計算
r_sum = r1 + r2
r_diff = abs(r1 - r2)

# 位置関係の判定
if d < r_diff:
    print(1)
elif d == r_diff:
    print(2)
elif d < r_sum:
    print(3)
elif d == r_sum:
    print(4)
else:
    print(5)
