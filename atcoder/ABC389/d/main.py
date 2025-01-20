import math

R = int(input())

res = 0
current_x = 1
for current_x in range(1, R):
    y = math.sqrt((R**2) - (current_x + 0.5) ** 2)
    y -= 0.5
    res += math.floor(y)
res = res * 4  # 対称性により合計を計算
res += (R - 1) * 4 + 1  # x軸とy軸上の正方形の数
print(res)
