from itertools import combinations

N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]

res = 0

# 3点をすべて選ぶ
for (x1, y1), (x2, y2), (x3, y3) in combinations(XY, 3):
    # 3点が一直線かどうかを判定（面積で判定）
    # 三角形の面積 ×2 = |(x2-x1)*(y3-y1) - (x3-x1)*(y2-y1)|
    s = (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)

    if s == 0:
        continue
    res += 1  # それ以外 → カウント

print(res)
