from math import gcd

N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]

dirs = set()  # 重複のない方向ベクトルを記録

for i in range(N):
    xi, yi = points[i]
    for j in range(N):
        if i == j:
            continue
        xj, yj = points[j]
        dx = xj - xi
        dy = yj - yi
        g = gcd(dx, dy)
        dx //= g
        dy //= g
        dirs.add((dx, dy))  # 正規化した方向ベクトルを保存

print(len(dirs))
