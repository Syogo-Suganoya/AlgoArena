import math

N = int(input())

res = 0.0
now = (0, 0)

for _ in range(N):
    X, Y = map(int, input().split())

    # 差分の2乗を使って距離を計算
    dx = now[0] - X
    dy = now[1] - Y
    dist = math.sqrt(dx**2 + dy**2)

    res += dist
    now = (X, Y)

# 原点回帰
X, Y = 0, 0
dx = now[0] - X
dy = now[1] - Y
dist = math.sqrt(dx**2 + dy**2)
res += dist

print(res)
